-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.3.0 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for healthyapp
CREATE DATABASE IF NOT EXISTS `healthyapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `healthyapp`;

-- Dumping structure for table healthyapp.account
CREATE TABLE IF NOT EXISTS `account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT (now()),
  `authenticated` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.account: ~1 rows (approximately)
INSERT INTO `account` (`id`, `email`, `password`, `created_at`, `authenticated`) VALUES
	(1, 'manhthang085213@gmail.com', '$2b$12$2mttOZXpt.76CLOxvEGerehy2fsufpNGR47mYNqKa/Ay9Nsqfrmv2', '2024-04-23 07:36:45', 0);

-- Dumping structure for table healthyapp.cannot_eat
CREATE TABLE IF NOT EXISTS `cannot_eat` (
  `disease_id` int NOT NULL,
  `ingredient_id` int NOT NULL,
  PRIMARY KEY (`disease_id`,`ingredient_id`),
  KEY `ingredient_id` (`ingredient_id`),
  CONSTRAINT `cannot_eat_ibfk_1` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredient` (`id`),
  CONSTRAINT `cannot_eat_ibfk_2` FOREIGN KEY (`disease_id`) REFERENCES `disease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.cannot_eat: ~0 rows (approximately)

-- Dumping structure for table healthyapp.disease
CREATE TABLE IF NOT EXISTS `disease` (
  `id` int NOT NULL AUTO_INCREMENT,
  `disease_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.disease: ~0 rows (approximately)

-- Dumping structure for table healthyapp.dish
CREATE TABLE IF NOT EXISTS `dish` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `calo` float DEFAULT NULL,
  `carb` float DEFAULT NULL,
  `fat` float DEFAULT NULL,
  `protein` float DEFAULT NULL,
  `img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_premium` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.dish: ~0 rows (approximately)

-- Dumping structure for table healthyapp.favorite
CREATE TABLE IF NOT EXISTS `favorite` (
  `user_id` int NOT NULL,
  `dish_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`dish_id`),
  KEY `dish_id` (`dish_id`),
  CONSTRAINT `favorite_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `favorite_ibfk_2` FOREIGN KEY (`dish_id`) REFERENCES `dish` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.favorite: ~0 rows (approximately)

-- Dumping structure for table healthyapp.ingredient
CREATE TABLE IF NOT EXISTS `ingredient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `calo` float DEFAULT NULL,
  `carb` float DEFAULT NULL,
  `fat` float DEFAULT NULL,
  `protein` float DEFAULT NULL,
  `img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.ingredient: ~0 rows (approximately)

-- Dumping structure for table healthyapp.meal
CREATE TABLE IF NOT EXISTS `meal` (
  `menu_id` int NOT NULL,
  `dish_order` int NOT NULL,
  `dish_id` int DEFAULT NULL,
  `meal_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`menu_id`,`dish_order`,`meal_type`),
  KEY `dish_id` (`dish_id`),
  CONSTRAINT `meal_ibfk_1` FOREIGN KEY (`dish_id`) REFERENCES `dish` (`id`),
  CONSTRAINT `meal_ibfk_2` FOREIGN KEY (`menu_id`) REFERENCES `suggested_menu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.meal: ~0 rows (approximately)

-- Dumping structure for table healthyapp.recipe
CREATE TABLE IF NOT EXISTS `recipe` (
  `ingredient_id` int NOT NULL,
  `dish_id` int NOT NULL,
  `grams` float DEFAULT NULL,
  PRIMARY KEY (`ingredient_id`,`dish_id`),
  KEY `dish_id` (`dish_id`),
  CONSTRAINT `recipe_ibfk_1` FOREIGN KEY (`dish_id`) REFERENCES `dish` (`id`),
  CONSTRAINT `recipe_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredient` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.recipe: ~0 rows (approximately)

-- Dumping structure for table healthyapp.statistic
CREATE TABLE IF NOT EXISTS `statistic` (
  `user_id` int NOT NULL,
  `date` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `morning_calo` int DEFAULT NULL,
  `noon_calo` int DEFAULT NULL,
  `dinner_calo` int DEFAULT NULL,
  `snack_calo` int DEFAULT NULL,
  `exercise_calo` int DEFAULT NULL,
  `water` int DEFAULT NULL,
  PRIMARY KEY (`user_id`,`date`),
  CONSTRAINT `statistic_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.statistic: ~0 rows (approximately)

-- Dumping structure for table healthyapp.subscription
CREATE TABLE IF NOT EXISTS `subscription` (
  `user_id` int NOT NULL,
  `is_activate` tinyint(1) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `is_paid` tinyint(1) DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `subscription_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.subscription: ~0 rows (approximately)

-- Dumping structure for table healthyapp.suggested_menu
CREATE TABLE IF NOT EXISTS `suggested_menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `fitness_Score` int DEFAULT NULL,
  `date_suggest` datetime DEFAULT NULL,
  `num_suggest` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `suggested_menu_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.suggested_menu: ~0 rows (approximately)

-- Dumping structure for table healthyapp.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `age` int DEFAULT NULL,
  `height` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `gender` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `exercise` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `aim` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `disease_id` int DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_id` (`account_id`),
  KEY `disease_id` (`disease_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`),
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`disease_id`) REFERENCES `disease` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table healthyapp.user: ~1 rows (approximately)
INSERT INTO `user` (`id`, `username`, `age`, `height`, `weight`, `gender`, `exercise`, `aim`, `disease_id`, `is_deleted`, `account_id`) VALUES
	(1, 'ManhThang', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
