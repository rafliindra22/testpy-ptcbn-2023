/*
 Navicat Premium Data Transfer

 Source Server         : localhost_postgre
 Source Server Type    : PostgreSQL
 Source Server Version : 130005
 Source Host           : localhost:5432
 Source Catalog        : hcc_new
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 130005
 File Encoding         : 65001

 Date: 27/12/2022 20:52:19
*/


-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "public"."users";
CREATE TABLE "public"."users" (
  "user_id" int8 NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
  "username" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "is_active" bool NOT NULL DEFAULT true,
  "created_by" varchar(100) COLLATE "pg_catalog"."default",
  "created_time" timestamp(6) DEFAULT now()
)
;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO "public"."users" VALUES (2, '99889988', 'usertest456', 't', '1', '2022-12-27 20:45:24');
INSERT INTO "public"."users" VALUES (1, '88998899', 'usertest123', 't', '1', '2022-12-27 20:45:24');

-- ----------------------------
-- Primary Key structure for table users
-- ----------------------------
ALTER TABLE "public"."users" ADD CONSTRAINT "users_pk" PRIMARY KEY ("user_id");
