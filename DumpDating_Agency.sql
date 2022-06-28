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
  `Описание` varchar(500) NOT NULL,
  PRIMARY KEY (`Код_Знака`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `знаки_зодиака`
--

LOCK TABLES `знаки_зодиака` WRITE;
/*!40000 ALTER TABLE `знаки_зодиака` DISABLE KEYS */;
INSERT INTO `знаки_зодиака` VALUES (1,'Овен','Скука и обыденность им претят, а мир кажется черно-белым. Любят говорить правду в лицо, очень упрямы. Привлекают людей простодушием, щедростью, мужественностью и умением брать на себя ответственность.'),(2,'Телец','По характеру Телец молчалив, многое держит в себе, умеет трезво рассуждать, интуитивен и обладает мощной силой воли. Пока спокоен, демонстрирует мягкость, терпение. Если задеть за живое, легко взрывается. Не любит давления извне, долго обижается. Советы — не для Тельцов: они все знают сами. Идут к своей цели по головам, проявляя властную и упрямую натуру.'),(3,'Близнецы','Есть в гороскопе двойственные знаки зодиака. Описание Близнецов непременно строится на крайностях. Они живут под управлением Меркурия, относятся к воздушной стихии, поэтому ветрены, переменчивы, но весьма дружелюбны.'),(4,'Рак','Рак переплюнул все знаки зодиака по чувственности и восприимчивости. Представитель водной стихии находится под покровительством планеты тайн, сомнений и переживаний — Луны.'),(5,'Лев','Люди, родившиеся под знаком Льва, творческие, любят главенствовать в работе и в жизни, идут к успеху, не задерживаясь на вторых ролях. Ненавидят любые ограничения. К себе относятся требовательно, придирчивы ко внешности, поэтому уделяют ей много внимания. Стараются произвести на людей благоприятное впечатление, любят нравиться.'),(6,'Дева','Трудолюбивые и надежные представители знака наделены трезвым взглядом на вещи, педантичностью. Девы склонны к системному анализу, постоянно критикуют себя и других, стараются все держать под контролем. Поддерживают порядок в деньгах, делах и доме, практичны и домовиты. В отношениях застенчивы, очень искренние и щедрые, умеют сочувствовать и помогать людям, не боятся ответственности.'),(7,'Весы','Весы любят, когда их хвалят, но не выносят критику. Редко проявляют оригинальность, стараются не брать на себя лишней ответственности.'),(8,'Скорпион','Скорпионы любят жить, как говорится, на полную катушку, крайне азартны, склонны к зависимостям, категоричны. Людям чаще не доверяют и создают трагедию на пустом месте. Врожденная интуиция сделала их отличными психологами и прирожденными манипуляторами.'),(9,'Стрелец','У представителей этого знака хорошо развита сила воли, они решительны и слегка воинственны, любят всех поучать. При этом всегда проявляют дружелюбие, прирожденные оптимисты. Взбесить их может только откровенная ложь, лицемерие и попытки подчинить себе их волю.'),(10,'Козерог','Земной знак Козерог — один из самых сильных, как утверждает гороскоп. Характеристика его включает практичность, рассудительность, трезвый взгляд на вещи. Козероги знают, что такое дисциплина, а от Сатурна получили ангельское терпение и желание быть признанными другими людьми.'),(11,'Водолей','Налет романтики мешает Водолею трезво смотреть на мир. Зато не мешает быть ярким, неординарным. Из профессий этот знак выбирает те, где можно проявить эрудицию, любит благотворительность, умеет сохранять спокойствие даже в стрессовой ситуации.'),(12,'Рыбы','Рыб считают пассивным знаком, ведь они находятся под влиянием планеты Нептун и относятся к водным знакам. В них много чувств и эмоций, Рыб тянет к мистике, всему необычному. У них хорошо развита интуиция и понимание других людей, они любят помечтать. Некоторая сентиментальность делает представителей этого знака уязвимыми. Но в общении Рыбы легки, приятны, обладают хорошим чувством юмора.');
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
  `Телефон` varchar(15) NOT NULL,
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
INSERT INTO `клиенты` VALUES (1,'Иванов Андрей Петрович','Мужской',23,175,75,'Показывать',1,1,1,'+79163256985'),(2,'Лагина Валентина Дмитриевна','Женский',36,168,70,'Показывать',5,3,5,'+79264589732'),(3,'Ронин Александр Николаевич','Мужской',21,185,80,'Скрывать',11,2,4,'+79853642873'),(4,'Быстров Иван Сергеевич','Мужской',34,181,90,'Показывать',9,4,2,'+79346497219'),(5,'Марков Геннадий Дмитриевич','Мужской',27,173,79,'Показывать',9,3,3,'+79771236554'),(6,'Васильев Сергей Андреевич','Мужской',25,171,73,'Показывать',9,1,1,'+79364587624'),(7,'Петрова Евгения Александровна','Женский',26,158,69,'Показывать',5,1,3,'+79548712698'),(8,'Добрынина Александра Никитична','Женский',21,165,71,'Показывать',12,2,1,'+79482182486'),(9,'Марлева Инна Игнатьевна','Женский',32,173,65,'Скрывать',8,4,4,'+79147892523'),(10,'Демичева Анастасия Васильевна','Женский',19,153,54,'Показывать',3,5,2,'+79475161163');
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
INSERT INTO `пользователи` VALUES (1,'Клиент','ivanov','ivanov',1),(2,'Администратор','admin','admin',NULL),(3,'Клиент','lagina','lagina',2),(4,'Клиент','ronin','ronin',3),(5,'Клиент','bistrov','bistrov',4),(6,'Клиент','markov','markov',5),(7,'Клиент','vasiliev','vasiliev',6),(8,'Клиент','petrova','petrova',7),(9,'Клиент','dobrinina','dobrinina',8),(10,'Клиент','marleva','marleva',9),(11,'Клиент','demicheva','demicheva',10);
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
INSERT INTO `цвета_волос` VALUES (1,'Брюнет'),(2,'Рыжий'),(3,'Блондин'),(4,'Шатен'),(5,'Русый'),(6,'Седой');
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
INSERT INTO `цвета_глаз` VALUES (1,'Карие'),(2,'Чёрные'),(3,'Зелёные'),(4,'Серые'),(5,'Голубые');
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

-- Dump completed on 2022-06-28 11:14:01
