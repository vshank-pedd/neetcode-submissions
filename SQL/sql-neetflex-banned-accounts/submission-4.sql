-- Write your query below
select distinct l1.account_id
from log_info l1 
join log_info l2 on l1.account_id = l2.account_id and l1.ip_address <> l2.ip_address and l1.login <= l2.logout and l1.logout >= l2.login