def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates()
    df = df.sort_values(ascending=False)
    column = 'getNthHighestSalary('+str(N)+')'
    if N > len(df) or N<=0:
        return pd.DataFrame({column:[None]})
    return pd.DataFrame({column:[df.iloc[N-1]]})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get the distinct salaries and sort them in descending order
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    # Check if there are at least two distinct salaries
    if len(distinct_salaries) < 2:
        second_highest_salary = None
    else:
        second_highest_salary = distinct_salaries.iloc[1]  # The second salary

    # Output the result
    result = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
    return result

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find the highest salary for each department
    max_salaries = employee.groupby('departmentId')['salary'].max().reset_index()
    print(max_salaries)
    # Step 2: Merge with the original employees DataFrame to get employees with highest salary
    employees_with_max_salary = pd.merge(employee, max_salaries, on=['departmentId', 'salary'])
    print(employees_with_max_salary)
    # Step 3: Merge with departments to get the department name
    result = pd.merge(employees_with_max_salary, department, left_on='departmentId', right_on='id', how='inner')
    print(result)
    # Select and rename the required columns
    result = result[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    return result

