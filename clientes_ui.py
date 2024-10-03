import customtkinter
from tkinter import END
from datetime import datetime, timedelta


#Definimos variables que vamos usar
titulos = ("Arial", 15, "bold")
tamanio_general = 300
today = datetime.now()

def clientes_ui_chidos(routers_guardados, antenas_guardadas, paquetes_guardados, antenas_guardadas_modelo, modelo_routers):


    #definimos las funciones que vamos a usar
    def limpieza_campos():
        nombre_entry.delete(0, END)
        direccion_entry.delete(0, END)
        telefono_entry.delete(0, END)
        ip_entry.delete(0, END)

    def obtener_datos():
        nombre = nombre_entry.get()
        direccion = direccion_entry.get()
        telefono = telefono_entry.get()
        antena = antena_entry.get()
        router = router_entry.get()
        ip = ip_entry.get()
        paquete = paquetes_entry.get()

        fechaInstalacion = today.strftime('%Y-%m-%d') #aqui ya tiene el fomrato AAAA-MM-DD

        nueva_fecha = today + timedelta(days=31)  #obtenemos la fecha de today y sumamos 31 dias con timedelta
        proximoPago = nueva_fecha.strftime('%Y-%m-%d') #formateamos en modo str


    ventana_clientes_ui = customtkinter.CTkToplevel()
    ventana_clientes_ui.title("Registro Cliente")
    ventana_clientes_ui.geometry("800x500")
    ventana_clientes_ui.resizable(False, False)


    #Definimos el frame izquiero para las opcioes
    banner_opciones = customtkinter.CTkFrame(ventana_clientes_ui, border_color="#36486c", border_width=2,
                                            corner_radius=2, fg_color="#36486c")
    
    #Definimos los botones con funciones obvias
    btn_save = customtkinter.CTkButton(banner_opciones, text="Guardar",
                                    command=obtener_datos)
    
    btn_limpiar = customtkinter.CTkButton(banner_opciones, text="Limpiar",
                                        command=limpieza_campos)
    
    btn_cancelar = customtkinter.CTkButton(banner_opciones, text="Cancelar",
                                        command=ventana_clientes_ui.destroy)
        
    demo_label = customtkinter.CTkLabel(banner_opciones, text="Doblenet v0.0.2", font=("Arial", 15, "bold"))


    #Scroll de los componentes
    scroll_componentes = customtkinter.CTkScrollableFrame(ventana_clientes_ui, border_color="#36486c", border_width=2, corner_radius=2)
    nombre_label = customtkinter.CTkLabel(scroll_componentes, text="Nombre del Cliente", font=titulos)
    nombre_entry = customtkinter.CTkEntry(scroll_componentes, placeholder_text="Ricardo Escobedo",
                                        width=tamanio_general)
    
    direccion_label = customtkinter.CTkLabel(scroll_componentes, text="Direccion del Cliente", font=titulos)
    direccion_entry = customtkinter.CTkEntry(scroll_componentes, placeholder_text="Solidariad #20",
                                            width=tamanio_general)
    
    telefono_label = customtkinter.CTkLabel(scroll_componentes, text="Celular del Cliente", font=titulos)
    telefono_entry = customtkinter.CTkEntry(scroll_componentes, placeholder_text="4981442266",
                                            width=tamanio_general)

    antena_label = customtkinter.CTkLabel(scroll_componentes, text="Tipo de Antena", font=titulos)
    antena_entry = customtkinter.CTkComboBox(scroll_componentes, values=antenas_guardadas, 
                                            width=tamanio_general)
    
    modelo_antena_label = customtkinter.CTkLabel(scroll_componentes, text="Modelo de Antena", font=titulos)
    modelo_antena_entry = customtkinter.CTkComboBox(scroll_componentes, values=antenas_guardadas_modelo,
                                                    width=tamanio_general)
    
    router_label = customtkinter.CTkLabel(scroll_componentes, text="Tipo de Router", font=titulos)
    router_entry = customtkinter.CTkComboBox(scroll_componentes, values=routers_guardados,
                                            width=tamanio_general)

    router_label_modelo = customtkinter.CTkLabel(scroll_componentes, text="Modelo de Router", font=titulos)
    router_entry_modelo = customtkinter.CTkComboBox(scroll_componentes, values=modelo_routers,
                                                width=tamanio_general)

    ip_label = customtkinter.CTkLabel(scroll_componentes, text="Ip Queue", font=titulos)
    ip_entry = customtkinter.CTkEntry(scroll_componentes, placeholder_text="10.20.20.33",
                                    width=tamanio_general)
    
    paquetes_label  = customtkinter.CTkLabel(scroll_componentes, text="Paquetes Disponibles", font=titulos)
    paquetes_entry = customtkinter.CTkComboBox(scroll_componentes, values=paquetes_guardados,
                                            width=tamanio_general)

    #fecha instalacion de manera automatica

    #dia corte, no aplica en este caso

    #proximo pago se hace automatico

    #mensualidad la obtiene del paquete
    
    #estado es activo por defecto

    #api no aplica

    #posiciones de los elemenos dentro del frame
    banner_opciones.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    btn_save.grid(row=0, column=0, padx=10, pady=10)
    btn_limpiar.grid(row=0, column=1, padx=10, pady=10)
    btn_cancelar.grid(row=0, column=2, padx=10, pady=10)
    demo_label.grid(row=0, column=3, padx=10, pady=10)

    #posiciones de los elemntos scroll
    scroll_componentes.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)
    nombre_label.grid(column=0, row=0, padx=10, pady=10)
    nombre_entry.grid(column=1, row=0, padx=10, pady=10)

    direccion_label.grid(column=0, row=1, padx=10, pady=10)
    direccion_entry.grid(column=1, row=1, padx=10, pady=10)
    telefono_label.grid(column=0, row=2, padx=10, pady=10)
    telefono_entry.grid(column=1, row=2, padx=10, pady=10)
    antena_label.grid(column=0, row=3, padx=10, pady=10)
    antena_entry.grid(column=1, row=3, padx=10, pady=10)
    modelo_antena_label.grid(column=0, row=4, padx=10, pady=10)
    modelo_antena_entry.grid(column=1, row=4, padx=10, pady=10)
    router_label.grid(column=0, row=5, padx=10, pady=10)
    router_entry.grid(column=1, row=5, padx=10, pady=10)

    router_label_modelo.grid(column=0, row=6, padx=10, pady=10)
    router_entry_modelo.grid(column=1, row=6, padx=10, pady=10)
    ip_label.grid(column=0, row=7, padx=10, pady=10)
    ip_entry.grid(column=1, row=7, padx=10, pady=10)

    paquetes_label.grid(column=0, row=8, padx=10, pady=10)
    paquetes_entry.grid(column=1, row=8, padx=10, pady=10)
    ventana_clientes_ui.mainloop()