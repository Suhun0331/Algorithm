SELECT B.ID, B.GENOTYPE, A.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS A JOIN ECOLI_DATA AS B ON A.ID = B.PARENT_ID
WHERE A.GENOTYPE & B.GENOTYPE = A.GENOTYPE
ORDER BY ID