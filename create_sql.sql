CREATE DATABASE phase_01;
USE phase_01;

CREATE TABLE `tax_payers` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `tax_pin` integer
);

INSERT `tax_payers` (`first_name`, `last_name`, `tax_pin`)
VALUES
  ('John', 'Doe', 12374364),
  ('Jane', 'Smith', 78643568),
  ('Alice', 'Johnson',  94643528);
