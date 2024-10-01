import customtkinter
from PIL import Image



def equipos_paquetes_ui():
    ventana_guardado = customtkinter.CTkToplevel()
    ventana_guardado.title("Equipos y paquetes")
    ventana_guardado.geometry("800x600")
    ventana_guardado.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    #Fuente de los titulos
    titulos = ("Arial", 15, "bold")

    #Contenedor de los widgets
    contenedor = customtkinter.CTkTabview(ventana_guardado)

    #Tab de equipos
    contenedor.add("Paquetes")
    contenedor.add("Antenas")
    contenedor.add("Routers")    


    #Tab de paquetes
    paquete_label = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Paquetes",
                                        font=titulos)
    paqeute_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"), width=200)

    velocidad_label = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Velocidad",
                                            font=titulos)
    velocidad_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"), width=200)

    precio_label = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Precio",
                                        font=titulos)
    precio_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"), width=200)


    #Tab de paquetes
    contenedor.place(relx=0.0 , rely=0.0, relwidth=1.0, relheight=1.0)
    ventana_guardado.mainloop()

equipos_paquetes_ui()