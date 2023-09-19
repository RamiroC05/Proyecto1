-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `ID_Empleado` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `DNI` int NOT NULL,
  `Domicilio` varchar(50) NOT NULL,
  `Email` varchar(70) NOT NULL,
  `Edad` int NOT NULL,
  `Género` varchar(45) NOT NULL,
  `Cuil` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_Empleado`),
  UNIQUE KEY `DNI_UNIQUE` (`DNI`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (3,'Ramiro','Corra',44878600,'castelli','corra@gmail.com',20,'Masculino','4829932'),(67,'Rodrigo','Vargas',35676543,'Videla','vargassilvio@gmail.com',35,'Masculino','40543221'),(70,'Maxi','Rodriguez',356723243,'Videla','maxirodriguez@gmail.com',35,'Masculino','403433221'),(94,'Josefina','Vargas',23478512,'Tierra del Fuego','josevar@gmail.com',13,'Femenino','12009311'),(103,'Agustin','Zolorza',1233321,'Rama Caida','zolorza@gmail.com',20,'Masculino','451233321'),(113,'David','Veisaga',34442322,'Paunero y Almirante Brown','davidveisaga@gmail.com',45,'Masculino','212345545'),(126,'Bautista','Riveira',23231111,'fuxias','colo@gmail.com',21,'Masculino','1234566512'),(136,'joaquin','condori',44878900,'Savedra','joacocondori09@gmail.com',19,'Masculino','221113345'),(139,'Gabriel','Rosendorn',245677889,'Avellaneda 276','gabriel@gmail.com',20,'Helicoptero de combate apache','123456789');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;