/*
 Navicat Premium Data Transfer

 Source Server         : mysqllocal
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : dbtest

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 27/03/2023 10:08:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for starsT
-- ----------------------------
DROP TABLE IF EXISTS `starsT`;
CREATE TABLE `starsT`  (
  `ra` decimal(10, 0) NULL DEFAULT NULL,
  `decd` decimal(10, 0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of starsT
-- ----------------------------
INSERT INTO `starsT` VALUES (10, 10);

SET FOREIGN_KEY_CHECKS = 1;
