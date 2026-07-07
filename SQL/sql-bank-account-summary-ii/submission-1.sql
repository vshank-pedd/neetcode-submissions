-- Write your query below
select name, sum(amount) as balance
from users u
join transactions t on u.account = t.account
group by t.account, u.name
having sum(amount)>10000