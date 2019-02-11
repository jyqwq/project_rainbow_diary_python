search_sql = {
    "searchByProductName": "",
    "searchByComponent": "",
    "searchByFunction": "",
    "searchBySkin": "",
    "searchByDynamic": "",
    "hotSearch": "",
    "hotDairy": "SELECT click,cots,fbs,images,user_id,title from journal ORDER BY (click+cots*2+fbs*4) DESC LIMIT 10",
    "hotCosmetics": "SELECT commodity_name,com_img,click,cots,fbs from commodity as c ORDER BY (click+cots*2+fbs*4) DESC LIMIT 10",
    "getUserName":"SELECT user_nickname FROM `user` WHERE user_id={user_id}"
}
