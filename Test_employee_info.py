import employee_info

def test_get_employees_by_age_range():
    lower = 29
    upper = 36
    test_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
        ]
    
    assert(employee_info.get_employees_by_age_range(lower, upper) == test_data)

def test_calculate_average_salary():
    assert(employee_info.calculate_average_salary() == 180500/3)

def test_get_employees_by_dept():
    department = "Sales"
    test_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    assert(employee_info.get_employees_by_dept(department) == test_data)

        