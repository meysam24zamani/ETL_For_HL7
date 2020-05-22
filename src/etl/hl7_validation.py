from marshmallow import Schema, fields, validate, post_load, pre_dump, ValidationError, pprint

# =========================== HL7 Fields: ORU_R01.PATIENT_RESULT =================================

####PID
#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  PID  ----->  PID.5  ----->  XPN.1
class XPN1_Schema(Schema):
    FN1 = fields.Str(load_from="FN.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  PID  ----->  PID.2
class PID2_Schema(Schema):
    CX1 = fields.Str(load_from="CX.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  PID  ----->  PID.5
class PID5_Schema(Schema):
    XPN1 = fields.Nested(XPN1_Schema, load_from="XPN.1", allow_none=True)
    XPN2 = fields.Str(load_from="XPN.2", allow_none=True)
    XPN3 = fields.Str(load_from="XPN.3", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  PID  ----->  PID.7
class PID7_Schema(Schema):
    TS1 = fields.Str(load_from="TS.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  PID
class PID_Schema(Schema):
    PID2 = fields.Nested(PID2_Schema, load_from="PID.2", allow_none=True)
    PID5 = fields.Nested(PID5_Schema, load_from="PID.5", allow_none=True)
    PID7 = fields.Nested(PID7_Schema, load_from="PID.7", allow_none=True)
    PID8 = fields.Str(load_from="PID.8", allow_none=True)

##########################

####ORU_R01.VISIT
#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT  ----->  PV1  ----->  PV1.3
class PV1_3_Schema(Schema):
    PL1 = fields.Str(load_from="PL.1", allow_none=True)
    PL3 = fields.Str(load_from="PL.3", allow_none=True)


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT  ----->  PV1  ----->  PV1.17  ----->  XCN.2
class XCN2_Schema(Schema):
    FN1 = fields.Str(load_from="FN.1", allow_none=True)


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT  ----->  PV1  ----->  PV1.17
class PV1_17_Schema(Schema):
    XCN1 = fields.Str(load_from="XCN.1", allow_none=True)
    XCN2 = fields.Nested(XCN2_Schema, load_from="XCN.2", allow_none=True)
    XCN3 = fields.Str(load_from="XCN.3", allow_none=True)
    XCN4 = fields.Str(load_from="XCN.4", allow_none=True)


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT  ----->  PV1  ----->  PV1.50
class PV1_50_Schema(Schema):
    CX1 = fields.Str(load_from="CX.1", allow_none=True)


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT  ----->  PV1  ----->  PV1.52
class PV1_52_Schema(Schema):
    XCN1 = fields.Str(load_from="XCN.1", allow_none=True)
    XCN3 = fields.Str(load_from="XCN.3", allow_none=True)


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT  ----->  PV1
class PV1_Schema(Schema):
    PV1_3 = fields.Nested(PV1_3_Schema, load_from="PV1.3", allow_none=True)
    PV1_4 = fields.Str(load_from="PV1.4", allow_none=True)
    PV1_17 = fields.Nested(PV1_17_Schema, load_from="PV1.17", allow_none=True)
    PV1_50 = fields.Nested(PV1_50_Schema, load_from="PV1.50", allow_none=True)
    PV1_52 = fields.Nested(PV1_52_Schema, load_from="PV1.52", allow_none=True)

###############################

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT  ----->  ORU_R01.VISIT
class ORU_R01_VISIT_Schema(Schema):
    PV1 = fields.Nested(PV1_Schema, load_from="PV1", allow_none=True)

####################################################

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.PATIENT
class ORU_R01_PATIENT_Schema(Schema):
    PID = fields.Nested(PID_Schema, load_from="PID", allow_none=True)
    ORU_R01_VISIT = fields.Nested(ORU_R01_VISIT_Schema, load_from="ORU_R01.VISIT", allow_none=True)


########################--ORU_R01.ORDER_OBSERVATION--##############################
####################################################--ORC--####################################################


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORC  ----->  ORC.2
class ORC2_Schema(Schema):
    EI1 = fields.Str(load_from="EI.1", allow_none=True)
   


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORC  ----->  ORC.3
class ORC3_Schema(Schema):
    EI1 = fields.Str(load_from="EI.1", allow_none=True)
 


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORC  ----->  ORC.9
class ORC9_Schema(Schema):
    TS1 = fields.Str(load_from="TS.1", allow_none=True)



#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORC
class ORC_Schema(Schema):
    ORC1 = fields.Str(load_from="ORC.1", allow_none=True)
    ORC2 = fields.Nested(ORC2_Schema, load_from="ORC.2", allow_none=True)
    ORC3 = fields.Nested(ORC3_Schema, load_from="ORC.3", allow_none=True)
    ORC5 = fields.Str(load_from="ORC.5", allow_none=True)
    ORC9 = fields.Nested(ORC9_Schema, load_from="ORC.9", allow_none=True)


####################################################--OBR--####################################################


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORC  ----->  OBR.2
class OBR2_Schema(Schema):
    EI1 = fields.Str(load_from="EI.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORC  ----->  OBR.4
class OBR4_Schema(Schema):
    CE1 = fields.Str(load_from="CE.1", allow_none=True)
    CE2 = fields.Str(load_from="CE.2", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  OBR
class OBR_Schema(Schema):
    OBR1 = fields.Str(load_from="OBR.1", allow_none=True)
    OBR2 = fields.Nested(OBR2_Schema, load_from="OBR.2", allow_none=True)
    OBR4 = fields.Nested(OBR4_Schema, load_from="OBR.4", allow_none=True)


####################################################--FT1--####################################################

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  FT1  ----->  FT.11  ----->  CP.1
class CP1_Schema(Schema):
    MO1 = fields.Str(load_from="MO.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  FT1  ----->  FT.11
class FT11_Schema(Schema):
    CP1 = fields.Nested(CP1_Schema, load_from="CP.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  FT1
class FT1_Schema(Schema):
    FT11 = fields.Nested(FT11_Schema, load_from="FT.11", allow_none=True)


####################################################--ORU_R01.OBSERVATION--####################################################

####OBX####
#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION  ----->  OBX  ----->  OBX.16
class OBX16_Schema(Schema):
    XCN1 = fields.Str(load_from="XCN.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION  ----->  OBX  ----->  OBX.14
class OBX14_Schema(Schema):
    TS1 = fields.Str(load_from="TS.1", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION  ----->  OBX  ----->  OBX.6
class OBX6_Schema(Schema):
    CE2 = fields.Str(load_from="CE.2", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION  ----->  OBX  ----->  OBX.3
class OBX3_Schema(Schema):
    CE1 = fields.Str(load_from="CE.1", allow_none=True)
    CE2 = fields.Str(load_from="CE.2", allow_none=True)
    CE3 = fields.Str(load_from="CE.3", allow_none=True)

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION  ----->  OBX
class OBX_Schema(Schema):
    OBX1 = fields.Str(load_from="OBX.1", allow_none=True)
    OBX2 = fields.Str(load_from="OBX.2", allow_none=True)
    OBX3 = fields.Nested(OBX3_Schema, load_from="OBX.3", allow_none=True)
    OBX5 = fields.Str(load_from="OBX.5", allow_none=True)
    OBX6 = fields.Nested(OBX6_Schema, load_from="OBX.6", allow_none=True)
    OBX7 = fields.Str(load_from="OBX.7", allow_none=True)
    OBX8 = fields.Str(load_from="OBX.8", allow_none=True)
    OBX14 = fields.Nested(OBX14_Schema, load_from="OBX.14", allow_none=True)
    OBX16 = fields.Nested(OBX16_Schema, load_from="OBX.16", allow_none=True)

    @post_load
    def make_obj(self, data):
        if data["OBX7"] is None:
            data["OBX7"] = ("0 - 0")
        return data

####NTE####
#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION  ----->  NTE
class NTE_Schema(Schema):
    NTE3 = fields.Str(load_from="NTE.3", allow_none=True)


#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION  ----->  ORU_R01.OBSERVATION
class ORU_R01_OBSERVATION_Schema(Schema):
    OBX = fields.Nested(OBX_Schema, load_from="OBX", allow_none=True)
    NTE = fields.Nested(NTE_Schema, load_from="NTE", allow_none=True)


#######################################################

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT  ----->  ORU_R01.ORDER_OBSERVATION  ----->  []  ----->  ORU_R01.ORDER_OBSERVATION
class ORU_R01_ORDER_OBSERVATION_Schema(Schema):
    ORC = fields.Nested(ORC_Schema, load_from="ORC", allow_none=True)
    OBR = fields.Nested(OBR_Schema, load_from="OBR", allow_none=True)
    FT1 = fields.Nested(FT1_Schema, load_from="FT1", allow_none=True)
    ORU_R01_OBSERVATION = fields.Nested(ORU_R01_OBSERVATION_Schema, load_from="ORU_R01.OBSERVATION", allow_none=True)


##############################################################################

#ORU_R01  ----->  ORU_R01.PATIENT_RESULT
class ORU_R01_PATIENT_RESULT_Schema(Schema):
    ORU_R01_PATIENT = fields.Nested(ORU_R01_PATIENT_Schema, load_from="ORU_R01.PATIENT", allow_none=True)
    # ORU_R01_ORDER_OBSERVATION = fields.List(fields.Nested(ORU_R01_ORDER_OBSERVATION_Schema, load_from="ORU_R01.ORDER_OBSERVATION"),
                            #    required=True, 
                            #    load_from="ORU_R01.ORDER_OBSERVATION",
                            #    validate=validate.Length(min=1))
    ORU_R01_ORDER_OBSERVATION = fields.Nested(ORU_R01_ORDER_OBSERVATION_Schema, load_from="ORU_R01.ORDER_OBSERVATION", allow_none=True, many=True)



# =========================== HL7 Fields: MSH =================================

#ORU_R01  ----->  MSH  ----->  MSH3
class MSH3Schema(Schema):
    HD1 = fields.Str(load_from="HD.1", allow_none=True)

#ORU_R01  ----->  MSH  ----->  MSH5
class MSH5Schema(Schema):
    HD1 = fields.Str(load_from="HD.1", allow_none=True)

#ORU_R01  ----->  MSH  ----->  MSH7
class MSH7Schema(Schema):
    TS1 = fields.Str(load_from="TS.1", allow_none=True)

#ORU_R01  ----->  MSH  ----->  MSH9
class MSH9Schema(Schema):
    MSG1 = fields.Str(load_from="MSG.1", allow_none=True)
    MSG2 = fields.Str(load_from="MSG.2", allow_none=True)

#ORU_R01  ----->  MSH  ----->  MSH11
class MSH11Schema(Schema):
    PT1 = fields.Str(load_from="PT.1", allow_none=True)

#ORU_R01  ----->  MSH  ----->  MSH12
class MSH12Schema(Schema):
    VID1 = fields.Str(load_from="VID.1", allow_none=True)


#ORU_R01  ----->  MSH
class MSHSchema(Schema):
    MSH1 = fields.Str(load_from="MSH.1", allow_none=True)
    MSH2 = fields.Str(load_from="MSH.2", allow_none=True)
    MSH3 = fields.Nested(MSH3Schema, load_from="MSH.3", allow_none=True)
    MSH5 = fields.Nested(MSH5Schema, load_from="MSH.5", allow_none=True)
    MSH7 = fields.Nested(MSH7Schema, load_from="MSH.7", allow_none=True)
    MSH9 = fields.Nested(MSH9Schema, load_from="MSH.9", allow_none=True)
    MSH10 = fields.Str(load_from="MSH.10", allow_none=True)
    MSH11 = fields.Nested(MSH11Schema, load_from="MSH.11", allow_none=True)
    MSH12 = fields.Nested(MSH12Schema, load_from="MSH.12", allow_none=True)

# =========================== HL7 Fields: ORU_R01 =================================
class HL7_Schema(Schema):
    xmlns_xsi = fields.Str(load_from='@xmlns:xsi', allow_none=True)
    xmlns_xsd = fields.Str(load_from='@xmlns:xsd', allow_none=True)
    xmlns = fields.Str(load_from='@xmlns', allow_none=True)
    MSH = fields.Nested(MSHSchema, load_from="MSH", allow_none=True)
    ORU_R01_PATIENT_RESULT = fields.Nested(ORU_R01_PATIENT_RESULT_Schema, load_from="ORU_R01.PATIENT_RESULT", allow_none=True)

    # @post_load
    # def make_obj(self, data):
        # return HL7_DTO(**data)
