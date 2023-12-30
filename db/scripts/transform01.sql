
-- load
insert into auto.ev_registration
select 
	state, 
	regexp_replace(reg_count_2020,'\,')::int,
	regexp_replace(pct_reg_count_2020,'\%')::numeric,
	regexp_replace(re_count_2021,'\,' )::int,
	regexp_replace(pct_reg_count_2021,'\%')::numeric,
	you_growth::numeric * 100
from auto.ev_registration_src;