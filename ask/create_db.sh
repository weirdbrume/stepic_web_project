#!/usr/bin/env bash
sudo mysql -u root -e "create database if not exists box_db default character set utf8 collate utf8_general_ci;
create user 'box'@'localhost' identified by 'password';
grant all privileges on box_db . * to 'box'@'localhost';
flush privileges;"