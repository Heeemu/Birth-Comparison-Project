select RES_TNAN.YEAR ,sum(RES_TNAN.NUM)as sum
from RES_TNAN
group by RES_TNAN.YEAR