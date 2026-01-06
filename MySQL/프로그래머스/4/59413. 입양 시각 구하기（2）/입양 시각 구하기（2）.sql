-- ANIMAL_OUTS에 존재하는 시간만 출력하기 때문에 시간 테이블을 만들고 시작해야 함

-- 0~23시까지의 "시간 기준 테이블"을 생성하기 위한 재귀 CTE
-- 목적:
-- 1) ANIMAL_OUTS 테이블에 데이터가 없는 시간도 결과에 포함시키기 위함
-- 2) GROUP BY는 존재하는 데이터만 그룹화하므로,
--    반드시 기준이 되는 시간 축(0~23)을 먼저 만들어야 함

WITH RECURSIVE HOURS AS (
    -- 초기값 (Anchor member)
    -- 재귀의 시작점
    -- hour = 0부터 시작
    SELECT 0 AS HOUR

    UNION ALL

    -- 재귀 부분 (Recursive member)
    -- 이전 단계에서 만든 HOUR 값에 +1
    -- HOUR < 23 조건이 없으면 무한 루프 발생
    SELECT HOUR + 1
    FROM HOURS
    WHERE HOUR < 23
)
-- HOUR < 23 이면, HOUR + 1 을 만듦


-- 시간 테이블(HOURS)을 기준으로 실제 데이터 테이블과 LEFT JOIN
-- LEFT JOIN을 사용해야 데이터가 없는 시간도 유지됨
SELECT 
    H.HOUR,
    COUNT(A.DATETIME) AS COUNT
FROM HOURS H
LEFT JOIN ANIMAL_OUTS A
    -- ANIMAL_OUTS의 DATETIME에서 시간(hour)을 추출하여 매칭
    ON HOUR(A.DATETIME) = H.HOUR
GROUP BY H.HOUR
ORDER BY H.HOUR
;


