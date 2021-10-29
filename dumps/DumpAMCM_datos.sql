-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: localhost    Database: amcm_db
-- ------------------------------------------------------
-- Server version	8.0.23

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_condicionesevento`
--

LOCK TABLES `amcm_condicionesevento` WRITE;
/*!40000 ALTER TABLE `amcm_condicionesevento` DISABLE KEYS */;
INSERT INTO `amcm_condicionesevento` VALUES (4,3,'Años',5,1,1);
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
  `nombre` varchar(200) NOT NULL,
  `representante` varchar(150) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `celular` varchar(15) NOT NULL,
  `correoElectronico` varchar(100) NOT NULL,
  `observaciones` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuadras`
--

LOCK TABLES `amcm_cuadras` WRITE;
/*!40000 ALTER TABLE `amcm_cuadras` DISABLE KEYS */;
INSERT INTO `amcm_cuadras` VALUES (1,'CUADRA AB','JOSE ALCANTARA','7224745123','','',''),(2,'CUADRA LAS VEGAS','TERESITA TREJO','26204504','5543508600','','x');
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuotaevento`
--

LOCK TABLES `amcm_cuotaevento` WRITE;
/*!40000 ALTER TABLE `amcm_cuotaevento` DISABLE KEYS */;
INSERT INTO `amcm_cuotaevento` VALUES (6,10000,'2021-01-26',5,3),(7,8000,'2021-02-02',7,3),(8,7000,'2021-10-30',5,4),(9,6000,'2021-11-06',7,4),(10,4500,'2021-12-05',8,4),(11,4000,'2022-01-09',9,4),(12,20000,'2021-11-02',2,5),(13,30000,'2021-11-09',1,5);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuotas`
--

