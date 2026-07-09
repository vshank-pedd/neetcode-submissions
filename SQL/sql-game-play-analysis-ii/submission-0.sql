-- Write your query below
select t.player_id, t.device_id
from (
    select a.player_id, a.device_id, row_number() over (partition by a.player_id order by a.event_date asc) as ranks
    from activity a
) t
where t.ranks = 1
