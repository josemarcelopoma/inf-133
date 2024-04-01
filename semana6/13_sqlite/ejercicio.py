# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("Restaurante.db")

# Crear tabla de Platos
conn.execute(
    """
    CREATE TABLE Platos
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    categoria TEXT NOT NULL);
    """
)

# Insertar datos de Platos
conn.execute(
    """
    INSERT INTO Platos (nombre, precio,categoria) 
    VALUES ('pizza', 10.00,'italiana')
    """
)
conn.execute(
    """
    INSERT INTO Platos (nombre, precio,categoria) 
    VALUES ('hamburguesa', 8,'americana')
    """
)
conn.execute(
    """
    INSERT INTO Platos (nombre, precio,categoria) 
    VALUES ('sushi', 12,'japonesa')
    """
)
conn.execute(
    """
    INSERT INTO Platos (nombre, precio,categoria) 
    VALUES ('ensalada', 6,'vegetariana')
    """
)

# Consultar datos
print("Platos:")
cursor = conn.execute("SELECT * FROM Platos")
for row in cursor:
    print(row)

# Platos:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)
   
# Crear tabla de mesas
conn.execute(
    """
    CREATE TABLE Mesas
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)

# Insertar datos de mesas
conn.execute(
    """
    INSERT INTO Mesas (numero) 
    VALUES (5)
    """
)
conn.execute(
    """
    INSERT INTO Mesas (numero) 
    VALUES (6)
    """
)

# Consultar datos mesas
print("Mesas:")
cursor = conn.execute("SELECT * FROM Mesas")
for row in cursor:
    print(row)




# Crear tabla de Pedidos
conn.execute(
    """
    CREATE TABLE Pedidos
    (id INTEGER PRIMARY KEY,
    platos_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (platos_id) REFERENCES Platos(id),
    FOREIGN KEY (mesa_id) REFERENCES Mesas(id));
    """
)

# Insertar datos de pedidos
conn.execute(
    """
    INSERT INTO Pedidos (platos_id, mesas_id, cantidad,fecha) 
    VALUES (1, 1, 3,'2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO Pedidos (platos_id, mesas_id, cantidad,fecha) 
    VALUES (1, 1, 3,'2024-01-15')
    """
)

# Consultar datos
print("Pedidos:")
cursor = conn.execute("SELECT * FROM Pedidos")
for row in cursor:
    print(row)
###--------------------------------------




conn.close()
