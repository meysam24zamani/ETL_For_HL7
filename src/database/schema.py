import psycopg2
from connection import conn, cur

conn.set_session(autocommit=True)

#Delete all tables and make the schema empty.
querydrop = """
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';
"""
cur.execute(querydrop)
print("All tables are deleted successfully")
print("-----------------------------------")
print("-----------------------------------")

#Query1: Create Dim_Patient table.
query1 = """
CREATE TABLE Dim_Patient
(
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    surname1 VARCHAR(500) NOT NULL,
    surname2 VARCHAR(500),
    date_of_birth DATE NOT NULL,
    age INT NOT NULL,
    range_age VARCHAR(200) NOT NULL,
    sex VARCHAR(70) NOT NULL,
    dni VARCHAR(200) NOT NULL
)
"""
cur.execute(query1)
print("Table -> Dim_Patient is created successfully")

#Query2: Create Dim_Date table.
query2 = """
CREATE TABLE Dim_Date
(
    sample_timestamp timestamp NOT NULL PRIMARY KEY,
    day INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL
)
"""
cur.execute(query2)
print("Table -> Dim_Date is created successfully")

#Query3: Create Dim_Group table.
query3 = """
CREATE TABLE Dim_Group
(
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(200) NOT NULL
)
"""
cur.execute(query3)
print("Table -> Dim_Group is created successfully")

#Query4: Create Dim_Type_Analysis table.
query4 = """
CREATE TABLE Dim_Type_Analysis
(
    code VARCHAR(200) NOT NULL PRIMARY KEY,
    group_id SERIAL NOT NULL REFERENCES Dim_Group (id),
    name VARCHAR(200) NOT NULL,
    min FLOAT,
    max FLOAT,
    units VARCHAR(200) NOT NULL
)
"""
cur.execute(query4)
print("Table -> Dim_Type_Analysis is created successfully")

#Query5: Create Fact_Observation table.
query5 = """
CREATE TABLE Fact_Observation
(
    patient_id SERIAL NOT NULL REFERENCES Dim_Patient (id),
    sample_date_id timestamp NOT NULL REFERENCES Dim_Date (sample_timestamp),
    type_analysis_id VARCHAR(200) NOT NULL REFERENCES Dim_Type_Analysis (code),
    result_value FLOAT NOT NULL,
    relative_discrepancy FLoat,
    consequence VARCHAR(200)
)
"""
cur.execute(query5)
print("Table -> Fact_Observation is created successfully")


# Close the cursor
cur.close()

# Close the connection
conn.close()
