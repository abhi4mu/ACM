-- CREATE DATABASE ACM;
USE ACM;

CREATE TABLE STUDENT_MEMBERS(SNO INT,ROLL_NUM VARCHAR(20), STUDENT_NAME VARCHAR(50), IMAGE varchar(30), GENDER CHAR, LINK varchar(500), primary key (SNO,ROLL_NUM));
create table STUDENT_YEARS(STUDENT_SNO INT, START_YEAR DATE, END_YEAR DATE, TITLE VARCHAR(30), CLUB VARCHAR(50));
ALTER TABLE STUDENT_YEARS ADD foreign key (STUDENT_SNO) REFERENCES STUDENT_MEMBERS(SNO); 

CREATE TABLE FACULTY_MEMBERS(SNO INT, ID VARCHAR(20), FACULTY_NAME VARCHAR(30), IMAGE varchar(30), GENDER CHAR, LINK varchar(500), primary key (SNO,ID));
create table FACULTY_YEARS(FACULTY_SNO INT, START_YEAR DATE, END_YEAR DATE, TITLE VARCHAR(30));
ALTER TABLE FACULTY_YEARS ADD foreign key (FACULTY_SNO) REFERENCES FACULTY_MEMBERS(SNO); 

CREATE TABLE EVENT_NAMES (EVENT_ID INT, EVENT_NAME VARCHAR(100), START_DATE DATE, END_DATE DATE, primary key(EVENT_ID));
CREATE TABLE EVENT_DESC (EVENT_ID INT, SPEAKER VARCHAR(50), ABOUT_SPEAKER VARCHAR(1000), ORGANIZED_BY VARCHAR(1000),ABOUT_EVENT varchar(2000));
ALTER TABLE EVENT_DESC ADD foreign KEY(EVENT_ID) REFERENCES EVENT_NAMES(EVENT_ID);
CREATE TABLE EVENT_IMAGES(EVENT_ID INT, IMAGE_ID VARCHAR(30));
ALTER TABLE EVENT_IMAGES ADD foreign key(EVENT_ID) references EVENT_NAMES(EVENT_ID);

CREATE TABLE TECH_NEWS(HEADING VARCHAR(1000), LINK VARCHAR(500));
CREATE TABLE CAREER_NEWS(HEADING VARCHAR(1000), LINK VARCHAR(500));
