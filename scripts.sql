CREATE TABLE DEPARTMENT (
  Department_Id varchar(15) NOT NULL,
  name varchar(15) DEFAULT NULL,
  location varchar(20) DEFAULT NULL,
  date_of_innaugration date DEFAULT NULL,
  PRIMARY KEY (Department_Id)
);

INSERT INTO DEPARTMENT VALUES (1,'Product', 'Bengaluru', '2019-07-1'),(2,'Engineering', 'Redwood City', '2019-07-1'),(3,'Marketing', 'New York', '2019-07-1');

CREATE TABLE TEAMS (
  Team_Id varchar(15) NOT NULL,
  Team_lead_id varchar(15) DEFAULT NULL,
  Department_id varchar(15) DEFAULT NULL,
  average_pay varchar(10) DEFAULT NULL,
  PRIMARY KEY (Team_Id),
  CONSTRAINT Department_id FOREIGN KEY (Department_id) REFERENCES DEPARTMENT (Department_Id)
);

INSERT INTO TEAMS VALUES (1,'1',1, '20000'),(2,'328',2, '30000'),(3,'487',1, '40000');

CREATE TABLE USERS (
  User_id varchar(12) NOT NULL,
  First_Name varchar(25) DEFAULT NULL,
  Last_Name varchar(25) DEFAULT NULL,
  Team_id varchar(12) DEFAULT NULL,
  PRIMARY KEY (User_id),
  CONSTRAINT Team_id FOREIGN KEY (Team_id) REFERENCES TEAMS (Team_Id)
);

INSERT INTO USERS VALUES (1,'Navneet','Menon', 1),(2,'Kailash','Raghav',2),(3,'Johnson','Stevenson', 1);

CREATE TABLE OBJECTIVES (
  Objective_Id varchar(12) DEFAULT NULL,
  User_id varchar(12) NOT NULL,
  Objective_text varchar(100) DEFAULT NULL,
  PRIMARY KEY (Objective_Id),
  CONSTRAINT User_id FOREIGN KEY (User_id) REFERENCES USERS (User_id)
);

INSERT INTO OBJECTIVES VALUES (1,1, 'Improve HR Processes'),(2,2, 'Raise participation in Surveys'),(3,2, 'Improve Engineering Processes');

CREATE TABLE KEYRESULTS (
  Keyresult_id varchar(12) NOT NULL,
  Objective_Id varchar(12) DEFAULT NULL,
  Status varchar(12) DEFAULT NULL,
  Due_date date DEFAULT NULL,
  PRIMARY KEY (Keyresult_id),
  CONSTRAINT Objective_Id FOREIGN KEY (Objective_Id) REFERENCES OBJECTIVES (Objective_Id)
);

INSERT INTO KEYRESULTS VALUES (1,1,'Pending', '2020-07-1'),(2,1,'Complete', '2020-07-1'),(3,1,'Complete', '2020-07-1');
INSERT INTO KEYRESULTS VALUES (4,2,'Complete', '2020-07-1'),(5,2,'Complete', '2020-07-1'),(6,2,'Complete', '2020-07-1');