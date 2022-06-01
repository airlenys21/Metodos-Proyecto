import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox    
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)


########################################################################


class VentanaBinario(tk.Toplevel):
   
    #----------------------------------------------------------------------
    def __init__(self, Ventbianrio):
        self.Ventbinario = Ventbianrio
        tk.Toplevel.__init__(self)
        self.title("Sistema Binario")
        self.geometry("850x600")
        self.config(bg="#DFEFF0")
        self.decimal=tk.StringVar()
        self.NumConv=tk.StringVar()
        

        #Titulos
        Titulo=Label (self, text="Métodos de búsqueda de raíces", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",35 ))
        Titulo.place(x=65, y=20)

        Titulo2=Label (self, text="Método cerrado y método cerrado ", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",30 ))
        Titulo2.place(x=100, y=75)

        Subtitulo=tk.Label (self, text="Bisección - Secante", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",21))
        Subtitulo.place(x=280, y=130)

        #Entrada
        info=tk.Label (self, text="Ingresa el número decimal", fg="#20664A", bg="#DEF0FC") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=60, y=220)
 
        self.EntradaDec=Entry(self, textvariable= self.decimal)
        self.EntradaDec.place(x=130, y=270)

        #Gráfica
        Gráfica=tk.Frame(self)
        Gráfica.place(x=370, y=190)
        Gráfica.config( width="425", height="350", borderwidth = 5, relief="groove")

        #Botón
        Convertir=tk.Button(self, text="Convertir", width=15 , command=self.decimal_a_binario)
        Convertir.place(x=130, y=310)

        regresar=tk.Button(self, text="Regresar", width=15,  command=self.onClose)
        regresar.place(x=425, y=565)

        Otro=tk.Button(self, text="Resetear", width=15 , command=self.reset)
        Otro.place(x=625, y=565)

        #Salida
        Salidader=tk.Label (self, text="La derivada es:", fg="#20664A", bg="#DEF0FC") 
        Salidader.config(font=("Segoe UI Black",15))
        Salidader.place(x=30, y=380)

        self.Pantalla1 = tk.Label(self, foreground="black", width=18, height=1, borderwidth = 1, relief="raised", textvariable= self.NumConv) 
        self.Pantalla1.place(x=200, y=390)

        Salidainfo=tk.Label (self, text="La raíz de la función es:", fg="#20664A", bg="#DEF0FC") 
        Salidainfo.config(font=("Segoe UI Black",15))
        Salidainfo.place(x=50, y=450)
    
        self.Pantalla2 = tk.Label(self, foreground="white", background="black", width=30, height=2, textvariable= self.NumConv) 
        self.Pantalla2.place(x=70, y=500)
        
    #----------------------------------------------------------------------
    def decimal_a_binario(self):
        try:
            decBinario = int(self.decimal.get())
            binario = ""

            if decBinario < 0:
                MessageBox.showerror("Error", "El numero debe ser entero positivo ")

            elif decBinario > 4096:
                MessageBox.showerror("Error", "El numero sobrepasa la cantidad que puede representar el sistema")
            
            else:
                while decBinario > 0:
                    residuo = decBinario % 2
                    binario = str(residuo) + binario
                    decBinario = int(decBinario/ 2)
                return self.NumConv.set(binario)
    
        except ValueError:
                MessageBox.showerror("Error", "Debe ingresar un numero entero")

    #----------------------------------------------------------------------
    def onClose(self):
        self.destroy()
        self.Ventbinario.show()

    def reset(self):
        self.EntradaDec.delete(0, "end")
        self.NumConv.set(0)
       


########################################################################
class principal(object):

    #----------------------------------------------------------------------
    def __init__(self, Ventana):
        self.vent = Ventana
        self.vent.title("Búsqueda de raíces")
        self.vent.config(bg="#DFEFF0")

        Titulo=Label (self.vent, text="Métodos de búsqueda de raíces", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",35 ))
        Titulo.place(x=65, y=40)

        Titulo2=tk.Label (self.vent, text="Método cerrado y método cerrado ", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",30 ))
        Titulo2.place(x=100, y=100)

        Subtitulo=tk.Label (self.vent, text="Bisección - Secante", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",21))
        Subtitulo.place(x=280, y=160)

        ##Info
        Info=tk.Label (self.vent, text="Selecciona con que método deseas buscar la raíz", fg="#002060", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",15))
        Info.place(x=190, y=250)

        Info=tk.Label (self.vent, text="Creadores", fg="#7D9C9F", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",10))
        Info.place(x=360, y=515)

        Info=tk.Label (self.vent, text="Airlenys Recuero , Gabriela Vásquez", fg="#7D9C9F", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",10))
        Info.place(x=280, y=540)
        
        ##Botones
        Binario=tk.Button(self.vent, text="Método cerrado", width=15, command=self.openBinario)
        Binario.place(x=220, y=340)
        
        Binario=tk.Button(self.vent, text="Método abierto ", width=15)#, command=self.openBinario)
        Binario.place(x=500, y=340)

        Cerrar=tk.Button(self.vent, text="Cerrar", width=10, command=self.cerrar)
        Cerrar.place(x=750, y=540)
    #----------------------------------------------------------------------

    def cerrar(self):
        self.vent.destroy()

    def openBinario(self):
        self.vent.withdraw()
        VentanaBinario(self)

    def show(self):
        self.vent.update()
        self.vent.deiconify()
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    Ventana = tk.Tk()
    Ventana.geometry("850x600")
    app = principal(Ventana)
    Ventana.mainloop()