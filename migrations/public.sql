/*
 Navicat Premium Data Transfer

 Source Server         : my_12
 Source Server Type    : PostgreSQL
 Source Server Version : 120005
 Source Host           : 194.99.21.140:5433
 Source Catalog        : Emcd
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 120005
 File Encoding         : 65001

 Date: 19/02/2021 20:50:06
*/

-- ----------------------------
-- Table structure for account
-- ----------------------------

DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int8 NOT NULL,
  "lang_id" int4 NOT NULL,
  "created_datetime" timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP
);
