select tnan.YEAR as year,round( sum(tnan.BIRTH*tnan.NUM)/sum(tnan.NUM),3) as avg_birth
from RES_TNAN as tnan
group by tnan.YEAR