-- 1、
-- 创建产品分类表
create table if not exists goods_cate(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);

-- 查询goods表中商品的种类
select cate_name from goods group by cate_name;

-- 将分组结果写入到goods_cate数据表中
-- 原本应该加value，但是value后面是从一张表中查出来的结果，则一定不要加value
-- insert into goods_cate(name) values select cate_name from goods group by cate_name;
insert into goods_cate (name) select cate_name from goods group by cate_name;

-- 将goods.cate_name修改为goods_cate.id
update goods as g inner join goods_cate as c on g.cate_name=c.name set g.cate_name=c.id;

-- 修改表结构
alter table goods change cate_name cate_id int unsigned not null;

-- 添加外键约束
alter table goods add foreign key (cate_id) references goods_cate(id);

-- 取消外键约束（在实际开发中，很少会使用到外键约束，会极大的降低表更新的效果）
show create table goods;
alter table goods drop foreign key goods_ibfk_1;  -- 通过上面语句查询得到的外键名称


-- 2、
-- 创建品牌表
create table if not exists goods_brand(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);

-- 查询goods表中品牌的种类
select brand_name from goods group by brand_name;

-- 将分组结果写入到goods_brand数据表中
insert into goods_brand(name) select brand_name from goods group by brand_name;

-- 将goods.brand_name修改为goods_brand.id
update goods as g inner join goods_brand as b on g.brand_name=b.name set g.brand_name=b.id;

-- 修改表结构
alter table goods change brand_name brand_id int unsigned not null;

-- 添加外键约束
alter table goods add foreign key (brand_id) references goods_brand(id);

-- 取消外键约束（在实际开发中，很少会使用到外键约束，会极大的降低表更新的效果）
show create table goods;
alter table goods drop foreign key goods_ibfk_2;  -- 通过上面语句查询得到的外键名称

