create database market;
use market;
create table market_demand_job(
    id int primary key auto_increment,
    source text,
    jobName text,
    price text,
    companyName text,
    address text,
    content text
);
insert into market_demand_job (source, jobName, price, companyName, address, content) value ('Boss直聘', 'Python爬虫工程师', '9-14K', '中软国际', '北京 海淀区 八里庄', "['岗位职责', '参与语音识别中的数据抓取、清洗、质量分析和相关自动化工具的开发工作', '岗位要求', '•统招本科，计算机科学学士学位，三年左右相关工作经验', '•Python扎实编程技巧，有爬虫经验，数据抓取经验', '•熟悉Web服务，例如TCP/IP，HTTP/HTTPS和API服务', '•熟悉Scrapy框架，由分布式爬虫经验', '•数据提取和质量分析经验', '•使用Python进行大数据处理的经验', '•了解分销系统，例如Spark/Hadoop/风暴/云计算', '职位亮点：半英化工作环境、AI方向、弹性上下班', '中软国际有限公司是国内大型综合性软件与信息服务企业，具有极高的市场感召力和客户忠诚度，自成立以来，中软国际取得了业界瞩目的成就，并作为国内第一家专注于电子政务领域的IT服务商，于2003年6月在香港联交所创业板成功上市，在未来的发展中，将软件外包作为重点的业务发展方向。']");

drop database market;

update user set password=password('135cylpsx4848@') where user='root';