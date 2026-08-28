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

 Date: 29/08/2026 04:32:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for enrollment
-- ----------------------------
DROP TABLE IF EXISTS `enrollment`;
CREATE TABLE `enrollment`  (
  `student_code` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学号',
  `subject_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '课程编号',
  `enrollment_date` date NULL DEFAULT NULL COMMENT '选课日期',
  `enrollment_time` time NULL DEFAULT NULL COMMENT '选课时间',
  `credit_card_no` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '信用卡号（CC#）',
  PRIMARY KEY (`student_code`, `subject_code`) USING BTREE,
  INDEX `subject_code`(`subject_code`) USING BTREE,
  CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`student_code`) REFERENCES `student` (`student_code`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`subject_code`) REFERENCES `subject` (`subject_code`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '选课记录（关联学生与课程）' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
