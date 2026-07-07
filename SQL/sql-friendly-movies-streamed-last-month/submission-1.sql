-- Write your query below
select distinct title
from content c
join tv_program t on t.content_id = c.content_id
where program_date like '2020-06%' and kids_content = 'Y' and content_type = 'Movies'