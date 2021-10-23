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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_cuadras`
--

LOCK TABLES `amcm_cuadras` WRITE;
/*!40000 ALTER TABLE `amcm_cuadras` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_cuadras` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_descuentos`
--

LOCK TABLES `amcm_descuentos` WRITE;
/*!40000 ALTER TABLE `amcm_descuentos` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_ejemplares`
--

LOCK TABLES `amcm_ejemplares` WRITE;
/*!40000 ALTER TABLE `amcm_ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_ejemplares` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_nacionalidad`
--

LOCK TABLES `amcm_nacionalidad` WRITE;
/*!40000 ALTER TABLE `amcm_nacionalidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `amcm_nacionalidad` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amcm_tipocuota`
--

LOCK TABLES `amcm_tipocuota` WRITE;
/*!40000 ALTER TABLE `amcm_tipocuota` DISABLE KEYS */;
INSERT INTO `amcm_tipocuota` VALUES (1,'Inscripción','Inscripción'),(2,'Nominación','Nominación'),(3,'Nominación Extemporánea','Nominación Extemporánea'),(4,'Anticipo de Anualidad','Anticipo de Anualidad)');
/*!40000 ALTER TABLE `amcm_tipocuota` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Descuento',7,'add_descuentos'),(26,'Can change Descuento',7,'change_descuentos'),(27,'Can delete Descuento',7,'delete_descuentos'),(28,'Can view Descuento',7,'view_descuentos'),(29,'Can add Ejemplar',8,'add_ejemplares'),(30,'Can change Ejemplar',8,'change_ejemplares'),(31,'Can delete Ejemplar',8,'delete_ejemplares'),(32,'Can view Ejemplar',8,'view_ejemplares'),(33,'Can add Nacionalidad',9,'add_nacionalidad'),(34,'Can change Nacionalidad',9,'change_nacionalidad'),(35,'Can delete Nacionalidad',9,'delete_nacionalidad'),(36,'Can view Nacionalidad',9,'view_nacionalidad'),(37,'Can add Sexo',10,'add_sexo'),(38,'Can change Sexo',10,'change_sexo'),(39,'Can delete Sexo',10,'delete_sexo'),(40,'Can view Sexo',10,'view_sexo'),(41,'Can add Cuadra',11,'add_cuadras'),(42,'Can change Cuadra',11,'change_cuadras'),(43,'Can delete Cuadra',11,'delete_cuadras'),(44,'Can view Cuadra',11,'view_cuadras'),(45,'Can add Cuota',12,'add_cuotas'),(46,'Can change Cuota',12,'change_cuotas'),(47,'Can delete Cuota',12,'delete_cuotas'),(48,'Can view Cuota',12,'view_cuotas'),(49,'Can add Tipo de Cuota',13,'add_tipocuota'),(50,'Can change Tipo de Cuota',13,'change_tipocuota'),(51,'Can delete Tipo de Cuota',13,'delete_tipocuota'),(52,'Can view Tipo de Cuota',13,'view_tipocuota');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$wVLShLJoPjR2ojcVvpLz24$v0feYIe1lSttPRAhZLDpr6bw6Ts/41uc8uKfHQPJQ4M=','2021-10-19 00:47:40.855692',1,'amcm','','','amcm@gmail.com',1,1,'2021-10-14 14:40:39.407867');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-10-19 05:36:01.144838','1','Masculino',1,'[{\"added\": {}}]',10,1),(2,'2021-10-19 05:36:08.081127','2','Femenino',1,'[{\"added\": {}}]',10,1),(3,'2021-10-19 05:49:05.641324','1','Masculino',2,'[]',10,1),(4,'2021-10-19 05:49:57.374038','1','Inscripción',1,'[{\"added\": {}}]',13,1),(5,'2021-10-19 05:50:12.495511','2','Nominación',1,'[{\"added\": {}}]',13,1),(6,'2021-10-19 05:50:37.930488','3','Nominación Extemporánea',1,'[{\"added\": {}}]',13,1),(7,'2021-10-19 05:50:56.202969','4','Anticipo de Anualidad',1,'[{\"added\": {}}]',13,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(11,'amcm','cuadras'),(12,'amcm','cuotas'),(7,'amcm','descuentos'),(8,'amcm','ejemplares'),(9,'amcm','nacionalidad'),(10,'amcm','sexo'),(13,'amcm','tipocuota'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-10-14 14:38:55.582417'),(2,'auth','0001_initial','2021-10-14 14:38:57.041343'),(3,'admin','0001_initial','2021-10-14 14:38:57.331072'),(4,'admin','0002_logentry_remove_auto_add','2021-10-14 14:38:57.343064'),(5,'admin','0003_logentry_add_action_flag_choices','2021-10-14 14:38:57.355058'),(6,'contenttypes','0002_remove_content_type_name','2021-10-14 14:38:57.533401'),(7,'auth','0002_alter_permission_name_max_length','2021-10-14 14:38:57.648554'),(8,'auth','0003_alter_user_email_max_length','2021-10-14 14:38:57.943287'),(9,'auth','0004_alter_user_username_opts','2021-10-14 14:38:57.959636'),(10,'auth','0005_alter_user_last_login_null','2021-10-14 14:38:58.048202'),(11,'auth','0006_require_contenttypes_0002','2021-10-14 14:38:58.054317'),(12,'auth','0007_alter_validators_add_error_messages','2021-10-14 14:38:58.066262'),(13,'auth','0008_alter_user_username_max_length','2021-10-14 14:38:58.166153'),(14,'auth','0009_alter_user_last_name_max_length','2021-10-14 14:38:58.262283'),(15,'auth','0010_alter_group_name_max_length','2021-10-14 14:38:58.355585'),(16,'auth','0011_update_proxy_permissions','2021-10-14 14:38:58.368610'),(17,'auth','0012_alter_user_first_name_max_length','2021-10-14 14:38:58.465538'),(18,'sessions','0001_initial','2021-10-14 14:38:58.534668'),(19,'amcm','0001_initial','2021-10-19 05:12:58.874804');
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
INSERT INTO `django_session` VALUES ('awu9h1m41pty1u0rwk2bd7aryb95ntmf','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mcdI4:FS9BEQfakNwKvKaQTpPMszrcT1fAzZbOpKx6xq6nTjI','2021-11-02 00:47:40.863422'),('svaliz4py08r4omr3k4sh5gu18nafqa6','.eJxVjEsOwjAMBe-SNYqcgtuYJXvOULm2QwookfpZIe4OlbqA7ZuZ93I9r0vu19mmflR3dsEdfreB5WFlA3rncqtealmmcfCb4nc6-2tVe1529-8g85y_Naq2R2oYlLuggkKRAVIagoA2YhEImAmDUWgVT1EsdWhEaAgpqHt_APiXOGQ:1mb1up:TTvDTdRS6y71vZyBRyBcuY1Rp1jyVJMSGXZkOJ90wKI','2021-10-28 14:41:03.780452');
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

-- Dump completed on 2021-10-19  1:02:28
