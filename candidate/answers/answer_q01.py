import duckdb
import os
import pandas as pd
from decimal import Decimal

pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)
pd.set_option("display.min_rows", 2000)

basepath = 'C:/Users/Andrea/smg-gdt-bi-hiring-challenge/candidate/data' # candidate/data

cursor = duckdb.connect()

dim_date = f"read_csv_auto('{basepath}/dim_date.csv', delim=',', header=True)"
dim_platform = f"read_csv_auto('{basepath}/dim_platform.csv', delim=',', header=True)"
dim_product_type = f"read_csv_auto('{basepath}/dim_product_type.csv', delim=',', header=True)"
dim_status = f"read_csv_auto('{basepath}/dim_status.csv', delim=',', header=True)"
dim_user = f"read_csv_auto('{basepath}/dim_user.csv', delim=',', header=True)"
#TEST = {'listing_date_key': 'DATE','listing_id': 'INTEGER', 'platform_id': 'INTEGER','product_type_id': 'INTEGER','user_id': 'INTEGER','price': 'DOUBLE','status_id': 'INTEGER','valid_from': 'DATE','valid_to': 'DATE'}
#print(TEST)
fct_listings = f"read_csv_auto('{basepath}/fct_listings.csv', delim=',', header=True)"
#f"read_csv('{basepath}/fct_listings.csv', delim=',', header=True, columns={TEST})"
#print(fct_listings)

# current_path = f"os.getcwd()"
#print(cursor.execute('SELECT * FROM duckdb_settings();').fetch_df())
#.to_csv('answer_q02_1.csv', sep=';',columns = header, index=False);

# Snapshots of listings
snapshots_listings = f"""--sql

SELECT
	d.date_key,
	l.*
FROM {dim_date} d 
LEFT JOIN {fct_listings} l 
	ON (d.date_key < l.valid_to OR l.valid_to IS NULL)
		AND d.date_key >= l.valid_from
WHERE d.first_day_of_month >= '2021-12-01' 
	AND d.last_day_of_month <= '2022-01-31' 
ORDER BY date_key;

"""

# ...and view the results for that query:
cursor.execute(snapshots_listings).fetch_df().to_csv('answer_q01.csv', sep=';',index=False);
