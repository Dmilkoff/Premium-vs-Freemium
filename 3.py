with download_paying as (select t.*,
mad.paying_customer 
from
ms_download_facts t
left join ms_user_dimension mud on t.user_id =
mud.user_id
left join ms_acc_dimension mad on mud.acc_id =
mad.acc_id
),

paying_agg as (

select t.date, sum(t.downloads) as downloads
    from download_paying t
where t.paying_customer = 'yes'
group by t.date
order by t.date),

nonpaying_agg as (

select t.date, sum(t.downloads) as downloads
    from download_paying t
where t.paying_customer = 'no'
group by t.date
order by t.date)

select t.date,
t.downloads as paying,
na.downloads as nonpaying 
from paying_agg t

left join nonpaying_agg na on t.date = na.date
where na.downloads >  t.downloads