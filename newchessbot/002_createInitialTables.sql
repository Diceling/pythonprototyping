drop table if exists boardStates;
drop table if exists connections;
drop table if exists games;
drop table if exists log;

create table boardStates (
  id int NOT NULL auto_increment,
  fen varchar(100) NOT NULL,
  white int NOT NULL default 0,
  black int NOT NULL default 0,
  ties int NOT NULL default 0,
  recursiveWhite int NOT NULL default 0,
  recursiveBlack int NOT NULL default 0,
  recursiveTies int NOT NULL default 0,
  endingMove tinyint NOT NULL default 0,
  PRIMARY KEY (id,fen)
);

create table connections (
  source int NOT NULL,
  destination int NOT NULL,
  PRIMARY KEY (source, destination)
);

create table games (
  id int NOT NULL auto_increment,
  hash varchar(10000),
  PRIMARY KEY (id)
);

create table log (
  id int NOT NULL auto_increment,
  created_at timestamp NOT NULL default NOW(),
  filename varchar(1000) default "Random",
  gamesRun int,
  newConnections int,
  totalConnections int,
  newBoardStates int,
  totalBoardStates int,
  PRIMARY KEY (id)
);
