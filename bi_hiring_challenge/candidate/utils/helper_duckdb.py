# helper_duckdb.py
# Prerequisites:
#   1. You need python installed on your machine -> https://www.python.org/downloads/
#   2. you need the python modulle duckdb installed, install via command line pip install duckdb==0.6.1 (you may need administrator permissions to install via pip)
#   3. Optional: If you want syntax highlighting for SQL in python with Visual Studio Code, you can use
#                using python-string-sql (https://marketplace.visualstudio.com/items?itemName=ptweir.python-string-sql) extensions to syntax-highlight sql in python string
#                to get highlighting working, one must
#                insert --sql, --beginsql, or --begin-sql at the beginning of the part of the string you would like highlighted
#                and a semicolon, --endsql, or --end-sql at the end of the highlighted section.
#
# SQL reference for duckdb: https://duckdb.org/docs/sql/functions/overview 

import duckdb

## avoid truncating results
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)
pd.set_option("display.min_rows", 2000)

# path to the folder with the datasets (eg. absolute path like C:/Users/xyz/Documents/01-datasets)
basepath = '<path-to-01-datasets>'

# preparing the data access
cursor = duckdb.connect()

# Note: if you need explicit data types for a table instead of auto inferring, you can use read_csv(...)
#       Example:
#       xyz = f"read_csv('{basepath}/xyz.csv', delim=',', header=True, columns={'FlightDate': 'DATE', 'UniqueCarrier': 'VARCHAR', 'OriginCityName': 'VARCHAR', 'DestCityName': 'VARCHAR'})"
# see data types: https://duckdb.org/docs/sql/data_types/overview

# auto inferring data types:
dim_date = f"read_csv_auto('{basepath}/dim_date.csv', delim=',', header=True)"
dim_platform = f"read_csv_auto('{basepath}/dim_platform.csv', delim=',', header=True)"
dim_product_type = f"read_csv_auto('{basepath}/dim_product_type.csv', delim=',', header=True)"
dim_status = f"read_csv_auto('{basepath}/dim_status.csv', delim=',', header=True)"
dim_user = f"read_csv_auto('{basepath}/dim_user.csv', delim=',', header=True)"
fct_listings = f"read_csv_auto('{basepath}/fct_listings.csv', delim=',', header=True)"



# Examples: Now you can define your SQL query...
some_query = f"""--sql
SELECT *
FROM {fct_listings};
"""

# ...and view the results for that query:
print(cursor.execute(some_query).fetch_df())

# Start your work from here
