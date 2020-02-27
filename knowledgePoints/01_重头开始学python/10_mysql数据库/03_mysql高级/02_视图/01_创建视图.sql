-- 视图：一张（虚拟）表，通过复杂sql语句查出来的结果，生成一张表

-- 复杂sql语句
select * from goods as g left join goods_cates as c on g.cates_id=c.id left join goods_brands as b on g.brand_id=b.id;

-- 将复杂sql语句查询出来的结果添加成视图
create view v_goods_info as select g.*,c.name,b.name from goods as g left join goods_cates as c on g.cates_id=c.id left join goods_brands as b on g.brand_id=b.id;

-- 视图v_goods_info就真的被创建为一张表，存放于jing_dong数据库中，通过show tables;可以查看到
select * from v_goods_info;
select * from v_goods_info where id=5;
select * from v_goods_info where price>20 limit(5,5);
select * from v_goods_info where price>20 limit(5,5) order by price desc;
select * from v_goods_info group by cates_name having price>20;
-- 视图创建好之后，就能很方便的查询到数据。
-- 特别注意，视图没有修改功能。即update v_goods_info set name='新款dvd' where id=23;

-- 删除视图
drop view v_goods_info

-- 视图的作用
-- 1、提高了重用性，就像一个函数
-- 2、对数据库重构，却不影响程序的运行
-- 3、提高了安全性能，可以对不同的用户。创建视图给开发者，视图中可以仅仅给到开发者必要的数据信息，而重要的数据，对其设置权限。这样就做到了敏感信息的安全
-- 4、让数据（可读性）更加清晰

-- 视图的理解
-- 我们python程序的sql语句是对视图进行查询的，比如select * from v_goods_info
-- 当我们需要对数据库进行修改时，就在创建一张新的同名视图，去替换旧的视图
-- 这样就做到了，修改数据库结构，也不用去修改python程序中的sql语句，成功解耦

-- 视图仅仅是一张虚拟的视图，它记录的是查询的方法，更生成器相同，调用它时才会产生数据
-- 同样的，如果数据表中的数据被修改后，再用视图去查数据，查出来的结果是数据被修改后的结果