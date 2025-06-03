-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: livraria_lusitana
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add book',8,'add_book'),(30,'Can change book',8,'change_book'),(31,'Can delete book',8,'delete_book'),(32,'Can view book',8,'view_book'),(33,'Can add review',9,'add_review'),(34,'Can change review',9,'change_review'),(35,'Can delete review',9,'delete_review'),(36,'Can view review',9,'view_review'),(37,'Can add user profile',10,'add_userprofile'),(38,'Can change user profile',10,'change_userprofile'),(39,'Can delete user profile',10,'delete_userprofile'),(40,'Can view user profile',10,'view_userprofile'),(41,'Can add wishlist',11,'add_wishlist'),(42,'Can change wishlist',11,'change_wishlist'),(43,'Can delete wishlist',11,'delete_wishlist'),(44,'Can view wishlist',11,'view_wishlist'),(45,'Can add order',12,'add_order'),(46,'Can change order',12,'change_order'),(47,'Can delete order',12,'delete_order'),(48,'Can view order',12,'view_order'),(49,'Can add order item',13,'add_orderitem'),(50,'Can change order item',13,'change_orderitem'),(51,'Can delete order item',13,'delete_orderitem'),(52,'Can view order item',13,'view_orderitem'),(53,'Can add Mensagem de Contato',14,'add_contactmessage'),(54,'Can change Mensagem de Contato',14,'change_contactmessage'),(55,'Can delete Mensagem de Contato',14,'delete_contactmessage'),(56,'Can view Mensagem de Contato',14,'view_contactmessage'),(57,'Can add newsletter subscription',15,'add_newslettersubscription'),(58,'Can change newsletter subscription',15,'change_newslettersubscription'),(59,'Can delete newsletter subscription',15,'delete_newslettersubscription'),(60,'Can view newsletter subscription',15,'view_newslettersubscription');
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
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1000000$YmkRF43QYYKqO4rIeNIt9T$fiwoX5Fw5HpGxcp3o5BE31SSnyM0O98vDHUigNzh4pY=','2025-06-03 15:48:54.677788',1,'livreiro_admin','','','',1,1,'2025-04-14 18:36:23.721441'),(2,'pbkdf2_sha256$1000000$GMJTxCCEo1ajQVHjiowANx$GTLVD3XZpGkFrHwO6SbEDkY7w7tM3RVu/v5nUaazsic=','2025-04-15 18:51:18.031705',0,'primeiroteste','','','',0,1,'2025-04-15 18:51:09.441591'),(3,'pbkdf2_sha256$1000000$Cw16T5hnBZKJl7sMnkt7QL$CFvvwIMwsYQNydZOgznDSGQsJ/P21v8fLeNAnJQB79s=','2025-05-31 13:14:38.342501',0,'contateste1','','','',0,1,'2025-05-31 13:14:22.096258'),(4,'pbkdf2_sha256$1000000$kEPeM0B9CtxUteTQfuyHan$s3ujC1IdVfhLsoXuJ49Qr/84tSvGsk2xVomJeijLMy0=','2025-06-03 16:45:36.203148',0,'inesteste','','','',0,1,'2025-06-01 20:24:26.391915'),(5,'pbkdf2_sha256$1000000$lTCXsu4bteQ3xDEzmtI8qk$Mf2VTB2msL5LXePFmxqsq9LcdZW5lp1rfC7uJfy9hXY=','2025-06-03 14:09:00.828659',0,'teste3','','','',0,1,'2025-06-03 14:05:31.221605'),(6,'pbkdf2_sha256$1000000$Zz1DvyCYbrZyEYgfhX6bWu$aIxyEDjhjDbeJIZz4MhbwmSEz1UWfH2+xpAlBkm06G0=','2025-06-03 15:26:23.955413',0,'novoteste','','','',0,1,'2025-06-03 15:26:13.821512');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_book`
--

