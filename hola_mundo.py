import tkinter

#api

api=tkinter.Tk()
api.title=("Aplicacion de turnos")
api.geometry("500x300")

api.iconbitmap("apple.ico")


api.config(bg="#23646A",relief="groove", bd=10)

#widgets
texto = tkinter.Label (api, text="Turnos Online Fútbol")
texto1= tkinter.Label (api, text="Turnos Online Fútbol")
texto.config(bg="#BBE3E6", fg="red", font=("Arial", 20))




texto.pack() 

api.mainloop() 
