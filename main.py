from tkinter import Tk, Entry, Frame, Label, END, Checkbutton, IntVar
from PIL import Image, ImageTk
from base_datos import *


# funciones

def al_hacer_click_username(event):
    if entradausuario.get() == "username":
        entradausuario.delete(0, END)
        entradausuario.config(fg="black", justify="center")


def al_hacer_click_password(event):
    if entradapassw.get() == "password":
        entradapassw.delete(0, END)
        entradapassw.config(fg="black", justify="center", show="*")


def al_hacer_click_sigin(event):
    nombre = entradausuario.get()
    contraseña = entradapassw.get()

    if (not entradausuario.get() and entradapassw.get() or entradausuario.get() == "username" and entradapassw.get() ==
            "" or entradausuario.get() == "" and entradapassw.get() == "password" or entradausuario.get() ==
            "username" and entradapassw.get() == "password"):
        messagebox.showinfo("Help", "Enter a username and password and then click here again")
    else:
        ingresar_datos(nombre, contraseña)


def al_hacer_click_login(event):
    nombre = entradausuario.get()
    contraseña = entradapassw.get()
    verificar_ingreso(nombre, contraseña, ventana, frame3)


def cuando_pierde_foco_username(event):
    if not entradausuario.get():
        entradausuario.insert(0, placeholderuser)
        entradausuario.config(fg=colorplaceholder, justify="left")


def cuando_pierde_foco_password(event):
    if not entradapassw.get():
        entradapassw.insert(0, placeholderpassword)
        entradapassw.config(fg=colorplaceholder, justify="left", show="")


def mostrar_contrasenia():
    if var.get() == 1:
        entradapassw.config(show="")
    else:
        entradapassw.config(show="*")


ventana = Tk()
ventana.title("login")
ventana.geometry("800x400")
ventana.resizable(False, False)

fuenteplaceholder = "Arial", 12

placeholderuser = "username"

placeholderpassword = "password"

colorplaceholder = "gray"

var = IntVar()

# Asignar icono de ventana (código relacionado con el icono)
icono = Image.open("icono.ico")
anchoico = 32
altoico = 32
icono2 = icono.resize((anchoico, altoico))
imagenfinalicono = ImageTk.PhotoImage(icono2)
ventana.iconphoto(True, imagenfinalicono)

frame1 = Frame(ventana)
frame1.place(x=0, y=0, width=800, height=400)

imagenfondo = Image.open("fondo3.png")
nuevoancho = 800
nuevoalto = 400
imageneditada = imagenfondo.resize((nuevoancho, nuevoalto))
imagenterminada = ImageTk.PhotoImage(imageneditada)

labelfondo = Label(frame1, image=imagenterminada)
labelfondo.place(x=0, y=0, width=800, height=400)

# Crear un nuevo frame que va a contener los datos de login
frame2 = Frame(frame1, bg="#F0F0F0")
frame2.place(x=200, y=50, width=400, height=300)

entradausuario = Entry(frame2, borderwidth=1, fg=colorplaceholder, font=fuenteplaceholder)
entradausuario.insert(0, placeholderuser)
entradausuario.place(x=50, y=40, width=300, height=40)

entradapassw = Entry(frame2, borderwidth=1, fg=colorplaceholder, font=fuenteplaceholder)
entradapassw.insert(0, placeholderpassword)
entradapassw.place(x=50, y=110, width=300, height=40)

casilla = Checkbutton(frame2, text="mostrar contraseña", fg="#4F709C", var=var, command=mostrar_contrasenia)
casilla.place(x=45, y=160)

# boton de login
botonlogin = Label(frame2, text="Login", bg="#9400FF", fg="white", font=fuenteplaceholder)
botonlogin.place(x=50, y=200, width=300, height=40)

# label invitacion

invitacion = Label(frame2, text="You do not have an account ?", fg="gray", font=fuenteplaceholder)
invitacion.place(x=65, y=240, width=200, height=40)

sigin = Label(frame2, text="Sign Up", fg="green", font=("Arial", 13))
sigin.place(x=270, y=240, width=80, height=40)

frame3 = Frame(ventana)
frame3.place_forget()

imagenfondo2 = Image.open("welcome.jpg")
ancho = 900
alto = 500
imageneditada2 = imagenfondo2.resize((ancho, alto))
imagenterminada2 = ImageTk.PhotoImage(imageneditada2)


labelfondo2 = Label(frame3, image=imagenterminada2)
labelfondo2.place(x=0, y=0, width=1000, height=600)

entradausuario.bind("<FocusIn>", al_hacer_click_username)
entradapassw.bind("<FocusIn>", al_hacer_click_password)
entradausuario.bind("<FocusOut>", cuando_pierde_foco_username)
entradapassw.bind("<FocusOut>", cuando_pierde_foco_password)
botonlogin.bind("<Button-1>", al_hacer_click_login)
sigin.bind("<Button-1>", al_hacer_click_sigin)

ventana.mainloop()