DROP TABLE IF EXISTS `books_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `isbn` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `synopsis` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `price_cents` int NOT NULL,
  `currency` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  `publication_date` date NOT NULL,
  `publisher` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `language` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dimensions` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `binding_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pages` int NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stock` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `books_book_category_id_406d8649_fk_books_category_id` (`category_id`),
  CONSTRAINT `books_book_category_id_406d8649_fk_books_category_id` FOREIGN KEY (`category_id`) REFERENCES `books_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_book`
--

LOCK TABLES `books_book` WRITE;
/*!40000 ALTER TABLE `books_book` DISABLE KEYS */;
INSERT INTO `books_book` VALUES (20,'9789720727602','Os Lusíadas','Luís Vaz de Camões','Os Lusíadas contam a história da viagem do caminho marítimo para a Índia por Vasco da Gama na época dos Descobrimentos, mas é muito mais do que isso. Carregada de simbolismo e de um claro orgulho patriótico, esta narrativa exalta os vários desafios superados pelo Herói – o Povo Português – cuja coragem e dedicação são inabaláveis, mesmo contra todas as adversidades.',3000,'EUR','2021-09-01','Porto Editora','Português','128 x 198 x 21 mm','Capa mole',304,'books/book1.jpg',15,'2025-04-16 17:17:51.129008','2025-05-27 15:47:20.952990',3),(21,'9789720726599','Mensagem','Fernando Pessoa','Originalmente intitulada Portugal, a única obra de Fernando Pessoa publicada em vida continua tão atual no século XXI como em 1934. Revisitando o passado - os heróis e as conquistas da História - encontramos uma mensagem para o futuro, porque hoje: Tudo é incerto e derradeiro. Tudo é disperso, nada é inteiro. Ó Portugal, hoje és nevoeiro… É a Hora!',885,'EUR','2016-01-01','Porto Editora','Português','128 x 198 x 7 mm','Capa mole',96,'books/book2.jpg',20,'2025-04-16 17:17:51.654209','2025-05-27 15:47:20.966709',4),(22,'9789720727251','Os Maias','Eça de Queirós','Na pequenez da Baixa e do Aterro, onde todos se acotovelam, os dois fatalmente se cruzam: e com o seu brilho pessoal, muito fatalmente se atraem! Há nada mais natural? Se ela fosse feia e trouxesse aos ombros uma confeção barata da Loja da América, se ele fosse um mocinho encolhido de chapéu-coco, nunca se notariam e seguiriam diversamente nos seus destinos diversos. Assim, o conhecerem-se era certo, o amarem-se era provável… Nem só das histórias de amor dos Maias vive o romance mais completo e brilhante de Eça de Queirós.',1110,'EUR','2016-01-01','Porto Editora','Português','128 x 198 x 40 mm','Capa mole',736,'books/book3.jpg',10,'2025-04-16 17:17:52.175182','2025-05-27 15:47:20.974041',3),(23,'9789720745989','Memorial do Convento','José Saramago','No século XVIII, enquanto D. João V mandava construir o convento de Mafra, Baltasar e Blimunda encontravam-se, e o padre Bartolomeu de Gusmão procurava maneiras de voar. A história que aqui se conta não está nos livros de história, quase como se as memórias de um amor entre dois seres humanos comuns, mas invulgares, pudesse ser mais duradoura e mais impressionante que as memórias da construção de um enorme convento.',1590,'EUR','2019-06-01','Porto Editora','Português','128 x 198 x 28 mm','Capa mole',392,'books/book4.jpg',12,'2025-04-16 17:17:52.673081','2025-05-27 15:47:20.980071',6),(24,'9789720731968','Frei Luís de Sousa','Almeida Garrett','Uma das obras maiores do teatro português, Frei Luís de Sousa conta uma história de desencontros, reencontros, espera, conflitos morais e religiosos, com um desfecho dramático. A descrição do ambiente de aparente normalidade, de início, vai dando lugar a uma crescente tensão dramática, onde questões históricas como o sebastianismo, o domínio filipino, e também os traumas daí resultantes, vão surgindo como um fundo que dá maior intensidade aos dilemas dos personagens.',755,'EUR','2021-07-01','Porto Editora','Português','128 x 198 x 9 mm','Capa mole',144,'books/book5.jpg',8,'2025-04-16 17:17:53.187935','2025-05-27 15:47:20.986430',5),(25,'9789720736437','O Ano da Morte de Ricardo Reis','José Saramago','Em 1936, Ricardo Reis - um dos heterónimos de Fernando Pessoa - decide regressar a Portugal após dezasseis anos no Brasil. Regressa a Lisboa para encontrar um país oprimido pela ditadura e para se confrontar com a morte do seu criador. Perdido, estranhando uma cidade que já não reconhece, procura recuperar uma identidade e reconstruir uma vida que, na verdade, nunca foi a sua. Neste extraordinário romance de busca e de fantasmas, Saramago convida-nos também a um exercício de reflexão sobre a relação entre o criador e a criatura.',1590,'EUR','2020-07-30','Porto Editora','Português','128 x 198 x 26 mm','Capa mole',424,'books/book6.jpg',7,'2025-04-16 17:17:53.689962','2025-05-27 15:47:20.994625',6),(26,'9789720732033','Livro do Desassossego','Fernando Pessoa','Um dos textos mais importantes e enigmáticos de Fernando Pessoa, o Livro do Desassossego é um projeto inacabado e fragmentário, escrito sob o heterónimo de Bernardo Soares. Apresenta reflexões profundas sobre a existência, a identidade, o tédio e a melancolia da vida moderna, compondo um diário íntimo de sensações e pensamentos.',1420,'EUR','2019-11-13','Porto Editora','Português','128 x 198 x 30 mm','Capa mole',496,'books/book7.jpg',9,'2025-04-16 17:17:54.197632','2025-05-27 15:47:21.001830',3),(27,'9789720728845','Auto da Barca do Inferno','Gil Vicente','Na Barca do Inferno, o Diabo e o seu companheiro preparam uma viagem, para a qual vão embarcar diversas personagens. Umas, pela sua conduta, estão já condenadas, outras reúnem-se com o Anjo, que levará os justos para a Glória, \"terra que dá pão\". Estas personagens são a representação da sociedade do tempo - membros do clero, da nobreza, do povo, e figuras cujo comportamento Gil Vicente pretendia criticar ou elogiar.',790,'EUR','2021-04-01','Porto Editora','Português','128 x 198 x 8 mm','Capa mole',112,'books/book8.jpg',13,'2025-04-16 17:17:54.695228','2025-06-03 14:11:16.538354',5),(28,'9789720728067','Sermões','Padre António Vieira','Os Sermões do Padre António Vieira são considerados a obra-prima da oratória barroca em língua portuguesa. Com grande engenho e extraordinário domínio da linguagem, Vieira utiliza os sermões para criticar os costumes da sociedade do seu tempo e defender causas como a liberdade dos índios no Brasil.',1250,'EUR','2018-05-15','Porto Editora','Português','128 x 198 x 25 mm','Capa mole',312,'books/book9.jpg',6,'2025-04-16 17:17:55.209358','2025-05-27 15:47:21.015835',1),(29,'9789720728883','Cartas Portuguesas','Mariana Alcoforado','As Cartas Portuguesas são uma coleção de cinco cartas apaixonadas, atribuídas à freira portuguesa Mariana Alcoforado, que expressam o sofrimento amoroso pela separação do seu amante, um oficial francês. Este conjunto de cartas representa um importante documento do Barroco português e é considerado uma das mais belas expressões literárias do amor não correspondido.',850,'EUR','2019-02-10','Assírio & Alvim','Português','130 x 200 x 10 mm','Capa mole',96,'books/book10.jpg',7,'2025-04-16 17:17:55.715443','2025-05-31 19:53:13.142954',1),(30,'9789720730206','Carta de Guia de Casados','D. Francisco Manuel de Melo','Publicado em 1651, este é um texto didático que pretende ensinar os maridos a conviver com as suas esposas. Embora reflita ideias sobre o casamento e a condição feminina próprias do século XVII, é também um documento importante para entender as relações conjugais na sociedade barroca portuguesa.',980,'EUR','2017-08-05','Porto Editora','Português','128 x 198 x 15 mm','Capa mole',160,'books/book11.jpg',5,'2025-04-16 17:17:56.205681','2025-06-01 20:28:02.763363',1),(31,'978-972-23-1234-5','A Cidade e as Serras','Eça de Queirós','Romance póstumo de Eça de Queirós que narra a história de Jacinto, um jovem português que vive em Paris rodeado de luxos e tecnologia, mas que descobre a verdadeira felicidade quando regressa às suas origens rurais nas serras de Tormes. Uma reflexão sobre o progresso, a modernidade e a busca da autenticidade.',1850,'EUR','1901-01-01','Editorial Presença','Português','128 x 198 x 19 mm','Capa mole',256,'books/book12_YuRyz1M.jpg',49,'2025-06-01 16:17:26.127947','2025-06-03 14:11:16.522987',3);
/*!40000 ALTER TABLE `books_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_category`
--

DROP TABLE IF EXISTS `books_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci,
  `parent_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `books_category_parent_id_912a2f9f_fk_books_category_id` (`parent_id`),
  CONSTRAINT `books_category_parent_id_912a2f9f_fk_books_category_id` FOREIGN KEY (`parent_id`) REFERENCES `books_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_category`
--

LOCK TABLES `books_category` WRITE;
/*!40000 ALTER TABLE `books_category` DISABLE KEYS */;
INSERT INTO `books_category` VALUES (1,'Barroco','Obras do período barroco portugues',NULL),(3,'Clássicos','Obras clássicas da literatura portuguesa',NULL),(4,'Poesia','Obras poéticas portuguesas',NULL),(5,'Teatro','Peças de teatro portuguesas',NULL),(6,'Romance','Romances portugueses',NULL),(7,'Ensaio','Ensaios e crítica literária',NULL),(8,'Contemporâneo','Literatura portuguesa contemporânea',NULL);
/*!40000 ALTER TABLE `books_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_review`
--

DROP TABLE IF EXISTS `books_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `review_text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `book_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `books_review_book_id_user_id_73f755df_uniq` (`book_id`,`user_id`),
  KEY `books_review_user_id_a55792c0_fk_auth_user_id` (`user_id`),
  CONSTRAINT `books_review_book_id_a67a4c60_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `books_review_user_id_a55792c0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_review`
--

LOCK TABLES `books_review` WRITE;
/*!40000 ALTER TABLE `books_review` DISABLE KEYS */;
INSERT INTO `books_review` VALUES (1,4,'testereview1','2025-04-17 16:00:58.314247','2025-04-17 16:00:58.314247',27,2),(2,5,'teste','2025-05-31 14:17:32.213786','2025-05-31 14:17:32.213786',29,3),(3,5,'Outro teste','2025-06-01 18:54:09.444499','2025-06-01 18:54:09.444499',31,1),(5,3,'1234','2025-06-03 14:09:19.891513','2025-06-03 14:09:19.891513',21,5);
/*!40000 ALTER TABLE `books_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_contactmessage`
--

DROP TABLE IF EXISTS `contact_contactmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_contactmessage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subject` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contact_contactmessage_user_id_0ac8080c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `contact_contactmessage_user_id_0ac8080c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_contactmessage`
--

LOCK TABLES `contact_contactmessage` WRITE;
/*!40000 ALTER TABLE `contact_contactmessage` DISABLE KEYS */;
INSERT INTO `contact_contactmessage` VALUES (1,'asd','asd@asd.asd','book','asd','2025-05-28 16:55:43.659700',0,1);
/*!40000 ALTER TABLE `contact_contactmessage` ENABLE KEYS */;
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
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-06-01 16:17:26.128947','31','A Cidade e as Serras by Eça de Queirós',1,'[{\"added\": {}}]',8,1),(2,'2025-06-01 17:56:29.457999','9','Infantil',3,'',7,1),(3,'2025-06-01 17:56:51.225702','2','Medieval',3,'',7,1),(4,'2025-06-01 19:22:26.585764','3','Order 3 by livreiro_admin on 2025-06-01',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',12,1),(5,'2025-06-01 20:33:58.903574','4','inesteste\'s review of Carta de Guia de Casados',3,'',9,1),(6,'2025-06-03 15:14:45.471261','4','Order 4 by inesteste on 2025-06-01',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',12,1),(7,'2025-06-03 15:15:46.233412','3','Order 3 by livreiro_admin on 2025-06-01',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',12,1),(8,'2025-06-03 15:15:54.802412','3','Order 3 by livreiro_admin on 2025-06-01',2,'[]',12,1),(9,'2025-06-03 15:16:00.303524','4','Order 4 by inesteste on 2025-06-01',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',12,1);
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
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'books','book'),(7,'books','category'),(9,'books','review'),(14,'contact','contactmessage'),(5,'contenttypes','contenttype'),(12,'orders','order'),(13,'orders','orderitem'),(6,'sessions','session'),(15,'users','newslettersubscription'),(10,'users','userprofile'),(11,'users','wishlist');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-04-14 18:34:39.788874'),(2,'auth','0001_initial','2025-04-14 18:34:40.709445'),(3,'admin','0001_initial','2025-04-14 18:34:40.850541'),(4,'admin','0002_logentry_remove_auto_add','2025-04-14 18:34:40.857542'),(5,'admin','0003_logentry_add_action_flag_choices','2025-04-14 18:34:40.864543'),(6,'contenttypes','0002_remove_content_type_name','2025-04-14 18:34:40.969546'),(7,'auth','0002_alter_permission_name_max_length','2025-04-14 18:34:41.033747'),(8,'auth','0003_alter_user_email_max_length','2025-04-14 18:34:41.052906'),(9,'auth','0004_alter_user_username_opts','2025-04-14 18:34:41.059728'),(10,'auth','0005_alter_user_last_login_null','2025-04-14 18:34:41.113782'),(11,'auth','0006_require_contenttypes_0002','2025-04-14 18:34:41.116650'),(12,'auth','0007_alter_validators_add_error_messages','2025-04-14 18:34:41.122660'),(13,'auth','0008_alter_user_username_max_length','2025-04-14 18:34:41.185124'),(14,'auth','0009_alter_user_last_name_max_length','2025-04-14 18:34:41.248774'),(15,'auth','0010_alter_group_name_max_length','2025-04-14 18:34:41.264739'),(16,'auth','0011_update_proxy_permissions','2025-04-14 18:34:41.271604'),(17,'auth','0012_alter_user_first_name_max_length','2025-04-14 18:34:41.333321'),(18,'books','0001_initial','2025-04-14 18:34:41.645974'),(19,'orders','0001_initial','2025-04-14 18:34:41.859658'),(20,'sessions','0001_initial','2025-04-14 18:34:41.894849'),(21,'users','0001_initial','2025-04-14 18:34:42.133873'),(22,'contact','0001_initial','2025-05-28 16:10:18.823728'),(23,'orders','0002_alter_order_status','2025-06-03 14:14:03.491221'),(24,'orders','0003_alter_order_status','2025-06-03 15:13:27.537346'),(25,'users','0002_newslettersubscription','2025-06-03 15:47:14.832941');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1lf1x05lzxmk2tymxyt6tym00jeh3xmz','.eJxVjMsOwiAURP-FtSGUNy7d-w3kcuFK1dCktCvjvytJF5rMas6ZebEI-1bj3ssa58zOTLLTb5cAH6UNkO_QbgvHpW3rnPhQ-EE7vy65PC-H-3dQodexDt4VayYMKlgCS064bww6m0gQgdYSS_BKKxRkjUwqOWMn5YOWGpC9P9IcNzE:1u4lNO:BlB9GnA_Yl7iYcCTRkGqsOXYFEdcpkX3eeGXPp-Sfm8','2025-04-29 18:51:18.039691'),('el8ugrjch3tot99nvwl6nnue24domzjl','.eJxVjDsOwjAQBe_iGln-xWYp6TmDtfaucQA5UpxUiLuTSCmgnZn33iLiutS4dp7jSOIitDj9soT5yW0X9MB2n2Se2jKPSe6JPGyXt4n4dT3av4OKvW5ryKyCRRvAFwA22Q4DBkLCc8kuoPNFGyicKVgddAKl_Aac88ZZMCQ-X-Z_N1Q:1u4OlL:LW_3AYAE_O2i8kH3GRew5w4B0ddXe98jKJi1anfUnT4','2025-04-28 18:42:31.310943'),('w5kmzartt3fvrokka549eavg4t5yqql1','.eJxVjMsOwiAQRf-FtSG8BopL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ0ZsNPvFjE9qO0g37HdOk-9rcsc-a7wgw5-7Zmel8P9O6g46rcuRMkqkxFAEHkkJ6F4AIRMymMCbySayRurtLDkkgUXpYVJaywiCvb-APerN7A:1uMSK4:KDj4jbRNE4v9OMNl9fGk01f_eRBeKTx7OeqJO4V1gqA','2025-06-17 14:09:00.841001'),('xks0yqwuh86u0len9a5q9i9zd7f64ktk','.eJxVjDsOwjAQBe_iGlnO-k9JnzNYu_YaB1Ai5VMh7o4spYD2zcx7i4TH3tKx8ZqmIq7CiMvvRpifPHdQHjjfF5mXeV8nkl2RJ93kuBR-3U7376Dh1npdsnIhR6qgqw9sDFjPjnUGWzUhQGU7wOAtxVqLRsyKQgEKTpGJVny-_Gg4Zg:1uMUlc:aAwE8pEKxQgkoQJYdD5FB6jfEptrVZHuhfbRdo00Rvg','2025-06-17 16:45:36.212458');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_date` datetime(6) NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_amount_cents` int NOT NULL,
  `shipping_address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `shipping_city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `shipping_postal_code` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `payment_method` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_order_user_id_e9b59eb1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `orders_order_user_id_e9b59eb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
