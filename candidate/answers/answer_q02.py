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
print(fct_listings)

# current_path = f"os.getcwd()"
#print(cursor.execute('SELECT * FROM duckdb_settings();').fetch_df())
#.to_csv('answer_q02_1.csv', sep=';',columns = header, index=False);

# Top 3 selling products by platform
top_3_selling_products_by_platform = f"""--sql


WITH Sales_Per_Platform_And_Product_Type AS 
(
	/*
	Since products might have same number of sales, I'm using rank in order to get same ranking for 
	such products (versus to row_no) and to skip ranking in case there are same numbers for sales (versus to dense_rank).
    If the goal is something else - then I would use other functions, but I believe I can't decide myself, I 
    would have to align with the requester of KPI.
	*/
	SELECT 
		pl.Platform_Name, 
        p.product_type_name, 
        sa.sales,
        RANK() OVER (PARTITION BY pl.Platform_Name ORDER BY sa.sales DESC) AS ranking 
	FROM (
		SELECT 
			/*
			Since platform id is the same, but it's name changes over time, I'm using string_agg
			in order to get 1 value per platform type. Also, since the request was number of sales per 
			platform, I'm setting platform as a join base in case there is a platform with no sales
			*/
			STRING_AGG(platform, '/') AS platform_name, 
			platform_id 
		FROM {dim_platform} 
		GROUP BY platform_id
		) pl
	LEFT JOIN (
				SELECT 
					platform_id, 
					product_type_id, 
					COUNT(*) AS sales
				FROM {fct_listings}
				WHERE status_id = 15
				GROUP BY platform_id, product_type_id
			  ) sa 
		ON sa.platform_id = pl.platform_id
	LEFT JOIN (
				/*
				Same logic for product applies to platform, I'm using string_agg to get same product_id-s 
				in 1 row.
				*/
				SELECT 
					STRING_AGG(product_type_name, '/') AS product_type_name, 
					product_type_id 
				FROM {dim_product_type} 
				GROUP BY product_type_id
				) p 
		ON p.product_type_id = sa.product_type_id
)


/*
--In case the goal is to get in 1 row all products with same number of sales and to use dense_rank in that case query would be something like:

SELECT 
	Platform_Name AS Platform,
	STRING_AGG(product_type_name, ', ') AS Products,
	COALESCE(sales, 0) AS Sales -- in case where there is a platform with no sales, the row will and should be shown, but with 0 instead of NULL.
FROM Sales_Per_Platform_And_Product_Type
WHERE ranking <= 3
GROUP BY platform_name, COALESCE(sales, 0)
ORDER BY platform_name, sales DESC;
*/
/*
--In case the goal is to make a list of products
*/
SELECT 
	Platform_Name as Platform,
	product_type_name AS Products,
	COALESCE(sales, 0) AS Sales -- in case where there is a platform with no sales, the row will and should be shown, but with 0 instead of NULL.
FROM Sales_Per_Platform_And_Product_Type
WHERE ranking <= 3
ORDER BY platform_name, sales DESC;


"""
header = ["Platform", "Products", "Sales"]
# ...and view the results for that query:
cursor.execute(top_3_selling_products_by_platform).fetch_df().to_csv('answer_q02_1.csv', sep=';',columns = header, index=False);

