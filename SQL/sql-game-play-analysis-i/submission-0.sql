-- Write your query below
select player_id, min(event_date) as first_login
from activity a
group by player_id