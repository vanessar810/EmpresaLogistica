-- MySQL dump 10.13  Distrib 9.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: logistics_db
-- ------------------------------------------------------
-- Server version	9.1.0

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

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('a3d512e62b7c');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bodegas`
--

DROP TABLE IF EXISTS `bodegas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bodegas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `ubicacion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_bodegas_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bodegas`
--

LOCK TABLES `bodegas` WRITE;
/*!40000 ALTER TABLE `bodegas` DISABLE KEYS */;
INSERT INTO `bodegas` VALUES (1,'Bodega Central Bogotá','Bogotá'),(2,'Bodega Norte Medellín','Medellín'),(3,'Bodega Central Cali','Cali'),(4,'Bodega Central Barranquilla','Barranquilla');
/*!40000 ALTER TABLE `bodegas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `user_id` (`user_id`),
  KEY `ix_clientes_id` (`id`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Laura','lauratrece@mail.com','1234',1),(2,'test','test@mail.com','1234',2),(3,'test1','test1@mail.com','1234',3),(4,'test2','test2@mail.com','123',4),(5,'test3','test3@mail.com','1234',5),(6,'test5','test5@mail.com','1234',7),(7,'test7','test7@mail.com','123',9),(8,'test7','test8@mail.com','123',10),(9,'test9','test9@mail.com','123',11),(10,'test10','test10@mail.com','1234',12),(11,'test11','test11@mail.com','123',13),(12,'test12','test12@mail.com','1234',14),(13,'test13','test13@mail.com','123',15),(14,'test14','test14@mail.com','1234',16),(15,'test14','test15@mail.com','321654',17),(16,'test16','test16@mail.com','123456',18),(17,'test17','test17@mail.com','171717',19),(18,'test18','test18@mail.com','181818',20);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envios_maritimos`
--

DROP TABLE IF EXISTS `envios_maritimos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `envios_maritimos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_producto` varchar(100) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `fecha_entrega` date DEFAULT NULL,
  `puerto_entrega` varchar(100) DEFAULT NULL,
  `precio_envio` float DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `numero_flota` varchar(8) DEFAULT NULL,
  `numero_guia` varchar(10) DEFAULT NULL,
  `cliente_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_flota` (`numero_flota`),
  UNIQUE KEY `numero_guia` (`numero_guia`),
  KEY `cliente_id` (`cliente_id`),
  KEY `ix_envios_maritimos_id` (`id`),
  CONSTRAINT `envios_maritimos_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envios_maritimos`
--

LOCK TABLES `envios_maritimos` WRITE;
/*!40000 ALTER TABLE `envios_maritimos` DISABLE KEYS */;
INSERT INTO `envios_maritimos` VALUES (1,'Alimentos',600,'2025-12-30','2026-01-25','Puerto de Cartagena',300,900,29400,'QPP3480X','UW06578769',6),(2,'Electrónicos',15,'2025-12-30','2026-01-29','Puerto de Buenaventura',300,56.25,2118.75,'SDH4010E','MN29584559',15);
/*!40000 ALTER TABLE `envios_maritimos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envios_preparados`
--

DROP TABLE IF EXISTS `envios_preparados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `envios_preparados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `producto_id` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_recogida` date DEFAULT NULL,
  `puerto_id` int DEFAULT NULL,
  `bodega_id` int DEFAULT NULL,
  `cliente_id` int DEFAULT NULL,
  `precio_envio` float DEFAULT NULL,
  `precio_productos` float DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `numero_guia` varchar(10) DEFAULT NULL,
  `numero_flota` varchar(8) DEFAULT NULL,
  `placa` varchar(8) DEFAULT NULL,
  `fecha_entrega` date DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_guia` (`numero_guia`),
  KEY `ix_envios_preparados_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envios_preparados`
--

LOCK TABLES `envios_preparados` WRITE;
/*!40000 ALTER TABLE `envios_preparados` DISABLE KEYS */;
INSERT INTO `envios_preparados` VALUES (3,4,600,'2026-01-15',1,NULL,6,300,50,900,29400,'EY62934690','NPU0471Y',NULL,'2026-01-25','2025-12-30');
/*!40000 ALTER TABLE `envios_preparados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envios_terrestres`
--

DROP TABLE IF EXISTS `envios_terrestres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `envios_terrestres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_producto` varchar(100) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `fecha_entrega` date DEFAULT NULL,
  `bodega_entrega` varchar(100) DEFAULT NULL,
  `precio_envio` float DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `placa` varchar(6) DEFAULT NULL,
  `numero_guia` varchar(10) DEFAULT NULL,
  `cliente_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_guia` (`numero_guia`),
  UNIQUE KEY `placa` (`placa`),
  KEY `cliente_id` (`cliente_id`),
  KEY `ix_envios_terrestres_id` (`id`),
  CONSTRAINT `envios_terrestres_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envios_terrestres`
--

LOCK TABLES `envios_terrestres` WRITE;
/*!40000 ALTER TABLE `envios_terrestres` DISABLE KEYS */;
INSERT INTO `envios_terrestres` VALUES (2,'Electrónicos',8,'2025-12-30','2026-01-02','Bodega Central Cali',100,0,1100,'JZI561','ZZ36698876',6);
/*!40000 ALTER TABLE `envios_terrestres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `precio` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_productos_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Electrónicos',125),(2,'Autos',500),(3,'Textiles',100),(4,'Alimentos',50);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puertos`
--

DROP TABLE IF EXISTS `puertos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puertos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `ubicacion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_puertos_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puertos`
--

LOCK TABLES `puertos` WRITE;
/*!40000 ALTER TABLE `puertos` DISABLE KEYS */;
INSERT INTO `puertos` VALUES (1,'Puerto de Cartagena','Colombia'),(2,'Puerto de Buenaventura','Colombia');
/*!40000 ALTER TABLE `puertos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  `role` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_users_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'lauratrece@mail.com','$pbkdf2-sha256$29000$cQ5hzJnzXisFAEBIyTknpA$JhT.XdkMWHfjeDSr/Omk1GSX0BobWqqhhMC0wLNaL84','cliente'),(2,'test@mail.com','$pbkdf2-sha256$29000$CgFg7B3DOEcopfT.//9/bw$0wGeoN9WvOHPVgy6U.8P87gMurfVktMa.A34jwNnZhw','cliente'),(3,'test1@mail.com','$pbkdf2-sha256$29000$oXSutfbeG4PwHgOAsFYqRQ$R7.nooHyxF8XYjTuofSLPUFM1RJLaY79OdtFL2Cp4Vg','cliente'),(4,'test2@mail.com','$pbkdf2-sha256$29000$N2ZsrXVOaY2RkpKyVso55w$1eUM5fTQyPpB6dnNv9WnsGcrAGp2K1gImtJ6gzdIH8M','cliente'),(5,'test3@mail.com','$pbkdf2-sha256$29000$4JwTAsD4XysFoBSCcG4thQ$ZqPXV4TzyVSnDczOMcRi5uOTiMGy9jWgVnNBqxKCZ0k','cliente'),(6,'test4@mail.com','$pbkdf2-sha256$29000$ZOydU.pdC4EwprS2dk5pjQ$gMk8aZHkCOs7MRJVcuOThYFc8E5dJZobBcZdYhYMARw','cliente'),(7,'test5@mail.com','$pbkdf2-sha256$29000$kRIipDSGUEqJkTLGWKu1tg$X3GdH0NUUO.VCMouibxBjbuBbV3DIXxCSLzz0dHaTrY','cliente'),(8,'test6@mail.com','$pbkdf2-sha256$29000$d44Rwvh/r3Xufe/dW2ttbQ$AAf90RN3pm.dnpav4UomV/U8gXTRNGHmFNBe8dKpe2Y','cliente'),(9,'test7@mail.com','$pbkdf2-sha256$29000$M0bIGQPAuDcG4Nw7p9R6Lw$yY9MVZTvp2dAWGb0ep9RjUU0TtFO7VmxB2TLgV57m34','cliente'),(10,'test8@mail.com','$pbkdf2-sha256$29000$EqLUOoewds7Z.793TsnZOw$b9lan5qrroGaAqOypY/wUmRBSSQT2Krz7vaP.WABG5k','cliente'),(11,'test9@mail.com','$pbkdf2-sha256$29000$rFVKqXXuPaf0/j8HYOw9hw$LE6ZmxhEPQ6t/Zn/QC9dIqlryiaStKYDpMT8vz4T67g','cliente'),(12,'test10@mail.com','$pbkdf2-sha256$29000$/1/LWeu9l3LO2ZuzthbCuA$zHQ5gU0seSsUXtYh2yIsPBQYBY4IIq7D61pew/dFCYU','cliente'),(13,'test11@mail.com','$pbkdf2-sha256$29000$yxnD2BtDCKH0nhOCsPZ.7w$fhohqEsRDTGCUpEmHgLGbiWiMJV5EEKynIIr4PF5oc8','cliente'),(14,'test12@mail.com','$pbkdf2-sha256$29000$ag2BkDJGqJXSOmdsLWXs/Q$.RUOybwGiav.jVDyNv.eH8upC0p3aImt5B1Qmfitli4','cliente'),(15,'test13@mail.com','$pbkdf2-sha256$29000$zvkfo5RyjhGitPa.t7b2vg$ee.DlzZSsv1gTIoMSHJULgQIQYiZ78uMxG3AFvj8R5w','cliente'),(16,'test14@mail.com','$pbkdf2-sha256$29000$iFEK4ZzTmhPCOKeU0jqnlA$HKR/Kl0acN84jRkOpRM2YEg6mi9QWbcbkT5FUWq/WOs','cliente'),(17,'test15@mail.com','$pbkdf2-sha256$29000$tlZqrdU6RyhlbM3ZGyOEMA$6iQLPJtltWPKauzF1LFaIOfXmcuYhdm3/sTLMcEp/Eo','cliente'),(18,'test16@mail.com','$pbkdf2-sha256$29000$.p/zXusdgxBi7D3HuLeWcg$qBMtfxAxgWaC32gK1DbU9VzJ2L1PMFw6Sh38SRWnVyo','cliente'),(19,'test17@mail.com','$pbkdf2-sha256$29000$.18LIQSAEALAOAeAEKK09g$VpWf6zbaYdh6XahPJUi3urbVbIwMcV2ufxZlYQ.TS/0','cliente'),(20,'test18@mail.com','$pbkdf2-sha256$29000$sba2NqbUem8thXDOee/dGw$c..MDuTBImk5gZu4oEruEYEnZZjbG82tnsqnitqFLtQ','cliente');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-06 10:44:59
COMMIT