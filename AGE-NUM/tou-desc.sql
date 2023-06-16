select res_TOU_age.YEAR,res_TOU_age.AGE,sum(res_TOU_age.NUM) as num
from res_TOU_age
group by res_TOU_age.YEAR,res_TOU_age.AGE 
order by sum(res_TOU_age.NUM) desc