-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 19, 2023 at 11:07 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `employee`
--

-- --------------------------------------------------------

--
-- Table structure for table `empdata`
--

CREATE TABLE `empdata` (
  `Id` int(13) NOT NULL,
  `Name` varchar(500) DEFAULT NULL,
  `Age` int(10) DEFAULT NULL,
  `Date_of_birth` date DEFAULT NULL,
  `Salary` bigint(20) DEFAULT NULL,
  `Department` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `empdata`
--

INSERT INTO `empdata` (`Id`, `Name`, `Age`, `Date_of_birth`, `Salary`, `Department`) VALUES
(1, 'Mani', 21, '2002-10-21', 20000, 'Dev'),
(2, 'Vara Prasad', 21, '2002-10-19', 27000, 'QA'),
(3, 'Jassu', 24, '1999-12-12', 23000, 'QA'),
(4, 'Sai Ram', 22, '2000-12-23', 26000, 'BA'),
(5, 'Mahidhar', 21, '2002-09-23', 25000, 'BA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `empdata`
--
ALTER TABLE `empdata`
  ADD PRIMARY KEY (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
