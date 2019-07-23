drop table if exists income_plan;
drop table if exists plan_day_labour;
drop table if exists epense_plan;
drop table if exists plan_npc;

create table income_plan (
  year int NOT NULL,
  fief_id int NOT NULL,
  farm_land int,
  livestock_land int,
  day_labours int,
  hired_help int,

  PRIMARY KEY(year, fief_id)
  );

create table plan_day_labour (
  id int NOT NULL auto_increment,
  income_plan_id int NOT NULL,
  estate_land int,
  logging int,
  land_breaking int,
  fishing int,
  PRIMARY KEY (id)
  );

create table expense_plan (
  id int NOT NULL auto_increment,
  year int NOT NULL,
  fief_id int NOT NULL,
  day_labours int,
  hired_help int,
  boats int,
  living int,
  PRIMARY KEY (id)
  );

create table plan_npc (
  id int NOT NULL auto_increment,
  year int NOT NULL,
  fief_id int NOT NULL,
  npc_id int NOT NULL,
  PRIMARY KEY (id)
  );
