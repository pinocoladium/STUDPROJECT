CREATE TABLE IF NOT EXISTS Departament (
    departament_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Employee (
	employee_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
	departament INTEGER REFERENCES Departament(departament_id)
);

CREATE TABLE IF NOT EXISTS Сhief (
	сhief_id SERIAL PRIMARY KEY,
	employee INTEGER REFERENCES Employee(employee_id),
	departament INTEGER REFERENCES Departament(departament_id)
);

CREATE TABLE IF NOT EXISTS Employee_chief (
	id SERIAL PRIMARY KEY,
	employee_id INTEGER REFERENCES Employee(employee_id),
	сhief_id INTEGER REFERENCES Сhief(сhief_id)
);



