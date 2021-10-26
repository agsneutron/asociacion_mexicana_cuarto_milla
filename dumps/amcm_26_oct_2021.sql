-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: amcm_db
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `amcm_condicionesevento`
--

DROP TABLE IF EXISTS `amcm_condicionesevento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_condicionesevento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `valor` double NOT NULL,
  `especificacion` varchar(500) NOT NULL,
  `evento_id` int NOT NULL,
  `limite_id` int NOT NULL,
  `tipoCondicion_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_condicionesevento_evento_id_2bac95a8_fk_amcm_evento_id` (`evento_id`),
  KEY `amcm_condicionesevento_limite_id_867aca5f_fk_amcm_limite_id` (`limite_id`),
  KEY `amcm_condicioneseven_tipoCondicion_id_3a88c15c_fk_amcm_tipo` (`tipoCondicion_id`),
  CONSTRAINT `amcm_condicioneseven_tipoCondicion_id_3a88c15c_fk_amcm_tipo` FOREIGN KEY (`tipoCondicion_id`) REFERENCES `amcm_tipocondicion` (`id`),
  CONSTRAINT `amcm_condicionesevento_evento_id_2bac95a8_fk_amcm_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `amcm_evento` (`id`),
  CONSTRAINT `amcm_condicionesevento_limite_id_867aca5f_fk_amcm_limite_id` FOREIGN KEY (`limite_id`) REFERENCES `amcm_limite` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_condicionesevento`
--

LOCK TABLES `amcm_condicionesevento` WRITE;
/*!40000 ALTER TABLE `amcm_condicionesevento` DISABLE KEYS */;
INSERT INTO `amcm_condicionesevento` VALUES (1,2,'caballos con una edad de 2 años',1,1,1);
/*!40000 ALTER TABLE `amcm_condicionesevento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_cuadras`
--

DROP TABLE IF EXISTS `amcm_cuadras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_cuadras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `representante` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `celular` varchar(15) NOT NULL,
  `correoElectronico` varchar(15) NOT NULL,
  `observaciones` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuadras`
--

LOCK TABLES `amcm_cuadras` WRITE;
/*!40000 ALTER TABLE `amcm_cuadras` DISABLE KEYS */;
INSERT INTO `amcm_cuadras` VALUES (1,'Cuadra AGS','Alejandro Gomez','7223724044','72237240444','agomezsanchez27','nada'),(2,'Cuadra ARI','Ari Sanchez','7223806473','72237240444','ariaocho@gmail','nada');
/*!40000 ALTER TABLE `amcm_cuadras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_cuotaevento`
--

DROP TABLE IF EXISTS `amcm_cuotaevento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_cuotaevento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `monto` double NOT NULL,
  `fechaVencimiento` date NOT NULL,
  `tipoCuota_id` int NOT NULL,
  `evento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_cuotaevento_tipoCuota_id_49d5a35c_fk_amcm_tipocuota_id` (`tipoCuota_id`),
  KEY `amcm_cuotaevento_evento_id_9823ca39_fk_amcm_evento_id` (`evento_id`),
  CONSTRAINT `amcm_cuotaevento_evento_id_9823ca39_fk_amcm_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `amcm_evento` (`id`),
  CONSTRAINT `amcm_cuotaevento_tipoCuota_id_49d5a35c_fk_amcm_tipocuota_id` FOREIGN KEY (`tipoCuota_id`) REFERENCES `amcm_tipocuota` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuotaevento`
--

