-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: asj
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `foodtypes`
--

DROP TABLE IF EXISTS `foodtypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `foodtypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` varchar(20) NOT NULL,
  `typename` varchar(20) NOT NULL,
  `childtypenames` varchar(100) NOT NULL,
  `typesort` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foodtypes`
--

LOCK TABLES `foodtypes` WRITE;
/*!40000 ALTER TABLE `foodtypes` DISABLE KEYS */;
INSERT INTO `foodtypes` VALUES (1,'001','热销榜','全部分类:0',1),(2,'002','鲜品尝鲜','全部分类:0',2),(3,'003','热销榜','全部分类:0#进口水果:0001#国产水果:0002',3),(4,'004','卤味熟食','全部分类:0',4),(5,'005','牛奶面包','全部分类0#酸奶乳酸菌:0003#牛奶豆漿:0004#面包蛋糕:0005',5),(6,'006','酒水飲料','全部分类:0#果汁饮料:0006#碳酸饮料:0007#整箱购:0008#植物蛋白:0009#进口饮料:0010',6),(7,'007','休闲零食','全部分类:0#进口零食:0011#饼干糕点:0012#膨化食品:0013#坚果炒货:0014#肉感蜜饯:0015#糖果巧克力:0016',7),(8,'008','方便速食','全部分类:0#方便面:0017#火腿肠卤蛋:0018#速冻面点:0019#下饭小菜:0020#罐头食品:0021#冲调饮品:0022',8),(9,'009','粮油调味','全部分类:0#杂粮米面油:0023#厨房调味:0024#调味酱:0025',9),(10,'010','生活用品','全部分类:0#个人护理:0026#纸品:0027#日常用品:0028#家居清洁:0029',10),(11,'011','冰淇淋','全部分类:0',11);
/*!40000 ALTER TABLE `foodtypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-06  8:46:30
