-- Write your query below
select player_id, player_name, 
   count(case when c.wimbledon = p.player_id then 1 end) 
    + count(case when c.fr_open = p.player_id then 1 end) 
    + count(case when c.us_open = p.player_id then 1 end) 
    + count(case when c.au_open = p.player_id then 1 end) as grand_slams_count
from players p
join championships c on p.player_id = c.wimbledon or c.fr_open = p.player_id or c.us_open = p.player_id or c.au_open = p.player_id
group by player_id, player_name
