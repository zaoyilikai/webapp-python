-- schema.sql

drop database if exists webapp;

create database webapp;

use webapp;

grant select, insert, update, delete on webapp.* to `www-data`@`localhost` identified by 'www-data';

create table users(
		`id` varchar(50),
		`email` varchar(50) ,
		`passwd` varchar(50) ,
		`admin` bool ,
		`name` varchar(50) ,
		`image` varchar(500) ,
		`created_at` real ,
		unique key `idx_email` (`email`),
		key `idx_created_at` (`created_at`),
		primary key (`id`)
)engine=innodb default charset=utf8;


create table blogs(
		`id` varchar(50) ,
		`user_id` varchar(50) ,
		`user_name` varchar(50) ,
		`user_image` varchar(500) ,
		`name` varchar(50) ,
		`summary` varchar(200) ,
		`content` mediumtext ,
		`created_at` real ,
		key `idx_created_at` (`created_at`),
		primary key (`id`)
)engine=innodb default charset=utf8;

create table comments(
		`id` varchar(50) ,
		`blog_id` varchar(50) ,
		`user_id` varchar(50) ,
		`user_name` varchar(50) ,
		`user_image` varchar(500) ,
		`content` mediumtext ,
		`created_at` real ,
		key `idx_created_at` (`created_at`),
		primary key (`id`)
)engine=innodb default charset=utf8;
