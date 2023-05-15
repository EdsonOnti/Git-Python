import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectamos con la base de datos
conn = sqlite3.connect("Base_datos.db")

# Obtenemos la lista de nombres de empleados disponibles
query = "SELECT DISTINCT LastName || ' ' || FirstName as FName FROM Employees"
empleados = pd.read_sql_query(query, conn)

# Iteramos sobre cada empleado y generamos un gráfico de líneas por empleado
for empleado in empleados['FName']:
    # Consulta SQL para obtener los datos de ventas del empleado por mes
    query = f"SELECT strftime('%m',o.OrderDate) as Month, substr(OrderDate, 1, 4) as Year, ROUND(sum(p.Price * od.Quantity)) AS VOLUMEN \
             FROM Orders o \
             INNER JOIN OrderDetails od ON o.OrderID = od.OrderID \
             INNER JOIN Products p ON p.ProductID = od.ProductID \
             INNER JOIN Employees e ON e.EmployeeID = o.EmployeeID \
             WHERE e.LastName || ' ' || e.FirstName = '{empleado}' \
             GROUP BY Year, Month \
             ORDER BY Year, Month"
    # Obtenemos los datos de ventas del empleado
    ventas = pd.read_sql_query(query, conn)
    
    # Generamos el gráfico de líneas
    plt.figure()
    plt.plot(ventas['Month'] + '-' + ventas['Year'], ventas['VOLUMEN'])
    plt.title(f'Ventas de {empleado}')
    plt.xlabel('Mes-Año')
    plt.ylabel('Volumen de ventas')
    plt.xticks(rotation=45)

# Mostramos todos los gráficos generados
plt.show()

