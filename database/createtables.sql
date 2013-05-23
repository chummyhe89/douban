create database if not exists `web_tag_douban`;
use `web_tag_douban`;

create table if not exists `local_tag_id`;
CREATE TABLE `local_tag_id` (
  `local_tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `local_tag_name` varchar(100) NOT NULL,
  PRIMARY KEY (`local_tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

create table if not exists `re_songs_tags`;
CREATE TABLE `re_songs_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `artist` varchar(100) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sid` (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

create table if not exists `re_songs_vartags`;
CREATE TABLE `re_songs_vartags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `title` varchar(512) NOT NULL,
  `artist` varchar(256) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sid` (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

