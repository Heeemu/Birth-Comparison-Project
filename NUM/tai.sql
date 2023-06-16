SELECT res_TAI.YEAR, SUM(res_TAI.NUM) AS sum
from res_TAI
GROUP BY res_TAI.YEAR;