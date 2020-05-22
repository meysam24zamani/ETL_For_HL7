import json
import os
import xmltodict
from xml.sax.saxutils import unescape

class SharedService():

    def __init__(self, 
            response: str
            ):

        self.response = response
        self.format_of_the_file = response[len(response)-3:len(response)]
 
    def get_from_file(self):

        if self.format_of_the_file == 'xml':
            data = self.xml_to_json_from_file()
        else:     
            with open(self.response) as json_file:
                data = json.load(json_file)
        return data

    def xml_to_json_from_file(self):
        patient_xml = json.loads(json.dumps(xmltodict.parse(unescape(open(self.response).read()))))
        return patient_xml

    def xml_to_json(self):
        patient_xml = json.loads(json.dumps(xmltodict.parse(unescape(self.response))))
        return patient_xml   

    def xml_decoder(self):
        decode_xml = unescape(open(self.response).read())
        return decode_xml