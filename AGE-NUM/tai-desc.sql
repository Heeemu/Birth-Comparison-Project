select res_TAI.YEAR,res_TAI.AGE,sum(res_TAI.NUM) as num
from res_TAI
where res_TAI.AGE <> 'SUM' 
group by res_TAI.YEAR,res_TAI.AGE 
order by sum(res_TAI.NUM) desc