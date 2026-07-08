-- Write your query below

select s.employee_id
from salaries s
left join employees e on s.employee_id = e.employee_id
where name is null

union

select e.employee_id
from employees e
left join salaries s on s.employee_id = e.employee_id
where salary is null

order by employee_id
