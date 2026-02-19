CREATE DATABASE IF NOT EXISTS project1;
USE project1;

DROP TABLE IF EXISTS Tasks;

CREATE TABLE IF NOT EXISTS Tasks(
  taskID INT PRIMARY KEY AUTO_INCREMENT,
  taskName VARCHAR(100) NOT NULL,
  category VARCHAR(25),
  dueDate DATE,
  completionStatus BOOLEAN
);

-- INSERT INTO Tasks(taskID, taskName, category, dueDate, completionStatus) VALUES
-- (1, "Buy groceries", "Household", "2026-12-12", TRUE),
-- (2, "Do homework", "School", "2026-12-12", TRUE);