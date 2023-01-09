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

 Date: 27/12/2022 20:52:27
*/


-- ----------------------------
-- Table structure for m_master
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_master";
CREATE TABLE "public"."m_master" (
  "master_id" int8 NOT NULL DEFAULT nextval('m_master_master_id_seq'::regclass),
  "code" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default",
  "is_active" bool NOT NULL DEFAULT true,
  "created_by" int8 NOT NULL,
  "created_time" timestamp(6) NOT NULL,
  "updated_by" int8,
  "updated_time" timestamp(6),
  "deleted_by" int8,
  "deleted_time" timestamp(6)
)
;

-- ----------------------------
-- Records of m_master
-- ----------------------------
INSERT INTO "public"."m_master" VALUES (1, '01', 'NOMOR HP', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (2, '02', 'TELP RUMAH', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (3, '03', 'EMAIL', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (4, '04', 'FACEBOOK', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (5, '05', 'INSTAGRAM', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (6, '06', 'FAX', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (7, '07', 'TWITTER', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_master" VALUES (8, '08', 'TIKTOK', NULL, 't', 1, '2022-12-27 20:51:24', NULL, NULL, NULL, NULL);

-- ----------------------------
-- Indexes structure for table m_master
-- ----------------------------
CREATE INDEX "idx_master_code" ON "public"."m_master" USING btree (
  "code" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "idx_master_description" ON "public"."m_master" USING btree (
  "description" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "idx_master_id" ON "public"."m_master" USING btree (
  "master_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "idx_master_is_active" ON "public"."m_master" USING btree (
  "is_active" "pg_catalog"."bool_ops" ASC NULLS LAST
);
CREATE INDEX "idx_master_name" ON "public"."m_master" USING btree (
  "name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table m_master
-- ----------------------------
ALTER TABLE "public"."m_master" ADD CONSTRAINT "m_master_pkey" PRIMARY KEY ("master_id");
