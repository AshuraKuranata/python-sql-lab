import psycopg2

database="python_sql_lab"
connection = psycopg2.connect(
    database=database
)
cursor = connection.cursor()

terminate_program = False

print('Welcome to your database of employees and companies.\nPlease select the action that you would like to take:')

while terminate_program is False:
    print('\n[C]reate [V]iew [U]pdate [D]elete [Q]uit')
    user_input = input('User Action: ').capitalize()
    if user_input == 'C':
        while user_input == 'C':
            create_obj = input('Create [c]ompany or [e]mployee: ').lower()
            if create_obj == 'c':
                name = input('Company Name: ')
                address = input('Company Address: ')
                cursor.execute("INSERT INTO companies (name, address) VALUES (%s, %s)", [name, address])
                connection.commit()
                print('Created:\nCompany: ' + name + '\nAddress: ' + address)
                user_input = None
            elif create_obj == 'e':
                name = input('Employee Name: ')
                age = input('Employee Age: ')
                cursor.execute("SELECT company_id, name FROM companies")
                companies = cursor.fetchall()
                for company in companies:
                    print('Company Name: ' + company[1] + 'Company ID: ' + str(company[0]))
                company = input('Input company id for employee to work at: ')
                cursor.execute("INSERT INTO employees (name, age, company_id) Values (%s, %s, %s)", [name, age, company])
                connection.commit()
                cursor.execute('SELECT name FROM companies WHERE company_id = %s', [company])
                print('Created:\nEmployee Name: ' + name + '\nAge: ' + age + '\nCompany: ' + cursor.fetchone()[0])
                user_input = None
            else:
                print('Invalid input, returning to main menu.')
                user_input = None
    elif user_input == 'V':
        while user_input == 'V':
            table_view = input('View [c]ompany data or [e]mployee data: ').lower()
            if table_view == 'c':
                print('List of all the companies and their addresses:')
                cursor.execute('SELECT companies.name, companies.address, COUNT(employees.company_id) FROM companies LEFT JOIN employees ON employees.company_id = companies.company_id GROUP BY companies.company_id ORDER BY companies.name ASC;')
                # cursor.execute("SELECT name, address FROM companies")
                companies = cursor.fetchall()
                for company in companies:
                    print('Company Name: ' + company[0] + ' Address: ' + company[1] + ' Employee Count: ' + str(company[2]))
                user_input = None
            elif table_view == 'e':
                cursor.execute("SELECT employees.employee_id, employees.name, employees.age, companies.name FROM employees JOIN companies ON employees.company_id = companies.company_id ORDER BY employees.name ASC;")
                print('List of all the employees, ages, and company ID:')
                employees = cursor.fetchall()
                for employee in employees:
                    print('Employee ID: ' + str(employee[0]) + ' Employee Name: ' + employee[1] + ' Age: ' + str(employee[2]) + ' Company: ' + employee[3])
                user_input = None
            else:
                print('Invalid input, returning to main menu.')
                user_input = None
    elif user_input == 'U':
        while user_input == 'U':
            update_obj = input('Update [c]ompany data or [e]mployee data: ').lower()
            if update_obj == 'c':
                cursor.execute("SELECT * FROM companies")
                companies = cursor.fetchall()
                for company in companies:
                    print('Company ID: ' + str(company[0]) + ' Company Name: ' + company[1] + ' Address: ' + company[2])
                update_company = input('Select ID of company to update:')
                cursor.execute('SELECT * FROM companies WHERE company_id = %s', [update_company])
                select_company = cursor.fetchone()
                print('You have selected the following company to update:')
                print('Company ID: ' + str(select_company[0]) + ' Company Name: ' + select_company[1] + ' Address: ' + select_company[2])
                name = input('Update Company Name: ')
                address = input('Update Company Address: ')
                cursor.execute("UPDATE companies SET name = %s, address = %s WHERE company_id = %s", [name, address, update_company])
                connection.commit()
                print('\nUpdated Company Name: ' + name + '\nAddress: ' + address)
                user_input = None
            elif update_obj == 'e':
                cursor.execute("SELECT * FROM employees")
                employees = cursor.fetchall()
                for employee in employees:
                    print('Employee ID: ' + str(employee[0]) + ' Employee Name: ' + employee[1] + ' Age: ' + str(employee[2]) + ' Company: ' + str(employee[3]))
                update_employee = input ('Select ID of employee to update:')
                cursor.execute('SELECT * FROM employees WHERE employee_id = %s', [update_employee])
                select_company = cursor.fetchone()
                name = input('Update Employee Name: ')
                age = input('Update Employee Age: ')
                cursor.execute("SELECT * FROM companies")
                companies = cursor.fetchall()
                for company in companies:
                    print('Company ID: ' + str(company[0]) + ' Company Name: ' + company[1] + ' Address: ' + company[2])
                company = input('Input new Company ID : ')
                cursor.execute('UPDATE employees SET name = %s, age = %s, company_id = %s WHERE employee_id = %s', [name, age, company, update_employee])
                connection.commit()
                cursor.execute('SELECT name FROM companies WHERE company_id = %s', [company])
                print('Created:\nEmployee Name: ' + name + '\nAge: ' + age + '\nCompany: ' + cursor.fetchone()[0])
                user_input = None
            else:
                print('Invalid input, returning to main menu.')
                user_input = None
    elif user_input == 'D':
        while user_input == 'D':
            delete_obj = input('Delete [c]ompany data or [e]mployee data: ').lower()
            if delete_obj == 'c':
                cursor.execute("SELECT * FROM companies")
                companies = cursor.fetchall()
                for company in companies:
                    print('Company ID: ' + str(company[0]) + ' Company Name: ' + company[1] + ' Address: ' + company[2])
                delete_choice = input('Input company ID to delete: ')
                for company in companies:
                    if delete_choice == str(company[0]):
                        print('Deleting ' + company[1] + ' from database')
                        cursor.execute('DELETE FROM companies WHERE company_id = %s', [delete_choice])
                        connection.commit()
                        user_input = None
                        continue
                print('Delete request ended, returning to main menu.')
                user_input = None
            elif delete_obj == 'e':
                cursor.execute("SELECT * FROM employees")
                employees = cursor.fetchall()
                # print(employees)
                for employee in employees:
                    print('Employee ID: ' + str(employee[0]) + ' Employee Name: ' + employee[1] + ' Age: ' + str(employee[2]) + ' Company: ' + str(employee[3]))
                delete_choice = input('Input employee ID to delete: ')
                for employee in employees:
                    if delete_choice == str(employee[0]):
                        print('Deleting ' + employee[1] + ' from database')
                        cursor.execute('DELETE FROM employees WHERE employee_id = %s', [delete_choice])
                        connection.commit()
                        user_input = None
                        continue
                print('Delete request ended, returning to main menu.')
                user_input = None
            else:
                print('Invalid input, returning to main menu.')
                user_input = None
    elif user_input == 'Q':
        terminate_program = True

print('Thank you for your time, see you later!')

connection.close()