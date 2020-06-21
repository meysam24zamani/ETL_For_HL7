from etl.shared.shared import SharedService
from etl.hl7_validation import HL7_Schema
from database.connection import conn, cur
from time import strftime, gmtime
from datetime import datetime
import os
import json
#import requests


class EtlService:
    labsuite_json = {}
    labsuite_response = {}

    def __init__(self, timestamp, sample_id, sample_date, sample_date_name):
        self.timestamp = timestamp
        self.sample_id = sample_id
        self.sample_date = sample_date
        self.sample_date_name = sample_date_name


    #Response of complete_json method will be the json format of hl7 file.
    def complete_json(self):
        schema = HL7_Schema(strict=True)


##################################       Extract Section       ##################################
        
        # Extract data from input folder
        patient_json = SharedService(f'input_files/{self.sample_id}_{self.sample_date_name}.xml').get_from_file()

        ##### Request to an outsource api with specific sample_id and sample_date for getting patient information and observation results.
        ## response_lab_precongen = requests.get('http://precongen-hl7.genomcore.net/api/labsuite/getsampleresults', params={"sampleID": self.sample_id, "sampleDate": self.sample_date})
        ## response_lab_precongen = response_lab_precongen.text
        ## patient_json = SharedService(response_lab_precongen).xml_to_json()

