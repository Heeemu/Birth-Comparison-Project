select tai.YEAR,tai.ACADEMIC,round(sum(tai.BIRTH*tai.NUM)/sum(tai.NUM),2) as avg_birth
from res_TAI as tai
where tai.ACADEMIC <> 'TOTAL'
group by tai.ACADEMIC,tai.YEAR
