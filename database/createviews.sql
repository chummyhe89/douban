USE web_tag_douban;
/*create view of relation about songs and local tags */
drop view if EXISTS `v_re_songs_tags`;
create view v_re_songs_tags as select rst.sid as web_song_id,rst.title as web_song_name,rst.artist as web_singer_name,lti.local_tag_name as local_tag_name from local_tag_id as lti inner join re_songs_tags as rst on lti.local_tag_id = rst.tag_id;

drop view if exists `v_re_songs_vartags`;
create view `v_re_songs_vartags` AS select  `rsv`.`sid` AS `web_song_id`,  `rsv`.`title` AS `web_song_name`,  `rsv`.`artist` AS `web_singer_name`,  `lti`.`local_tag_name` AS `local_tag_name` from (`local_tag_id` `lti`  join `re_songs_vartags` `rsv`  on ((`lti`.`local_tag_id` = `rsv`.`tag_id`)));
