import tkinter as tk
from datetime import datetime
import calendar


def presupuesto_restante():
    # Obtener dia actual
    dia_actual = datetime.now().day
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Obtener el último día del mes actual
    ultimo_dia = calendar.monthrange(fecha_actual.year, fecha_actual.month)[1]
    #Cantidad de días que le queda al mes
    dias_restantes_del_mes = (ultimo_dia-dia_actual+1)
    

    cobro_de_impuesto = str(pago_de_impuestos_entrada.get())
    
    
    if cobro_de_impuesto == "Sí" or cobro_de_impuesto=="Si" or cobro_de_impuesto == "sí" or cobro_de_impuesto=="si":
        presupuesto = float(presupuesto_entrada.get())
        presupuesto_neto = presupuesto/(1.19)
        presupuesto_diario = round((presupuesto_neto/dias_restantes_del_mes),2)
        respuesta.config(text= ("El presupuesto diario es de: "+ str(presupuesto_diario)))
    elif cobro_de_impuesto == "No" or cobro_de_impuesto=="no":
        presupuesto = float(presupuesto_entrada.get())
        presupuesto_diario = round(presupuesto/dias_restantes_del_mes,2)
        respuesta.config(text= ("El presupuesto diario es de: " + str(presupuesto_diario)))
    else:
        respuesta.config(text="Debes indicar con un Sí o un No en el Campo: Indicar si paga o no impuestos")

ventana = tk.Tk()

ventana.title("Calculadora de Presupuesto Diario")
ventana.geometry("600x400")
ventana.configure(bg="gray")
ventana.resizable(False, False)

titulo = tk.Label(ventana, text="Calculadora de Presupuesto Diario", fg="black", font=("Arial",20), bg="gray")
titulo.place(relx=0.14, rely=0.05)

presupuesto = tk.Label(ventana, text="Indicar el presupuesto restante", fg="black", font=("Arial",13), bg="gray")
presupuesto.place(relx=0.2, rely=0.22, relheight=0.07, relwidth=0.4)
presupuesto_entrada = tk.Entry(ventana, fg="black", font=("Arial",15), bg="white")
presupuesto_entrada.place(relx=0.6, rely=0.24, relheight=0.05, relwidth=0.2)

pago_de_impuestos = tk.Label(ventana, text="Indicar si paga o no impuestos", fg="black", font=("Arial",13), bg="gray")
pago_de_impuestos.place(relx=0.2, rely=0.35, relheight=0.07, relwidth=0.4)
pago_de_impuestos_entrada = tk.Entry(ventana, fg="black", font=("Arial",15), bg="white")
pago_de_impuestos_entrada.place(relx=0.6, rely=0.36, relheight=0.05, relwidth=0.2)

boton_calcular = tk.Button(ventana, text="Calcular", fg="white", bg="blue", font=("Arial",13), command=presupuesto_restante)
boton_calcular.place(rely=0.55, relx=0.4, relheight= 0.1, relwidth=0.2)

respuesta = tk.Label(ventana, text="Debes responder con un Sí o con un No", fg="orange", font=("Arial",16), bg="gray")
respuesta.place(relx=0.09, rely=0.77, relheight=0.07, relwidth=0.8)

ventana.mainloop()