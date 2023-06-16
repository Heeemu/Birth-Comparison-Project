SELECT res_touaca.YEAR, SUM(res_touaca.NUM) AS sum
FROM res_touaca
group by res_touaca.YEAR