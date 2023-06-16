select tou.YEAR,tou.ACADEMIC,sum(tou.NUM) as NUM
from res_touaca as tou
group by tou.YEAR,tou.ACADEMIC
order by sum(tou.NUM)  desc