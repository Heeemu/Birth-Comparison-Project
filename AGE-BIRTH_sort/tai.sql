select tai.YEAR as year,round( sum(tai.BIRTH*tai.NUM)/sum(tai.NUM),3) as avg_birth
from res_TAI as tai
group by tai.YEAR