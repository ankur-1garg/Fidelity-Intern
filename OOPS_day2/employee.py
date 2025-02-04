class InvalidIDException(Exception):
    """Exception raised for invalid employee ID."""

    def __init__(self, msg):
        self.msg = msg


class NonNumericIDException(Exception):
    """Exception raised when Employee ID is not numeric."""

    def __init__(self, msg):
        self.msg = msg


class Employee:
    def __init__(self, name, role, emp_id):
        self.name = name
        self.role = role
        self.emp_id = emp_id
        self.validate_id()

    def validate_id(self):
        if not self.emp_id.isdigit():
            raise NonNumericIDException("Employee ID must contain only digits")
        if len(self.emp_id) != 4:
            raise InvalidIDException("Employee ID must be exactly 4 digits")


# Function to create an employee with user input
def create_employee():
    try:
        name = input("Enter employee name: ")
        role = input("Enter employee role: ")
        emp_id = input("Enter employee ID (4-digit number, e.g., 0001): ")

        emp = Employee(name, role, emp_id)
        print(f"Employee created: {emp.name}, {emp.role}, {emp.emp_id}")

    except NonNumericIDException as e:
        print(f"Non-Numeric ID Error: {e.msg}")
    except InvalidIDException as e:
        print(f"Invalid ID Error: {e.msg}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Example usage:
create_employee()
