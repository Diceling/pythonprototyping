drop table if exists fiefdom;
drop table if exists estate;
drop table if exists village;
drop table if exists npc;
drop table if exists home_type;

create table fiefdom (
  id int NOT NULL auto_increment,
  name varchar(100),
  farming int default 1,
  livestock int default 1,
  forest int default 1,
  hunting int default 1,
  fishing int default 0,
  assets_base int default 0,
  assets_luxury int default 0,
  assets_money float default 0,
  noble_rank int default 1,
  forest_land int default 0,
  boats int default 0,
  PRIMARY KEY (id)
);

create table estate (
  id int NOT NULL auto_increment,
  fiefdom_id int NOT NULL,
  name varchar(100),
  estate_land int,
  PRIMARY KEY (id)
  );

create table village (
  id int NOT NULL auto_increment,
  estate_id int NOT NULL,
  name VARCHAR(100),
  free_villagers int,
  indentured_villagers int,
  PRIMARY KEY (id)
  );

create table npc (
  id int NOT NULL auto_increment,
  belongs_to int NOT NULL,
  home_type int NOT NULL,
  cost_base int,
  cost_luxury int,
  cost_silver int,
  income_base int,
  income_luxury int,
  income_silver int,
  PRIMARY KEY(id, home_type)
  );

create table home_type (
  id int,
  name varchar(50)
  );

insert into home_type(name)
  values
    ("village"),
    ("estate"),
    ("fief");
