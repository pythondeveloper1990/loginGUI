import sqlite3
from tkinter import messagebox


def crear_tabla():
    # Conectar a la base de datos (si no existe, se creará)
    conexion = sqlite3.connect("login.db")

    # Crear un objeto cursor
    cursor = conexion.cursor()

    # Query SQL para crear la tabla
    query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50),
        contraseña VARCHAR(50)
    )
    """

    # Ejecutar el query
    cursor.execute(query)

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()


def verificar_existencia_usuario(nombre):
    try:
        crear_tabla()
        conexion = sqlite3.connect("login.db")
        cursor = conexion.cursor()

        # Consulta SQL para verificar si el nombre ya existe
        consulta = "SELECT COUNT(*) FROM usuarios WHERE nombre = ?"

        # Valor a buscar
        valor = (nombre,)

        # Ejecutar la consulta
        cursor.execute(consulta, valor)

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        conexion.commit()
        conexion.close()

        # Si el resultado es 0, el nombre no existe
        return resultado[0] == 0

    except sqlite3.Error as error:
        print("Error al verificar la existencia del usuario:", error)
        return False


def ingresar_datos(nombre, contraseña):
    try:
        if verificar_existencia_usuario(nombre):
            conexion = sqlite3.connect("login.db")
            cursor = conexion.cursor()

            # Consulta SQL para insertar datos en la tabla "login"
            consulta = "INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)"

            # Valores a insertar
            valores = (nombre, contraseña)

            # Ejecutar la consulta
            cursor.execute(consulta, valores)

            # Confirmar la transacción y cerrar la conexión
            conexion.commit()
            conexion.close()

            print("Usuario registrado correctamente.")
            messagebox.showinfo("Help", "account created successfully")
        else:
            print("El nombre de usuario ya está en uso. Por favor, elige otro nombre.")
            messagebox.showinfo("Help", "The username is already in use. Please choose another name.")

    except sqlite3.Error as error:
        print("Error al insertar datos:", error)
        messagebox.showinfo("Help", error)


def verificar_ingreso(nombre, contraseña, ventana, frame3):
    try:
        conexion = sqlite3.connect("login.db")
        cursor = conexion.cursor()

        consulta = "SELECT COUNT(*) FROM usuarios WHERE nombre = ? AND contraseña = ?"
        valores = (nombre, contraseña)

        cursor.execute(consulta, valores)

        resultado = cursor.fetchone()[0]

        conexion.commit()
        cursor.close()
        conexion.close()

        if resultado > 0:
            print("Usuario autenticado.")
            messagebox.showinfo("Alert", "WELCOME")
            welcome(ventana, frame3)

        else:
            print("Usuario no encontrado o contraseña incorrecta.")
            messagebox.showinfo("Alert", "incorrect username or password")

    except sqlite3.Error as error:
        print("Error al acceder a la base de datos:", error)
        messagebox.showinfo("Alert", error)


def welcome(ventana, frame3):
    ventana.geometry("1000x600")
    ventana.title("work space")
    frame3.place(x=0, y=0, width=1000, height=600)
