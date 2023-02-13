import pandas as pd
import pymysql
from sqlalchemy import create_engine


dim_date = pd.read_csv("~/Desktop/bi-test/smg-gdt-bi-hiring-challenge/candidate/data/dim_date.csv")
dim_platform = pd.read_csv("~/Desktop/bi-test/smg-gdt-bi-hiring-challenge/candidate/data/dim_platform.csv")
dim_product_type = pd.read_csv("~/Desktop/bi-test/smg-gdt-bi-hiring-challenge/candidate/data/dim_product_type.csv")
dim_status = pd.read_csv("~/Desktop/bi-test/smg-gdt-bi-hiring-challenge/candidate/data/dim_status.csv")
dim_user = pd.read_csv("~/Desktop/bi-test/smg-gdt-bi-hiring-challenge/candidate/data/dim_user.csv")
fct_listings = pd.read_csv("~/Desktop/bi-test/smg-gdt-bi-hiring-challenge/candidate/data/fct_listings.csv")

engine = create_engine('mysql+pymysql://admin:Daniel123!@localhost/smg',echo=False)

dim_user.to_sql(name='dim_user',con=engine,if_exists='replace',index=False)
dim_platform.to_sql(name='dim_platform',con=engine,if_exists='replace',index=False)
dim_product_type.to_sql(name='dim_product_type',con=engine,if_exists='replace',index=False)
dim_status.to_sql(name='dim_status',con=engine,if_exists='replace',index=False)
dim_date.to_sql(name='dim_date',con=engine,if_exists='replace',index=False)
fct_listings.to_sql(name='fct_listings',con=engine,if_exists='replace',index=False)