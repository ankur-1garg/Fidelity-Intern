import pandas as pd
from snowflake.connector import connect

# Snowflake connection parameters
conn = connect(
    account='ut20337.ap-southeast-1',
    user='Ankur',
    password='x16bTJawBrXFJb4VyE',
    warehouse='COMPUTE_WH',
    database='TRIAL_DB',
    schema='TRIAL_SCMA'
)

# Execute your SQL query
cur=conn.cursor()
cur.execute("SELECT * FROM CUSTOMER")

data=cur.fetchall()
df=pd.DataFrame(data, columns=[[X] for X in cur.description])
print(df)
