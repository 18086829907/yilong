-- 创建数据库
create database jing_dong charset=utf8;

-- 使用数据库
use jing_dong;

-- 创建一个商品goods数据表
create table goods(
    id int unsigned primary key auto_increment not null ,
    name varchar(150) not null,
    cate_name varchar(40) not null ,
    brand_name varchar(40) not null,
    price decimal(10, 3) not null default 0,
    is_show bit not null default 1,  -- 是否显示，0不显示，1显示
    is_saleoff bit not null default 0  -- 是否售罄，0未售罄，1售罄
);

-- 插入数据
insert into goods value
(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default),
(0,'y400n 14.0英寸笔记本','笔记本','联想','4999',default,default),
(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default),
(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);

-- 查询cate_name为'笔记本'的商品名称、价格
select name,price from goods where cate_name='笔记本';
select name as 商品名称,price as 商品价格 from goods where cate_name='笔记本';

-- 显示商品种类
select distinct cate_name from goods;  -- 去重方式查询
select cate_name from goods group by cate_name;  -- 分组方式查询
select cate_name, group_concat(name,price) from goods group by cate_name;  -- 分组方式查询

-- 显示所有电脑产品的平均价格，并且保留两位小数
select round(avg(price),2) from goods;

-- 显示每种商品的平均价格，并且保留两位数
select cate_name, round(avg(price),2) from goods group by cate_name;

-- 查询每种类型的商品中 最贵的、最便宜的、平均价、数量
select cate_name,max(price),min(price),avg(price*10000)/10000,count(*) from goods group by cate_name;

-- 查询所有价格大于平均价格的商品，并且按照价格降序排序 -- 子查询，即sql语句中包含sql语句的sql语句
select * from goods where price > (select round(avg(price),2) from goods) order by price desc;

-- 查询每种类型中最贵的商品信息
select * from goods inner join (select max(price) as max_price from goods group by cate_name) as goods2 on goods.price = goods2.max_price;
select g.id, g.name, g2.cate_name, g.price  from (select cate_name,max(price) as max_price from goods group by cate_name) as g2 left join goods as g on g2.max_price=g.price and g2.cate_name=g.cate_name;
