#流程
#   将全国省市区县.sql传入~/sqlData
#   cd ~/sqlData
#   mysql -uroot -p
#   135cylpsx
#   show databases;
#   create database value_test charset='utf8';
#   use value_test;
#   source 全国省市区县.sql  # 这句话就自动执行当前目录下的 全国省市区县.sql文件


#查询流程
#   查询省级行政单位
#       select * from China where parent_id=0;
#   查询四川省的市级行政单位
#       select * from China where parent_id=510000;
#   查询成都市的区县行政单位
#       select * from China where parent_id=510100;
#   输入一个行政单位，显示它的所有下级行政单位(自联表，查询技巧，同一个表，可以给自己取不同的别名，不同的别名之间可以用关联查询)
#        select province.name, city.name from China as province inner join China as city on city.parent_id=province.id having province.name='成都';
