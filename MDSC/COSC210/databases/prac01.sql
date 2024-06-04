CREATE TABLE employee (
  fname    varchar(15) NOT NULL, 
  minit    varchar(1),
  lname    varchar(15) NOT NULL,
  ssn      char(9) PRIMARY KEY,
  bdate    date,
  address  varchar(50),
  sex      char,
  salary   decimal(10,2),
  superssn char(9),
  dno      integer,
  foreign key (superssn) references employee(ssn)
        ON DELETE SET NULL ON UPDATE CASCADE,
  foreign key (dno) references department(dnumber)
        ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE department (
  dname        varchar(50) not null,
  dnumber      integer primary key,
  mgrssn       char(9) not null, 
  mgrstartdate date
);


CREATE TABLE project (
  pname      varchar(25) unique not null,
  pnumber    integer primary key,
  plocation  varchar(15),
  dnum       integer not null,
  foreign key (dnum) references department(dnumber)
);

CREATE TABLE employee (
  fname    varchar(15) NOT NULL, 
  minit    varchar(1),
  lname    varchar(15) NOT NULL,
  ssn      char(9) PRIMARY KEY,
  bdate    date,
  address  varchar(50),
  sex      char,
  salary   decimal(10,2),
  superssn char(9),
  dno      integer,
  foreign key (superssn) references employee(ssn)
        ON DELETE SET NULL ON UPDATE CASCADE,
  foreign key (dno) references department(dnumber)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE dependent (
  essn           char(9),
  dependent_name varchar(15),
  sex            char,
  bdate          date,
  relationship   varchar(8),
  primary key (essn,dependent_name),
  foreign key (essn) references employee(ssn)
);

CREATE TABLE dept_locations (
  dnumber   integer,
  dlocation varchar(15), 
  primary key (dnumber,dlocation),
  foreign key (dnumber) references department(dnumber)
);

    CREATE TABLE works_on (
    essn   char(9),
    pno    integer,
    hours  decimal(4,1),
    primary key (essn,pno),
    foreign key (essn) references employee(ssn),
    foreign key (pno) references project(pnumber)
    );