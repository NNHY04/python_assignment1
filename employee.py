from prettytable import PrettyTable   # pip install prettytable
from colorama import Fore, Back, Style  # pip install colorama
from datetime import datetime

key = hash("password")  # hash values for "password"
class Employee:
    def __init__(self, name, id, department, job_title, annual_salary, status):
        self._name = name
        self._id = int(id)
        self._department = department
        self._job_title = job_title
        self._annual_salary = float(annual_salary)
        self._status = bool(status)
        self._logs = []
        self._counter = 0

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_annual_salary(self):
        return self._annual_salary

    def get_status(self):
        return self._status

    def get_logs(self):
        return self._logs

    def get_time(self):
        return self._time

    def get_message(self):
        return self._message

    def get_counter(self):
        return self._counter

    def display_all(self):
        myTable = PrettyTable(["Employee Name", "Employee ID", "Department", "Job Tittle", "Annual Salary", "Employment Status"])
        for emp in employee:
            if emp.get_status() == True:
                empstatus = Fore.GREEN + 'Active' + Style.RESET_ALL
            else:
                empstatus = Fore.RED + 'Inactive' + Style.RESET_ALL
            myTable.add_row([ emp.get_name(), emp.get_id(), emp.get_department(), emp.get_job_title(), f"${emp.get_annual_salary():,.2f}", empstatus ])

        print(myTable)

        # ------log message -------------
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        log_message = Fore.GREEN + "User tries to view all employee records" + Style.RESET_ALL
        self.log_message(current_time,log_message)
        # ------log message -------------

    def add_employee(self):
        max_attempts = 3
        attempts = 0

        # -----log message  -------------
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        log_message = Fore.YELLOW + f"User attempts to login" + Style.RESET_ALL
        self.log_message(current_time,log_message)
        # ------log message -------------

        while attempts < max_attempts:  # prompt user to enter password to add employee
            if self.login() == key:
                print("You've entered the correct password, you may now proceed to add an employee.")

                # -----log message  -------------
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                log_message = Fore.YELLOW + f"User successfully logged in" + Style.RESET_ALL
                self.log_message(current_time, log_message)
                # ------log message -------------

                while True:  # prompt enter employee name
                    name = input("Enter employee name: ")
                    if name.strip():
                        break
                    print("Invalid input. Name cannot be blank!")

                while True:  # prompt enter Employee ID number
                    try:
                        id = int(input("Enter employee ID Number: "))
                        id_exists = False
                        for emp in employee:
                            if id == emp.get_id():
                                print("ID already exists. Please enter a different ID")
                                id_exists = True
                                break
                        if not id_exists:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                while True:  # prompt enter department
                    department = input("Enter department: ")
                    if department.strip():
                        break
                    print("Invalid input. The department cannot be blank.")

                while True:  # prompt enter job title
                    job_title = input("Enter Job Title: ")
                    if job_title.strip():
                        break
                    print("Invalid input. The job title cannot be blank.")

                while True:  # prompt enter annual salary
                    try:
                        annual_salary = float(input("Enter annual salary: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the annual salary.")

                while True:  # prompt enter yes or no for employment status
                    status = input("Is the employee active? (yes/no): ").strip().lower()
                    if status in ["yes", "no"]:
                        break
                    print("Invalid input. Please enter 'yes' or 'no'.")

                if status == "yes":
                    final_status = True
                else:
                    final_status = False

                new_employee = Employee(name, id, department, job_title, annual_salary, final_status)
                employee.append(new_employee)
                print("Employee added successfully!")

                # -----log message  -------------
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                log_message = Fore.GREEN + "User successfully added an employee" + Style.RESET_ALL
                self.log_message(current_time, log_message)
                # ------log message -------------

                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print(f"Incorrect Password. You have {max_attempts - attempts} attempts left")

                    # -----log message  -------------
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    log_message = Fore.RED + f"User keyed in the wrong password" + Style.RESET_ALL
                    self.log_message(current_time, log_message)
                    # ------log message -------------

                else:
                    print(f"Incorrect password. You have exceeded the maximum number({max_attempts}) of attempts .")

                    # -----log message  -------------
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    log_message = Fore.RED + f"User keyed in WRONGLY 3 times" + Style.RESET_ALL
                    self.log_message(current_time, log_message)
                    # ------log message -------------


    def sort_department(self):  # Bubble sort by Ascending Order
        n = len(employee)
        for i in range(n-1, 0, -1):  # Starting from the Back
            for j in range(i):
                if employee[j].get_department() > employee[j+1].get_department():
                    temp = employee[j]
                    employee[j] = employee[j+1]
                    employee[j+1] = temp  # primary sort (sort by department)
                elif employee[j].get_department() == employee[j+1].get_department():
                    if employee[j].get_id() > employee[j+1].get_id():
                        temp = employee[j]
                        employee[j] = employee[j+1]
                        employee[j+1] = temp  # secondary sort (sort by employee ID)
        print("\nEmployees sorted by department(Ascending Order): ")

        # -----log message  -------------
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        log_message = Fore.GREEN + f"User sorts employee records by department in ascending order" + Style.RESET_ALL
        self.log_message(current_time, log_message)
        # ------log message -------------


        self.display_all()

    def sort_salary(self):
        n = len(employee)

        for i in range(n-1):
            max = i  # Assuming the first is the max
            for j in range(i+1,n):
                if employee[j].get_annual_salary() > employee[max].get_annual_salary():  # To determine any other element is bigger then max
                    max = j  # if j(i+1) is more then i, max will change to j(i+1)
                elif employee[j].get_annual_salary() == employee[max].get_annual_salary():
                    if employee[j].get_id() < employee[max].get_id():
                        max = j  # secondary sort (sort by employee ID)

            if max != i:  # if max is not equal to i, it will swap position
                temp = employee[i]
                employee[i] = employee[max]
                employee[max] = temp

        print("\nEmployees sorted by annual salary(Descending Order): ")

        # -----log message  -------------
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        log_message = Fore.GREEN + f"User sorts employee records by salary in descending order" + Style.RESET_ALL
        self.log_message(current_time, log_message)
        # ------log message -------------

        self.display_all()

    def log_message(self, time, message):
        self._counter += 1
        self._logs.append((self._counter,time, message))

    def view_log(self):
        log = self._logs
        logTable = PrettyTable(["No.", "Time", "Message"])
        for i in log:
            logTable.add_row(i)
        print(logTable)



    def exit(self):
        exit()

    def menu(self):

        # -----log message  -------------
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        log_message = Fore.CYAN + f"User initiate Employee Management System" + Style.RESET_ALL
        self.log_message(current_time, log_message)
        # ------log message -------------

        while True:
            print("\nWelcome to the Employee Management System")
            print("1. Display all employee records")
            print("2. Add new employee records")
            print("3. Sort employees by department")
            print("4. Sort employees by salary")
            print("5. View Logs")
            print("6. Exit program")

            try:
                option = int(input("Please select an option (1-5): "))
                if option == 1:
                    self.display_all()
                elif option == 2:
                    self.add_employee()
                elif option == 3:
                    self.sort_department()
                elif option == 4:
                    self.sort_salary()
                elif option == 5:
                    self.view_log()
                elif option == 6:
                    self.exit()
                else:
                    print("Invalid option. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a numeric option (1-5).")

    def login(self):
        get_key = input("Enter password to add an employee: " ).strip()
        return hash(get_key)




if __name__ == '__main__':
    # Adding data into the list
    employee = []
    employee.append(Employee("Abdul Rahman", 10001, "Human Resources", "HR Manager", 82000.00, True))
    employee.append(Employee("Bobby Chan", 10003, "Engineering", "Software Engineer", 74000.50, False))
    employee.append(Employee("Charlie Cheng", 10002, "Human Resources", "HR Manager", 74000.50, True))
    employee.append(Employee("David Dan", 10004, "IT", "Software Engineer", 88888.80, True))
    emp_system = Employee('', 0, '', '', 0, False)
    emp_system.menu()
