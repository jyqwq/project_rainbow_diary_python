index_sql = {
    "recommendedVolume": "SELECT c.id,c.commodity_name,c.commodity_component,c.commodity_price,c.capacity,c.com_img,c.save,t.tags_content from commodity as c LEFT JOIN tags as t on c.com_tags=t.tags_id WHERE c.commodity_texture_id={skinid} limit 4;",
    "hotDynamic":"SELECT u.user_nickname,j.id,j.title as 'tit',j.words,j.images,j.cots,j.click as 'clicked',j.fbs from journal j LEFT JOIN `user` u on j.user_id=u.user_id ORDER BY j.click+j.fbs*2+j.cots*4 DESC LIMIT 7",
    "evaluationInformation":"SELECT id,title,img FROM commodity_test_main ORDER BY (click+cots*2+fbs*4) DESC LIMIT 5"
}
