use test;
create table mark(id int(10) unsigned not null auto_increment primary key,
				  english tinyint unsigned not null comment'英语成绩',
                  mathematics tinyint unsigned not null comment'数学成绩',
                  chinese tinyint unsigned not null comment'语文成绩',
                  stu_id int(10) unsigned not null comment'学生id'
				 );

insert into mark(english,mathematics,chinese,stu_id) values(98,99,100,1);
insert into mark(english,mathematics,chinese,stu_id) values(78,99,100,2);
insert into mark(english,mathematics,chinese,stu_id) values(100,100,100,3);
insert into mark(english,mathematics,chinese,stu_id) values(100,99,80,4);

select * from mark;
select * from student;