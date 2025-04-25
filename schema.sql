DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS employees;

CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT
)

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    age INT,
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
)