-- Write your query below
Select person.first_name, person.last_name, address.city, address.state
from person
left join address on address.person_id = person.person_id