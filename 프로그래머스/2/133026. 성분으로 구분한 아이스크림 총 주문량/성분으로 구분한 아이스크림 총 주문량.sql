SELECT I.INGREDIENT_TYPE, SUM(H.TOTAL_ORDER)
FROM FIRST_HALF AS H NATURAL JOIN ICECREAM_INFO AS I
GROUP BY I.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER
