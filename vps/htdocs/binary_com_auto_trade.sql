-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th12 04, 2019 lúc 10:12 AM
-- Phiên bản máy phục vụ: 10.1.38-MariaDB
-- Phiên bản PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `binary com auto trade`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `idicator5m`
--

CREATE TABLE `idicator5m` (
  `id` int(11) NOT NULL,
  `timestamp_start` int(11) NOT NULL,
  `open` text NOT NULL,
  `close` text NOT NULL,
  `min` text NOT NULL,
  `max` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Đang đổ dữ liệu cho bảng `idicator5m`
--

INSERT INTO `idicator5m` (`id`, `timestamp_start`, `open`, `close`, `min`, `max`) VALUES
(1, 1575447441, '1', '2', '3', '4'),
(2, 1575447442, '5', '6', '7', '8'),
(3, 1575447444, '10', '11', '12', '13'),
(4, 1575450600, '0', '1.10804', '1.10797', '1.10814'),
(5, 1575450660, '1.10804', '1.1078', '1.1078', '1.10813'),
(6, 1575450720, '1.1078', '1.10762', '1.10752', '1.10781');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `idicator5m`
--
ALTER TABLE `idicator5m`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `idicator5m`
--
ALTER TABLE `idicator5m`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
