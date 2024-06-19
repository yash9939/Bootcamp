# Normalization

# Using a Database for Normalization
USE testdb;

# First Normal Form (1NF)
# A table is in 1NF if it contains only atomic (indivisible) values and each column contains values of a single type.

# | StudentID | StudentName | Courses                  |
# |-----------|-------------|--------------------------|
# | 1         | Bruce Wayne | Math, Science            |
# | 2         | Clark Kent  | English, History, Science|

# The above table is not in INF

#Query for 1NF
CREATE TABLE Students_1NF (
StudentID INT(10) PRIMARY KEY,
StudentName VARCHAR(100),
Course VARCHAR(100)
);

INSERT INTO Students_1NF (StudentID, StudentName, Course) VALUES
(1, 'Bruce Wayne', 'Math'),
(1, 'Bruce Wayne', 'Science'),
(2, 'Clark Kent', 'English'),
(2, 'Clark Kent', 'History'),
(2, 'Clark Kent', 'Science');

# Second Normal Form(2NF)
# A table is in 2NF if it is in 1NF and all non-key attributes are fully functionally dependent on the primary key. This usually involves removing partial dependencies.

# | StudentID | StudentName | Course  |
# |-----------|-------------|---------|
# | 1         | John Doe    | Math    |
# | 1         | John Doe    | Science |
# | 2         | Jane Smith  | English |
# | 2         | Jane Smith  | History |
# | 2         | Jane Smith  | Science |
# The above table of students 1NF has partial dependencies

CREATE TABLE Students_2NF (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100)
);

CREATE TABLE Courses_2NF (
    StudentID INT,
    Course VARCHAR(100),
    PRIMARY KEY (StudentID, Course),
    FOREIGN KEY (StudentID) REFERENCES Students_2NF(StudentID)
);

INSERT INTO Students_2NF (StudentID, StudentName) VALUES
(1, 'Bruce Wayne'),
(2, 'Clark Kent');

INSERT INTO Courses_2NF (StudentID, Course) VALUES
(1, 'Math'),
(1, 'Science'),
(2, 'English'),
(2, 'History'),
(2, 'Science');

# Third Normal Form (3NF)
# A table is in 3NF if it is in 2NF and all the attributes are functionally dependent only on the primary key.

# | Course   | Instructor    |
# |----------|---------------|
# | Math     | Mr. Smith     |
# | Science  | Dr. Johnson   |
# | English  | Mrs. Brown    |
# | History  | Mr. White     |
# Consider the Courses_2NF table. Suppose each course has a specific instructor.

CREATE TABLE Instructors_3NF (
    Course VARCHAR(100) PRIMARY KEY,
    Instructor VARCHAR(100)
);

INSERT INTO Instructors_3NF (Course, Instructor) VALUES
('Math', 'Mr. Smith'),
('Science', 'Dr. Johnson'),
('English', 'Mrs. Brown'),
('History', 'Mr. White');

CREATE TABLE Courses_3NF (
    StudentID INT,
    Course VARCHAR(100),
    PRIMARY KEY (StudentID, Course),
    FOREIGN KEY (StudentID) REFERENCES Students_2NF(StudentID),
    FOREIGN KEY (Course) REFERENCES Instructors_3NF(Course)
);

INSERT INTO Courses_3NF (StudentID, Course) VALUES
(1, 'Math'),
(1, 'Science'),
(2, 'English'),
(2, 'History'),
(2, 'Science');