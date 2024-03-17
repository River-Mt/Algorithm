select 
    a.apnt_no,
    (select p.pt_name from patient p where p.pt_no = a.pt_no) pt_name,
    a.pt_no,
    a.mcdp_cd,
    (select d.dr_name from doctor d where d.dr_id = a.mddr_id) dr_name,
    a.apnt_ymd
from appointment a
where 1=1
    and to_char(a.apnt_ymd, 'yyyy-mm-dd') = '2022-04-13'
    and a.apnt_cncl_yn = 'N'
    and a.mcdp_cd = 'CS'
order by a.apnt_ymd