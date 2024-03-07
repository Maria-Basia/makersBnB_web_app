-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    password VARCHAR(255)

);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price float,
    date_from date,
    date_to date,
    available_dates VARCHAR(255)[],
-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    selected_date VARCHAR(255),
    user_id int,
    constraint fk_space_user foreign key(user_id)
    references users(id)
    on delete cascade,
    space_id int,
    constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade
);





-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email_address, password) VALUES ('user_1@test.com', 'Rock');
INSERT INTO users (email_address, password) VALUES ('user_2@test.com', 'Pop');
INSERT INTO users (email_address, password) VALUES ('user_3@test.com', 'Pop');
INSERT INTO users (email_address, password) VALUES ('user_4@test.com', 'Jazz');



-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, description, price, date_from, date_to, available_dates, user_id) VALUES ('space_1', 'description_1', 45.5, DATE '2004-04-22', DATE '2005-05-24', '{"2004-04-23", "2004-04-24", "2004-04-25"}', 1);
INSERT INTO spaces (name, description, price, date_from, date_to, user_id) VALUES ('space_2', 'description_2', 14000.99, DATE '2003-03-11', DATE '2002-02-03', 2);    


INSERT INTO bookings (selected_date, user_id, space_id) VALUES ('2024-03-24', 1, 1);
-- INSERT INTO bookings (date_from, date_to, user_id, space_id) VALUES ('2024/03/20', '2024/04/01', 2, 2);
