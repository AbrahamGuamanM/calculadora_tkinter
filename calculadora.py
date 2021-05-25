from tkinter import *

raiz= Tk()

raiz.title("Calculadora Python")
#raiz.resizable(True,True)
raiz.iconbitmap("calculadora.ico")
#raiz.geometry("750x450")
raiz.config(bg="#FF5733")




cuadropantallita=Entry(raiz,width= 34)
cuadropantallita.grid(row=0,column=0, columnspan=4,padx=5,pady=5)
#botones



boton1=Button(raiz,text="1",width= 5, height= 2, command= lambda: click_boton(1))
boton2=Button(raiz,text="2",width= 5, height= 2, command= lambda: click_boton(2))
boton3=Button(raiz,text="3",width= 5, height= 2, command= lambda: click_boton(3))
boton4=Button(raiz,text="4",width= 5, height= 2, command= lambda: click_boton(4))
boton5=Button(raiz,text="5",width= 5, height= 2, command= lambda: click_boton(5))
boton6=Button(raiz,text="6",width= 5, height= 2, command= lambda: click_boton(6))
boton7=Button(raiz,text="7",width= 5, height= 2, command= lambda: click_boton(7))
boton8=Button(raiz,text="8",width= 5, height= 2, command= lambda: click_boton(8))
boton9=Button(raiz,text="9",width= 5, height= 2, command= lambda: click_boton(9))
boton0=Button(raiz,text="0",width= 13, height= 2, command= lambda: click_boton(0))

boton_borrar=Button(raiz,text="⌫",width= 5, height= 2, command= lambda: borrar())
boton_parentesis1=Button(raiz,text="(",width= 5, height= 2, command= lambda: click_boton("("))
boton_parentesis2=Button(raiz,text=")",width= 5, height= 2, command= lambda: click_boton(")"))
boton_punto=Button(raiz,text=".",width= 5, height= 2, command= lambda: click_boton("."))

boton_div=Button(raiz,text="÷",width= 5, height= 2, command= lambda: click_boton("÷"))
boton_mul=Button(raiz,text="x",width= 5, height= 2, command= lambda: click_boton("*"))
boton_sum=Button(raiz,text="+",width= 5, height= 2, command= lambda: click_boton("+"))
boton_res=Button(raiz,text="-",width= 5, height= 2, command= lambda: click_boton("-"))
boton_igual=Button(raiz,text="=",width= 5, height= 2, command= lambda: operacion())



boton1.grid(row=4,column=0, padx=5,pady=5)
boton2.grid(row=4,column=1, padx=5,pady=5)
boton3.grid(row=4,column=2, padx=5,pady=5)

boton_res.grid(row=4,column=3, padx=5,pady=5)
boton4.grid(row=3,column=0, padx=5,pady=5)
boton5.grid(row=3,column=1, padx=5,pady=5)
boton6.grid(row=3,column=2, padx=5,pady=5)

boton_sum.grid(row=3,column=3, padx=5,pady=5)
boton7.grid(row=2,column=0, padx=5,pady=5)
boton8.grid(row=2,column=1, padx=5,pady=5)
boton9.grid(row=2,column=2, padx=5,pady=5)
boton_mul.grid(row=2,column=3, padx=5,pady=5)
boton_borrar.grid(row=1,column=0, padx=5,pady=5)
boton_parentesis1.grid(row=1,column=1, padx=5,pady=5)
boton_parentesis2.grid(row=1,column=2, padx=5,pady=5)
boton_div.grid(row=1,column=3, padx=5,pady=5)
 

boton0.grid(row=5,column=0,columnspan=2, padx=5,pady=5)
boton_punto.grid(row=5,column=2, padx=5,pady=5)
boton_igual.grid(row=5,column=3, padx=5,pady=5)

i=0
#funciones

def click_boton(valor):
	global i
	cuadropantallita.insert(i,valor) 
	i+=1


def borrar():
	cuadropantallita.delete(0,END)
	i=0

def operacion():
	ecuacion= cuadropantallita.get()
	resultado= eval(ecuacion)
	cuadropantallita.delete(0,END)
	cuadropantallita.insert(0,resultado)
	i=0 
#miframe=Frame(raiz,width="1200",height="600")
#miframe.config(width="650",height="350")
#miframe.pack()#side="left",anchor="s",fill="both",expand="True"

#miframe.config(bg="red")
#miframe.config(width="650",height="350",(bd=35 )
#miframe.config(relief="groove")
#miframe.config(cursor="hand2")


#milabel=Label(miframe, text="hola calculadora",fg="red",font=("Comic Sans MS",28)).place(x=100,y=20)

#miimagen=PhotoImage(file="calculadora.png")
#milabel2=Label(miframe, image=miimagen).place(x=100,y=80)




# cuadroNombre=Entry(miframe)
# cuadroNombre.grid(row=0,column=1)

# cuadroApellido=Entry(miframe)
# cuadroApellido.grid(row=1,column=1)

# cuadroDireccion=Entry(miframe)
# cuadroDireccion.grid(row=2,column=1)


# nombrelabel=Label(miframe, text="Nombre:")
# nombrelabel.grid(row=0,column=0)

# apellidolabel=Label(miframe, text="Apellido:")
# apellidolabel.grid(row=1,column=0)


# direccionlabel=Label(miframe, text="Direccion:")
# direccionlabel.grid(row=2,column=0)



raiz.mainloop()