##################################       Transform Section       ##################################

        # Getting main result of response which is in level 4 of hierarchy result
        xml_inside_json = patient_json.get('soap:Envelope',
                                                    {}).get('soap:Body',
                                                            {}).get('ObtenerResultadosMuestraResponse',
                                                                    {}).get('ObtenerResultadosMuestraResult',
                                                                            {}).get('ORU_R01',
                                                                            {})
        analysis = schema.load(xml_inside_json).data
        self.labsuite_json = analysis
        return analysis

    #Response of bio_value_json method will be the json format of medical test result of the patient.
    def bio_value_json(self):
        analysis = self.labsuite_json

        bio_value_list = []
        observations = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_ORDER_OBSERVATION']
        patient_id = observations[0]['ORC']['ORC3']['EI1']
        sample_date = observations[0]['ORC']['ORC9']['TS1']
        for obs in observations:

            bio_value = {}

            range_valid = obs['ORU_R01_OBSERVATION']['OBX']['OBX7']
            range_valid = range_valid.split(' - ')

            bio_value['title'] = obs['ORU_R01_OBSERVATION']['OBX']['OBX3']['CE2']

            bio_value['code'] = obs['ORU_R01_OBSERVATION']['OBX']['OBX3']['CE1']

            bio_value['group'] = obs['ORU_R01_OBSERVATION']['OBX']['OBX3']['CE3']

            stringmin = range_valid[0] 
            bio_value['min'] = float(stringmin.replace(",","."))

            stringmax = range_valid[1]
            bio_value['max'] = float(stringmax.replace(",","."))

            bio_value['units'] = obs['ORU_R01_OBSERVATION']['OBX']['OBX6']['CE2']

            stringvalue = obs['ORU_R01_OBSERVATION']['OBX']['OBX5']
            bio_value['value'] = float(stringvalue.replace(",","."))

            if bio_value['value'] > bio_value['max']:
                absolute_diff = abs(bio_value['max'] - bio_value['value'])
                relative_diff = absolute_diff / bio_value['max']
                relative_diff = round(relative_diff, 2)
            elif bio_value['value'] < bio_value['min']:
                absolute_diff = abs(bio_value['min'] - bio_value['value'])
                relative_diff = absolute_diff / bio_value['min']
                relative_diff = round(relative_diff, 2)
            else:
                relative_diff = 0

            bio_value['relative_discrepancy'] = relative_diff 
          

            bio_value['consequence'] = obs['ORU_R01_OBSERVATION']['OBX']['OBX8']

            bio_value_list.append(bio_value)

        bio_value_dict = {'section_bio_values': {
            'title': 'Patient bio values',
            'sample_date': sample_date,
            'sample_timestamp': str(datetime.strptime(sample_date, '%Y%m%d%H%M%S')),
            'value': bio_value_list
            }}

        return bio_value_dict

    #Response of patient_Identification_json method will be the json format of patient identification information.
    def patient_Identification_json(self):
        analysis = self.labsuite_json
        observations = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_ORDER_OBSERVATION']

        patient_Identification = {}

        patient_Identification['name'] = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_PATIENT']['PID']['PID5']['XPN3']

        patient_Identification['surname1'] = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_PATIENT']['PID']['PID5']['XPN1']['FN1']

        patient_Identification['surname2'] = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_PATIENT']['PID']['PID5']['XPN2']

        patient_Identification['sex'] = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_PATIENT']['PID']['PID8']

        patient_Identification['dni'] = observations[0]['ORC']['ORC3']['EI1']

        patient_Identification['dateOfBirth'] = analysis['ORU_R01_PATIENT_RESULT']['ORU_R01_PATIENT']['PID']['PID7']['TS1']


        current_year = int(strftime("%Y", gmtime()))
        patient_birth_year = int(patient_Identification['dateOfBirth'][:4])
        age = current_year - patient_birth_year
        if age < 40:
            range_age = "young"
        elif  40 <= age < 60:
            range_age = "middle_aged"
        else:
            range_age = "old"

        patient_Identification['age'] = age

        patient_Identification['range_age'] = range_age


        return patient_Identification

    # Getting all response from complete_Json, bio_value and patient_Identification and save them in a dictionary.
    def get_data(self):
        response = {
            "analysis":  self.complete_json(),
            "bio_value": self.bio_value_json(),
            "patient_Identification": self.patient_Identification_json()
        }
        self.labsuite_response = response
        return response


    #save all 3 response in to the JSON files
    def files_create_to_path(self):
        response = self.labsuite_response
        analysis = response["analysis"]
        bio_value = response["bio_value"]
        patient_Identification = response["patient_Identification"]

        # Check if output folder exists and if not create it.
        path = f'output_files/{self.sample_id}_{self.sample_date_name}/[{self.timestamp}]/*.json'
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.makedirs(d)

        # Create JSON file for final response in the folder named output_files
        path_response = f'output_files/{self.sample_id}_{self.sample_date_name}/[{self.timestamp}]/response.json'
        with open(path_response, 'w') as outfile:
                json.dump(analysis, outfile, ensure_ascii=False, indent=4)

        # Create JSON file for biovalue in the folder named output_files
        path_biovalue = f'output_files/{self.sample_id}_{self.sample_date_name}/[{self.timestamp}]/bio_value.json'
        with open(path_biovalue, 'w') as outfile:
                json.dump(bio_value, outfile, ensure_ascii=False, indent=4)

        # Create JSON file for final patientidentification in the folder named output_files
        path_patientidentification = f'output_files/{self.sample_id}_{self.sample_date_name}/[{self.timestamp}]/patient_identification.json'
        with open(path_patientidentification, 'w') as outfile:
                json.dump(patient_Identification, outfile, ensure_ascii=False, indent=4)



