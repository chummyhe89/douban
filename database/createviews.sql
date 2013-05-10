USE douban;
/*create view of relation about songs and local tags */
drop view if EXISTS `v_re_songs_tags`;
create view v_re_songs_tags as select rst.sid as web_song_id,rst.title as web_song_name,rst.artist as web_singer_name,lti.local_tag_name as local_tag_name from local_tag_id as lti inner join re_songs_tags as rst on lti.local_tag_id = rst.tag_id;
