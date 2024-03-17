


select (select z.member_name from member_profile z where z.member_id = a.member_id) member_name
, a.review_text 
, to_char(a.review_date, 'yyyy-mm-dd') review_date
from rest_review a
where a.member_id in (
    select member_id
    from rest_review 
    group by member_id
    having count(member_id) = (select max(count(member_id)) from rest_review group by member_id)
) 
order by review_date, review_text