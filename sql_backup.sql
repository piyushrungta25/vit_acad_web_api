-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 24, 2016 at 03:21 PM
-- Server version: 5.5.44-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `all_posts`
--

-- --------------------------------------------------------

--
-- Table structure for table `club_info`
--

CREATE TABLE IF NOT EXISTS `club_info` (
  `club_name` varchar(128) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `club_logo` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `club_desc` text COLLATE utf8mb4_unicode_ci,
  `contact_info` text COLLATE utf8mb4_unicode_ci,
  UNIQUE KEY `club_name` (`club_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `club_info`
--

INSERT INTO `club_info` (`club_name`, `club_logo`, `club_desc`, `contact_info`) VALUES
('club_name0', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description0', 'contact info0'),
('club_name1', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description1', 'contact info1'),
('club_name2', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description2', 'contact info2'),
('club_name3', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description3', 'contact info3'),
('club_name4', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description4', 'contact info4'),
('club_name5', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description5', 'contact info5'),
('club_name6', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description6', 'contact info6'),
('club_name7', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description7', 'contact info7'),
('club_name8', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description8', 'contact info8'),
('club_name9', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description9', 'contact info9'),
('club_name10', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description10', 'contact info10'),
('club_name11', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description11', 'contact info11'),
('club_name12', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description12', 'contact info12'),
('club_name13', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description13', 'contact info13'),
('club_name14', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description14', 'contact info14'),
('club_name15', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description15', 'contact info15'),
('club_name16', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description16', 'contact info16'),
('club_name17', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description17', 'contact info17'),
('club_name18', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description18', 'contact info18'),
('club_name19', 'http://www.youthedesigner.com/wp-content/uploads/2012/06/full_ps.jpg', 'long description19', 'contact info19');

-- --------------------------------------------------------

--
-- Table structure for table `login_data`
--

CREATE TABLE IF NOT EXISTS `login_data` (
  `club_name` varchar(128) NOT NULL,
  `username` varchar(16) NOT NULL,
  `password` varchar(8) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `session_id` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_data`
--

INSERT INTO `login_data` (`club_name`, `username`, `password`, `email`, `session_id`) VALUES
('club_name0', 'club_name_user0', '100', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name1', 'club_name_user1', '101', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name2', 'club_name_user2', '102', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name3', 'club_name_user3', '103', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name4', 'club_name_user4', '104', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name5', 'club_name_user5', '105', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name6', 'club_name_user6', '106', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name7', 'club_name_user7', '107', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name8', 'club_name_user8', '108', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name9', 'club_name_user9', '109', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name10', 'club_name_user10', '110', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name11', 'club_name_user11', '111', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name12', 'club_name_user12', '112', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name13', 'club_name_user13', '113', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name14', 'club_name_user14', '114', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name15', 'club_name_user15', '115', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name16', 'club_name_user16', '116', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name17', 'club_name_user17', '117', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name18', 'club_name_user18', '118', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name19', 'club_name_user19', '119', 'piyushrungta25@gmail.com', '1oyXg9l89ZH3LyR0BzSqpwjhR6fSOj65yFo6RyG1K6WKDIi740GTHs0butVSkuWE'),
('club_name69', 'piy', '111', '111', 'RwK9gHDCXjXOVtlwNv7JDOAeOrc0xsQzJ6dOG7juTSMGZFiPdiB7gKBmAA1BLJMa');

-- --------------------------------------------------------

--
-- Table structure for table `pending_verification`
--

CREATE TABLE IF NOT EXISTS `pending_verification` (
  `club_name` varchar(128) NOT NULL,
  `club_mail` varchar(128) NOT NULL,
  `unique_key` varchar(32) DEFAULT NULL,
  UNIQUE KEY `club_mail` (`club_mail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pending_verification`
--

INSERT INTO `pending_verification` (`club_name`, `club_mail`, `unique_key`) VALUES
('aa', 'aa', 'PhTMESXMB3dnpYCWkDLPBeKO8NYCoFzC'),
('kakak', 'kakak', 'NrBFEIJnDTkTKu9FRzdZ9f4bf0HTxPzJ'),
('papap', 'papap', 'bfQUY4rP4qWL2cy2Oa7V797csnuD3atl'),
('new_club_1', 'piyushrungta25@gmail.com', '7eo7JX5JRsNfJ6wfQEA8BZBLfqOUqmwd');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE IF NOT EXISTS `posts` (
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `club_name` varchar(255) NOT NULL,
  `event_name` varchar(255) NOT NULL,
  `post_body` text NOT NULL,
  `event_date` date NOT NULL,
  `event_time` time DEFAULT NULL,
  `event_venue` varchar(255) NOT NULL,
  `image_link` varchar(255) NOT NULL,
  `event_manager` varchar(32) DEFAULT NULL,
  `evnt_mngr_phno` varchar(10) DEFAULT NULL,
  UNIQUE KEY `timestamp` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`timestamp`, `club_name`, `event_name`, `post_body`, `event_date`, `event_time`, `event_venue`, `image_link`, `event_manager`, `evnt_mngr_phno`) VALUES
('2016-01-19 14:52:47', 'club_name1', 'event_name1', 'postbody1', '2016-01-01', '01:01:01', 'event_venue1', 'image_link1', NULL, NULL),
('2016-01-19 14:52:49', 'club_name2', 'event_name2', 'postbody2', '2016-02-02', '02:02:02', 'event_venue2', 'image_link2', NULL, NULL),
('2016-01-19 14:52:51', 'club_name3', 'event_name3', 'postbody3', '2016-03-03', '03:03:03', 'event_venue3', 'image_link3', NULL, NULL),
('2016-01-19 14:52:53', 'club_name4', 'event_name4', 'postbody4', '2016-04-04', '04:04:04', 'event_venue4', 'image_link4', NULL, NULL),
('2016-01-19 14:52:55', 'club_name5', 'event_name5', 'postbody5', '2016-05-05', '05:05:05', 'event_venue5', 'image_link5', NULL, NULL),
('2016-01-19 14:52:57', 'club_name6', 'event_name6', 'postbody6', '2016-06-06', '06:06:06', 'event_venue6', 'image_link6', NULL, NULL),
('2016-01-19 14:52:59', 'club_name7', 'event_name7', 'postbody7', '2016-07-07', '07:07:07', 'event_venue7', 'image_link7', NULL, NULL),
('2016-01-19 14:53:01', 'club_name8', 'event_name8', 'postbody8', '2016-08-08', '08:08:08', 'event_venue8', 'image_link8', NULL, NULL),
('2016-01-19 14:53:03', 'club_name9', 'event_name9', 'postbody9', '2016-09-09', '09:09:09', 'event_venue9', 'image_link9', NULL, NULL),
('2016-01-19 14:53:05', 'club_name10', 'event_name10', 'postbody10', '2016-10-10', '10:10:10', 'event_venue10', 'image_link10', NULL, NULL),
('2016-01-19 14:53:07', 'club_name11', 'event_name11', 'postbody11', '2016-11-11', '11:11:11', 'event_venue11', 'image_link11', NULL, NULL),
('2016-01-19 14:53:11', 'club_name13', 'event_name13', 'postbody13', '2016-01-13', '01:13:13', 'event_venue13', 'image_link13', NULL, NULL),
('2016-01-19 14:53:13', 'club_name14', 'event_name14', 'postbody14', '2016-02-14', '02:14:14', 'event_venue14', 'image_link14', NULL, NULL),
('2016-01-19 14:53:15', 'club_name15', 'event_name15', 'postbody15', '2016-03-15', '03:15:15', 'event_venue15', 'image_link15', NULL, NULL),
('2016-01-19 14:53:18', 'club_name16', 'event_name16', 'postbody16', '2016-04-16', '04:16:16', 'event_venue16', 'image_link16', NULL, NULL),
('2016-01-19 14:53:20', 'club_name17', 'event_name17', 'postbody17', '2016-05-17', '05:17:17', 'event_venue17', 'image_link17', NULL, NULL),
('2016-01-19 14:53:22', 'club_name18', 'event_name18', 'postbody18', '2016-06-18', '06:18:18', 'event_venue18', 'image_link18', NULL, NULL),
('2016-01-19 14:53:24', 'club_name19', 'event_name19', 'postbody19', '2016-07-19', '07:19:19', 'event_venue19', 'image_link19', NULL, NULL),
('2016-01-19 14:53:26', 'club_name0', 'event_name20', 'postbody20', '2016-08-20', '08:20:20', 'event_venue20', 'image_link20', NULL, NULL),
('2016-01-19 14:53:28', 'club_name1', 'event_name21', 'postbody21', '2016-09-21', '09:21:21', 'event_venue21', 'image_link21', NULL, NULL),
('2016-01-19 14:53:30', 'club_name2', 'event_name22', 'postbody22', '2016-10-22', '10:22:22', 'event_venue22', 'image_link22', NULL, NULL),
('2016-01-19 14:53:32', 'club_name3', 'event_name23', 'postbody23', '2016-11-23', '11:23:23', 'event_venue23', 'image_link23', NULL, NULL),
('2016-01-19 14:53:36', 'club_name5', 'event_name25', 'postbody25', '2016-01-25', '01:25:25', 'event_venue25', 'image_link25', NULL, NULL),
('2016-01-19 14:53:38', 'club_name6', 'event_name26', 'postbody26', '2016-02-26', '02:26:26', 'event_venue26', 'image_link26', NULL, NULL),
('2016-01-19 14:53:40', 'club_name7', 'event_name27', 'postbody27', '2016-03-27', '03:27:27', 'event_venue27', 'image_link27', NULL, NULL),
('2016-01-19 14:53:42', 'club_name8', 'event_name28', 'postbody28', '2016-04-28', '04:28:28', 'event_venue28', 'image_link28', NULL, NULL),
('2016-01-19 14:53:44', 'club_name9', 'event_name29', 'postbody29', '2016-05-29', '05:29:29', 'event_venue29', 'image_link29', NULL, NULL),
('2016-01-19 14:53:48', 'club_name11', 'event_name31', 'postbody31', '2016-07-01', '07:31:31', 'event_venue31', 'image_link31', NULL, NULL),
('2016-01-19 14:53:50', 'club_name12', 'event_name32', 'postbody32', '2016-08-02', '08:32:32', 'event_venue32', 'image_link32', NULL, NULL),
('2016-01-19 14:53:52', 'club_name13', 'event_name33', 'postbody33', '2016-09-03', '09:33:33', 'event_venue33', 'image_link33', NULL, NULL),
('2016-01-19 14:53:54', 'club_name14', 'event_name34', 'postbody34', '2016-10-04', '10:34:34', 'event_venue34', 'image_link34', NULL, NULL),
('2016-01-19 14:53:56', 'club_name15', 'event_name35', 'postbody35', '2016-11-05', '11:35:35', 'event_venue35', 'image_link35', NULL, NULL),
('2016-01-19 14:54:00', 'club_name17', 'event_name37', 'postbody37', '2016-01-07', '01:37:37', 'event_venue37', 'image_link37', NULL, NULL),
('2016-01-19 14:54:02', 'club_name18', 'event_name38', 'postbody38', '2016-02-08', '02:38:38', 'event_venue38', 'image_link38', NULL, NULL),
('2016-01-19 14:54:04', 'club_name19', 'event_name39', 'postbody39', '2016-03-09', '03:39:39', 'event_venue39', 'image_link39', NULL, NULL),
('2016-01-19 14:54:06', 'club_name0', 'event_name40', 'postbody40', '2016-04-10', '04:40:40', 'event_venue40', 'image_link40', NULL, NULL),
('2016-01-19 14:54:09', 'club_name1', 'event_name41', 'postbody41', '2016-05-11', '05:41:41', 'event_venue41', 'image_link41', NULL, NULL),
('2016-01-19 14:54:11', 'club_name2', 'event_name42', 'postbody42', '2016-06-12', '06:42:42', 'event_venue42', 'image_link42', NULL, NULL),
('2016-01-19 14:54:13', 'club_name3', 'event_name43', 'postbody43', '2016-07-13', '07:43:43', 'event_venue43', 'image_link43', NULL, NULL),
('2016-01-19 14:54:15', 'club_name4', 'event_name44', 'postbody44', '2016-08-14', '08:44:44', 'event_venue44', 'image_link44', NULL, NULL),
('2016-01-19 14:54:17', 'club_name5', 'event_name45', 'postbody45', '2016-09-15', '09:45:45', 'event_venue45', 'image_link45', NULL, NULL),
('2016-01-19 14:54:19', 'club_name6', 'event_name46', 'postbody46', '2016-10-16', '10:46:46', 'event_venue46', 'image_link46', NULL, NULL),
('2016-01-19 14:54:21', 'club_name7', 'event_name47', 'postbody47', '2016-11-17', '11:47:47', 'event_venue47', 'image_link47', NULL, NULL),
('2016-01-19 14:54:25', 'club_name9', 'event_name49', 'postbody49', '2016-01-19', '01:49:49', 'event_venue49', 'image_link49', NULL, NULL),
('2016-01-23 17:03:00', 'club_name3', 'some event', 'long post body', '2016-01-28', '06:15:35', 'sjt 501', 'http://i.imgur.com/9C2YX7r.jpg', 'piyush rungta', '2147483647'),
('2016-01-23 17:15:40', 'club_name3', 'some event', 'long post body', '2016-01-28', '06:15:35', 'sjt 501', 'http://i.imgur.com/9C2YX7r.jpg', 'piyush rungta', '9090909090'),
('2016-01-23 17:17:27', 'club_name0', 'name', 'aaaaaa ss', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212'),
('2016-01-23 17:18:22', 'club_name0', 'name', 'qqqqqqqqqqqaaaasdf', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212'),
('2016-01-23 17:18:54', 'club_name0', 'name', 'asdfgh', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212'),
('2016-01-23 17:33:25', 'club_name0', 'name', 'asdf', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212'),
('2016-01-23 17:34:14', 'club_name0', 'name', 'asdf', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212'),
('2016-01-23 17:36:00', 'club_name0', 'name', 'k', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212'),
('2016-01-23 17:36:19', 'club_name3', 'some event', 'long post body', '2016-01-28', '06:15:35', 'sjt 501', 'http://i.imgur.com/9C2YX7r.jpg', 'piyush rungta', '9090909090'),
('2016-01-23 17:38:26', 'club_name69', 'name', 'qq', '2016-01-30', '12:59:59', 'tt 001', 'http://i.imgur.com/9C2YX7r.jpg', 'someone', '1212121212');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
