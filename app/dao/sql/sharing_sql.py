sharing_sql = {
    "evaluationIndex":"SELECT m.user_id,m.title,m.content,m.click,m.cots,m.fbs,m.img,GROUP_CONCAT(s.title SEPARATOR '&') as f_title from commodity_test_main as m  LEFT JOIN commodity_test_subtitle as s on m.id=s.main_id GROUP BY m.title ORDER BY m.click DESC LIMIT 10",
    "graphicDy":"INSERT into dynamic(user_id,words,dynamic_images,tags,data) VALUES ({user_id},'{content}','{img}','{tags}','{data}')",
    "graphicDairy":"INSERT into journal(user_id,title,words,images,tags,data) VALUES ({user_id},'{title}','{content}','{img}','{tags}','{data}')",
    "graphicTest1":"insert into commodity_test_main (title,content,user_id,tags,img,data) VALUES('{main_title}','{main_content}',{user_id},'{tags}','{img}','{data}')",
    "graphicTest2":"INSERT into commodity_test_subtitle (title,content,main_id) VALUES ('{title1}','{content1}',{test_id}),('{title2}','{content2}',{test_id})",
    "getTag":"SELECT tags_id from tags WHERE tags_content='{tag_name}'",
    "getCom":"SELECT id from commodity WHERE commodity_name='{com_name}'"
}
