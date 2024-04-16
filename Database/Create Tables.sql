CREATE TABLE bootcamp
(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(55) NOT NULL UNIQUE
);

CREATE TABLE task
(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(55) NOT NULL UNIQUE
);

CREATE TABLE bootcamp_task
(
    id SERIAL PRIMARY KEY,
    bootcamp_id INT NOT NULL,
    task_id INT NOT NULL,
    is_mandetory BOOLEAN DEFAULT true,
    number INT NOT NULL,
    FOREIGN KEY (bootcamp_id) REFERENCES bootcamp(id),
    FOREIGN KEY (task_id) REFERENCES task(id)
);

CREATE TABLE submission
(
    id SERIAL PRIMARY KEY,
    bootcamp_task_id INT NOT NULL,
    score INT,
    date DATE NOT NULL,
    status VARCHAR(30)
);