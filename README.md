# User Manual of ETL_for_HL7:
## Install
To run this application, you need to use python 3.7 and with some packages installed which they are prepared in requirements.txt file except two of them that you have to install them manually.
I recommend to create a virtual env in  order to prepare envirnoment for running application properly.


```bash
# Creat a virtual envirnoment with all dependencies installed in python version 3.7
python3.7 -m venv env && source env/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && sudo apt install python3-dev libpq-dev && pip install psycopg2

## Run the application.
./wrapper.sh 


