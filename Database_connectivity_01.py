import pyodbc
sqlServerName = 'LAPTOP-1QBOMH8E\SQLEXPRESS'
databaseName = 'python_conn'
trusted_connection = 'yes'
#Below is the connection string, which will use above information
connenction_string = (
f"DRIVER={{SQL Server}};"
f"SERVER={sqlServerName};"
f"DATABASE={databaseName};"
f"Trusted_Connection={trusted_connection}"
)
try:
    #create connection to sql-server database
    connection = pyodbc.connect(connenction_string)
    cursor = connection.cursor()
    empName = input("Enter Employee Name: ")
    empSalary = int(input("Enter Employee Salary: "))
    empCity = input("Enter Employee City: ")
    cursor.execute("insert into Employee1(EmpName, EmpSalary, EmpCity) values(?, ?, ?)", empName, empSalary, empCity)
    connection.commit()
    cursor.close()
    print("Record Inserted Successfully in SQL-Server-Database!!!")
except pyodbc.Error as ex:
    print("Some exception occured: ", ex)
finally:
    if 'connection' in locals():
        connection.close()

