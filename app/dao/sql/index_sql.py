index_sql = {
    "recommendedVolume": "SELECT c.commodity_name,c.commodity_component,c.commodity_price,c.capacity,c.com_img,c.save,t.tags_content from commodity as c LEFT JOIN tags as t on c.com_tags=t.tags_id WHERE c.commodity_texture_id={skinid} limit 4;",
    "hotDynamic":"SELECT u.user_nickname,d.title as 'tit',d.words,d.dynamic_images,d.cots,d.click as 'clicked',d.fbs from dynamic d LEFT JOIN `user` u on d.user_id=u.user_id ORDER BY d.click+d.fbs*2+d.cots*4 DESC LIMIT 7",
    "evaluationInformation":""
}
