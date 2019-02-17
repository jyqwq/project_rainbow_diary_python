search_sql = {
    "searchByProductName": "SELECT * from commodity  WHERE commodity.commodity_name like '%{keyword}%' and commodity.category_id={category_id};",
    "searchAll": "SELECT * from commodity  WHERE commodity.commodity_name like '%{keyword}%'",
    "searchByComponent": "",
    "searchByFunction": "",
    "searchBySkin": "",
    "searchByDynamic": "",
    "hotSearch": "SELECT j.title,j.click,j.images,j.cots,j.fbs,j.user_id,'日记' as t_name from journal j UNION ALL SELECT d.words,d.click,d.dynamic_images,d.cots,d.fbs,d.user_id,'心情' as t_name from dynamic d UNION ALL SELECT c.title,c.click,c.img,c.cots,c.fbs,c.user_id ,'测评' as t_name from commodity_test_main as c ORDER BY click DESC LIMIT 10",
    "hotDairy": "SELECT click,cots,fbs,images,user_id,title from journal ORDER BY (click+cots*2+fbs*4) DESC LIMIT 10",
    "hotCosmetics": "SELECT commodity_name,com_img,click,cots,fbs from commodity as c ORDER BY (click+cots*2+fbs*4) DESC LIMIT 10",
    "getUserName":"SELECT user_nickname FROM `user` WHERE user_id={user_id}",
    "hotKeyword":"SELECT s.search_content from search as s GROUP BY s.search_content ORDER BY COUNT(*) DESC LIMIT 20",
    "recordKeyword":""
}
