CREATE DATABASE IF NOT EXISTS project1;
USE project1;

DROP TABLE IF EXISTS Tasks;

CREATE TABLE IF NOT EXISTS Tasks(
  taskID INT PRIMARY KEY AUTO_INCREMENT,
  taskName VARCHAR(100) NOT NULL,
  categoryID INT,
  category VARCHAR(25),
  dueDate DATE,
  completionStatus BOOLEAN
);



INSERT INTO Tasks(taskID, taskName, categoryID, category, dueDate, completionStatus) VALUES
(1, "Buy groceries", 3, "Household", "2026-12-12", TRUE);

