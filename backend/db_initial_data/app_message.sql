insert into app_message (message_text, dttm, user_id)
select 
	md5(random()::text),
	now() - random() * interval '365 days',
	(select id from app_user where full_name='Генри Чинаски')
from generate_series(1, 1000);

insert into app_message (message_text, dttm, user_id)
select 
	md5(random()::text),
	now() - random() * interval '365 days',
	(select id from app_user where full_name='Стрелок Роланд') 
from generate_series(1, 1000);
