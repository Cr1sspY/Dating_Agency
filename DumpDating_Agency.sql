CREATE DATABASE  IF NOT EXISTS `dating_agency` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dating_agency`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: dating_agency
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `знаки_зодиака`
--

DROP TABLE IF EXISTS `знаки_зодиака`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `знаки_зодиака` (
  `Код_Знака` int NOT NULL,
  `Название_Знака` varchar(20) NOT NULL,
  `Описание` varchar(254) NOT NULL,
  PRIMARY KEY (`Код_Знака`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `знаки_зодиака`
--

LOCK TABLES `знаки_зодиака` WRITE;
/*!40000 ALTER TABLE `знаки_зодиака` DISABLE KEYS */;
INSERT INTO `знаки_зодиака` VALUES (1,'Овен','Бла-бла');
/*!40000 ALTER TABLE `знаки_зодиака` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `клиенты`
--

DROP TABLE IF EXISTS `клиенты`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `клиенты` (
  `Код_Клиента` int NOT NULL,
  `ФИО` varchar(255) NOT NULL,
  `Пол` varchar(7) NOT NULL,
  `Возраст` int NOT NULL,
  `Рост` int NOT NULL,
  `Вес` int NOT NULL,
  `Статус` varchar(25) NOT NULL,
  `Код_Знака` int NOT NULL,
  `Код_Глаз` int NOT NULL,
  `Код_Волос` int NOT NULL,
  PRIMARY KEY (`Код_Клиента`),
  KEY `Код_Знака` (`Код_Знака`),
  KEY `Код_Глаз` (`Код_Глаз`),
  KEY `Код_Волос` (`Код_Волос`),
  CONSTRAINT `клиенты_ibfk_1` FOREIGN KEY (`Код_Знака`) REFERENCES `знаки_зодиака` (`Код_Знака`),
  CONSTRAINT `клиенты_ibfk_2` FOREIGN KEY (`Код_Глаз`) REFERENCES `цвета_глаз` (`Код_Глаз`),
  CONSTRAINT `клиенты_ibfk_3` FOREIGN KEY (`Код_Волос`) REFERENCES `цвета_волос` (`Код_Волос`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `клиенты`
--

LOCK TABLES `клиенты` WRITE;
/*!40000 ALTER TABLE `клиенты` DISABLE KEYS */;
INSERT INTO `клиенты` VALUES (1,'Агуст Ди','Мужской',23,175,75,'Новый',1,1,1);
/*!40000 ALTER TABLE `клиенты` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `пользователи`
--

DROP TABLE IF EXISTS `пользователи`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `пользователи` (
  `Код_Пользователя` int NOT NULL,
  `Роль` varchar(20) NOT NULL,
  `Логин` varchar(30) NOT NULL,
  `Пароль` varchar(18) NOT NULL,
  `Код_Клиента` int DEFAULT NULL,
  PRIMARY KEY (`Код_Пользователя`),
  KEY `пользователи_ibfk_1` (`Код_Клиента`),
  CONSTRAINT `пользователи_ibfk_1` FOREIGN KEY (`Код_Клиента`) REFERENCES `клиенты` (`Код_Клиента`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `пользователи`
--

LOCK TABLES `пользователи` WRITE;
/*!40000 ALTER TABLE `пользователи` DISABLE KEYS */;
INSERT INTO `пользователи` VALUES (1,'Клиент','agust_d','12345678',1),(2,'Администратор','RM','87654321',NULL);
/*!40000 ALTER TABLE `пользователи` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `цвета_волос`
--

DROP TABLE IF EXISTS `цвета_волос`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `цвета_волос` (
  `Код_Волос` int NOT NULL,
  `ЦветВ` varchar(20) NOT NULL,
  PRIMARY KEY (`Код_Волос`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `цвета_волос`
--

LOCK TABLES `цвета_волос` WRITE;
/*!40000 ALTER TABLE `цвета_волос` DISABLE KEYS */;
INSERT INTO `цвета_волос` VALUES (1,'Каштановый');
/*!40000 ALTER TABLE `цвета_волос` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `цвета_глаз`
--

DROP TABLE IF EXISTS `цвета_глаз`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `цвета_глаз` (
  `Код_Глаз` int NOT NULL,
  `ЦветГ` varchar(20) NOT NULL,
  PRIMARY KEY (`Код_Глаз`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `цвета_глаз`
--

LOCK TABLES `цвета_глаз` WRITE;
/*!40000 ALTER TABLE `цвета_глаз` DISABLE KEYS */;
INSERT INTO `цвета_глаз` VALUES (1,'Карие');
/*!40000 ALTER TABLE `цвета_глаз` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dating_agency'
--

--
-- Dumping routines for database 'dating_agency'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-27 17:38:55
