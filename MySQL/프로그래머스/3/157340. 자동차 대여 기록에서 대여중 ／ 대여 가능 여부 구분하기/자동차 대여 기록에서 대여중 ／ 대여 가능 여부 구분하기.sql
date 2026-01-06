SELECT
    CAR_ID,
    CASE
        WHEN MAX(CASE
                    WHEN START_DATE <= '2022-10-16'
                     AND END_DATE   >= '2022-10-16'
                    THEN 1 ELSE 0
                 END) = 1
        THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;

-- START_DATE ≤ '2022-10-16' ≤ END_DATE 이면 대여중
-- 그 외는 대여 가능
-- 출력은 자동차별(CAR_ID별) 1행이어야 함(히스토리는 여러 행이라 그대로 뽑으면 중복 발생)