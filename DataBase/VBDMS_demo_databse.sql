
--
-- Host: localhost    Database: sensordb
-- ------------------------------------------------------
-- Server version	8.0.41
CREATE DATABASE IF NOT EXISTS SensorDB;
USE SensorDB;
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
-- Table structure for table `sensordata`
--

DROP TABLE IF EXISTS `sensordata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensordata` (
  `time_stamp` datetime NOT NULL,
  `Sensor 1` float DEFAULT NULL,
  `Sensor 2` float DEFAULT NULL,
  `Sensor 3` float DEFAULT NULL,
  `Sensor 4` float DEFAULT NULL,
  `Sensor 5` float DEFAULT NULL,
  `Sensor 6` float DEFAULT NULL,
  `Sensor 7` float DEFAULT NULL,
  `Sensor 8` float DEFAULT NULL,
  `Sensor 9` float DEFAULT NULL,
  `Sensor 10` float DEFAULT NULL,
  `Sensor 11` float DEFAULT NULL,
  `Sensor 12` float DEFAULT NULL,
  `Sensor 13` float DEFAULT NULL,
  `Sensor 14` float DEFAULT NULL,
  `Sensor 15` float DEFAULT NULL,
  `Sensor 16` float DEFAULT NULL,
  `Sensor 17` float DEFAULT NULL,
  `Sensor 18` float DEFAULT NULL,
  `Sensor 19` float DEFAULT NULL,
  `Sensor 20` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensordata`
--

LOCK TABLES `sensordata` WRITE;
/*!40000 ALTER TABLE `sensordata` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensordata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensorstatus`
--

DROP TABLE IF EXISTS `sensorstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensorstatus` (
  `sensor_name` varchar(20) NOT NULL,
  `status` enum('Active','Inactive') NOT NULL,
  PRIMARY KEY (`sensor_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensorstatus`
--

LOCK TABLES `sensorstatus` WRITE;
/*!40000 ALTER TABLE `sensorstatus` DISABLE KEYS */;
INSERT INTO `sensorstatus` VALUES ('Sensor 1','Active'),('Sensor 10','Active'),('Sensor 11','Active'),('Sensor 12','Active'),('Sensor 13','Active'),('Sensor 14','Active'),('Sensor 15','Active'),('Sensor 16','Active'),('Sensor 17','Active'),('Sensor 18','Active'),('Sensor 19','Active'),('Sensor 2','Active'),('Sensor 20','Active'),('Sensor 3','Active'),('Sensor 4','Active'),('Sensor 5','Active'),('Sensor 6','Active'),('Sensor 7','Active'),('Sensor 8','Active'),('Sensor 9','Active');
/*!40000 ALTER TABLE `sensorstatus` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-11  0:08:50
