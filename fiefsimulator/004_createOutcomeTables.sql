drop table if exists actual_income;
drop table if exists actual_expenses;

create table actual_income (
  id int NOT NULL auto_increment,
  year int NOT NULL,
  fief_id int NOT NULL,
  estate_land int,
  hunting int,
  fishing int,
  logging int,
  taxes int,
  avrad int,
  toll int,
  PRIMARY KEY (id)
  );

create table actual_expenses (
  id int NOT NULL auto_increment,
  year int NOT NULL,
  fief_id int NOT NULL,
  day_labours int,
  hired_help int,
  boats int,
  living int,
  staff_base int,
  staff_luxury int,
  PRIMARY KEY (id)
  );
