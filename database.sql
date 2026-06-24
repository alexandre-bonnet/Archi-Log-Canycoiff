-- MySQL dump 10.13  Distrib 9.6.0, for macos26.3 (arm64)
--
-- Host: localhost    Database: canycoiff
-- ------------------------------------------------------
-- Server version	9.6.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '59358a4a-3731-11f1-87a9-9958eea056cd:1-362';

--
-- Table structure for table `chien`
--

DROP TABLE IF EXISTS `chien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chien` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) DEFAULT NULL,
  `race` varchar(100) DEFAULT NULL,
  `client_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `chien_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chien`
--

LOCK TABLES `chien` WRITE;
/*!40000 ALTER TABLE `chien` DISABLE KEYS */;
INSERT INTO `chien` VALUES (1,'Nawak','Coton',NULL),(2,'Helium','Techel nain ',NULL),(3,'hello','d',NULL),(4,'fkf','kff',NULL),(5,'nawak','coton',NULL),(6,'nawak','coton',1),(7,'helium','teckel',2),(8,'caniwaf','chien',1),(9,'nawak','chien',1),(10,'nawak','coton',1),(11,'nawak','coton',1),(12,'nawak','coton',1),(13,'nawak','coton',1),(14,'nawak','coton',1),(15,'nawak','coton ',1),(16,'nawak','coton',1),(17,'nawak','coton',1),(18,'nawak','coton',1);
/*!40000 ALTER TABLE `chien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'roro','&é\"\'('),(2,'roro','123'),(3,'alexB','1234'),(4,'AlexB','12345'),(5,'romane ','1234'),(6,'alex','1234'),(7,'alex','12'),(8,'alex','1234'),(9,'alex','1234'),(10,'alex','1234'),(11,'alex','1234'),(12,'alex','1234'),(13,'alex','1234'),(14,'alex','1234'),(15,'alex','1234'),(16,'alex','1234'),(17,'alex','12'),(18,'alex','1234'),(19,'alex','1234'),(20,'alex','1234'),(21,'alex','1234'),(22,'alex','1234');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faire`
--

DROP TABLE IF EXISTS `faire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faire` (
  `chien_id` int NOT NULL,
  `sortie_id` int NOT NULL,
  PRIMARY KEY (`chien_id`,`sortie_id`),
  KEY `sortie_id` (`sortie_id`),
  CONSTRAINT `faire_ibfk_1` FOREIGN KEY (`chien_id`) REFERENCES `chien` (`id`),
  CONSTRAINT `faire_ibfk_2` FOREIGN KEY (`sortie_id`) REFERENCES `sortie` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faire`
--

LOCK TABLES `faire` WRITE;
/*!40000 ALTER TABLE `faire` DISABLE KEYS */;
INSERT INTO `faire` VALUES (1,7),(2,7);
/*!40000 ALTER TABLE `faire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sortie`
--

DROP TABLE IF EXISTS `sortie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sortie` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_sortie` date DEFAULT NULL,
  `chien_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chien_id` (`chien_id`),
  CONSTRAINT `sortie_ibfk_1` FOREIGN KEY (`chien_id`) REFERENCES `chien` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sortie`
--

LOCK TABLES `sortie` WRITE;
/*!40000 ALTER TABLE `sortie` DISABLE KEYS */;
INSERT INTO `sortie` VALUES (1,'2025-01-12',NULL),(2,'2025-01-12',NULL),(3,'2025-12-21',NULL),(4,'2025-12-21',NULL),(5,'2025-12-12',NULL),(6,'2025-12-21',NULL),(7,'2025-12-12',NULL);
/*!40000 ALTER TABLE `sortie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USER` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `client_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_client` (`client_id`),
  CONSTRAINT `fk_user_client` FOREIGN KEY (`client_id`) REFERENCES `CLIENT` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-24 12:15:30
