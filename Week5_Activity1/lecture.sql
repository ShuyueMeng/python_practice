/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100424
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 100424
 File Encoding         : 65001

 Date: 29/08/2026 04:33:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for lecture
-- ----------------------------
DROP TABLE IF EXISTS `lecture`;
CREATE TABLE `lecture`  (
  `lecture_id` int NOT NULL AUTO_INCREMENT COMMENT '讲座ID',
  `lecture_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '讲座名称',
  `subject_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '所属课程编号',
  `lecturer_id` int NOT NULL COMMENT '授课讲师ID',
  `lecture_date` date NULL DEFAULT NULL COMMENT '上课日期（原Date）',
  `lecture_time` time NULL DEFAULT NULL COMMENT '上课时间（原Time）',
  PRIMARY KEY (`lecture_id`) USING BTREE,
  INDEX `subject_code`(`subject_code`) USING BTREE,
  INDEX `lecturer_id`(`lecturer_id`) USING BTREE,
  CONSTRAINT `lecture_ibfk_1` FOREIGN KEY (`subject_code`) REFERENCES `subject` (`subject_code`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `lecture_ibfk_2` FOREIGN KEY (`lecturer_id`) REFERENCES `lecturer` (`lecturer_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '讲座安排' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
