-- create database stock_db charset=utf8;
-- use stock_db;

create table focus(
    id int unsigned not null primary key auto_increment,
    note_info varchar(100),
    info_id int unsigned
);

create table info(
    id int unsigned not null primary key auto_increment,
    code varchar(10) not null,
    short varchar(20) not null,
    chg varchar(10) not null,
    turnover varchar(10) not null,
    price decimal(5,2) not null,
    hights decimal(5,2) not null,
    time date not null
);

insert into focus value
    (0, '你确定买这个？', 36),
    (0, '利好', 37);

insert into info value
    (0, '000007', '全新好', '10.01%', '4.40%', 16.05, 14.60, '2017-07-18'),
    (0, '000036', '华联控股', '10.04%','10.80%', 11.29, 10.26, '2017-07-18');


create view stock_center as select i.code,i.short,i.chg,i.turnover,i.price,i.hights,f.note_info from info as i inner join focus as f on i.id = f.info_id;

insert into info value
    (0, '600408', '安泰集团', '1.98%', '3.38%', 4.13, 4.22, '2017-04-08'),
    (0, '600436', '三友化工', '0.64%','17.80%', 5.29, 13.26, '2017-09-18');


insert into info value
    (0, '600499', '科达节能', '1.98%', '3.38%', 4.13, 4.22, '2017-04-08'),
    (0, '600966', '博汇纸业', '0.64%','17.80%', 5.29, 13.26, '2017-09-18');