import customtkinter
from PIL import Image
from tkinter import END
from paquetes_back import guardar_paquetes
from paquetes_back import guardar_antenas
from paquetes_back import guardar_router

def equipos_paquetes_ui():
    ventana_guardado = customtkinter.CTkToplevel()
    ventana_guardado.title("Equipos y paquetes")
    ventana_guardado.geometry("800x600")
    ventana_guardado.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    #Funciones
    def limpiar():
        paqeute_entry.delete(0, END)
        velocidad_entry.delete(0, END)
        velocidad_baja_entry.delete(0, END)
        precio_entry.delete(0, END)

        #Limpieza de los fatos en antenas
        antena_nombre_entry.delete(0, END)
        antena_modelo_entry.delete(0, END)

        #Limpieza de los datos router
        router_nombre_entry.delete(0, END)
        router_modelo_entry.delete(0, END)
    
    def obtener_datos():
        nombre = paqeute_entry.get()
        velocidad_formato = velocidad_entry.get() + "M" + "/" + velocidad_baja_entry.get() + "M"
        precio = precio_entry.get()
        velocidad = velocidad_formato
        print("Nombre del paquete: " + nombre + " con velocidad: " + velocidad_formato + " y precio mensual de: " + precio)
        guardar_paquetes(nombre, velocidad, precio)
        limpiar()
        

    def obtener_datos_antena():
        nombre = antena_nombre_entry.get()
        modelo = antena_modelo_entry.get()
        guardar_antenas(nombre, modelo)
        limpiar()

    def obtener_datos_router():
        nombre = router_nombre_entry.get()
        modelo = router_modelo_entry.get()
        guardar_router(nombre, modelo)
        limpiar()


    #Fuente de los titulos
    titulos = ("Arial", 15, "bold")

    #Contenedor de los widgets
    contenedor = customtkinter.CTkTabview(ventana_guardado)

    #Tab de equipos
    contenedor.add("Paquetes")
    contenedor.add("Antenas")
    contenedor.add("Routers")    


    #Tab de paquetes
    paquete_label = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Nombre del Paquete",
                                        font=titulos)
    paqeute_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"),
                                        placeholder_text="Paquete Plasma")

    velocidad_label_subidad = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Velocidad Subida",
                                            font=titulos)
    velocidad_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"),
                                            placeholder_text="100")

    velocidad_baja_label = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Velocidad Bajada",
                                        font=titulos)
    velocidad_baja_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"),
                                                placeholder_text="30")

    precio_label = customtkinter.CTkLabel(contenedor.tab("Paquetes"), text="Precio",
                                        font=titulos)
    precio_entry = customtkinter.CTkEntry(contenedor.tab("Paquetes"),
                                        placeholder_text="400")

    btn_guardar = customtkinter.CTkButton(contenedor.tab("Paquetes"), text="Guardar",
                                        command=obtener_datos)
    
    btn_limpiar = customtkinter.CTkButton(contenedor.tab("Paquetes"), text="Limpiar",
                                        command=limpiar)


    btn_cancelar = customtkinter.CTkButton(contenedor.tab("Paquetes"), text="Cancelar",
                                        command=ventana_guardado.destroy)


    #Tab de las antenas
    antena_nombre_label = customtkinter.CTkLabel(contenedor.tab("Antenas"), text="Nombre Antena",
                                        font=titulos)
    antena_nombre_entry = customtkinter.CTkEntry(contenedor.tab("Antenas"),
                                        placeholder_text="LiteBeam")

    antena_modelo_label = customtkinter.CTkLabel(contenedor.tab("Antenas"), text="Modelo Antena",
                                            font=titulos)
    antena_modelo_entry = customtkinter.CTkEntry(contenedor.tab("Antenas"),
                                            placeholder_text="M5")


    btn_guardar_antena = customtkinter.CTkButton(contenedor.tab("Antenas"), text="Guardar",
                                                command=obtener_datos_antena)
    
    btn_limpiar_antena = customtkinter.CTkButton(contenedor.tab("Antenas"), text="Limpiar",
                                        command=limpiar)


    btn_cancelar_antena = customtkinter.CTkButton(contenedor.tab("Antenas"), text="Cancelar",
                                        command=ventana_guardado.destroy)


    #Tab routers
    router_nombre_label = customtkinter.CTkLabel(contenedor.tab("Routers"), text="Nombre Router",
                                        font=titulos)
    router_nombre_entry  = customtkinter.CTkEntry(contenedor.tab("Routers"),
                                        placeholder_text="TpLink")

    router_modelo_label = customtkinter.CTkLabel(contenedor.tab("Routers"), text="Modelo Router",
                                            font=titulos)
    router_modelo_entry = customtkinter.CTkEntry(contenedor.tab("Routers"),
                                            placeholder_text="840N")


    btn_guardar_router = customtkinter.CTkButton(contenedor.tab("Routers"), text="Guardar",
                                                command=obtener_datos_router)
    
    btn_limpiar_router = customtkinter.CTkButton(contenedor.tab("Routers"), text="Limpiar",
                                        command=limpiar)


    btn_cancelar_router = customtkinter.CTkButton(contenedor.tab("Routers"), text="Cancelar",
                                        command=ventana_guardado.destroy)

    #Tab de paquetes
    contenedor.place(relx=0.0 , rely=0.0, relwidth=1.0, relheight=1.0)

    #Posiciones de los widgets de paquetes
    paquete_label.place(relx=0.2, rely=0.2)
    paqeute_entry.place(relx=0.2, rely=0.3, relwidth=0.6)
    velocidad_label_subidad.place(relx=0.2, rely=0.4)
    velocidad_entry.place(relx=0.2, rely=0.5, relwidth=0.28)
    velocidad_baja_label.place(relx=0.5, rely=0.4)
    velocidad_baja_entry.place(relx=0.5, rely=0.5, relwidth=0.28)
    precio_label.place(relx=0.2, rely=0.6)
    precio_entry.place(relx=0.3, rely=0.6, relwidth=0.5)
    btn_guardar.place(relx=0.2, rely=0.7, relwidth=0.2)
    btn_limpiar.place(relx=0.4, rely=0.7, relwidth=0.2)
    btn_cancelar.place(relx=0.6, rely=0.7, relwidth=0.2)


    #Posiciones de los widgets de antenas
    antena_nombre_label.place(relx=0.2, rely=0.2)
    antena_nombre_entry.place(relx=0.2, rely=0.3, relwidth=0.5)
    antena_modelo_label.place(relx=0.2, rely=0.4)
    antena_modelo_entry.place(relx=0.2, rely=0.5, relwidth=0.5)
    btn_guardar_antena.place(relx=0.2, rely=0.6, relwidth=0.2)
    btn_limpiar_antena.place(relx=0.4, rely=0.6, relwidth=0.2)
    btn_cancelar_antena.place(relx=0.6, rely=0.6, relwidth=0.2)

    #Posiciones de los widgest de router
    router_nombre_label.place(relx=0.2, rely=0.2)
    router_nombre_entry.place(relx=0.2, rely=0.3, relwidth=0.5)
    router_modelo_label.place(relx=0.2, rely=0.4)
    router_modelo_entry.place(relx=0.2, rely=0.5, relwidth=0.5)
    btn_guardar_router.place(relx=0.2, rely=0.6, relwidth=0.2)
    btn_limpiar_router.place(relx=0.4, rely=0.6, relwidth=0.2)
    btn_cancelar_router.place(relx=0.6, rely=0.6, relwidth=0.2)


    ventana_guardado.mainloop()