INSERT INTO `orders_order` VALUES (1,'2025-05-31 14:15:38.483719','processing',790,'PayPal Payment ID: 80V021746N3648806','Lisboa','1000-001','paypal',3),(2,'2025-05-31 19:53:13.123587','processing',850,'Rua das Oliveiras','Porto','2000-123','paypal',3),(3,'2025-06-01 19:19:01.338732','pending',980,'Rua das Figueiras 24','Funchal','1000-001','paypal',1),(4,'2025-06-01 20:28:02.745724','delivered',980,'Rua das Oliveiras','Aveiro','2000-123','paypal',4),(5,'2025-06-03 14:11:16.508594','processing',2640,'Rua das Oliveiras','Elvas','1234-123','paypal',5);
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_orderitem`
--

DROP TABLE IF EXISTS `orders_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `price_at_order_cents` int NOT NULL,
  `book_id` bigint NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orderitem_book_id_ed013cad_fk_books_book_id` (`book_id`),
  KEY `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` (`order_id`),
  CONSTRAINT `orders_orderitem_book_id_ed013cad_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_orderitem`
--

LOCK TABLES `orders_orderitem` WRITE;
/*!40000 ALTER TABLE `orders_orderitem` DISABLE KEYS */;
INSERT INTO `orders_orderitem` VALUES (1,1,790,27,1),(2,1,850,29,2),(3,1,980,30,3),(4,1,980,30,4),(5,1,1850,31,5),(6,1,790,27,5);
/*!40000 ALTER TABLE `orders_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_newslettersubscription`
--

DROP TABLE IF EXISTS `users_newslettersubscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_newslettersubscription` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subscribed_date` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_newslettersubscription`
--

LOCK TABLES `users_newslettersubscription` WRITE;
/*!40000 ALTER TABLE `users_newslettersubscription` DISABLE KEYS */;
INSERT INTO `users_newslettersubscription` VALUES (1,'newslettertest@test.com','2025-06-03 15:48:31.802907',1);
/*!40000 ALTER TABLE `users_newslettersubscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile`
--

DROP TABLE IF EXISTS `users_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `postal_code` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `preferred_language` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `users_userprofile_user_id_87251ef1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
INSERT INTO `users_userprofile` VALUES (1,NULL,NULL,NULL,NULL,NULL,'pt',1),(2,NULL,NULL,NULL,NULL,NULL,'pt',2),(3,NULL,NULL,NULL,NULL,NULL,'pt',3),(4,NULL,NULL,NULL,NULL,NULL,'pt',4),(5,NULL,NULL,NULL,NULL,NULL,'pt',5),(6,NULL,NULL,NULL,NULL,NULL,'pt',6);
/*!40000 ALTER TABLE `users_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_wishlist`
--

DROP TABLE IF EXISTS `users_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_wishlist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `added_date` datetime(6) NOT NULL,
  `book_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_wishlist_user_id_book_id_dbca7406_uniq` (`user_id`,`book_id`),
  KEY `users_wishlist_book_id_8e51ee3e_fk_books_book_id` (`book_id`),
  CONSTRAINT `users_wishlist_book_id_8e51ee3e_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `users_wishlist_user_id_6507553e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_wishlist`
--

LOCK TABLES `users_wishlist` WRITE;
/*!40000 ALTER TABLE `users_wishlist` DISABLE KEYS */;
INSERT INTO `users_wishlist` VALUES (1,'2025-05-31 19:19:00.518695',29,3),(2,'2025-06-01 18:22:26.418233',31,1),(3,'2025-06-03 14:09:11.866096',21,5),(4,'2025-06-03 15:27:34.077947',27,1);
/*!40000 ALTER TABLE `users_wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-03 18:44:47
