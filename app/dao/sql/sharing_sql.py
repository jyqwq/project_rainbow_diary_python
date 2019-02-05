sharing_sql = {
    "evaluationIndex":"",
    "graphicDy":"INSERT into dynamic(user_id,words,dynamic_images,tags) VALUES ({user_id},'{content}','{img}','{tags}')",
    "graphicDairy":"INSERT into journal(user_id,title,words,images,tags) VALUES ({user_id},'{title}','{content}','{img}','{tags}')",
    "graphicTest1":"insert into commodity_test_main (title,content,user_id,tags,img) VALUES('{main_title}','{main_content}',{user_id},'{tags}','{img}')",
    "graphicTest2":"INSERT into commodity_test_subtitle (title,content,main_id) VALUES ('{title1}','{content1}',{test_id}),('{title2}','{content2}',{test_id})",
    "getTag":"SELECT tags_id from tags WHERE tags_content='{tag_name}'",
    "getCom":"SELECT id from commodity WHERE commodity_name='{com_name}'"
}
