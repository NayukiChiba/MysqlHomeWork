/*
 Navicat Premium Data Transfer

 Source Server         : mysql80
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 22/03/2022 22:46:45
*/
drop database if exists test;
create database if not exists test;
use test;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `id` char(4) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `name` varchar(20) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES ('101', '数学学院');
INSERT INTO `department` VALUES ('102', '计算机学院');
INSERT INTO `department` VALUES ('103', '外语学院');
INSERT INTO `department` VALUES ('104', '物理学院');
INSERT INTO `department` VALUES ('105', '电气学院');
INSERT INTO `department` VALUES ('106', '马克思主义学院');
INSERT INTO `department` VALUES ('107', '哲学院');

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `level`;
CREATE TABLE `level`  (
  `grade` char(2) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL DEFAULT '',
  `lowScore` int(0) NULL DEFAULT NULL,
  `highScore` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`grade`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of level
-- ----------------------------
INSERT INTO `level` VALUES ('A', 90, 100);
INSERT INTO `level` VALUES ('B', 80, 89);
INSERT INTO `level` VALUES ('C', 70, 79);
INSERT INTO `level` VALUES ('D', 60, 69);
INSERT INTO `level` VALUES ('E', 0, 59);

-- ----------------------------
-- Table structure for lesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson`;
CREATE TABLE `lesson`  (
  `lessonid` int(0) NOT NULL,
  `lessonName` varchar(20) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `score` int(0) NULL DEFAULT NULL,
  `deparmentId` char(5) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  INDEX `lessonid`(`lessonid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson
-- ----------------------------
INSERT INTO `lesson` VALUES (101, '数学', 4, '101');
INSERT INTO `lesson` VALUES (102, '英语', 6, '102');
INSERT INTO `lesson` VALUES (103, '计算机', 3, '103');
INSERT INTO `lesson` VALUES (104, '物理', 3, '104');
INSERT INTO `lesson` VALUES (105, '政治', 3, '106');
INSERT INTO `lesson` VALUES (106, '法语', 2, '102');

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `Id` int(0) NOT NULL AUTO_INCREMENT,
  `stuId` char(13) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `LessonId` int(0) NOT NULL,
  `grade` int(0) NULL DEFAULT 0,
  PRIMARY KEY (`Id`) USING BTREE,
  INDEX `课程`(`LessonId`) USING BTREE,
  INDEX `fk-stu`(`stuId`) USING BTREE,
  CONSTRAINT `fk-stu` FOREIGN KEY (`stuId`) REFERENCES `stu` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `课程` FOREIGN KEY (`LessonId`) REFERENCES `lesson` (`lessonid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES (1, '20201001', 103, 99);
INSERT INTO `score` VALUES (2, '20201002', 101, 77);
INSERT INTO `score` VALUES (3, '20201001', 101, 65);
INSERT INTO `score` VALUES (4, '20201003', 101, 88);
INSERT INTO `score` VALUES (5, '20201002', 102, 98);
INSERT INTO `score` VALUES (6, '20211001', 103, 91);
INSERT INTO `score` VALUES (7, '20191002', 102, 82);
INSERT INTO `score` VALUES (8, '20191002', 101, 63);
INSERT INTO `score` VALUES (9, '20201003', 103, 71);
INSERT INTO `score` VALUES (10, '20201001', 104, 72);
INSERT INTO `score` VALUES (11, '20201003', 104, 94);
INSERT INTO `score` VALUES (12, '20201003', 102, 77);
INSERT INTO `score` VALUES (13, '20201004', 103, 82);
INSERT INTO `score` VALUES (14, '20211001', 104, 78);
INSERT INTO `score` VALUES (15, '20191003', 104, 74);
INSERT INTO `score` VALUES (16, '20211002', 102, 87);
INSERT INTO `score` VALUES (17, '20211001', 101, 51);
INSERT INTO `score` VALUES (18, '20201004', 101, 86);
INSERT INTO `score` VALUES (19, '20201001', 102, 84);
INSERT INTO `score` VALUES (20, '20201002', 103, 94);
INSERT INTO `score` VALUES (21, '20201002', 104, 48);
INSERT INTO `score` VALUES (29, '20191001', 101, 85);
INSERT INTO `score` VALUES (30, '20211002', 104, 82);
INSERT INTO `score` VALUES (31, '20191001', 103, 90);
INSERT INTO `score` VALUES (34, '20191004', 101, 68);
INSERT INTO `score` VALUES (35, '20211003', 102, 80);
INSERT INTO `score` VALUES (36, '20191004', 103, 83);
INSERT INTO `score` VALUES (37, '20191004', 105, 91);
INSERT INTO `score` VALUES (38, '20211002', 105, 84);
INSERT INTO `score` VALUES (39, '20211001', 105, 70);
INSERT INTO `score` VALUES (40, '20211002', 103, 88);

-- ----------------------------
-- Table structure for stu
-- ----------------------------
DROP TABLE IF EXISTS `stu`;
CREATE TABLE `stu`  (
  `id` char(13) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `name` char(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `sex` enum('男','女') CHARACTER SET gbk COLLATE gbk_bin NULL DEFAULT '男',
  `departmentId` char(5) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL DEFAULT '',
  `birthday` date NULL DEFAULT NULL,
  `address` json NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu
-- ----------------------------
INSERT INTO `stu` VALUES ('20191001', '许和雅', '女', '102', '2001-01-12', '{\"$.tel\": \"189776356\", \"$.name\": \"John\", \"$.address\": \"Beijing\"}');
INSERT INTO `stu` VALUES ('20191002', '冯红云', '女', '103', '2001-05-10', '{\"tel\": \"139862356\", \"name\": \"Alice\", \"address\": \"ShangHai\"}');
INSERT INTO `stu` VALUES ('20191003', '冯海', '男', '103', NULL, NULL);
INSERT INTO `stu` VALUES ('20191004', '刘一凡', '男', '105', NULL, NULL);
INSERT INTO `stu` VALUES ('20201001', '张三', '男', '101', NULL, NULL);
INSERT INTO `stu` VALUES ('20201002', '李四', '男', '102', NULL, NULL);
INSERT INTO `stu` VALUES ('20201003', '王五', '女', '103', NULL, NULL);
INSERT INTO `stu` VALUES ('20201004', '赵六', '女', '101', NULL, NULL);
INSERT INTO `stu` VALUES ('20201005', 'abc', '男', '103', NULL, '{\"tel\": \"189776123\", \"name\": \"abc\", \"address\": \"Wuhan\"}');
INSERT INTO `stu` VALUES ('20211001', '韦俊豪', '男', '101', NULL, NULL);
INSERT INTO `stu` VALUES ('20211002', '雷淳雅', '女', '101', NULL, NULL);
INSERT INTO `stu` VALUES ('20211003', '李磊', '男', '104', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
