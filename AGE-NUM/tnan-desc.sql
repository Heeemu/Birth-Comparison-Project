select RES_TNAN.YEAR,RES_TNAN.AGE,sum(RES_TNAN.NUM) as num
from RES_TNAN 
where RES_TNAN.AGE <> 'SUM' 
group by RES_TNAN.YEAR,RES_TNAN.AGE 
order by sum(RES_TNAN.NUM) desc