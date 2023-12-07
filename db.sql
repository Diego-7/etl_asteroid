CREATE DATABASE IF NOT EXISTS asteroid_db;

CREATE TABLE IF NOT  EXISTS asteroid_db.asteroid (
    id INT NOT NULL AUTO_INCREMENT,
    asteroid_name VARCHAR(255),
    absolute_magnitude_h DECIMAL(10, 2),
    is_potentially_hazardous BOOLEAN,
    orbiting_body VARCHAR(255),
    is_sentry_object BOOLEAN,
    extraction_date DATETIME NOT NULL,
    primary key (id)
) ENGINE=INNODB