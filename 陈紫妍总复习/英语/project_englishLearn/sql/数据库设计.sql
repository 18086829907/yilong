drop database english_learn;

create database english_learn charset='utf8';

use english_learn;


# 单词与句子
create table word_and_sentence(
    id int unsigned auto_increment primary key,
    id_grade int unsigned not null,
    id_type int unsigned not null,
    id_unit int unsigned not null,
    word varchar(50) not null,
    translate varchar(50) not null
);

# insert into word_and_sentence value
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', ''),
#     (0, 7, 1, 1, '', '');

# 单元表
create table unit(
    id int unsigned auto_increment primary key,
    unit char(6) not null
);

insert into unit value
    (0, 'Unit_1'),
    (0, 'Unit_2'),
    (0, 'Unit_3'),
    (0, 'Unit_4'),
    (0, 'Unit_5'),
    (0, 'Unit_6'),
    (0, 'Unit_7');


# 单词/句子类型表
create table idWord_idSentence(
    id int unsigned auto_increment primary key,
    type varchar(8) not null
);

insert into idWord_idSentence value
    (0, 'word'),
    (0, 'sentence');


# 年级表
create table grade(
    id int unsigned auto_increment primary key,
    grade varchar(20) not null
);

insert into grade value
    (0, '小学一年级上册'),(0, '小学一年级下册'),
    (0, '小学二年级上册'),(0, '小学二年级下册'),
    (0, '小学三年级上册'),(0, '小学三年级下册'),
    (0, '小学四年级上册'),(0, '小学四年级下册'),
    (0, '小学五年级上册'),(0, '小学五年级下册'),
    (0, '小学六年级上册'),(0, '小学六年级下册'),
    (0, '初中一年级上册'),(0, '初中一年级下册'),
    (0, '初中二年级上册'),(0, '初中二年级下册'),
    (0, '初中三年级上册'),(0, '初中三年级下册'),
    (0, '高中一年级上册'),(0, '高中一年级下册'),
    (0, '高中二年级上册'),(0, '高中二年级下册'),
    (0, '高中三年级上册'),(0, '高中三年级下册'),
    (0, '大学一年级上册'),(0, '大学一年级下册'),
    (0, '大学二年级上册'),(0, '大学二年级下册'),
    (0, '大学三年级上册'),(0, '大学三年级下册'),
    (0, '大学四年级上册'),(0, '大学四年级下册'),
    (0, '博士一年级上册'),(0, '博士一年级下册'),
    (0, '博士二年级上册'),(0, '博士二年级下册'),
    (0, '博士三年级上册'),(0, '博士三年级下册'),
    (0, '博士四年级上册'),(0, '博士四年级下册')
