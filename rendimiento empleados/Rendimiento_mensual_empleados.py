import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectamos con la base de datos
conn = sqlite3.connect("Base_datos.db")

# Obtenemos la lista de nombres de empleados
querry_nombres = "SELECT DISTINCT LastName || ' ' || FirstName as FName FROM Employees"
nombres_df = pd.read_sql_query(querry_nombres, conn)
nombres_empleados = nombres_df['FName'].tolist()

# Iteramos sobre los nombres de empleados y generamos un gráfico de línea para cada uno
for nombre in nombres_empleados:
    # Ejecutamos la consulta SQL con una cláusula WHERE que filtra solo los datos para el empleado en cuestión
    querry = f"""
    SELECT strftime('%m',o.OrderDate) as Month, substr(OrderDate, 1, 4) as Year, ROUND(sum(p.Price*od.Quantity)) as VOLUMEN
    FROM Employees e
    INNER JOIN Orders o ON e.EmployeeID = o.EmployeeID
    INNER JOIN OrderDetails od ON o.OrderID = od.OrderID
    INNER JOIN Products p ON od.ProductID = p.ProductID
    WHERE e.LastName || ' ' || e.FirstName = '{nombre}'
    GROUP BY Month, Year
    ORDER BY Year, Month
    """
    resultado = pd.read_sql_query(querry, conn)
    print(resultado)
    
    # Generamos el gráfico de línea
    plt.plot(resultado['Year'].astype(str) + "-" + resultado['Month'].astype(str), resultado['VOLUMEN'], label=nombre)

# Configuramos el título y etiquetas de los ejes
plt.title('Ventas por empleado')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.legend(loc='upper left')

# Mostramos el gráfico
plt.show()



    
    
