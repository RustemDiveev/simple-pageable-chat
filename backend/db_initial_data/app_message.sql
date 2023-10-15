insert into app_message (message_text, dttm, user_id)
select 
	md5(random()::text),
	now() - random() * interval '365 days',
	1 
from generate_series(1, 1000);

insert into app_message (message_text, dttm, user_id)
select 
	md5(random()::text),
	now() - random() * interval '365 days',
	2 
from generate_series(1, 1000);
