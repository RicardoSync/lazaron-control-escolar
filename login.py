import customtkinter
from PIL import Image
from login_back import iniciar_sesion
from panel import panel_inicio
from tkinter import messagebox

login_ventana = customtkinter.CTk()
login_ventana.title("Inicio de Sesion Doblenet")
login_ventana.resizable(False, False)
login_ventana.geometry("800x500")


logo = customtkinter.CTkImage(light_image=Image.open("img/log.png"),
                            dark_image=Image.open("img/log.png"),
                            size=(250,500))


#Definimos la funciona para iniciar sesion
def obtener_datos():
    username = usuario_entry.get()
    clave = clave_entry.get()
    if iniciar_sesion(username, clave):
        print("Inicio de sesión exitoso")
        panel_inicio(login_ventana)
    else:
        messagebox.showerror("Error", "Usuario o clave incorrectos")

#Frame de lado izquierdo
frame_izquierdo = customtkinter.CTkFrame(login_ventana, border_color="#36486c",
                                        border_width=2, corner_radius=2, fg_color="transparent")
logo_label = customtkinter.CTkLabel(frame_izquierdo, image=logo, text="")




#Widgets para el inicio de sesion
usuario_label = customtkinter.CTkLabel(login_ventana, text="Usuario", font=("Monospace", 20, "bold"))
usuario_entry = customtkinter.CTkEntry(login_ventana, font=("Monospace", 15, "bold"))
clave_label = customtkinter.CTkLabel(login_ventana, text="Clave", font=("Monospace", 20, "bold"))
clave_entry = customtkinter.CTkEntry(login_ventana, font=("Monospace", 15, "bold"), show="*")
buton_iniciar_sesion = customtkinter.CTkButton(login_ventana, text="Iniciar Sesion", font=("Monospace", 15, "bold"),
                                            command=obtener_datos)


frame_izquierdo.place(relx=0.0, rely=0.0, relwidth=0.3, relheight=1.0)
logo_label.pack()
usuario_label.place(relx=0.4, rely=0.2)
usuario_entry.place(relx=0.4, rely=0.3, relwidth=0.4)
clave_label.place(relx=0.4, rely=0.4)
clave_entry.place(relx=0.4, rely=0.5, relwidth=0.4)
buton_iniciar_sesion.place(relx=0.7, rely=0.9, relwidth=0.2)
login_ventana.mainloop()