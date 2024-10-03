import customtkinter
from PIL import Image
from equipos_paquetes import equipos_paquetes_ui
from clientes import llamado_avengers

icono_crear_cliente = customtkinter.CTkImage(light_image=Image.open("img/agregar-usuario.png"),
                                    dark_image=Image.open("img/agregar-usuario.png"),
                                    size=(50,50))
icono_crear_paquete = customtkinter.CTkImage(light_image=Image.open("img/soundcloud.png"),
                                    dark_image=Image.open("img/soundcloud.png"),
                                    size=(50,50))
icono_registo_pago = customtkinter.CTkImage(light_image=Image.open("img/salario-del-usuario.png"),
                                    dark_image=Image.open("img/salario-del-usuario.png"),
                                    size=(50,50))
fondo = customtkinter.CTkImage(light_image=Image.open("img/fondo_lnx.png"),
                                    dark_image=Image.open("img/fondo_lnx.png"),
                                    size=(250, 200))


def panel_inicio(login_ventana):
    login_ventana.destroy()
    panel_ventana = customtkinter.CTk()
    panel_ventana.title("Panel de Administrador")
    panel_ventana.resizable(False, False)
    panel_ventana.geometry("900x500")
    

    logo = customtkinter.CTkImage(light_image=Image.open("img/iconos.png"),
                                dark_image=Image.open("img/iconos.png"),
                                size=(180,180))


    #Definimos la barra de opciones
    barra_opcion = customtkinter.CTkFrame(panel_ventana, border_color="#36486c",
                                        border_width=2, corner_radius=2, fg_color="#36486c")
    logo_label = customtkinter.CTkLabel(barra_opcion, image=logo, text="")
    fondo_label = customtkinter.CTkLabel(panel_ventana, image=fondo, text="")


    #Definimos los botones de la barra de opciones
    buton_crear_cliente = customtkinter.CTkButton(barra_opcion, text="",
                                                image=icono_crear_cliente,
                                                command=llamado_avengers)
    
    buton_crear_paquete = customtkinter.CTkButton(barra_opcion, text="",
                                                image=icono_crear_paquete,
                                                command=equipos_paquetes_ui)
    
    buton_registro_pago = customtkinter.CTkButton(barra_opcion, text="",
                                                image=icono_registo_pago)


    
    barra_opcion.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    buton_crear_cliente.place(relx=0.1, rely=0.1)
    buton_crear_paquete.place(relx=0.1, rely=0.5)
    buton_registro_pago.place(relx=0.1, rely=0.3)
    logo_label.place(relx=0.0, rely=0.7)
    fondo_label.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    panel_ventana.mainloop()
