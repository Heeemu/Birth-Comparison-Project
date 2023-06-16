select tou.YEAR,tou.ACADEMIC,round(sum(tou.BIRTH*tou.NUM)/sum(tou.NUM),2) as avg_birth
from res_touaca as tou
group by tou.ACADEMIC,tou.YEAR
order by avg_birth desc