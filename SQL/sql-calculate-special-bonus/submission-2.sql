-- Write your query below
Select employee_id,
    Case 
        When MOD(employee_id,2)=1 and name not like 'M%' Then salary
        else 0
    end as bonus
From employees
order by employee_id