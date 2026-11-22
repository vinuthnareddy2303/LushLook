CREATE DATABASE IF NOT EXISTS lushlook CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lushlook;

CREATE TABLE IF NOT EXISTS bookings (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(150) NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    appointment_date DATE NOT NULL,
    notes VARCHAR(500) NULL,
    status ENUM('requested', 'confirmed', 'completed', 'cancelled') NOT NULL DEFAULT 'requested',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
