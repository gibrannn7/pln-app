-- Database schema for PLN Application
-- This file contains all required tables for the application

-- Create database
CREATE DATABASE IF NOT EXISTS pln_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pln_db;

-- Areas table
CREATE TABLE areas (
    code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'coordinator', 'field_officer') NOT NULL,
    area_code VARCHAR(20),
    active BOOLEAN DEFAULT TRUE,
    imei VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    FOREIGN KEY (area_code) REFERENCES areas(code)
);

-- Officers table
CREATE TABLE officers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    rbm_code VARCHAR(20),
    coordinator_id INT,
    active BOOLEAN DEFAULT TRUE,
    imei VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (coordinator_id) REFERENCES users(id)
);

-- Transactions table
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idpel VARCHAR(20) NOT NULL,
    periode DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    payment_type ENUM('cash', 'installment', 'transfer') DEFAULT 'cash',
    officer_id INT NOT NULL,
    status ENUM('pending', 'completed', 'failed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (officer_id) REFERENCES officers(id)
);

-- Talangan Transactions table
CREATE TABLE talangan_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idpel VARCHAR(20) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    date DATE NOT NULL,
    status ENUM('pending', 'approved', 'rejected', 'settled') DEFAULT 'pending',
    officer_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (officer_id) REFERENCES officers(id)
);

-- WA Logs table
CREATE TABLE wa_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idpel VARCHAR(20) NOT NULL,
    message TEXT,
    status ENUM('sent', 'delivered', 'read', 'failed') DEFAULT 'sent',
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivered_at TIMESTAMP NULL,
    read_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Print Logs table
CREATE TABLE print_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT NOT NULL,
    printed_by INT NOT NULL,
    file_path VARCHAR(255),
    printed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transaction_id) REFERENCES transactions(id),
    FOREIGN KEY (printed_by) REFERENCES users(id)
);

-- Monitoring Logs table
CREATE TABLE monitoring_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    module_name VARCHAR(100) NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    details TEXT,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Anomalies table
CREATE TABLE anomalies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idpel VARCHAR(20) NOT NULL,
    anomaly_type VARCHAR(100) NOT NULL,
    description TEXT,
    status ENUM('reported', 'investigating', 'resolved') DEFAULT 'reported',
    reported_by INT NOT NULL,
    resolved_by INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP NULL,
    FOREIGN KEY (reported_by) REFERENCES users(id),
    FOREIGN KEY (resolved_by) REFERENCES users(id)
);

-- Report Exports table
CREATE TABLE report_exports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    report_type VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    exported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Anomaly Master Data table
CREATE TABLE anomaly_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    category VARCHAR(100),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Daily Settlement Monitoring table
CREATE TABLE daily_settlements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    officer_id INT NOT NULL,
    status ENUM('pending', 'completed', 'verified') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    verified_at TIMESTAMP NULL,
    FOREIGN KEY (officer_id) REFERENCES officers(id)
);

-- Insert seed data
INSERT INTO areas (code, name) VALUES 
('A001', 'Area Jakarta Pusat'),
('A002', 'Area Jakarta Utara'),
('A003', 'Area Jakarta Barat'),
('A004', 'Area Jakarta Selatan'),
('A005', 'Area Jakarta Timur');

-- Insert admin user
INSERT INTO users (username, password_hash, role, area_code, active) VALUES 
('admin', 'scrypt:32768:8:1$JS39sNDLxYZbiGBU$d723423ffc481f665c15c888f4de1eca7852f3fb43b1d8dcc0635f996d9adfcc60ae98eb2fd75a261159975c510043fd6fe0f9b7c5d6419d0c8ee8f7eefebf56', 'admin', 'A001', TRUE),
('coordinator1', 'scrypt:32768:8:1$6HGQCTNvUZqKFdnk$0fa1ee3b2fb7a727dac3f50932b7037f5741a76ddfec6ae11ecf8025d3cd42f2b947abc1b9fc21d963ffc4b929ba66a839a6c3554a73898e8098dabb2dc078d4', 'coordinator', 'A001', TRUE),
('officer1', 'scrypt:32768:8:1$3NO1ZyZ6GYK4t43Z$c167c65a03ebe4bf290b809accaec5681ce7bab10bcdc9250e2e139b54368787379e862b26e1b0cccd706b6eacd29ab2f5d289eec4890405b1d460bcdbf7d0ef', 'field_officer', 'A001', TRUE);

-- Insert officers
INSERT INTO officers (user_id, rbm_code, active) VALUES 
(1, 'RBM001', TRUE),
(2, 'RBM001', TRUE),
(3, 'RBM001', TRUE);

-- Insert some sample transactions
INSERT INTO transactions (idpel, periode, total, payment_type, officer_id, status) VALUES
('00123456789', '2025-09-01', 120000.00, 'cash', 3, 'completed'),
('00123456790', '2025-09-01', 95000.00, 'installment', 3, 'completed'),
('00123456791', '2025-08-01', 150000.00, 'cash', 3, 'pending');