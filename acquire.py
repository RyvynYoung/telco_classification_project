
import pandas as pd
import env
import os

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# get_telco_data: returns the titanic data from the codeup data science database as a pandas data frame.
def get_telco_data():
    query = '''select * from customers 
join contract_types using (contract_type_id) 
join internet_service_types using (internet_service_type_id) 
join payment_types using (payment_type_id);'''
    filename = 'telco.csv'
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col=0)
        return df
    else:
        df = pd.read_sql(query, get_connection('telco_churn'))
        df.to_csv(filename)
        return df
    
