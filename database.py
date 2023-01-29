import sqlite3
import pandas as pd

df = pd.read_csv("Database/Lab_Info.csv")

def df_to_db(database, table_name):
# table_name = 'Lab_Info'
    conn = sqlite3.connect("Database/"+database+".sqlite")
    query = f'Create table if not Exists {table_name} (Query)'
    conn.execute(query)
    df.to_sql(table_name,conn,if_exists='replace',index=False)
    conn.commit()
    conn.close()

df_to_db("AIMS_Lab","Lab_Info")