LOCK TABLES `amcm_cuotaevento` WRITE;
/*!40000 ALTER TABLE `amcm_cuotaevento` DISABLE KEYS */;
INSERT INTO `amcm_cuotaevento` VALUES (1,2500,'2021-10-31',1,1);
/*!40000 ALTER TABLE `amcm_cuotaevento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_cuotas`
--

DROP TABLE IF EXISTS `amcm_cuotas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_cuotas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `monto` double NOT NULL,
  `tipoCuota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `amcm_cuotas_tipoCuota_id_9bb6e747_fk_amcm_tipocuota_id` (`tipoCuota_id`),
  CONSTRAINT `amcm_cuotas_tipoCuota_id_9bb6e747_fk_amcm_tipocuota_id` FOREIGN KEY (`tipoCuota_id`) REFERENCES `amcm_tipocuota` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuotas`
--

LOCK TABLES `amcm_cuotas` WRITE;
/*!40000 ALTER TABLE `amcm_cuotas` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_cuotas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_descuentos`
--

DROP TABLE IF EXISTS `amcm_descuentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_descuentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `porcentaje` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_descuentos`
--

LOCK TABLES `amcm_descuentos` WRITE;
/*!40000 ALTER TABLE `amcm_descuentos` DISABLE KEYS */;
INSERT INTO `amcm_descuentos` VALUES (1,'25%','descuento',25);
/*!40000 ALTER TABLE `amcm_descuentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_ejemplares`
--

DROP TABLE IF EXISTS `amcm_ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_ejemplares` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `edad` double NOT NULL,
  `peso` double NOT NULL,
  `color` varchar(100) NOT NULL,
  `padre` varchar(100) NOT NULL,
  `madre` varchar(100) NOT NULL,
  `observaciones` longtext NOT NULL,
  `cuadra_id` int NOT NULL,
  `nacionalidad_id` int NOT NULL,
  `sexo_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_ejemplares_cuadra_id_7c3b65fc_fk_amcm_cuadras_id` (`cuadra_id`),
  KEY `amcm_ejemplares_nacionalidad_id_d75dff57_fk_amcm_nacionalidad_id` (`nacionalidad_id`),
  KEY `amcm_ejemplares_sexo_id_14e99806_fk_amcm_sexo_id` (`sexo_id`),
  CONSTRAINT `amcm_ejemplares_cuadra_id_7c3b65fc_fk_amcm_cuadras_id` FOREIGN KEY (`cuadra_id`) REFERENCES `amcm_cuadras` (`id`),
  CONSTRAINT `amcm_ejemplares_nacionalidad_id_d75dff57_fk_amcm_nacionalidad_id` FOREIGN KEY (`nacionalidad_id`) REFERENCES `amcm_nacionalidad` (`id`),
  CONSTRAINT `amcm_ejemplares_sexo_id_14e99806_fk_amcm_sexo_id` FOREIGN KEY (`sexo_id`) REFERENCES `amcm_sexo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_ejemplares`
--

LOCK TABLES `amcm_ejemplares` WRITE;
/*!40000 ALTER TABLE `amcm_ejemplares` DISABLE KEYS */;
INSERT INTO `amcm_ejemplares` VALUES (1,'Cachito',2,200,'Negro','Patito','Lausana','',1,1,1),(2,'Rayito',2,210,'Rojo','Raserito','Tumca','',1,1,1),(3,'lazarito',2,200,'café','Santi','Lorenza','',2,1,1);
/*!40000 ALTER TABLE `amcm_ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_evento`
--

DROP TABLE IF EXISTS `amcm_evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_evento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `yardas` int NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `bolsa` double NOT NULL,
  `fondo` double NOT NULL,
  `temporada` int NOT NULL,
  `observaciones` longtext NOT NULL,
  `descuento_id` int NOT NULL,
  `tipoEvento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_evento_tipoEvento_id_c9032485_fk_amcm_tipoevento_id` (`tipoEvento_id`),
  KEY `amcm_evento_descuento_id_535ec5f6_fk_amcm_descuentos_id` (`descuento_id`),
  CONSTRAINT `amcm_evento_descuento_id_535ec5f6_fk_amcm_descuentos_id` FOREIGN KEY (`descuento_id`) REFERENCES `amcm_descuentos` (`id`),
  CONSTRAINT `amcm_evento_tipoEvento_id_c9032485_fk_amcm_tipoevento_id` FOREIGN KEY (`tipoEvento_id`) REFERENCES `amcm_tipoevento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_evento`
--

LOCK TABLES `amcm_evento` WRITE;
/*!40000 ALTER TABLE `amcm_evento` DISABLE KEYS */;
INSERT INTO `amcm_evento` VALUES (1,'Futurity Garañones',300,'futurity de temporada',100000,10000,2021,'para registrar un ejemplo',1,1);
/*!40000 ALTER TABLE `amcm_evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_fechasevento`
--

DROP TABLE IF EXISTS `amcm_fechasevento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_fechasevento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `evento_id` int NOT NULL,
  `tipoFecha_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_fechasevento_evento_id_e73d4672_fk_amcm_evento_id` (`evento_id`),
  KEY `amcm_fechasevento_tipoFecha_id_10cc4303_fk_amcm_tipofecha_id` (`tipoFecha_id`),
  CONSTRAINT `amcm_fechasevento_evento_id_e73d4672_fk_amcm_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `amcm_evento` (`id`),
  CONSTRAINT `amcm_fechasevento_tipoFecha_id_10cc4303_fk_amcm_tipofecha_id` FOREIGN KEY (`tipoFecha_id`) REFERENCES `amcm_tipofecha` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_fechasevento`
--

LOCK TABLES `amcm_fechasevento` WRITE;
/*!40000 ALTER TABLE `amcm_fechasevento` DISABLE KEYS */;
INSERT INTO `amcm_fechasevento` VALUES (1,'2021-10-28',1,1);
/*!40000 ALTER TABLE `amcm_fechasevento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_inscripcion`
--

DROP TABLE IF EXISTS `amcm_inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_inscripcion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fechaRegistro` date NOT NULL,
  `status` varchar(15) NOT NULL,
  `cuadra_id` int NOT NULL,
  `ejemplar_id` int DEFAULT NULL,
  `evento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_inscripcion_cuadra_id_4cabff65_fk_amcm_cuadras_id` (`cuadra_id`),
  KEY `amcm_inscripcion_evento_id_97ceb3b8_fk_amcm_evento_id` (`evento_id`),
  KEY `amcm_inscripcion_ejemplar_id_38b67426` (`ejemplar_id`),
  CONSTRAINT `amcm_inscripcion_cuadra_id_4cabff65_fk_amcm_cuadras_id` FOREIGN KEY (`cuadra_id`) REFERENCES `amcm_cuadras` (`id`),
  CONSTRAINT `amcm_inscripcion_ejemplar_id_38b67426_fk_amcm_ejemplares_id` FOREIGN KEY (`ejemplar_id`) REFERENCES `amcm_ejemplares` (`id`),
  CONSTRAINT `amcm_inscripcion_evento_id_97ceb3b8_fk_amcm_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `amcm_evento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_inscripcion`
--

LOCK TABLES `amcm_inscripcion` WRITE;
/*!40000 ALTER TABLE `amcm_inscripcion` DISABLE KEYS */;
INSERT INTO `amcm_inscripcion` VALUES (1,'2021-10-26','ACTIVO',1,1,1);
/*!40000 ALTER TABLE `amcm_inscripcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_limite`
--

DROP TABLE IF EXISTS `amcm_limite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_limite` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_limite`
--

LOCK TABLES `amcm_limite` WRITE;
/*!40000 ALTER TABLE `amcm_limite` DISABLE KEYS */;
INSERT INTO `amcm_limite` VALUES (1,'Edad','edad del caballo');
/*!40000 ALTER TABLE `amcm_limite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_nacionalidad`
--

DROP TABLE IF EXISTS `amcm_nacionalidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_nacionalidad` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `abreviatura` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `abreviatura` (`abreviatura`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_nacionalidad`
--

LOCK TABLES `amcm_nacionalidad` WRITE;
/*!40000 ALTER TABLE `amcm_nacionalidad` DISABLE KEYS */;
INSERT INTO `amcm_nacionalidad` VALUES (1,'Mexicana','MX');
/*!40000 ALTER TABLE `amcm_nacionalidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_registrocuotaevento`
--

DROP TABLE IF EXISTS `amcm_registrocuotaevento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_registrocuotaevento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fechaRegistro` date NOT NULL,
  `valorRecibido` varchar(500) NOT NULL,
  `cuadras_id` int NOT NULL,
  `cuotaEvento_id` int NOT NULL,
  `evento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_registrocuotaevento_cuadras_id_c0323b9f_fk_amcm_cuadras_id` (`cuadras_id`),
  KEY `amcm_registrocuotaev_cuotaEvento_id_3524db9e_fk_amcm_cuot` (`cuotaEvento_id`),
  KEY `amcm_registrocuotaevento_evento_id_9330c433_fk_amcm_evento_id` (`evento_id`),
  CONSTRAINT `amcm_registrocuotaev_cuotaEvento_id_3524db9e_fk_amcm_cuot` FOREIGN KEY (`cuotaEvento_id`) REFERENCES `amcm_cuotaevento` (`id`),
  CONSTRAINT `amcm_registrocuotaevento_cuadras_id_c0323b9f_fk_amcm_cuadras_id` FOREIGN KEY (`cuadras_id`) REFERENCES `amcm_cuadras` (`id`),
  CONSTRAINT `amcm_registrocuotaevento_evento_id_9330c433_fk_amcm_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `amcm_evento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_registrocuotaevento`
--

LOCK TABLES `amcm_registrocuotaevento` WRITE;
/*!40000 ALTER TABLE `amcm_registrocuotaevento` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_registrocuotaevento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_registrocuotaevento_ejemplares`
--

DROP TABLE IF EXISTS `amcm_registrocuotaevento_ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_registrocuotaevento_ejemplares` (
  `id` int NOT NULL AUTO_INCREMENT,
  `registrocuotaevento_id` int NOT NULL,
  `ejemplares_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `amcm_registrocuotaevento_registrocuotaevento_id_e_d35a2940_uniq` (`registrocuotaevento_id`,`ejemplares_id`),
  KEY `amcm_registrocuotaev_ejemplares_id_2baf8fbd_fk_amcm_ejem` (`ejemplares_id`),
  CONSTRAINT `amcm_registrocuotaev_ejemplares_id_2baf8fbd_fk_amcm_ejem` FOREIGN KEY (`ejemplares_id`) REFERENCES `amcm_ejemplares` (`id`),
  CONSTRAINT `amcm_registrocuotaev_registrocuotaevento__61758dc4_fk_amcm_regi` FOREIGN KEY (`registrocuotaevento_id`) REFERENCES `amcm_registrocuotaevento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_registrocuotaevento_ejemplares`
--

LOCK TABLES `amcm_registrocuotaevento_ejemplares` WRITE;
/*!40000 ALTER TABLE `amcm_registrocuotaevento_ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_registrocuotaevento_ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_sexo`
--

DROP TABLE IF EXISTS `amcm_sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_sexo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_sexo`
--

LOCK TABLES `amcm_sexo` WRITE;
/*!40000 ALTER TABLE `amcm_sexo` DISABLE KEYS */;
INSERT INTO `amcm_sexo` VALUES (1,'Masculino');
/*!40000 ALTER TABLE `amcm_sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_tipocondicion`
--

DROP TABLE IF EXISTS `amcm_tipocondicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_tipocondicion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipocondicion`
--

LOCK TABLES `amcm_tipocondicion` WRITE;
/*!40000 ALTER TABLE `amcm_tipocondicion` DISABLE KEYS */;
INSERT INTO `amcm_tipocondicion` VALUES (1,'Igual','igual a');
/*!40000 ALTER TABLE `amcm_tipocondicion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_tipocuota`
--

DROP TABLE IF EXISTS `amcm_tipocuota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_tipocuota` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipocuota`
--

LOCK TABLES `amcm_tipocuota` WRITE;
/*!40000 ALTER TABLE `amcm_tipocuota` DISABLE KEYS */;
INSERT INTO `amcm_tipocuota` VALUES (1,'Cuota 1','Primer cuota');
/*!40000 ALTER TABLE `amcm_tipocuota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_tipoevento`
--

DROP TABLE IF EXISTS `amcm_tipoevento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_tipoevento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipoevento`
--

LOCK TABLES `amcm_tipoevento` WRITE;
/*!40000 ALTER TABLE `amcm_tipoevento` DISABLE KEYS */;
INSERT INTO `amcm_tipoevento` VALUES (1,'Furutity','Futurity');
/*!40000 ALTER TABLE `amcm_tipoevento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_tipofecha`
--

DROP TABLE IF EXISTS `amcm_tipofecha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_tipofecha` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(500) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipofecha`
--

LOCK TABLES `amcm_tipofecha` WRITE;
/*!40000 ALTER TABLE `amcm_tipofecha` DISABLE KEYS */;
INSERT INTO `amcm_tipofecha` VALUES (1,'Inscripción','Inscrpción');
/*!40000 ALTER TABLE `amcm_tipofecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Cuadra',7,'add_cuadras'),(26,'Can change Cuadra',7,'change_cuadras'),(27,'Can delete Cuadra',7,'delete_cuadras'),(28,'Can view Cuadra',7,'view_cuadras'),(29,'Can add Descuento',8,'add_descuentos'),(30,'Can change Descuento',8,'change_descuentos'),(31,'Can delete Descuento',8,'delete_descuentos'),(32,'Can view Descuento',8,'view_descuentos'),(33,'Can add Nacionalidad',9,'add_nacionalidad'),(34,'Can change Nacionalidad',9,'change_nacionalidad'),(35,'Can delete Nacionalidad',9,'delete_nacionalidad'),(36,'Can view Nacionalidad',9,'view_nacionalidad'),(37,'Can add Sexo',10,'add_sexo'),(38,'Can change Sexo',10,'change_sexo'),(39,'Can delete Sexo',10,'delete_sexo'),(40,'Can view Sexo',10,'view_sexo'),(41,'Can add Tipo de Cuota',11,'add_tipocuota'),(42,'Can change Tipo de Cuota',11,'change_tipocuota'),(43,'Can delete Tipo de Cuota',11,'delete_tipocuota'),(44,'Can view Tipo de Cuota',11,'view_tipocuota'),(45,'Can add Ejemplar',12,'add_ejemplares'),(46,'Can change Ejemplar',12,'change_ejemplares'),(47,'Can delete Ejemplar',12,'delete_ejemplares'),(48,'Can view Ejemplar',12,'view_ejemplares'),(49,'Can add Cuota',13,'add_cuotas'),(50,'Can change Cuota',13,'change_cuotas'),(51,'Can delete Cuota',13,'delete_cuotas'),(52,'Can view Cuota',13,'view_cuotas'),(53,'Can add Cuota',14,'add_cuotaevento'),(54,'Can change Cuota',14,'change_cuotaevento'),(55,'Can delete Cuota',14,'delete_cuotaevento'),(56,'Can view Cuota',14,'view_cuotaevento'),(57,'Can add Evento',15,'add_evento'),(58,'Can change Evento',15,'change_evento'),(59,'Can delete Evento',15,'delete_evento'),(60,'Can view Evento',15,'view_evento'),(61,'Can add límite de Condición',16,'add_limite'),(62,'Can change límite de Condición',16,'change_limite'),(63,'Can delete límite de Condición',16,'delete_limite'),(64,'Can view límite de Condición',16,'view_limite'),(65,'Can add Tipo de Condición',17,'add_tipocondicion'),(66,'Can change Tipo de Condición',17,'change_tipocondicion'),(67,'Can delete Tipo de Condición',17,'delete_tipocondicion'),(68,'Can view Tipo de Condición',17,'view_tipocondicion'),(69,'Can add Tipo de Evento',18,'add_tipoevento'),(70,'Can change Tipo de Evento',18,'change_tipoevento'),(71,'Can delete Tipo de Evento',18,'delete_tipoevento'),(72,'Can view Tipo de Evento',18,'view_tipoevento'),(73,'Can add Tipo de Fecha del Evento',19,'add_tipofecha'),(74,'Can change Tipo de Fecha del Evento',19,'change_tipofecha'),(75,'Can delete Tipo de Fecha del Evento',19,'delete_tipofecha'),(76,'Can view Tipo de Fecha del Evento',19,'view_tipofecha'),(77,'Can add Registro a Evento',20,'add_registrocuotaevento'),(78,'Can change Registro a Evento',20,'change_registrocuotaevento'),(79,'Can delete Registro a Evento',20,'delete_registrocuotaevento'),(80,'Can view Registro a Evento',20,'view_registrocuotaevento'),(81,'Can add Fechas del Evento',21,'add_fechasevento'),(82,'Can change Fechas del Evento',21,'change_fechasevento'),(83,'Can delete Fechas del Evento',21,'delete_fechasevento'),(84,'Can view Fechas del Evento',21,'view_fechasevento'),(85,'Can add Condición del Evento',22,'add_condicionesevento'),(86,'Can change Condición del Evento',22,'change_condicionesevento'),(87,'Can delete Condición del Evento',22,'delete_condicionesevento'),(88,'Can view Condición del Evento',22,'view_condicionesevento'),(89,'Can add Inscripción',23,'add_inscripcion'),(90,'Can change Inscripción',23,'change_inscripcion'),(91,'Can delete Inscripción',23,'delete_inscripcion'),(92,'Can view Inscripción',23,'view_inscripcion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$wVLShLJoPjR2ojcVvpLz24$v0feYIe1lSttPRAhZLDpr6bw6Ts/41uc8uKfHQPJQ4M=','2021-10-26 15:21:25.830226',1,'amcm','','','amcm@gmail.com',1,1,'2021-10-14 14:40:39.407867');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-10-25 14:39:34.220790','1','Masculino',1,'[{\"added\": {}}]',10,1),(2,'2021-10-25 14:39:45.661285','1','Mexicana',1,'[{\"added\": {}}]',9,1),(3,'2021-10-25 14:39:54.864975','1','Cuadra AGS',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Ejemplar\", \"object\": \"Cachito\"}}]',7,1),(4,'2021-10-25 14:40:26.853711','1','Cuadra AGS',2,'[{\"added\": {\"name\": \"Ejemplar\", \"object\": \"Rayito\"}}]',7,1),(5,'2021-10-25 14:41:25.527076','2','Cuadra ARI',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Ejemplar\", \"object\": \"lazarito\"}}]',7,1),(6,'2021-10-25 18:36:22.011370','1','Furutity',1,'[{\"added\": {}}]',18,1),(7,'2021-10-25 18:38:27.734349','1','Inscripción',1,'[{\"added\": {}}]',19,1),(8,'2021-10-25 18:39:29.946267','1','Edad',1,'[{\"added\": {}}]',16,1),(9,'2021-10-25 18:40:01.613386','1','Igual',1,'[{\"added\": {}}]',17,1),(10,'2021-10-25 18:40:35.307433','1','Cuota 1',1,'[{\"added\": {}}]',11,1),(11,'2021-10-25 18:44:14.894095','1','25%',1,'[{\"added\": {}}]',8,1),(12,'2021-10-26 16:45:47.842256','1','Futurity Garañones',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"Inscripci\\u00f3n\"}}, {\"added\": {\"name\": \"Condici\\u00f3n del Evento\", \"object\": \"Igual\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Cuota 1\"}}]',15,1),(13,'2021-10-26 16:57:04.889247','1','Futurity Garañones Cuadra AGS',1,'[{\"added\": {}}]',23,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(22,'amcm','condicionesevento'),(7,'amcm','cuadras'),(14,'amcm','cuotaevento'),(13,'amcm','cuotas'),(8,'amcm','descuentos'),(12,'amcm','ejemplares'),(15,'amcm','evento'),(21,'amcm','fechasevento'),(23,'amcm','inscripcion'),(16,'amcm','limite'),(9,'amcm','nacionalidad'),(20,'amcm','registrocuotaevento'),(10,'amcm','sexo'),(17,'amcm','tipocondicion'),(11,'amcm','tipocuota'),(18,'amcm','tipoevento'),(19,'amcm','tipofecha'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-10-14 14:38:55.582417'),(2,'auth','0001_initial','2021-10-14 14:38:57.041343'),(3,'admin','0001_initial','2021-10-14 14:38:57.331072'),(4,'admin','0002_logentry_remove_auto_add','2021-10-14 14:38:57.343064'),(5,'admin','0003_logentry_add_action_flag_choices','2021-10-14 14:38:57.355058'),(6,'contenttypes','0002_remove_content_type_name','2021-10-14 14:38:57.533401'),(7,'auth','0002_alter_permission_name_max_length','2021-10-14 14:38:57.648554'),(8,'auth','0003_alter_user_email_max_length','2021-10-14 14:38:57.943287'),(9,'auth','0004_alter_user_username_opts','2021-10-14 14:38:57.959636'),(10,'auth','0005_alter_user_last_login_null','2021-10-14 14:38:58.048202'),(11,'auth','0006_require_contenttypes_0002','2021-10-14 14:38:58.054317'),(12,'auth','0007_alter_validators_add_error_messages','2021-10-14 14:38:58.066262'),(13,'auth','0008_alter_user_username_max_length','2021-10-14 14:38:58.166153'),(14,'auth','0009_alter_user_last_name_max_length','2021-10-14 14:38:58.262283'),(15,'auth','0010_alter_group_name_max_length','2021-10-14 14:38:58.355585'),(16,'auth','0011_update_proxy_permissions','2021-10-14 14:38:58.368610'),(17,'auth','0012_alter_user_first_name_max_length','2021-10-14 14:38:58.465538'),(18,'sessions','0001_initial','2021-10-14 14:38:58.534668'),(19,'amcm','0001_initial','2021-10-25 14:37:18.313968'),(20,'amcm','0002_auto_20211024_0134','2021-10-25 14:37:20.537526'),(21,'amcm','0003_auto_20211024_0256','2021-10-25 14:37:20.847563'),(22,'amcm','0004_alter_cuotaevento_fechavencimiento','2021-10-25 14:37:20.866495'),(23,'amcm','0005_inscripcion','2021-10-25 14:37:21.220468');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1h9syx747famvrk7f794o18b7qmitqod','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mf3m5:IKF9pEnTp8iyYgcJar1Z4CCp3LZNpDd1UoQjN9_9bJY','2021-11-08 17:28:41.773419'),('29sbaajapbklkj8ooz4g921b2l9hfdc4','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mb47D:6WwVvAnU-omTtSyRw5o2a4gGCFUcWjxxMzIt7VYgH5c','2021-10-28 17:01:59.245235'),('lvjlhykz6rnhujy5q46r58g62tdifpwz','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mfOGT:9jVLE8e6QInBXye91OdY8uvxiVGqRUjWdJ46lb9Vwlk','2021-11-09 15:21:25.843232'),('ohopfm77rmyczhteys3owhoew4vadsvb','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mf16c:zrnxbhwS10K0dX7yLG-eVcj3m6EQUauNwaXXzeZnIGM','2021-11-08 14:37:42.360902'),('svaliz4py08r4omr3k4sh5gu18nafqa6','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mb1up:TTvDTdRS6y71vZyBRyBcuY1Rp1jyVJMSGXZkOJ90wKI','2021-10-28 14:41:03.780452'),('wobr92yyauw627wkwv2h3xky0thy8g0h','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mf1SL:s0uczESoi3DG8KjF0Sdi03uJvmdkp1Vdbf87FaoOxEI','2021-11-08 15:00:09.668472'),('wsqc3wfvo56vz2ulbn1yh2oynrpqz7sm','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mf4oU:vddvVpumvV759Lmm7Hihm94lHtCi0F7tNvBP2jRnF1U','2021-11-08 18:35:14.131722');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 12:03:32
