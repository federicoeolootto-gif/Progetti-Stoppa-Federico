-- All records are fabricated. PostgreSQL 13+ syntax.
-- 1. Monthly creation volume by team.
SELECT DATE_TRUNC('month', opened_at)::date AS opened_month,
       team, COUNT(*) AS tickets_opened
FROM support_tickets
GROUP BY 1, 2 ORDER BY 1, 2;

-- 2. First-view delay in hours, calculated for observed first views only.
SELECT team, COUNT(first_viewed_at) AS tickets_with_first_view,
       ROUND(AVG(EXTRACT(EPOCH FROM (first_viewed_at - opened_at)) / 3600.0)::numeric, 2)
           AS avg_first_view_hours
FROM support_tickets
GROUP BY team ORDER BY team;

-- 3. Monthly closures and resolution time; unresolved tickets are not falsely
-- classified as zero-hour resolutions.
SELECT DATE_TRUNC('month', closed_at)::date AS closed_month,
       team, COUNT(*) AS tickets_closed,
       ROUND(AVG(EXTRACT(EPOCH FROM (closed_at - opened_at)) / 3600.0)::numeric, 2)
           AS avg_resolution_hours
FROM support_tickets
WHERE status = 'Closed'
GROUP BY 1, 2 ORDER BY 1, 2;

-- 4. Share of ticket records per ASSIGNED operator within each team.
-- The dataset does not prove who opened or closed a ticket.
WITH assigned AS (
 SELECT team, operator_id, COUNT(*) AS assigned_tickets
 FROM support_tickets GROUP BY team, operator_id
)
SELECT team, operator_id, assigned_tickets,
       ROUND(100.0 * assigned_tickets /
                 NULLIF(SUM(assigned_tickets) OVER (PARTITION BY team), 0), 1)
           AS pct_of_team_assignments
FROM assigned ORDER BY team, assigned_tickets DESC;

-- 5. Open ticket aging at a FIXED reproducible snapshot date.
SELECT team, COUNT(*) AS unresolved,
       ROUND(AVG(EXTRACT(EPOCH FROM (TIMESTAMP '2026-10-22 00:00:00' - opened_at)) / 86400.0)::numeric, 1)
           AS avg_open_age_days
FROM support_tickets
WHERE status = 'Open' AND opened_at <= TIMESTAMP '2026-10-22 00:00:00'
GROUP BY team ORDER BY team;
