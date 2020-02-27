/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/2/15 16:48:18                           */
/*==============================================================*/


alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods_cates_2 
   drop foreign key FK_GOODS_CA_REFERENCE_GOODS_CA;

alter table goods_cates_3 
   drop foreign key FK_GOODS_CA_REFERENCE_GOODS_CA;

alter table goods_cates_4 
   drop foreign key FK_GOODS_CA_REFERENCE_GOODS_CA;

alter table orders 
   drop foreign key FK_ORDERS_REFERENCE_CUSTOMER;

alter table orders_detail 
   drop foreign key FK_ORDERS_D_REFERENCE_ORDERS;

alter table orders_detail 
   drop foreign key FK_ORDERS_D_REFERENCE_GOODS;

drop table if exists customers;


alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

alter table goods 
   drop foreign key FK_GOODS_REFERENCE_GOODS_CA;

drop table if exists goods;

drop table if exists goods_cates_1;


alter table goods_cates_2 
   drop foreign key FK_GOODS_CA_REFERENCE_GOODS_CA;

drop table if exists goods_cates_2;


alter table goods_cates_3 
   drop foreign key FK_GOODS_CA_REFERENCE_GOODS_CA;

drop table if exists goods_cates_3;


alter table goods_cates_4 
   drop foreign key FK_GOODS_CA_REFERENCE_GOODS_CA;

drop table if exists goods_cates_4;


alter table orders 
   drop foreign key FK_ORDERS_REFERENCE_CUSTOMER;

drop table if exists orders;


alter table orders_detail 
   drop foreign key FK_ORDERS_D_REFERENCE_ORDERS;

alter table orders_detail 
   drop foreign key FK_ORDERS_D_REFERENCE_GOODS;

drop table if exists orders_detail;

/*==============================================================*/
/* Table: customers                                             */
/*==============================================================*/
create table customers
(
   id                   int not null  comment '',
   name                 varchar(10) not null  comment '',
   password             varchar(18) not null  comment '',
   tel                  char(11) not null  comment '',
   addres               varchar(50)  comment '',
   idCard               char(18)  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: goods                                                 */
/*==============================================================*/
create table goods
(
   id                   int not null  comment '',
   name                 varchar(50)  comment '',
   cate1_id             int not null  comment '',
   cate2_id             int not null  comment '',
   cate3_id             int not null  comment '',
   cate4_id             int not null  comment '',
   price                decimal(10,3)  comment '',
   discount             decimal(3,2) not null  comment '',
   is_show              char(10) not null  comment '',
   is_saleof            char(10) not null  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: goods_cates_1                                         */
/*==============================================================*/
create table goods_cates_1
(
   id                   int not null  comment '',
   name                 varchar(100) not null  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: goods_cates_2                                         */
/*==============================================================*/
create table goods_cates_2
(
   id                   int not null  comment '',
   name                 varchar(100) not null  comment '',
   up_level_id          int not null  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: goods_cates_3                                         */
/*==============================================================*/
create table goods_cates_3
(
   id                   int not null  comment '',
   name                 varchar(100) not null  comment '',
   up_level_id          int not null  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: goods_cates_4                                         */
/*==============================================================*/
create table goods_cates_4
(
   id                   int not null  comment '',
   name                 varchar(100) not null  comment '',
   up_level_id          int not null  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: orders                                                */
/*==============================================================*/
create table orders
(
   id                   int not null  comment '',
   order_date_time      datetime not null  comment '',
   customer_id          int not null  comment '',
   primary key (id)
);

/*==============================================================*/
/* Table: orders_detail                                         */
/*==============================================================*/
create table orders_detail
(
   id                   int not null  comment '',
   order_id             int not null  comment '',
   goods_id             int not null  comment '',
   quantity             int  comment '',
   primary key (id)
);

alter table goods add constraint FK_GOODS_REFERENCE_GOODS_CA foreign key (cate1_id)
      references goods_cates_1 (id) on delete restrict on update restrict;

alter table goods add constraint FK_GOODS_REFERENCE_GOODS_CA foreign key (cate2_id)
      references goods_cates_2 (id) on delete restrict on update restrict;

alter table goods add constraint FK_GOODS_REFERENCE_GOODS_CA foreign key (cate3_id)
      references goods_cates_3 (id) on delete restrict on update restrict;

alter table goods add constraint FK_GOODS_REFERENCE_GOODS_CA foreign key (cate4_id)
      references goods_cates_4 (id) on delete restrict on update restrict;

alter table goods_cates_2 add constraint FK_GOODS_CA_REFERENCE_GOODS_CA foreign key (up_level_id)
      references goods_cates_1 (id) on delete restrict on update restrict;

alter table goods_cates_3 add constraint FK_GOODS_CA_REFERENCE_GOODS_CA foreign key (up_level_id)
      references goods_cates_2 (id) on delete restrict on update restrict;

alter table goods_cates_4 add constraint FK_GOODS_CA_REFERENCE_GOODS_CA foreign key (up_level_id)
      references goods_cates_3 (id) on delete restrict on update restrict;

alter table orders add constraint FK_ORDERS_REFERENCE_CUSTOMER foreign key (customer_id)
      references customers (id) on delete restrict on update restrict;

alter table orders_detail add constraint FK_ORDERS_D_REFERENCE_ORDERS foreign key (order_id)
      references orders (id) on delete restrict on update restrict;

alter table orders_detail add constraint FK_ORDERS_D_REFERENCE_GOODS foreign key (goods_id)
      references goods (id) on delete restrict on update restrict;