# Bottom 3 selling products by platform
bottom_3_selling_products_by_platform = f"""--sql

/* NOTE: In this case I am using qualify instead of filtering rank later */

	/*
	Since products might have same number of sales, I'm using rank in order to get same ranking for 
	such products (versus to row_no) and to skip ranking in case there are same numbers for sales (versus to dense_rank).
    If the goal is something else - then I would use other functions, but I believe I can't decide myself, I 
    would have to align with the requester of KPI.
	*/
	SELECT 
		pl.Platform_Name AS Platform, 
        p.product_type_name AS Products, 
        sa.sales AS Sales,
        RANK() OVER (PARTITION BY pl.Platform_Name ORDER BY sa.sales ASC) AS ranking 
	FROM (
		SELECT 
			/*
			Since platform id is the same, but it's name changes over time, I'm using string_agg
			in order to get 1 value per platform type. Also, since the request was number of sales per 
			platform, I'm setting platform as a join base in case there is a platform with no sales
			*/
			STRING_AGG(platform, '/') AS platform_name, 
			platform_id 
		FROM {dim_platform} 
		GROUP BY platform_id
		) pl
	LEFT JOIN   (
				SELECT 
					platform_id, 
					product_type_id, 
					COUNT(*) AS sales
				FROM {fct_listings}
				WHERE status_id = 15
				GROUP BY platform_id, product_type_id
                ) sa 
		ON sa.platform_id = pl.platform_id
	LEFT JOIN   (
				/*
				Same logic for product applies to platform, I'm using string_agg to get same product_id-s 
				in 1 row.
				*/
				SELECT 
					STRING_AGG(product_type_name, '/') AS product_type_name, 
					product_type_id 
				FROM {dim_product_type} 
				GROUP BY product_type_id
				) p 
		ON p.product_type_id = sa.product_type_id
    QUALIFY 
         RANK() OVER (PARTITION BY pl.Platform_Name ORDER BY sa.sales ASC) <=3



"""
header = ["Platform", "Products", "Sales"]
# ...and view the results for that query:
cursor.execute(bottom_3_selling_products_by_platform).fetch_df().to_csv('answer_q02_2.csv', sep=';',columns = header, index=False);

# Top 3 idle products
top_3_idle_products_by_platform = f"""--sql


SELECT 
	product_type_name AS Products,
	COUNT(dates.date_key) AS Number_Of_Days,
	COUNT( 
            CASE 
				WHEN is_week_day = 1 and is_uk_holiday = 0
				THEN 1
			END
		) AS Number_Of_Working_Days
FROM	(
		SELECT 
			product_type_id,
			status_id,
			valid_from,
			ROW_NUMBER() OVER ( PARTITION BY product_type_id ORDER BY VALID_FROM DESC ) AS Sorting
		FROM {fct_listings} 
		) list 
	LEFT JOIN	(
				SELECT 
					STRING_AGG(product_type_name, '/') as product_type_name, 
					product_type_id 
				FROM {dim_product_type} 
				GROUP BY product_type_id
				) p 
		ON p.product_type_id = list.product_type_id
	LEFT JOIN {dim_date} dates 
		ON dates.date_key >= list.valid_from 
			AND dates.date_key < '2022-01-31'
WHERE list.status_id <> 10 
	AND Sorting = 1
GROUP BY product_type_name
ORDER BY Number_Of_Days DESC -- Depending on definition of KPI.
LIMIT 3;
"""
header = ["Products", "Number_Of_Days", "Number_Of_Working_Days"]
# ...and view the results for that query:
cursor.execute(top_3_idle_products_by_platform).fetch_df().to_csv('answer_q02_3.csv', sep=';',columns = header, index=False);



# Total amount sold by product type
total_amount_sold_by_product_type = f"""--sql


SELECT 
	product_type_name AS Products, 
	ROUND(SUM(CAST(replace(price, ',', '') AS FLOAT)), 2) AS Sold    
FROM (
	SELECT 
		STRING_AGG(product_type_name, '/') AS product_type_name, 
		product_type_id 
	FROM {dim_product_type} 
	GROUP BY product_type_id
	) p
	LEFT JOIN {fct_listings} l 
		ON p.product_type_id = l.product_type_id
WHERE status_id = 15
GROUP BY product_type_name
;

"""
header = ["Products", "Sold"]
# ...and view the results for that query:

cursor.execute(total_amount_sold_by_product_type).fetch_df().to_csv('answer_q02_4.csv', sep=';',columns = header, index=False, float_format = '%.2f');


# Top 3 cities by listings
top_3_cities_by_listings = f"""--sql

SELECT  
city, 
count(*) as num_of_listings
FROM 
{fct_listings} o
left join {dim_user}  pl
on pl.user_id = o.user_id and COALESCE(pl.valid_from, '2999-12-31')<=o.valid_from  
and COALESCE(pl.valid_to, '2999-12-31') >= o.valid_from
group by city
order by num_of_listings DESC
LIMIT 3
"""
header = ["city", "num_of_listings"]
# ...and view the results for that query:
cursor.execute(top_3_cities_by_listings).fetch_df().to_csv('answer_q02_5.csv', sep=';',columns = header, index=False);


# Snapshots of active listings per day
active_listings_per_day = f"""--sql

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
cursor.execute(active_listings_per_day).fetch_df().to_csv('answer_q02_6.csv', sep=';',index=False);
