-- DATABASE ENGINE: MySQL

CREATE SCHEMA IF NOT EXISTS JARI;

USE JARI;

DROP TABLE IF EXISTS User_project;
DROP TABLE IF EXISTS User_role;
DROP TABLE IF EXISTS Role_permission;
DROP TABLE IF EXISTS Required_task;
DROP TABLE IF EXISTS Task_subtask;
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Permission;

CREATE TABLE IF NOT EXISTS User
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Project
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  start_date DATE,
  delivery_date DATE,
  manager_id INT NOT NULL,
  status enum('paused', 'planned', 'in progress', 'delivered') NOT NULL DEFAULT 'paused',
  FOREIGN KEY (manager_id) REFERENCES User(id) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS Task
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  description TEXT,
  status enum('planned', 'in progress', 'completed', 'validated', 'paused') NOT NULL DEFAULT 'paused',
  start_date DATE,
  priotity INT,
  advancement INT NOT NULL,
  project_id INT NOT NULL,
  FOREIGN KEY (project_id) REFERENCES Project(id) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS rol
(
  name VARCHAR(100) NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Permission
(
  name VARCHAR(100) NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS User_project
(
  user_id INT NOT NULL,
  project_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id) ON UPDATE no action ON DELETE no action,
  FOREIGN KEY (project_id) REFERENCES project(id) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS User_role
(
  user_id INT NOT NULL,
  role_name VARCHAR(100) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User(id) ON UPDATE no action ON DELETE no action,
  FOREIGN KEY (role_name) REFERENCES Role(name) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS Role_permission
(
  role_name VARCHAR(100) NOT NULL,
  permission_name VARCHAR(100) NOT NULL,
  FOREIGN KEY (role_name) REFERENCES Role(name) ON UPDATE no action ON DELETE no action,
  FOREIGN KEY (permission_name) REFERENCES Permission(name) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS Required_task
(
  task_id INT NOT NULL,
  required_task_id INT NOT NULL,
  FOREIGN KEY (task_id) REFERENCES Task(id) ON UPDATE no action ON DELETE no action,
  FOREIGN KEY (required_task_id) REFERENCES Task(id) ON UPDATE no action ON DELETE no action
);

CREATE TABLE IF NOT EXISTS Task_subtask
(
  task_id INT NOT NULL,
  subtask_id INT NOT NULL,
  FOREIGN KEY (task_id) REFERENCES Task(id) ON UPDATE no action ON DELETE no action,
  FOREIGN KEY (subtask_id) REFERENCES Task(id) ON UPDATE no action ON DELETE no action
);
