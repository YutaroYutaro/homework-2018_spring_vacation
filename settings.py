import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ID = os.environ.get("ID")
PW = os.environ.get("PW")
CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
AS = os.environ.get("AS")
dbname = os.environ.get("dbname")
table1 = os.environ.get("table1")
table2 = os.environ.get("table2")