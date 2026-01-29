CREATE DATABASE IF NOT EXISTS project1;
USE project1;


CREATE TABLE IF NOT EXISTS Tasks(
  taskID INT PRIMARY KEY AUTO_INCREMENT,
  taskName VARCHAR(100) NOT NULL
  categoryID INT
  category VARCHAR(25)
  dueDate DATE 
  completionStatus BOOLEAN
);


INSERT INTO Tasks(taskName) VALUES
('Buy groceries'),
('Clean house');

SELECT *
FROM Tasks;