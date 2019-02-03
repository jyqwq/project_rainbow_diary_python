sharing_sql = {
    "graphicDynamic": "",
    "evaluationIndex":"",
    "graphicDy":"",
    "graphicDairy":"",
    "graphicTest1":"insert into commodity_test_main (commodity_id,title,content,user_id,tags,img) VALUES({com_id},'{main_title}','{main_content}',{user_id},'{tags_id}','{img}')",
    "graphicTest2":"INSERT into commodity_test_subtitle (title,content,main_id) VALUES ('{title1}','{content1}',{test_id}),('{title2}','{content2}',{test_id})",
    "getTag":"SELECT tags_id from tags WHERE tags_content='{tag_name}'",
    "getCom":"SELECT id from commodity WHERE commodity_name='{com_name}'"
}
