select tai.YEAR,tai.ACADEMIC,sum(tai.NUM) as NUM
from res_TAI as tai 
where tai.ACADEMIC <> 'TOTAL'
group by tai.YEAR,tai.ACADEMIC
order by sum(tai.NUM) desc