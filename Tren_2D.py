from tkinter import *

#------------------------
# variables globales
#------------------------
BASE = 560
ALTURA = 560

#------------------------
# ventana principal 
#------------------------
ventana_principal = Tk()
ventana_principal.title("Graficas_2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("600x600")
ventana_principal.config(bg="white")

#-------------------------
# frame de graficación
#-------------------------
frame_graficación = Frame(ventana_principal)
frame_graficación.config(bg="purple", width=580, height=580)
frame_graficación.place(x=10,y=10)

# creación canvas
c = Canvas(frame_graficación, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=2, y=2)

#lineas
linea_central_horizontal= c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="green")
linea_vertical= c.create_line(BASE/2,0,BASE/2,ALTURA, fill="green")

#Poligonos Tren
cuerpo_Tren = c.create_rectangle(BASE/1.8+80,ALTURA/2.1,BASE/2-70,ALTURA/3,fill="VioletRed1")
ruedas_Tren = c.create_oval(BASE/2+60,ALTURA/2.5,BASE/1.8+90,ALTURA/2,fill="gray")
ruedas_Tren = c.create_oval(BASE/2+60,ALTURA/2.5,BASE/1.8-30,ALTURA/2,fill="gray")
ruedas_Tren = c.create_oval(BASE/2-140,ALTURA/2-30,BASE/2-40,ALTURA/2+50,fill="gray")
cabeza_Tren = c.create_rectangle(BASE/1.8-10,ALTURA/3,BASE/2+110,ALTURA/4,fill="PaleVioletRed1")
Gorro_Tren = c.create_rectangle(BASE/1.8-18,ALTURA/4-20,BASE/3+210,ALTURA/4,fill="Pink3")
Final_Gorro = c.create_rectangle(BASE/1.8-10,ALTURA/4-38,BASE/3+200,ALTURA/4-20,fill="Pink4")
#-------------------------
# frame de controles
#-------------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="purple", width=580, height=270)
frame_controles.place(x=10, y=370)

# deaplegar ventana
ventana_principal.mainloop()
