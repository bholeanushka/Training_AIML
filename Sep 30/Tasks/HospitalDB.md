# CREATING DATABASE HospitalDB
``` sql
CREATE DATABASE HospitalDB;
USE HospitalDB;
```
# CREATING TABLES
``` sql
-- PATIENTS TABLE
CREATE TABLE Patients (
patient_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
gender CHAR(1),
city VARCHAR(50)
);

-- DOCTORS TABLE
CREATE TABLE Doctors (
doctor_id INT PRIMARY KEY,
name VARCHAR(50),
specialization VARCHAR(50),
experience INT
);

-- APPOINTMENTS TABLE
CREATE TABLE Appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
status VARCHAR(20),
FOREIGN KEY(patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id)
);

-- MEDICAL RECORDS TABLE
CREATE TABLE MedicalRecords (
record_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
diagnosis VARCHAR(100),
treatment VARCHAR(100),
FOREIGN KEY(patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id)
);

-- BILLING TABLE
CREATE TABLE Billing (
bill_id INT PRIMARY KEY,
patient_id INT,
amount DECIMAL(10,2),
bill_date DATE,
status VARCHAR(20),
FOREIGN KEY(patient_id) REFERENCES Patients(patient_id)
);
```
``` sql

-- INSERTING VALUES
INSERT INTO Patients VALUES
(1, 'Amit Sharma', 30, 'M', 'Delhi'),
(2, 'Priya Verma', 25, 'F', 'Mumbai'),
(3, 'Rahul Singh', 40, 'M', 'Bangalore'),
(4, 'Sneha Iyer', 35, 'F', 'Chennai'),
(5, 'Vikram Patel', 28, 'M', 'Ahmedabad'),
(6, 'Neha Das', 32, 'F', 'Kolkata'),
(7, 'Ravi Kumar', 45, 'M', 'Hyderabad'),
(8, 'Anjali Mehta', 29, 'F', 'Pune'),
(9, 'Karan Joshi', 50, 'M', 'Jaipur'),
(10, 'Meera Nair', 38, 'F', 'Coimbatore');

INSERT INTO Doctors VALUES
(1, 'Dr. Ramesh Gupta', 'Cardiology', 15),
(2, 'Dr. Sunita Rao', 'Orthopedics', 10),
(3, 'Dr. Arvind Menon', 'Pediatrics', 8),
(4, 'Dr. Kavita Shah', 'Dermatology', 12),
(5, 'Dr. Manoj Desai', 'Neurology', 20);

INSERT INTO Appointments VALUES
(1, 1, 1, '2025-09-01', 'Completed'),
(2, 2, 2, '2025-09-05', 'Scheduled'),
(3, 3, 3, '2025-09-10', 'Completed'),
(4, 4, 4, '2025-09-15', 'Cancelled'),
(5, 5, 5, '2025-09-20', 'Scheduled'),
(6, 6, 1, '2025-09-25', 'Completed'),
(7, 7, 2, '2025-09-28', 'Scheduled'),
(8, 8, 3, '2025-09-29', 'Completed'),
(9, 9, 4, '2025-09-30', 'Scheduled'),
(10, 10, 5, '2025-10-01', 'Scheduled');

INSERT INTO MedicalRecords VALUES
(1, 1, 1, 'Hypertension', 'Medication and lifestyle changes'),
(2, 2, 2, 'Fractured Arm', 'Cast and physiotherapy'),
(3, 3, 3, 'Flu', 'Rest and antiviral drugs'),
(4, 4, 4, 'Acne', 'Topical creams'),
(5, 5, 5, 'Migraine', 'Pain management therapy'),
(6, 6, 1, 'High Cholesterol', 'Diet and statins'),
(7, 7, 2, 'Knee Pain', 'Exercise and painkillers'),
(8, 8, 3, 'Chickenpox', 'Antihistamines and rest'),
(9, 9, 4, 'Eczema', 'Moisturizers and steroids'),
(10, 10, 5, 'Epilepsy', 'Anticonvulsant medication');

INSERT INTO Billing VALUES
(1, 1, 1500.00, '2025-09-01', 'Paid'),
(2, 2, 2000.00, '2025-09-05', 'Unpaid'),
(3, 3, 800.00, '2025-09-10', 'Paid'),
(4, 4, 1200.00, '2025-09-15', 'Unpaid'),
(5, 5, 2500.00, '2025-09-20', 'Paid'),
(6, 6, 1800.00, '2025-09-25', 'Paid'),
(7, 7, 1600.00, '2025-09-28', 'Unpaid'),
(8, 8, 900.00, '2025-09-29', 'Paid'),
(9, 9, 1100.00, '2025-09-30', 'Unpaid'),
(10, 10, 3000.00, '2025-10-01', 'Paid');
```
# TASK - BASIC QUERIES

## 1. List all patients assigned to a cardiologist.
``` sql
-- 1. List all patients assigned to a cardiologist.
SELECT p.name,d.name,a.appointment_date,a.status FROM Patients p
JOIN Appointments a ON p.patient_id = a.patient_id
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE d.specialization = 'Cardiology';
```
## 2. Find all appointments for a given doctor.
``` sql
-- 2. Find all appointments for a given doctor.
SELECT a.appointment_id,p.name,a.appointment_date,a.status FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = 2;
```
## 3. Show unpaid bills of patients.
``` sql
-- 3. Show unpaid bills of patients.
SELECT p.name,b.bill_id,b.amount,b.bill_date FROM Billing b
JOIN Patients p ON b.patient_id = p.patient_id
WHERE b.status = 'Unpaid';
```

# TASK- STORED PROCEDURES

## 4. Procedure: GetDoctorAppointments(doctor_id) → returns all appointments for a doctor.
``` sql
DELIMITER //
CREATE PROCEDURE FindAppointments(IN did INT)
BEGIN
SELECT a.appointment_id,p.name,a.appointment_date,a.status FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = did;
END //
DELIMITER ;

CALL FindAppointments(2);
```
## 5. Procedure: GetPatientHistory(patient_id) → returns all visits, diagnoses, and treatments for a patient.
``` sql
DELIMITER //

CREATE PROCEDURE GetPatientHistory(IN pid INT)
BEGIN
    SELECT 
        p.name AS patient_name,
        a.appointment_date,
        d.name AS doctor_name,
        d.specialization,
        mr.diagnosis,
        mr.treatment
    FROM 
        Patients p
    JOIN 
        Appointments a ON p.patient_id = a.patient_id
    JOIN 
        Doctors d ON a.doctor_id = d.doctor_id
    LEFT JOIN 
        MedicalRecords mr ON p.patient_id = mr.patient_id AND d.doctor_id = mr.doctor_id
    WHERE 
        p.patient_id = pid
    ORDER BY 
        a.appointment_date;
END //

DELIMITER ;

CALL GetPatientHistory(6);
```
