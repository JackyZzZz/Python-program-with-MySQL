# cs122a_db.sql

DROP DATABASE IF EXISTS cs122a;
CREATE DATABASE cs122a;
USE cs122a;

-- User Table
CREATE TABLE users (
    UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50),
    MiddleName VARCHAR(50),
    LastName VARCHAR(50)
);

-- User Email Table
CREATE TABLE emails (
    UCINetID VARCHAR(20) NOT NULL,
    Email VARCHAR(100),
    PRIMARY KEY (UCINetID, Email),
    FOREIGN KEY (UCINetID) REFERENCES users (UCINetID)
        ON DELETE CASCADE
);

-- Student Delta Table
CREATE TABLE students (
    UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UCINetID) REFERENCES users(UCINetID)
        ON DELETE CASCADE
);

-- Administrator Delta Table
CREATE TABLE admins (
    UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UCINetID) REFERENCES users(UCINetID)
      ON DELETE CASCADE
);

-- Course Table
CREATE TABLE courses (
    CourseID INT PRIMARY KEY NOT NULL,
    Title VARCHAR(100),
    Quarter VARCHAR(20)
);

-- Project Table
CREATE TABLE projects (
    ProjectID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100),
    Description TEXT,
    CourseID INT NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID)
);

-- Machine Table
CREATE TABLE machines (
    MachineID INT PRIMARY KEY NOT NULL,
    Hostname VARCHAR(255),
    IPAddress VARCHAR(15),
    OperationalStatus VARCHAR(50),
    Location VARCHAR(255)
);


-- Use Relationship Table
CREATE TABLE StudentUseMachinesInProject (
    ProjectID INT,
    StudentUCINetID VARCHAR(20),
    MachineID INT,
    StartDate DATE,
    EndDate DATE,
    PRIMARY KEY (ProjectID, StudentUCINetID, MachineID),
    FOREIGN KEY (ProjectID) REFERENCES projects(ProjectID),
    FOREIGN KEY (StudentUCINetID) REFERENCES students(UCINetID),
    FOREIGN KEY (MachineID) REFERENCES machines(MachineID)
);



-- Administrator Machine Management Table
CREATE TABLE manage (
    AdministratorUCINetID VARCHAR(20),
    MachineID INT,
    PRIMARY KEY (AdministratorUCINetID, MachineID),
    FOREIGN KEY (AdministratorUCINetID) REFERENCES admins(UCINetID),
    FOREIGN KEY (MachineID) REFERENCES machines(MachineID)
);