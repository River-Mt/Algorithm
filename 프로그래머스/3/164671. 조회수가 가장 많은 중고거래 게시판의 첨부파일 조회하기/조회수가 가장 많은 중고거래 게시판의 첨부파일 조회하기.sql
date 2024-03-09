select 
    '/home/grep/src/' || b.board_id || '/' || f.file_id || f.file_name || f.file_ext FILE_PATH
from USED_GOODS_BOARD b, USED_GOODS_FILE f
where 1=1 
    and b.board_id = f.board_id
    and b.views = (select max(views) from USED_GOODS_BOARD)
order by f.file_id desc