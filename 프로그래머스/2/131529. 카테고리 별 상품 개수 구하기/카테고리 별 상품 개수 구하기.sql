SELECT SUBSTR(PRODUCT_CODE,1,2) AS CATEROGY, COUNT(*)
FROM PRODUCT
GROUP BY CATEROGY
ORDER BY PRODUCT_CODE
