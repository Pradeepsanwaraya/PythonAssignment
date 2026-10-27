# 1.
# Create a table named Students with the following columns:

# StudentID (INT, Primary Key)
# Name (VARCHAR(50), NOT NULL)
# Age (INT, should be between 18 and 25)
# Marks (DECIMAL(5,2), should be between 0 and 100)
# Insert the following records and observe what happens:

# CREATE TABLE students (
#     studentid INT PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     age INT CHECK (age BETWEEN 18 AND 25),
#     marks DECIMAL(5,2) CHECK (marks BETWEEN 0 AND 100)
# );
# (101, 'Alice', 20, 85.5)
# INSERT INTO students
# VALUES (101, 'Alice', 20, 85.5);

# (102, 'Bob', 17, 90.0) (This should fail due to Age constraint)
# INSERT INTO students
# VALUES (102, 'Bob', 17, 90.5); 
#  mysql> INSERT INTO students
#     -> VALUES (102, 'Bob', 17, 90.5);
# ERROR 3819 (HY000): Check constraint 'students_chk_1' is violated.
# mysql>

# (103, 'Charlie', 22, 105.0) (This should fail due to Marks constraint)
# INSERT INTO students
# VALUES (103, 'Charli',22, 105.0);

# (104, 'David', 24, 75.0)
# INSERT INTO students
# VALUES (103, 'David',24, 75.0);


# 2.

# Create a table Patients with:

# PatientID (INT, Primary Key)
# PatientName (VARCHAR(50), NOT NULL)
# Age (INT, should be between 1 and 100)
# AdmissionStatus VARCHAR(15), should be 'Admitted' or 'Discharged', DEFAULT 'Admitted')
# TreatmentCost (DECIMAL(10,2), should be at least 1000)
	
# Insert records and check constraints:

# (201, 'Michael', 25, 'Admitted', 5000)
# INSERT INTO patients
# VALUES (201, 'Michael', 25, 'Admitted', 5000);


# (202, 'Linda', 105, 'Admitted', 8000) (Should fail due to Age constraint)
# INSERT INTO patients
# VALUES (202, 'Linda', 105, 'Admitted', 8000);


# (203, 'David', 40, DEFAULT, 1200) (Should insert 'Admitted' as default)
# INSERT INTO patients(patientid ,patientname, age  ,treatmentcost )
# VALUES (203, 'David', 40, 1200);


# (204, 'Sarah', 30, 'Discharged', 700) (Should fail due to TreatmentCost constraint)
# INSERT INTO patients
# VALUES (204, 'Sarah', 30, 'Discharged', 700);


# 3.
# Create a table GymMembers with:

# MemberID (INT, Primary Key)
# MemberName (VARCHAR(50), NOT NULL)
# MembershipType (VARCHAR(15), should be 'Basic', 'Premium', or 'VIP', DEFAULT 'Basic')
# MonthlyFee (DECIMAL(6,2), should be at least 500)


# CREATE TABLE GymMembers (
#     MemberID INT PRIMARY KEY,
#     MemberName VARCHAR(50) NOT NULL,
#     MembershipType VARCHAR(15)
#         CHECK (MembershipType IN ('Basic', 'Premium', 'VIP'))
#         DEFAULT 'Basic',
#     MonthlyFee DECIMAL(6,2)
#         CHECK (MonthlyFee >= 500)
# );


# Insert records and check constraints:

# (501, 'John', 'Premium', 1200)
# insert into GymMembers values(501, 'John', 'Premium', 1200);


# (502, 'Emma', 'Gold', 800) (Should fail due to MembershipType constraint)
# insert into GymMembers values(502, 'Emma', 'Gold', 800);


# (503, 'Daniel', DEFAULT, 700) (Should insert 'Basic' as default)
# insert into GymMembers(MemberID , MemberName  ,MonthlyFee   ) values(503, 'Daniel', 700);


# (504, 'Sophia', 'VIP', 300) (Should fail due to MonthlyFee constraint)

# insert into GymMembers values(504, 'Sophia', 'VIP', 300);