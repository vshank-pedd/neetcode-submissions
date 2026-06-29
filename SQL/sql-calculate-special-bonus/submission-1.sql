-- Write your query below
Select employee_id,
    Case
        When Mod(employee_id,2) = 1 and name not like 'M%' then salary
        else 0
    End as Bonus
from employees
Order by employee_id
