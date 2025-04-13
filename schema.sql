CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password TEXT
);

CREATE TABLE IF NOT EXISTS rides (
    id SERIAL PRIMARY KEY,
    departure VARCHAR(100),
    destination VARCHAR(100),
    date TIMESTAMP,
    seats INTEGER,
    user_id INTEGER REFERENCES users(id)
);