##################################       Load Section       ##################################
    #Create record with patient Identification and bio_values into the PostgreSQL
    def record_create_into_postgresql(self):
        response = self.labsuite_response



        #Query1: Insert data into Dim_Patient table.

        value_name = str(response['patient_Identification']['name'])
        value_surname1 = str(response['patient_Identification']['surname1'])
        value_surname2 = str(response['patient_Identification']['surname2'])
        value_date_of_birth = str(response['patient_Identification']['dateOfBirth'])
        value_age = str(response['patient_Identification']['age'])
        value_range_age = str(response['patient_Identification']['range_age'])
        value_sex = str(response['patient_Identification']['sex'])
        value_dni = str(response['patient_Identification']['dni'])
        

        cur.execute("SELECT dni FROM Dim_Patient WHERE dni = %s", (value_dni,))
        if len(cur.fetchall()) > 0:
            pass
        else:
            query1 = "INSERT INTO Dim_Patient (name, surname1, surname2, date_of_birth, age, range_age," \
            "sex, dni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query1, (value_name, value_surname1, value_surname2,  \
            value_date_of_birth, value_age, value_range_age, value_sex, value_dni))
        print("Record created successfully in Dim_Patient table")
        conn.commit()



        #Query2: Insert data into Dim_Date table.

        value_sample_date = str(response['bio_value']['section_bio_values']['sample_date'])
        value_sample_timestamp = str(response['bio_value']['section_bio_values']['sample_timestamp'])
        value_date = value_sample_date[:8]
        value_day = value_date[6:8]
        value_month = value_date[4:6]
        value_year = value_date[0:4]


        cur.execute("SELECT sample_timestamp FROM Dim_Date WHERE sample_timestamp = %s", (value_sample_timestamp,))
        if len(cur.fetchall()) > 0:
            pass
        else:
            query2 = "INSERT INTO Dim_Date (sample_timestamp, day, month, year) VALUES (%s, %s, %s, %s)"
            cur.execute(query2, (value_sample_timestamp, value_day, value_month, value_year))
        print("Record created successfully in Dim_Date table")
        conn.commit()



        #Query3: Insert data into Dim_Group table.
        
        value_all_values = response['bio_value']['section_bio_values']['value']

        for key in value_all_values:
            value_group_name = str(key['group'])
            cur.execute("SELECT name FROM Dim_Group WHERE name = %s", (value_group_name,))
            if len(cur.fetchall()) > 0:
                pass
            else:
                query3 = "INSERT INTO Dim_Group (name) VALUES (%s)"
                cur.execute(query3, (value_group_name,))

        print("Record created successfully in Dim_Group table")
        conn.commit()



        #Query4: Insert data into Dim_Type_Analysis table.  
        for key in value_all_values:
            value_group_name2 = str(key['group'])
            cur.execute("SELECT id FROM Dim_Group WHERE name = %s", (value_group_name2,))
            rows = cur.fetchall()
            for y in rows:
                value_group_id = str(y[0])
            
            value_name = str(key['title'])
            value_code = str(key['code'])
            value_min = str(key['min'])
            value_max = str(key['max'])
            value_units = str(key['units'])

            cur.execute("SELECT code FROM Dim_Type_Analysis WHERE code = %s", (value_code,))
            if len(cur.fetchall()) > 0:
                pass
            else:
                query4 = "INSERT INTO Dim_Type_Analysis (code, group_id, name, min, max, units)" \
                "VALUES (%s, %s, %s, %s, %s, %s)"
                cur.execute(query4, (value_code, value_group_id, value_name,  \
                value_min, value_max, value_units))
        print("Record created successfully in Dim_Type_Analysis table")
        conn.commit()



        #Query5: Insert data into Fact_Observation table.  
        for key in value_all_values:
            value_result = str(key['value'])
            value_relative_discrepancy = str(key['relative_discrepancy'])
            value_code = str(key['code'])
            value_consequence = str(key['consequence'])

            cur.execute("SELECT id FROM Dim_Patient WHERE dni = %s", (value_dni,))
            rows = cur.fetchall()
            for r in rows:
                value_Patient_id = str(r[0])
            
            cur.execute("SELECT patient_id, sample_date_id, type_analysis_id, " \
            + "result_value FROM Fact_Observation WHERE patient_id = %s AND sample_date_id = %s AND " \
            + "type_analysis_id = %s AND result_value = %s", (value_Patient_id, value_sample_timestamp, value_code, value_result))
            if len(cur.fetchall()) > 0:
                pass
            else:
                query5 = "INSERT INTO Fact_Observation (patient_id, sample_date_id, type_analysis_id, " \
                "result_value, relative_discrepancy, consequence) VALUES (%s, %s, %s, %s, %s, %s)"
                cur.execute(query5, (value_Patient_id, value_sample_timestamp, value_code, value_result, \
                value_relative_discrepancy, value_consequence))
        print("Record created successfully in Fact_Observation table")
        conn.commit()


        # Close the cursor
        cur.close()
        # Close the connection
        conn.close()


    def run(self):
        """Run ETL service:
        """
        self.get_data()
        self.record_create_into_postgresql()
        self.files_create_to_path()
