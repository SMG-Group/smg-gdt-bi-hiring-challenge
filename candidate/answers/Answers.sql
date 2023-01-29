/*
The provided data files I've imported into SQL Server, and all queries are in T-SQL dialect.
The most intriguing part is how to interpret Statuses. Since there aren't any other data (quantities)
that could be used for Q2 answers the statuses are the only atribute that we can rely upon, and how
are statuses interpreted greately affects answers.

I've assumed following:
	Active - On stock and activly sold
	Inactive - On stock but not sold (no demand)
	Sold - Sold out, not on stock (and thus not sold)

Question 1. 
No dilemma here.

Question 2.
For some of the answers here I used already prepared query from Q1, just without time span where clause.

a) How to determine top selling products without quantities? Those with status Inactive or Cancelled aren't sold for sure.
   Does change of status from Active to Sold indicates that a product is top seller? Maybe, but most probably indicates bad
   supply, and all products which have in some periods Sold status have more days in Sold status than in Active status. 
   Therefore I've decided to calculate best sellers by number of days in Active status.

b) After decisions about a), it is clear that bottom sellera are those with the most days in statuses oter than Active.

c) What would be idle products? Idle-stock? I guess that would be those in Inactive status. 

d) This can't be calculated. We would need quantities given to calculate this.

e) I've prepared two additional calculations. Top 3 products that most ofen goes into Sold status (might be interesting for procurement). 
   And top 3 products with the biggest percentage price drop. We can see that it is good idea to wait until January to buy skiis.

Question 3.
For visalisations I'have used Excel. Simle neat charts to give clear insigts to management. In real situation I'd use Looker (or simillar) 
but for these simple insights I believe Excel is quite good tool.

*/

--Question 1.

select	d.date_key, p.platform_id, t.product_type_id, l.price, l.status_id
from	dim_date as d
cross join (select distinct platform_id from dim_platform) as p
cross join (select distinct product_type_id from dim_product_type) as t
cross apply (select top 1 *
			 from	fct_listings as f
			 where	f.platform_id = p.platform_id
			 and	f.product_type_id = t.product_type_id
			 and	d.date_key between f.valid_from and isnull(f.valid_to, '2200.01.01')
			 order by f.listing_date_key desc, listing_id desc, isnull(f.valid_to, '2200.01.01') desc
			) as l
where	d.date_key between '2021.12.01' and '2022.01.31'
order by date_key, platform_id, product_type_id


-- Question 2.
drop table if exists #snaps
select	d.date_key, p.platform_id, t.product_type_id, l.price, l.status_id
into #snaps
from	dim_date as d
cross join (select distinct platform_id from dim_platform) as p
cross join (select distinct product_type_id from dim_product_type) as t
cross apply (select top 1 *
			 from	fct_listings as f
			 where	f.platform_id = p.platform_id
			 and	f.product_type_id = t.product_type_id
			 and	d.date_key between f.valid_from and isnull(f.valid_to, '2200.01.01')
			 order by f.listing_date_key desc, listing_id desc, isnull(f.valid_to, '2200.01.01') desc
			) as l
order by date_key, platform_id, product_type_id

-- a)
;with cte as
(
select	p.platform, t.product_type_name, count(*) as active_days
from	#snaps as s
join	dim_platform as p 
	on p.platform_id = s.platform_id and 
		p.valid_to is null
join	dim_product_type as t 
	on t.product_type_id = s.product_type_id and 
		t.valid_to is null
where	s.status_id = 10	-- Active
group by p.platform, t.product_type_name
)
, cte2 as
(
select	*, row_number() over(partition by platform order by active_days desc) as rn
from	cte
)
select	*
from	cte2
where	rn <= 3

-- b)
;with cte as
(
select	p.platform, t.product_type_name, count(*) as non_active_days
from	#snaps as s
join	dim_platform as p 
	on p.platform_id = s.platform_id and 
		p.valid_to is null
join	dim_product_type as t 
	on t.product_type_id = s.product_type_id and 
		t.valid_to is null
where	s.status_id <> 10
group by p.platform, t.product_type_name
)
, cte2 as
(
select	*, row_number() over(partition by platform order by non_active_days desc) as rn
from	cte
)
select	*
from	cte2
where	rn <= 3

-- c)
;with cte as
(
select	t.product_type_name, count(*) inactive_days
from	#snaps as s
join	dim_product_type as t 
	on t.product_type_id = s.product_type_id and 
		t.valid_to is null
where	s.status_id = 20
group by t.product_type_name
)
, cte2 as
(
select	*, row_number() over(order by inactive_days desc) as rn
from	cte
)
select	*
from	cte2
where	rn <= 3

-- d)
select null

-- e)
;with cte as
(
select	*, 
		LAG(status_id) over(partition by platform_id, product_type_id order by listing_date_key) as previous_status
from	fct_listings as s
)
select	t.product_type_name, 
		count(*) as cnt
from	cte as c
join	dim_platform as p on p.platform_id = c.platform_id and p.valid_to is null
join	dim_product_type as t on t.product_type_id = c.product_type_id and t.valid_to is null
where	status_id = 15
and		previous_status = 10
group by t.product_type_name
order by cnt desc


select top 3 platform, product_type_name, [2021.12.31], [2022.01.31], [2022.02.28], [2022.03.31]
		,[2022.03.31] - isnull([2021.12.31], [2022.01.31]) as diff
		, ([2022.03.31] - isnull([2021.12.31], [2022.01.31])) / isnull([2021.12.31], [2022.01.31]) as diff2
from 
	(
	select	platform, product_type_name, date_key, price
	from	#snaps as s
	join	dim_platform as p on p.platform_id = s.platform_id and p.valid_to is null
	join	dim_product_type as t on t.product_type_id = s.product_type_id and t.valid_to is null
	where	date_key in ('2021.12.31', '2022.01.31', '2022.02.28', '2022.03.31')
	) as tbl
pivot (max(price) for date_key in ([2021.12.31], [2022.01.31], [2022.02.28], [2022.03.31])) as pvt
order by diff2 asc