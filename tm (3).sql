-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 25, 2024 at 01:03 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tm`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_admin`
--

CREATE TABLE `accounts_admin` (
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts_admin`
--

INSERT INTO `accounts_admin` (`user_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_customer`
--

CREATE TABLE `accounts_customer` (
  `user_id` bigint NOT NULL,
  `address` longtext NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts_customer`
--

INSERT INTO `accounts_customer` (`user_id`, `address`, `profile_picture`) VALUES
(2, 'Taman Sentosa, blok EF no. 86', NULL),
(11, 'Taman Sentosa, blok EF no. 86', NULL),
(16, 'asd', 'customer/16/profile/user.png');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_driver`
--

CREATE TABLE `accounts_driver` (
  `user_id` bigint NOT NULL,
  `license_number` varchar(20) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `id_card` varchar(100) DEFAULT NULL,
  `license_card` varchar(100) DEFAULT NULL,
  `profile_picture_confirmed` tinyint(1) NOT NULL,
  `accepted` tinyint(1) NOT NULL,
  `vehicle_available` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts_driver`
--

INSERT INTO `accounts_driver` (`user_id`, `license_number`, `availability`, `profile_picture`, `id_card`, `license_card`, `profile_picture_confirmed`, `accepted`, `vehicle_available`) VALUES
(3, '098190283019283901', 0, '', '', '', 0, 0, 0),
(13, '', 0, '', 'flow process sourcing cpro.png', 'struktur org.png', 0, 0, 0),
(14, '098190283019283901', 1, 'driver/14/profile/R.jpg', 'driver/14/id_card/no-home.jpeg', 'driver/14/license_card/Libur.png', 1, 1, 0),
(15, '098190283019283901', 0, 'driver/15/profile/mack.jpeg', 'media/driver/id/TnSbg2.png', 'media/driver/license/TnSbg3.png', 0, 1, 0),
(17, '', 0, '', 'download.jpeg', 'avatar-11.jpg', 0, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL,
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
  `is_customer` tinyint(1) NOT NULL,
  `is_driver` tinyint(1) NOT NULL,
  `phone_number` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_customer`, `is_driver`, `phone_number`) VALUES
(1, 'pbkdf2_sha256$720000$929aFeCOfbIFAx0jlofctp$k3g0QNXcvsggmz2Qg46598I5rTUyQhMb600lq3WROc8=', '2024-03-21 03:51:05.053084', 1, 'admin', '', '', 'admin@admin.admin', 1, 1, '2024-01-15 01:45:42.763857', 0, 0, ''),
(2, 'gerald', NULL, 0, 'gerald.sutarso', 'Gerald', 'Sutarso', 'geraldsutarso@gmail.com', 0, 1, '2024-01-15 02:13:20.000000', 1, 0, '+6282311921842'),
(3, 'lightningmcqueen', NULL, 0, 'mr.driver', 'Mister', 'Driver', 'misterdriver@mister.driver', 0, 1, '2024-01-15 06:52:28.000000', 0, 1, '00001010101010'),
(4, 'plslah', NULL, 0, 'student', '', '', '', 0, 1, '2024-01-19 07:47:39.000000', 1, 0, '6666666'),
(5, 'plslah', NULL, 0, 'acz', '', '', '', 0, 1, '2024-01-19 07:48:26.000000', 0, 1, '888888888'),
(6, 'pbkdf2_sha256$720000$DtygiM1PNf7F1zTqNMEQcL$oW9lDPIvzDlAcKdiObmT2k+EVqaED3UWHKiOEGnXjXY=', '2024-03-22 07:47:35.590243', 0, 'NOOOOO', 'I AM', 'YOUR FATHER', 'adada@gmail.com', 0, 1, '2024-01-19 08:17:27.703153', 1, 0, '0123123123'),
(11, 'pbkdf2_sha256$720000$UA597K1G35mduGUp3dyoen$0QSfhv4EUMkkdpSB0USQSx76HDjEmapIkiA7sk1nHTU=', '2024-01-26 06:09:21.894995', 0, 'gerald.sutarsosaaddd', 'asdasdas', 'asdasdasd', 'asdasdasd@dasdasd.asdaaaa', 0, 1, '2024-01-26 06:09:21.612992', 1, 0, '1231-1231-1236'),
(12, 'pbkdf2_sha256$720000$IhHWKcFUWn8efYNMhAfiyT$G6m6EQsmiCEODSYe93+ZD1pK3+jyom4RoWU2noUgacQ=', NULL, 1, 'donut', '', '', 'donut@donut.con', 1, 1, '2024-01-26 06:54:58.224544', 0, 0, ''),
(13, 'pbkdf2_sha256$720000$43xlkCNJZ2SrSov94oTvxA$h0LhcwELPqoxEZ11Pvu9aKgjuuZCq24Nuyog5y8J0l0=', NULL, 0, 'plslah', 'I WANT', 'TO BE DRIVER', 'plslah@plslah.pls', 0, 1, '2024-01-26 07:14:54.192744', 0, 1, '3131-3131-3131'),
(14, 'pbkdf2_sha256$720000$SwPUBCDJTXxyO7unf4TLfX$Djp66Dygap/sSQQzKDVKBHWHb2vTFzooqpS1n2D7ECo=', '2024-03-22 07:45:07.285303', 0, 'plslahda', 'I WANT', 'TO BE DRIVER', 'plslah@plslah.plsaa', 0, 1, '2024-01-26 07:23:29.798442', 0, 1, '3131-3131-3131'),
(15, 'pbkdf2_sha256$720000$5CafF8mYJz1fbGNOkaINhU$kh8hpYOEmBRDr/HyAVeW8HFa4K9SVoWuN9D14lzVx50=', '2024-03-22 08:06:17.253980', 0, 'Truckdriver', 'I WANT', 'Mack', 'mack@mek.mack', 0, 1, '2024-01-26 07:46:32.346852', 0, 1, '5555-5555-5555'),
(16, 'pbkdf2_sha256$720000$oBFeb5FPHVjZ7aLpgkzbfh$7T857VW3aaIG6KcZ6QjP4PE77/UPiTL3dvFnToaX1vc=', '2024-03-22 07:47:49.456657', 0, 'jk', 'ba', 'bi', 'ad@ad.ad', 0, 1, '2024-01-29 02:21:09.705472', 1, 0, '1313-1313-1313'),
(17, 'pbkdf2_sha256$720000$w5EZAp8dPBTrBWdIPslscO$pxE92jWp59BpIZPEcuzEC8FtlCpHsS1nC/TSrZ1J/jc=', '2024-03-22 07:43:15.959747', 0, 'vroom', 'asdasdas', 'asdasdasd', 'asdasdasd@dasdasd.asd', 0, 1, '2024-01-29 02:50:57.988551', 0, 1, '1231-1231-1231');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_groups`
--

CREATE TABLE `accounts_user_groups` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_user_permissions`
--

CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts_user_user_permissions`
--

INSERT INTO `accounts_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(1, 2, 39);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add admin', 7, 'add_admin'),
(26, 'Can change admin', 7, 'change_admin'),
(27, 'Can delete admin', 7, 'delete_admin'),
(28, 'Can view admin', 7, 'view_admin'),
(29, 'Can add customer', 8, 'add_customer'),
(30, 'Can change customer', 8, 'change_customer'),
(31, 'Can delete customer', 8, 'delete_customer'),
(32, 'Can view customer', 8, 'view_customer'),
(33, 'Can add driver', 9, 'add_driver'),
(34, 'Can change driver', 9, 'change_driver'),
(35, 'Can delete driver', 9, 'delete_driver'),
(36, 'Can view driver', 9, 'view_driver'),
(37, 'Can add truck', 10, 'add_truck'),
(38, 'Can change truck', 10, 'change_truck'),
(39, 'Can delete truck', 10, 'delete_truck'),
(40, 'Can view truck', 10, 'view_truck'),
(41, 'Can add maintenance', 11, 'add_maintenance'),
(42, 'Can change maintenance', 11, 'change_maintenance'),
(43, 'Can delete maintenance', 11, 'delete_maintenance'),
(44, 'Can view maintenance', 11, 'view_maintenance');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-01-15 01:46:19.051123', '1', 'Admin object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-01-15 02:16:12.255604', '2', 'gerald.sutarso', 1, '[{\"added\": {}}]', 6, 1),
(3, '2024-01-15 02:16:25.644462', '2', 'Customer object (2)', 1, '[{\"added\": {}}]', 8, 1),
(4, '2024-01-15 06:52:59.011729', '3', 'mr.driver', 1, '[{\"added\": {}}]', 6, 1),
(5, '2024-01-15 06:53:10.686198', '3', 'Driver object (3)', 1, '[{\"added\": {}}]', 9, 1),
(6, '2024-01-15 06:53:45.927997', '3', 'mr.driver', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]', 6, 1),
(7, '2024-01-15 07:01:08.315611', '1', 'Truck object (1)', 1, '[{\"added\": {}}]', 10, 1),
(8, '2024-01-16 00:57:13.554120', '1', 'Maintenance object (1)', 1, '[{\"added\": {}}]', 11, 1),
(9, '2024-01-16 01:35:58.367635', '2', 'Maintenance object (2)', 1, '[{\"added\": {}}]', 11, 1),
(10, '2024-01-16 02:14:53.889353', '1', 'Maintenance object (1)', 2, '[{\"changed\": {\"fields\": [\"Schedule\"]}}]', 11, 1),
(11, '2024-01-16 02:15:09.965193', '1', 'Lightning McQueen', 2, '[{\"changed\": {\"fields\": [\"Status\", \"Last maintained\"]}}]', 10, 1),
(12, '2024-01-19 07:48:26.209971', '4', 'student', 1, '[{\"added\": {}}]', 6, 1),
(13, '2024-01-19 07:48:54.629672', '5', 'acz', 1, '[{\"added\": {}}]', 6, 1),
(14, '2024-01-26 07:12:00.672076', '10', 'gerald.sutarsosaad', 3, '', 6, 1),
(15, '2024-01-26 07:12:00.674059', '9', 'gerald.sutarsosa', 3, '', 6, 1),
(16, '2024-01-26 07:12:00.675072', '8', 'gerald.sutarsos', 3, '', 6, 1),
(17, '2024-01-26 07:12:00.677066', '7', 'asdasdasda', 3, '', 6, 1),
(18, '2024-01-26 08:49:30.776422', '15', 'I WANT Mack', 2, '[{\"changed\": {\"fields\": [\"License number\", \"Id card\", \"License card\"]}}]', 9, 1),
(19, '2024-01-26 08:49:45.972401', '15', 'I WANT Mack', 2, '[{\"changed\": {\"fields\": [\"Profile picture\", \"Id card\", \"License card\"]}}]', 9, 1),
(20, '2024-01-26 08:50:05.946815', '15', 'I WANT Mack', 2, '[{\"changed\": {\"fields\": [\"Accepted\"]}}]', 9, 1),
(21, '2024-03-21 01:20:04.920362', '1', 'Lightning McQueen', 2, '[{\"changed\": {\"fields\": [\"Overall view\", \"Truck available\"]}}]', 10, 1),
(22, '2024-03-21 03:05:17.990503', '2', 'Mack', 1, '[{\"added\": {}}]', 10, 1),
(23, '2024-03-21 03:51:21.145172', '2', 'Mack', 2, '[{\"changed\": {\"fields\": [\"Driver\"]}}]', 10, 1),
(24, '2024-03-21 03:51:37.980395', '2', 'Mack', 2, '[{\"changed\": {\"fields\": [\"Driver\"]}}]', 10, 1),
(25, '2024-03-21 03:58:47.748484', '1', 'Lightning McQueen', 2, '[{\"changed\": {\"fields\": [\"Driver\"]}}]', 10, 1),
(26, '2024-03-21 03:58:57.263734', '2', 'Mack', 2, '[{\"changed\": {\"fields\": [\"Driver\"]}}]', 10, 1),
(27, '2024-03-21 04:00:07.042232', '2', 'Mack', 2, '[{\"changed\": {\"fields\": [\"Driver\"]}}]', 10, 1),
(28, '2024-03-21 04:00:10.171322', '1', 'Lightning McQueen', 2, '[{\"changed\": {\"fields\": [\"Driver\"]}}]', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'admin'),
(8, 'accounts', 'customer'),
(9, 'accounts', 'driver'),
(6, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(11, 'vehicles', 'maintenance'),
(10, 'vehicles', 'truck');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-01-15 01:20:38.079738'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-01-15 01:20:38.110738'),
(3, 'auth', '0001_initial', '2024-01-15 01:20:38.248024'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-01-15 01:20:38.279894'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-01-15 01:20:38.283882'),
(6, 'auth', '0004_alter_user_username_opts', '2024-01-15 01:20:38.288882'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-01-15 01:20:38.293882'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-01-15 01:20:38.296325'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-01-15 01:20:38.299339'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-01-15 01:20:38.303339'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-01-15 01:20:38.309350'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-01-15 01:20:38.319389'),
(13, 'auth', '0011_update_proxy_permissions', '2024-01-15 01:20:38.325999'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-01-15 01:20:38.331999'),
(15, 'accounts', '0001_initial', '2024-01-15 01:20:38.590120'),
(16, 'admin', '0001_initial', '2024-01-15 01:20:38.655964'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-01-15 01:20:38.664376'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-01-15 01:20:38.670404'),
(19, 'sessions', '0001_initial', '2024-01-15 01:20:38.708931'),
(20, 'vehicles', '0001_initial', '2024-01-15 01:20:38.805179'),
(21, 'accounts', '0002_driver_vehicle_available_alter_driver_availability', '2024-01-15 01:30:33.629814'),
(22, 'accounts', '0003_alter_user_is_customer_alter_user_is_driver', '2024-01-16 00:56:55.624326'),
(23, 'vehicles', '0002_alter_maintenance_status_alter_truck_capacity_and_more', '2024-01-16 00:56:55.742507'),
(24, 'vehicles', '0003_rename_model_truck_truck_model', '2024-01-16 01:19:37.354718'),
(25, 'vehicles', '0004_remove_maintenance_status_maintenance_schedule_and_more', '2024-01-16 02:14:31.700850'),
(26, 'accounts', '0004_alter_admin_user_alter_customer_user_and_more', '2024-01-26 07:44:54.357201'),
(27, 'vehicles', '0005_alter_maintenance_truck_alter_truck_driver', '2024-01-26 07:44:54.370203'),
(28, 'accounts', '0005_alter_driver_id_card_alter_driver_license_card_and_more', '2024-01-26 08:44:31.772430'),
(29, 'accounts', '0006_customer_profile_picture', '2024-02-28 04:10:41.673977'),
(30, 'accounts', '0007_alter_customer_profile_picture_alter_driver_id_card_and_more', '2024-03-04 07:04:42.518592'),
(31, 'vehicles', '0006_truck_back_view_truck_front_view_truck_side_view_and_more', '2024-03-13 07:23:07.968885'),
(32, 'vehicles', '0007_truck_overall_view', '2024-03-14 01:10:01.790427'),
(33, 'vehicles', '0008_truck_truck_accepted_truck_truck_available', '2024-03-21 01:13:53.795847'),
(34, 'vehicles', '0009_remove_truck_driver_truck_driver', '2024-03-21 03:58:04.958882'),
(35, 'vehicles', '0010_remove_truck_driver_truck_driver', '2024-03-21 03:59:54.747691'),
(36, 'vehicles', '0011_alter_truck_status_alter_truck_truck_available', '2024-03-21 08:44:44.451761');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7l5i970cb14rs962rg3mj6suv94qd8xn', '.eJxVjDsOwjAQRO_iGln-xD9K-pzBsndXOIBsKU4qxN2JpRRQTDPvzbxZTPtW4t5pjQuyK5Ps8tvlBE-qA-Aj1Xvj0Oq2LpkPhZ-087khvW6n-3dQUi_H2lklEbzWciKr7JEkAF1woIMJNJFR4IciUDhDXmiS6AhMCqApA_t8AcgfN9U:1rPDp8:eka9PiiKOuPSlCQXKm5VOmVb1bactu4L3pldWEElRXM', '2024-01-29 03:39:42.393659'),
('8wuib1hqrcent11cqyuxaqmjxk2zcfki', '.eJxVjDkOwyAUBe9CHSE-myFl-pwBAR_iJQHJ2FWUu8dIbtzOzHtfsre0Fv9J5E7mhdyI8_s2uk7dhAcEfYXBxyWVbnD25VVprGVbp0B7Qk_b6LNiej_O9nIw-jb2NYKRqIFLL1EGxocQTMjcKrACQFluYMCkFeOMqygyHhSF1gqyskKQ3x-N7jvM:1rUz8W:otu7akan7H6FPUju54DXRzebo6gEhFf9mu-c5_xTcVM', '2024-02-14 01:11:32.401099'),
('bflxsypnkll4o4dm9lhwdu6etohs1n5r', '.eJx9kTtvgzAUhf9KxdyCzSs4U9qtQ7o0Ukd0bV_AiTHIQKSq6n_vRbHSpEMZLHHO-e7D_oqWCb2DHqNtdPCLOmlvzuijx6iGZe7q1a6NJpcX96IEdUK3OvoIrh1iNbjZGxmvkTi4U7wfNNqXkL0r0MHUEZ1KJvOMyRKEkDlLM1VpZAJBVU2ZKq1ZvkmbUmLGmVZiU3CeSZGXjOWqgkJQ0cb4aQ5LvD58PL8dSLRw1fbUnpSxGxzWbuklLbiNCvqergf52IOxZPQU3_V4ivsLZ41CN92QTFRcsLTKGBd0CsYpBWeiQRpr5s9o24CdkFr6oTEW69GoefHrLEmP2kByueaEF0mIJGuz-DhiS7WMrhV4_Ru_g4xODu5dtmk8uvZmvn-QELlwWeD-DFfTA9JNEncdH5TCcV6F2S_0f8bOKCLCrhZD8vsHGGPCWw:1rna3p:C6iEdyXh9Te4fkCtijMGG0QmTs-0dmKfofqgFnHQND0', '2024-04-05 08:15:33.021114'),
('chguf1u38hwjs30wqhsk62rlzb6oqud8', 'eyJ1c2VybmFtZSI6ImFkbWluIn0:1rVM7V:_rm5L1HQp49l3klLXBRbSZJbKHgbbTiKVX4cUoWdNzA', '2024-02-15 01:44:01.247207'),
('e3bk8l6qnquac02q8ejipj2esd4tlfz0', '.eJxVj8FuwyAQRP-Fc4sNGGLnVPWeb7AW7zomMWCBfYr67wXJapXLSvNmdrT7YkemFMATu7LHk32wEY59GSsdHRYozDu0MD0pVAcfEO6RTzHsyVleI_x0M79FpPX7zL4VLJCXuo2i79AI2UGHnW3lxdreznLQYlBC6EH24oJkdCtbqSc1Y6GojNFi1oNSpXR2Ke_n7RYKWOFfu6K3JQYaw-EtpfqKEurzbxSfPLi1GIBfgBzqoYCYKOcKc9VbirNbadzctB-pNjee0EEzHXmPnlIjTHOGmvof38Kd_fwCucNt1g:1rkJzG:sr2DFKKDtXxBTDG2iBGea8YsUHdbOv_p1hZx6hKKtc0', '2024-03-27 08:29:22.401304'),
('jjw7a76vy2cv3snwjjx555kznboglko8', '.eJxVj8FuwyAQRP-Fc4sNGGLnVPWeb7AW7zomMWCBfYr67wXJapXLSvNmdrT7YkemFMATu7LHk32wEY59GSsdHRYozDu0MD0pVAcfEO6RTzHsyVleI_x0M79FpPX7zL4VLJCXuo2i79AI2UGHnW3lxdreznLQYlBC6EH24oJkdCtbqSc1Y6GojNFi1oNSpXR2Ke_n7RYKWOFfu6K3JQYaw-EtpfqKEurzbxSfPLi1GIBfgBzqoYCYKOcKc9VbirNbadzctB-pNjee0EEzHXmPnlIjTHOGmvof38Kd_fwCucNt1g:1rnYu6:O7E2Hrdc_bBWB7fLGp3omi4dWGbicD6Z0Lrt8ahe2Mw', '2024-04-05 07:01:26.534492'),
('nfoxt8b3xg6ll483jvkvkih76384ps2n', 'eyJ1c2VybmFtZSI6InBsc2xhaCJ9:1rnYze:UAlk0pvq9dk6BaS194XwW2VBlZLJmdjOXXbSZMyCii4', '2024-04-05 07:07:10.321408'),
('rg7d5xt7t1habxjpir3qssc2d8tmba48', '.eJxVjDsOwjAQRO_iGln-xD9K-pzBsndXOIBsKU4qxN2JpRRQTDPvzbxZTPtW4t5pjQuyK5Ps8tvlBE-qA-Aj1Xvj0Oq2LpkPhZ-087khvW6n-3dQUi_H2lklEbzWciKr7JEkAF1woIMJNJFR4IciUDhDXmiS6AhMCqApA_t8AcgfN9U:1rPC35:y79n8dD1p-fnyqnUBVGNa_anz1hoafItjFp1hiF4hnY', '2024-01-29 01:45:59.759335'),
('rokwqggq9vg8dspccono5mterw8jvi54', '.eJxVj8FuwyAQRP-Fc4sNGGLnVPWeb7AW7zomMWCBfYr67wXJapXLSvNmdrT7YkemFMATu7LHk32wEY59GSsdHRYozDu0MD0pVAcfEO6RTzHsyVleI_x0M79FpPX7zL4VLJCXuo2i79AI2UGHnW3lxdreznLQYlBC6EH24oJkdCtbqSc1Y6GojNFi1oNSpXR2Ke_n7RYKWOFfu6K3JQYaw-EtpfqKEurzbxSfPLi1GIBfgBzqoYCYKOcKc9VbirNbadzctB-pNjee0EEzHXmPnlIjTHOGmvof38Kd_fwCucNt1g:1rnYvt:ih1rbxO0PGJES109fe5RmXmm9iyPQ7Uq2HPIHZmW5gM', '2024-04-05 07:03:17.848985'),
('yda70tezztpd1ri8ohc8mwoe7p49vobr', '.eJxVjDsOgzAQRO_iOrL8wdhOmZ4zoGV3FTsJRsJQRbl7sERDMc28N_MVe-W1wMziLoDmXMRNjLBvaWxgzHT0-tpNgG8uDdALynORuJRtzZNsijxplcNC_Hmc7uUgQU3H2vdGEwZrdce96Y-AQvLRo40ucsfOYGiKIuUdB2VZk2d0ENHyhOL3B0oVPiw:1rUJfN:_eOttOw3ImzEpiFXLv99Bg-tZiuYBUZOREw_LknaY64', '2024-02-12 04:54:41.797646');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_maintenance`
--

CREATE TABLE `vehicles_maintenance` (
  `id` bigint NOT NULL,
  `sensor_type` varchar(50) NOT NULL,
  `notification_date` datetime(6) NOT NULL,
  `truck_id` bigint NOT NULL,
  `schedule` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `vehicles_maintenance`
--

INSERT INTO `vehicles_maintenance` (`id`, `sensor_type`, `notification_date`, `truck_id`, `schedule`) VALUES
(1, 'ADADA', '2024-01-16 00:57:13.552128', 1, '2024-01-16 02:14:50.000000'),
(2, 'ADADA', '2024-01-16 01:35:58.366634', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_truck`
--

CREATE TABLE `vehicles_truck` (
  `id` bigint NOT NULL,
  `truck_model` varchar(255) NOT NULL,
  `license_plate` varchar(20) NOT NULL,
  `capacity` int DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `last_maintained` date DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `back_view` varchar(100) DEFAULT NULL,
  `front_view` varchar(100) DEFAULT NULL,
  `side_view` varchar(100) DEFAULT NULL,
  `top_view` varchar(100) DEFAULT NULL,
  `overall_view` varchar(100) DEFAULT NULL,
  `truck_accepted` tinyint(1) NOT NULL,
  `truck_available` tinyint(1) NOT NULL,
  `driver_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `vehicles_truck`
--

INSERT INTO `vehicles_truck` (`id`, `truck_model`, `license_plate`, `capacity`, `location`, `last_maintained`, `status`, `back_view`, `front_view`, `side_view`, `top_view`, `overall_view`, `truck_accepted`, `truck_available`, `driver_id`) VALUES
(1, 'Lightning McQueen', 'B 4131 KAU', 2020, 'AAHAHAHA', '2024-01-16', 'WARNING', '', '', '', '', 'truck/1/overall/mcqueen.png', 0, 0, 14),
(10, 'Optimus Prime', 'G 4130 OOT', 1111, NULL, NULL, 'OK', 'truck/None/backview/hino.jpeg', 'truck/None/frontview/hino.jpeg', 'truck/None/sideview/hino.jpeg', 'truck/None/topview/hino.jpeg', 'truck/None/overall/optimumpride.jpeg', 0, 0, 14),
(12, 'Hino', 'T 4111 KAU', 33333, NULL, NULL, 'OK', 'truck/None/backview/optimumpride.jpeg', 'truck/None/frontview/mack_aHtSOZB.jpeg', 'truck/None/sideview/mack_sIsZbZV.jpeg', 'truck/None/topview/optimumpride_b1BH3jn.jpeg', 'truck/None/overall/hino_OTfsNn4.jpeg', 0, 0, 14),
(17, 'Mack', 'T 4111 LAH', 333332, NULL, NULL, 'OK', 'truck/None/backview/hino_U5iNele.jpeg', 'truck/None/frontview/hino_PU1SkSc.jpeg', 'truck/None/sideview/hino_4IvVwQt.jpeg', 'truck/None/topview/hino_mHFSWNB.jpeg', 'truck/None/overall/mack_oSokqqo.jpeg', 0, 0, 14);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_admin`
--
ALTER TABLE `accounts_admin`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `accounts_driver`
--
ALTER TABLE `accounts_driver`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  ADD KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  ADD KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `vehicles_maintenance`
--
ALTER TABLE `vehicles_maintenance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicles_maintenance_truck_id_881233c9_fk_vehicles_truck_id` (`truck_id`);

--
-- Indexes for table `vehicles_truck`
--
ALTER TABLE `vehicles_truck`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicles_truck_driver_id_3a442e20_fk_accounts_driver_user_id` (`driver_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `vehicles_maintenance`
--
ALTER TABLE `vehicles_maintenance`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vehicles_truck`
--
ALTER TABLE `vehicles_truck`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_admin`
--
ALTER TABLE `accounts_admin`
  ADD CONSTRAINT `accounts_admin_user_id_af8a3aeb_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  ADD CONSTRAINT `accounts_customer_user_id_11606857_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_driver`
--
ALTER TABLE `accounts_driver`
  ADD CONSTRAINT `accounts_driver_user_id_193e1fcf_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `vehicles_maintenance`
--
ALTER TABLE `vehicles_maintenance`
  ADD CONSTRAINT `vehicles_maintenance_truck_id_881233c9_fk_vehicles_truck_id` FOREIGN KEY (`truck_id`) REFERENCES `vehicles_truck` (`id`);

--
-- Constraints for table `vehicles_truck`
--
ALTER TABLE `vehicles_truck`
  ADD CONSTRAINT `vehicles_truck_driver_id_3a442e20_fk_accounts_driver_user_id` FOREIGN KEY (`driver_id`) REFERENCES `accounts_driver` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