LOCK TABLES `amcm_cuotas` WRITE;
/*!40000 ALTER TABLE `amcm_cuotas` DISABLE KEYS */;
INSERT INTO `amcm_cuotas` VALUES (1,'a','a',12,4),(2,'b','b',3,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_descuentos`
--

LOCK TABLES `amcm_descuentos` WRITE;
/*!40000 ALTER TABLE `amcm_descuentos` DISABLE KEYS */;
INSERT INTO `amcm_descuentos` VALUES (1,'PAGO UNICO','pagos realizados en la primera cuota',25);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_ejemplares`
--

LOCK TABLES `amcm_ejemplares` WRITE;
/*!40000 ALTER TABLE `amcm_ejemplares` DISABLE KEYS */;
INSERT INTO `amcm_ejemplares` VALUES (1,'ESPEJO FINITO CASH',3,54.6,'BAYO','LOOKING NOTES','FLIER HORSE','',1,1,1),(2,'DANCESAQQARA',1,43,'NEGRO','THE FIRST LADY','LH TOAST TO FLASH','',1,1,2),(3,'TRES SOLO',1,45,'PINTO','RUNAWAY','GIRL PAULA','',2,1,1),(4,'BUYTIST',2,56,'BLANCO','TROYANO','MERRI CORONA','',2,1,2);
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
  `descripcion` varchar(500) NOT NULL,
  `bolsa` double NOT NULL,
  `fondo` double NOT NULL,
  `temporada` int NOT NULL,
  `observaciones` longtext NOT NULL,
  `descuento_id` int DEFAULT NULL,
  `tipoEvento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_evento_tipoEvento_id_c9032485_fk_amcm_tipoevento_id` (`tipoEvento_id`),
  KEY `amcm_evento_descuento_id_535ec5f6_fk_amcm_descuentos_id` (`descuento_id`),
  CONSTRAINT `amcm_evento_descuento_id_535ec5f6_fk_amcm_descuentos_id` FOREIGN KEY (`descuento_id`) REFERENCES `amcm_descuentos` (`id`),
  CONSTRAINT `amcm_evento_tipoEvento_id_c9032485_fk_amcm_tipoevento_id` FOREIGN KEY (`tipoEvento_id`) REFERENCES `amcm_tipoevento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_evento`
--

LOCK TABLES `amcm_evento` WRITE;
/*!40000 ALTER TABLE `amcm_evento` DISABLE KEYS */;
INSERT INTO `amcm_evento` VALUES (3,'VII DERBY DESAFIO',350,'SON ELEGIBLES LOS EJEMPLARES QUE PAGARON TODAS LAS CUOTAS DEL VII FUTURITY DESAFIO CRIANZA  MEXICANA',0,0,2021,'',NULL,2),(4,'XVII FUTURITY GARAñONES CUARTO DE MILLA (RG2)',300,'SON ELEGIBLES LOS EJEMPLARES QUE APARECEN EN EL catálogo  DE LA XXXVI SUBASTA SELECTA Y QUE PAGARON LA INSCRIPCION PARA ESTE FUTURITY',0,0,2021,'SI EN LA PRIMERA CUOTA (19-1-210 PAGAN TODAS LAS CUOTAS ($21,500), SE hará UN 25 % DE DESCUENTO ( $16,125.00) - NO REEMBOLSABLE',1,1),(5,'XVIII Clásico',440,'CAMPEO DE CAMPEONES- RG3',0,0,2021,'',NULL,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_fechasevento`
--

LOCK TABLES `amcm_fechasevento` WRITE;
/*!40000 ALTER TABLE `amcm_fechasevento` DISABLE KEYS */;
INSERT INTO `amcm_fechasevento` VALUES (3,'2021-02-21',3,2),(4,'2021-03-07',3,3),(5,'2022-02-05',4,2),(6,'2022-02-06',4,2),(7,'2022-03-06',4,3),(8,'2021-11-21',5,2),(9,'2021-12-12',5,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_inscripcion`
--

LOCK TABLES `amcm_inscripcion` WRITE;
/*!40000 ALTER TABLE `amcm_inscripcion` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_limite`
--

LOCK TABLES `amcm_limite` WRITE;
/*!40000 ALTER TABLE `amcm_limite` DISABLE KEYS */;
INSERT INTO `amcm_limite` VALUES (1,'EDAD','Límite de edad para inscripción'),(2,'PESO','Peso máximo  aceptado para participar'),(3,'NACIONALIDAD','Los ejemplares deben cumplir con la nacionalidad indicada'),(4,'mayor o igual','el valor debe cumplir con la condición  indicads');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_nacionalidad`
--

LOCK TABLES `amcm_nacionalidad` WRITE;
/*!40000 ALTER TABLE `amcm_nacionalidad` DISABLE KEYS */;
INSERT INTO `amcm_nacionalidad` VALUES (1,'Mexicano','MX');
/*!40000 ALTER TABLE `amcm_nacionalidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amcm_pago`
--

DROP TABLE IF EXISTS `amcm_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amcm_pago` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cuotaPagada` double NOT NULL,
  `cuotaLetra` varchar(500) NOT NULL,
  `conceptoPago` varchar(250) NOT NULL,
  `fechaPago` date NOT NULL,
  `fechaRegistro` date NOT NULL,
  `numeroRecibo` int NOT NULL,
  `valorRecibido` varchar(500) NOT NULL,
  `cuota_id` int NOT NULL,
  `inscripcion_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `amcm_pago_cuota_id_b6ffb760_fk_amcm_cuotaevento_id` (`cuota_id`),
  KEY `amcm_pago_inscripcion_id_6b182b9b_fk_amcm_inscripcion_id` (`inscripcion_id`),
  CONSTRAINT `amcm_pago_cuota_id_b6ffb760_fk_amcm_cuotaevento_id` FOREIGN KEY (`cuota_id`) REFERENCES `amcm_cuotaevento` (`id`),
  CONSTRAINT `amcm_pago_inscripcion_id_6b182b9b_fk_amcm_inscripcion_id` FOREIGN KEY (`inscripcion_id`) REFERENCES `amcm_inscripcion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_pago`
--

LOCK TABLES `amcm_pago` WRITE;
/*!40000 ALTER TABLE `amcm_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_pago` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_sexo`
--

LOCK TABLES `amcm_sexo` WRITE;
/*!40000 ALTER TABLE `amcm_sexo` DISABLE KEYS */;
INSERT INTO `amcm_sexo` VALUES (2,'Femenino'),(1,'Masculino');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipocondicion`
--

LOCK TABLES `amcm_tipocondicion` WRITE;
/*!40000 ALTER TABLE `amcm_tipocondicion` DISABLE KEYS */;
INSERT INTO `amcm_tipocondicion` VALUES (1,'mayor','el valor de la condición  debe  ser mayor a'),(2,'IGUAL','la condición  debe ser igual al valor indicado'),(3,'menor','el valor debe ser menor a la condición  indicada');
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipocuota`
--

LOCK TABLES `amcm_tipocuota` WRITE;
/*!40000 ALTER TABLE `amcm_tipocuota` DISABLE KEYS */;
INSERT INTO `amcm_tipocuota` VALUES (1,'Inscripción','Inscripción'),(2,'Nominación','Nominación'),(3,'Nominación Extemporánea','Nominación Extemporánea'),(4,'Anticipo de Anualidad','Anticipo de Anualidad)'),(5,'Cuota 1','primer cuota'),(6,'Pago Unico','Pago de todas las cuotas en un solo pago'),(7,'Cuota 2','Segunda cuota'),(8,'CUOTA 3','TERCER PAGO'),(9,'CUOTA 4','CUARTO PAGO');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipoevento`
--

LOCK TABLES `amcm_tipoevento` WRITE;
/*!40000 ALTER TABLE `amcm_tipoevento` DISABLE KEYS */;
INSERT INTO `amcm_tipoevento` VALUES (1,'FUTURITY','Futurity ...'),(2,'DERBY','Derby ...'),(3,'CLASICO','Clásico .....');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipofecha`
--

LOCK TABLES `amcm_tipofecha` WRITE;
/*!40000 ALTER TABLE `amcm_tipofecha` DISABLE KEYS */;
INSERT INTO `amcm_tipofecha` VALUES (2,'ELIMINATORIA','Fecha en la  que ...'),(3,'FINAL','Fecha en la que ....'),(4,'Nominación','Nominación  de  clásico'),(5,'INSCRIPCION','Inscripción  A clásicos');
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
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Descuento',7,'add_descuentos'),(26,'Can change Descuento',7,'change_descuentos'),(27,'Can delete Descuento',7,'delete_descuentos'),(28,'Can view Descuento',7,'view_descuentos'),(29,'Can add Ejemplar',8,'add_ejemplares'),(30,'Can change Ejemplar',8,'change_ejemplares'),(31,'Can delete Ejemplar',8,'delete_ejemplares'),(32,'Can view Ejemplar',8,'view_ejemplares'),(33,'Can add Nacionalidad',9,'add_nacionalidad'),(34,'Can change Nacionalidad',9,'change_nacionalidad'),(35,'Can delete Nacionalidad',9,'delete_nacionalidad'),(36,'Can view Nacionalidad',9,'view_nacionalidad'),(37,'Can add Sexo',10,'add_sexo'),(38,'Can change Sexo',10,'change_sexo'),(39,'Can delete Sexo',10,'delete_sexo'),(40,'Can view Sexo',10,'view_sexo'),(41,'Can add Cuadra',11,'add_cuadras'),(42,'Can change Cuadra',11,'change_cuadras'),(43,'Can delete Cuadra',11,'delete_cuadras'),(44,'Can view Cuadra',11,'view_cuadras'),(45,'Can add Cuota',12,'add_cuotas'),(46,'Can change Cuota',12,'change_cuotas'),(47,'Can delete Cuota',12,'delete_cuotas'),(48,'Can view Cuota',12,'view_cuotas'),(49,'Can add Tipo de Cuota',13,'add_tipocuota'),(50,'Can change Tipo de Cuota',13,'change_tipocuota'),(51,'Can delete Tipo de Cuota',13,'delete_tipocuota'),(52,'Can view Tipo de Cuota',13,'view_tipocuota'),(53,'Can add Evento',14,'add_evento'),(54,'Can change Evento',14,'change_evento'),(55,'Can delete Evento',14,'delete_evento'),(56,'Can view Evento',14,'view_evento'),(57,'Can add Tipo de Condición',15,'add_tipocondicion'),(58,'Can change Tipo de Condición',15,'change_tipocondicion'),(59,'Can delete Tipo de Condición',15,'delete_tipocondicion'),(60,'Can view Tipo de Condición',15,'view_tipocondicion'),(61,'Can add límite de Condición',16,'add_limite'),(62,'Can change límite de Condición',16,'change_limite'),(63,'Can delete límite de Condición',16,'delete_limite'),(64,'Can view límite de Condición',16,'view_limite'),(65,'Can add Fechas del Evento',17,'add_fechasevento'),(66,'Can change Fechas del Evento',17,'change_fechasevento'),(67,'Can delete Fechas del Evento',17,'delete_fechasevento'),(68,'Can view Fechas del Evento',17,'view_fechasevento'),(69,'Can add Cuota',18,'add_cuotaevento'),(70,'Can change Cuota',18,'change_cuotaevento'),(71,'Can delete Cuota',18,'delete_cuotaevento'),(72,'Can view Cuota',18,'view_cuotaevento'),(73,'Can add Fecha del Evento',19,'add_tipofecha'),(74,'Can change Fecha del Evento',19,'change_tipofecha'),(75,'Can delete Fecha del Evento',19,'delete_tipofecha'),(76,'Can view Fecha del Evento',19,'view_tipofecha'),(77,'Can add Tipo de Evento',20,'add_tipoevento'),(78,'Can change Tipo de Evento',20,'change_tipoevento'),(79,'Can delete Tipo de Evento',20,'delete_tipoevento'),(80,'Can view Tipo de Evento',20,'view_tipoevento'),(81,'Can add Condición del Evento',21,'add_condicionesevento'),(82,'Can change Condición del Evento',21,'change_condicionesevento'),(83,'Can delete Condición del Evento',21,'delete_condicionesevento'),(84,'Can view Condición del Evento',21,'view_condicionesevento'),(85,'Can add Registro a Evento',22,'add_registrocuotaevento'),(86,'Can change Registro a Evento',22,'change_registrocuotaevento'),(87,'Can delete Registro a Evento',22,'delete_registrocuotaevento'),(88,'Can view Registro a Evento',22,'view_registrocuotaevento'),(89,'Can add Inscripción',23,'add_inscripcion'),(90,'Can change Inscripción',23,'change_inscripcion'),(91,'Can delete Inscripción',23,'delete_inscripcion'),(92,'Can view Inscripción',23,'view_inscripcion'),(93,'Can add Pago',24,'add_pago'),(94,'Can change Pago',24,'change_pago'),(95,'Can delete Pago',24,'delete_pago'),(96,'Can view Pago',24,'view_pago');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$wVLShLJoPjR2ojcVvpLz24$v0feYIe1lSttPRAhZLDpr6bw6Ts/41uc8uKfHQPJQ4M=','2021-10-19 19:15:33.890898',1,'amcm','','','amcm@gmail.com',1,1,'2021-10-14 14:40:39.407867');
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
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-10-19 05:36:01.144838','1','Masculino',1,'[{\"added\": {}}]',10,1),(2,'2021-10-19 05:36:08.081127','2','Femenino',1,'[{\"added\": {}}]',10,1),(3,'2021-10-19 05:49:05.641324','1','Masculino',2,'[]',10,1),(4,'2021-10-19 05:49:57.374038','1','Inscripción',1,'[{\"added\": {}}]',13,1),(5,'2021-10-19 05:50:12.495511','2','Nominación',1,'[{\"added\": {}}]',13,1),(6,'2021-10-19 05:50:37.930488','3','Nominación Extemporánea',1,'[{\"added\": {}}]',13,1),(7,'2021-10-19 05:50:56.202969','4','Anticipo de Anualidad',1,'[{\"added\": {}}]',13,1),(8,'2021-10-19 19:36:41.307099','1','a',1,'[{\"added\": {}}]',12,1),(9,'2021-10-19 19:37:02.701521','2','b',1,'[{\"added\": {}}]',12,1),(10,'2021-10-22 19:20:32.415224','1','Mexicano',1,'[{\"added\": {}}]',9,1),(11,'2021-10-24 01:45:36.944476','1','Futurity',1,'[{\"added\": {}}]',20,1),(12,'2021-10-24 01:45:51.769624','2','DERBY',1,'[{\"added\": {}}]',20,1),(13,'2021-10-24 01:46:20.780142','3','CLASICO',1,'[{\"added\": {}}]',20,1),(14,'2021-10-24 01:49:13.638880','2','ELIMINATORIA',1,'[{\"added\": {}}]',19,1),(15,'2021-10-24 01:49:30.564169','3','FINAL',1,'[{\"added\": {}}]',19,1),(16,'2021-10-24 01:50:52.728114','1','EDAD',1,'[{\"added\": {}}]',16,1),(17,'2021-10-24 01:51:20.348849','2','PESO',1,'[{\"added\": {}}]',16,1),(18,'2021-10-24 01:52:59.800896','3','NACIONALIDAD',1,'[{\"added\": {}}]',16,1),(19,'2021-10-24 01:53:35.907623','1','mayor',1,'[{\"added\": {}}]',15,1),(20,'2021-10-24 01:54:04.613258','2','IGUAL',1,'[{\"added\": {}}]',15,1),(21,'2021-10-24 01:54:36.297450','3','menor',1,'[{\"added\": {}}]',15,1),(22,'2021-10-24 01:55:49.395467','4','menor o igual a',1,'[{\"added\": {}}]',16,1),(23,'2021-10-24 01:56:57.509357','4','mayor o igual',2,'[{\"changed\": {\"fields\": [\"Nombre\", \"Descripci\\u00f3n\"]}}]',16,1),(24,'2021-10-24 02:07:31.447795','1','pago único',1,'[{\"added\": {}}]',7,1),(25,'2021-10-25 03:17:09.729498','1','FUTURITY',2,'[{\"changed\": {\"fields\": [\"Nombre\"]}}]',20,1),(26,'2021-10-25 03:17:31.266020','1','PAGO UNICO',2,'[{\"changed\": {\"fields\": [\"Nombre\"]}}]',7,1),(27,'2021-10-25 04:09:31.677839','5','Cuota 1',1,'[{\"added\": {}}]',13,1),(28,'2021-10-25 04:11:38.574785','2','Fururity Garañón',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"ELIMINATORIA\"}}, {\"added\": {\"name\": \"Condici\\u00f3n del Evento\", \"object\": \"menor\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Anticipo de Anualidad\"}}]',14,1),(29,'2021-10-25 04:15:12.547343','2','Fururity Garañón',2,'[{\"changed\": {\"fields\": [\"Descuento\"]}}, {\"changed\": {\"name\": \"Fechas del Evento\", \"object\": \"FINAL\", \"fields\": [\"Tipo de Fecha\", \"Fecha de Vencimiento\"]}}]',14,1),(30,'2021-10-25 04:22:28.358210','2','Fururity Garañón',2,'[]',14,1),(31,'2021-10-25 04:22:50.671711','2','Fururity Garañón',2,'[]',14,1),(32,'2021-10-25 04:23:16.769846','2','Fururity Garañón',2,'[]',14,1),(33,'2021-10-25 04:23:52.839052','2','Fururity Garañón',2,'[{\"added\": {\"name\": \"Condici\\u00f3n del Evento\", \"object\": \"menor\"}}]',14,1),(34,'2021-10-25 04:25:08.227978','2','Fururity Garañón',2,'[{\"changed\": {\"name\": \"Condici\\u00f3n del Evento\", \"object\": \"menor\", \"fields\": [\"Especificaci\\u00f3n de la Condici\\u00f3n\"]}}]',14,1),(35,'2021-10-25 12:59:22.281516','1','Meson',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Ejemplar\", \"object\": \"spirit\"}}]',11,1),(36,'2021-10-25 13:10:48.742868','2','rayo',1,'[{\"added\": {}}]',8,1),(37,'2021-10-25 13:56:50.805497','1','Fururity Garañón Meson',1,'[{\"added\": {}}]',23,1),(38,'2021-10-25 15:27:03.838710','2','Villa',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Ejemplar\", \"object\": \"sebastian\"}}]',11,1),(39,'2021-10-25 15:29:08.698832','2','Fururity Garañón Meson',1,'[{\"added\": {}}]',23,1),(40,'2021-10-25 17:41:50.345876','3','Fururity Garañón Meson',1,'[{\"added\": {}}]',23,1),(41,'2021-10-25 20:08:13.398136','2','Fururity Garañón',2,'[{\"changed\": {\"fields\": [\"Tipo de Evento\"]}}]',14,1),(42,'2021-10-25 20:09:10.363524','3','Fururity Garañón Meson',2,'[]',23,1),(43,'2021-10-25 20:09:14.907017','2','Fururity Garañón Meson',2,'[]',23,1),(44,'2021-10-26 17:51:22.044422','6','Pago Unico',1,'[{\"added\": {}}]',13,1),(45,'2021-10-26 17:51:33.391687','2','Fururity Garañón',2,'[{\"added\": {\"name\": \"Cuota\", \"object\": \"Cuota 1\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Pago Unico\"}}]',14,1),(46,'2021-10-26 17:54:24.049936','4','None Anticipo de Anualidad 1',1,'[{\"added\": {}}]',24,1),(47,'2021-10-26 17:55:46.860613','4','Fururity Garañón Meson Anticipo de Anualidad 1',2,'[]',24,1),(48,'2021-10-26 19:36:35.988867','1','Fururity Garañón Villa',2,'[{\"changed\": {\"fields\": [\"Cuadra\", \"Ejemplar\"]}}]',23,1),(49,'2021-10-26 19:37:02.164468','4','Fururity Garañón Villa Anticipo de Anualidad 1',2,'[]',24,1),(50,'2021-10-26 19:56:15.572368','4','Fururity Garañón Villa Anticipo de Anualidad',2,'[]',24,1),(51,'2021-10-26 19:57:24.998324','5','Fururity Garañón Meson Pago Unico',1,'[{\"added\": {}}]',24,1),(52,'2021-10-26 19:57:37.079688','4','Fururity Garañón Villa Anticipo de Anualidad',2,'[]',24,1),(53,'2021-10-26 19:57:45.766717','5','Fururity Garañón Meson Pago Unico',2,'[]',24,1),(54,'2021-10-27 00:03:13.873723','2','Fururity Garañón',3,'',14,1),(55,'2021-10-27 00:30:30.903231','1','CUADRA AB',2,'[{\"changed\": {\"fields\": [\"Nombre\", \"Representante\", \"Tel\\u00e9fono\", \"Celular\", \"Correo Electr\\u00f3nico\", \"Observaciones\"]}}]',11,1),(56,'2021-10-27 00:42:13.600476','1','CUADRA AB',2,'[{\"changed\": {\"name\": \"Ejemplar\", \"object\": \"DANCESAQQARA\", \"fields\": [\"Nombre\", \"Sexo\", \"Color\", \"Padre del Caballo\", \"Madre del Caballo\"]}}, {\"changed\": {\"name\": \"Ejemplar\", \"object\": \"ESPEJO FINITO CASH\", \"fields\": [\"Nombre\", \"Color\", \"Padre del Caballo\", \"Madre del Caballo\"]}}]',11,1),(57,'2021-10-27 01:28:04.133251','2','CUADRA LAS VEGAS',2,'[{\"changed\": {\"fields\": [\"Nombre\", \"Representante\", \"Tel\\u00e9fono\", \"Celular\", \"Correo Electr\\u00f3nico\"]}}, {\"added\": {\"name\": \"Ejemplar\", \"object\": \"BUYTIST\"}}, {\"changed\": {\"name\": \"Ejemplar\", \"object\": \"TRES SOLO\", \"fields\": [\"Nombre\", \"Color\", \"Padre del Caballo\", \"Madre del Caballo\"]}}]',11,1),(58,'2021-10-27 01:58:52.803717','7','Cuota 2',1,'[{\"added\": {}}]',13,1),(59,'2021-10-27 01:59:26.519001','3','VII DERBY DESAFIO',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"ELIMINATORIA\"}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"FINAL\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Cuota 1\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Cuota 2\"}}]',14,1),(60,'2021-10-27 02:17:57.005563','8','CUOTA 3',1,'[{\"added\": {}}]',13,1),(61,'2021-10-27 02:18:24.893956','9','CUOTA 4',1,'[{\"added\": {}}]',13,1),(62,'2021-10-27 02:18:42.367418','4','XVII FUTURITY GARAñONES CUARTO DE MILLA (RG2)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"ELIMINATORIA\"}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"ELIMINATORIA\"}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"FINAL\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Cuota 1\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Cuota 2\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"CUOTA 3\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"CUOTA 4\"}}]',14,1),(63,'2021-10-27 02:23:15.188373','4','Nominación',1,'[{\"added\": {}}]',19,1),(64,'2021-10-27 02:23:58.264304','5','INSCRIPCION',1,'[{\"added\": {}}]',19,1),(65,'2021-10-27 02:26:07.805674','5','XVIII Clásico',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"ELIMINATORIA\"}}, {\"added\": {\"name\": \"Fechas del Evento\", \"object\": \"FINAL\"}}, {\"added\": {\"name\": \"Condici\\u00f3n del Evento\", \"object\": \"mayor\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Nominaci\\u00f3n\"}}, {\"added\": {\"name\": \"Cuota\", \"object\": \"Inscripci\\u00f3n\"}}]',14,1),(66,'2021-10-27 02:28:40.586628','5','XVIII Clásico',2,'[]',14,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(21,'amcm','condicionesevento'),(11,'amcm','cuadras'),(18,'amcm','cuotaevento'),(12,'amcm','cuotas'),(7,'amcm','descuentos'),(8,'amcm','ejemplares'),(14,'amcm','evento'),(17,'amcm','fechasevento'),(23,'amcm','inscripcion'),(16,'amcm','limite'),(9,'amcm','nacionalidad'),(24,'amcm','pago'),(22,'amcm','registrocuotaevento'),(10,'amcm','sexo'),(15,'amcm','tipocondicion'),(13,'amcm','tipocuota'),(20,'amcm','tipoevento'),(19,'amcm','tipofecha'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-10-14 14:38:55.582417'),(2,'auth','0001_initial','2021-10-14 14:38:57.041343'),(3,'admin','0001_initial','2021-10-14 14:38:57.331072'),(4,'admin','0002_logentry_remove_auto_add','2021-10-14 14:38:57.343064'),(5,'admin','0003_logentry_add_action_flag_choices','2021-10-14 14:38:57.355058'),(6,'contenttypes','0002_remove_content_type_name','2021-10-14 14:38:57.533401'),(7,'auth','0002_alter_permission_name_max_length','2021-10-14 14:38:57.648554'),(8,'auth','0003_alter_user_email_max_length','2021-10-14 14:38:57.943287'),(9,'auth','0004_alter_user_username_opts','2021-10-14 14:38:57.959636'),(10,'auth','0005_alter_user_last_login_null','2021-10-14 14:38:58.048202'),(11,'auth','0006_require_contenttypes_0002','2021-10-14 14:38:58.054317'),(12,'auth','0007_alter_validators_add_error_messages','2021-10-14 14:38:58.066262'),(13,'auth','0008_alter_user_username_max_length','2021-10-14 14:38:58.166153'),(14,'auth','0009_alter_user_last_name_max_length','2021-10-14 14:38:58.262283'),(15,'auth','0010_alter_group_name_max_length','2021-10-14 14:38:58.355585'),(16,'auth','0011_update_proxy_permissions','2021-10-14 14:38:58.368610'),(17,'auth','0012_alter_user_first_name_max_length','2021-10-14 14:38:58.465538'),(18,'sessions','0001_initial','2021-10-14 14:38:58.534668'),(19,'amcm','0001_initial','2021-10-19 05:12:58.874804'),(20,'amcm','0002_auto_20211024_0134','2021-10-24 01:35:00.421508'),(21,'amcm','0003_auto_20211024_0256','2021-10-24 02:56:44.288474'),(22,'amcm','0004_alter_cuotaevento_fechavencimiento','2021-10-24 02:58:00.742572'),(23,'amcm','0005_alter_evento_descuento','2021-10-25 04:14:49.474761'),(24,'amcm','0005_inscripcion','2021-10-25 12:55:48.453966'),(25,'amcm','0006_merge_0005_alter_evento_descuento_0005_inscripcion','2021-10-25 12:55:48.460644'),(26,'amcm','0007_auto_20211025_1006','2021-10-25 15:06:34.914590'),(27,'amcm','0008_auto_20211026_1246','2021-10-26 17:46:19.337615'),(28,'amcm','0009_auto_20211026_1927','2021-10-27 00:27:43.675086');
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
INSERT INTO `django_session` VALUES ('svaliz4py08r4omr3k4sh5gu18nafqa6','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mb1up:TTvDTdRS6y71vZyBRyBcuY1Rp1jyVJMSGXZkOJ90wKI','2021-10-28 14:41:03.780452'),('wq62tm6cttxwwczvol2eve4xv1u5x6ys','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mcuaD:y_I3Kzcx8L2b7FUkTz4QVD0Bn6pj9M6LsTuzz0DX8v0','2021-11-02 19:15:33.911024');
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

-- Dump completed on 2021-10-26 21:41:16
