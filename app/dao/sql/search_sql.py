search_sql = {
    "searchByProductName": "",
    "searchByComponent": "",
    "searchByFunction": "",
    "searchBySkin": "",
    "searchByDynamic": "",
    "hotSearch": "SELECT e.enterprise_name ,c.commodity_name ,c.com_img,c.click,c.fbs,c.cots from commodity as c LEFT JOIN enterprise as e on c.etp_id = e.id UNION ALL SELECT u.user_nickname,d.title,d.dynamic_images,d.click,d.fbs,d.cots from dynamic as d LEFT JOIN `user` as u on d.user_id=u.user_id  order by click desc LIMIT 20;",
    "hotDairy": "",
    "hotCosmetics": ""
}
