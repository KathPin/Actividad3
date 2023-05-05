import tkinter as tk
class aplication:
    def __init__(Ventana):
        Ventana.box= tk.Tk()
        Ventana.box.grid()
        Ventana.box.title("Actividad 03")
        Ventana.box.resizable(width=0, height=0)
        Ventana.BtnCalcular = tk.Button(Ventana.box,text="Generar Planificacion de Vuelo",command=Ventana.Calculos).grid(column=4,row=4)


        tk.Label(Ventana.box,text="Datos de la Camara").grid(column=0,row=0,columnspan=3)
        Ventana.Focal1 = tk.DoubleVar(Ventana.box,"Focal")
        Ventana.AI1    = tk.DoubleVar(Ventana.box,"Ancho  de imagen en pixeles")
        Ventana.HI1    = tk.DoubleVar(Ventana.box,"Altura de imagen en pixeles")
        Ventana.AS1    = tk.DoubleVar(Ventana.box,"Ancho del sensor en milimetros ")
        Ventana.HS1    = tk.DoubleVar(Ventana.box,"Alto del sensor en milimetros ")
        Ventana.RSI1   = tk.DoubleVar(Ventana.box,"Relacion ancho sensor")
        Ventana.Focal  = tk.Entry(Ventana.box,textvariable=Ventana.Focal1).grid(column=0,row=1)
        Ventana.AI     = tk.Entry(Ventana.box,textvariable=Ventana.AI1).grid(column=1,row=1)
        Ventana.HI     = tk.Entry(Ventana.box,textvariable=Ventana.HI1 ).grid(column=2,row=1)
        Ventana.AS     = tk.Entry(Ventana.box,textvariable=Ventana.AS1).grid(column=0,row=2)
        Ventana.HS     = tk.Entry(Ventana.box,textvariable=Ventana.HS1).grid(column=1,row=2)
        Ventana.RSI    = tk.Entry(Ventana.box,textvariable=Ventana.RSI1).grid(column=2,row=2)
        

        tk.Label(Ventana.box,text="Datos de la Parcela").grid(column=0,row=4,columnspan=3)
        Ventana.L1     = tk.DoubleVar(Ventana.box,"Largo parcela en metros")
        Ventana.A1     = tk.DoubleVar(Ventana.box,"Ancho Parcela en metros")
        Ventana.L      = tk.Entry(Ventana.box,textvariable=Ventana.L1).grid(column=0,row=5)
        Ventana.A      = tk.Entry(Ventana.box,textvariable=Ventana.A1).grid(column=1,row=5)


        tk.Label(Ventana.box,text="Parametros iniciales del vuelo").grid(column=0,row=6,columnspan=3)
        Ventana.AV1   = tk.DoubleVar(Ventana.box,"Altura de Vuelo en metros")
        Ventana.SL1   = tk.DoubleVar(Ventana.box,"Solape longitudinal %")
        Ventana.ST1   = tk.DoubleVar(Ventana.box,"Solape transversal %")
        Ventana.VV1   = tk.DoubleVar(Ventana.box,"Velocidad de Vuelo")
        Ventana.AV    = tk.Entry(Ventana.box,textvariable=Ventana.AV1).grid(column=0,row=7)
        Ventana.SL    = tk.Entry(Ventana.box,textvariable=Ventana.SL1).grid(column=1,row=7)
        Ventana.ST    = tk.Entry(Ventana.box,textvariable=Ventana.ST1).grid(column=2,row=7)
        Ventana.VV    = tk.Entry(Ventana.box,textvariable=Ventana.VV1).grid(column=3,row=7)


        tk.Label(Ventana.box,text="Calculos", anchor="e").grid(column=0,row=8,columnspan=7)
        tk.Label(Ventana.box,text="Resolucion en Terreno centimetro por pixel", anchor="e").grid(column=0,row=9)
        tk.Label(Ventana.box,text="Escala de vuelo", anchor="e").grid(column=2,row=9)
        tk.Label(Ventana.box,text="Ancho de la imagen sobre el terreno en metros", anchor="e").grid(column=4,row=9)
        tk.Label(Ventana.box,text="Alto de la imagen sobre el terreno en metros", anchor="e").grid(column=0,row=10)
        tk.Label(Ventana.box,text="Base area", anchor="e").grid(column=2,row=10)
        tk.Label(Ventana.box,text="Distancia entre pasadas en metros", anchor="e").grid(column=4,row=10)
        tk.Label(Ventana.box,text="Intervalo entre fotos", anchor="e").grid(column=0,row=11)
        tk.Label(Ventana.box,text="Tiempo entre fotos", anchor="e").grid(column=2,row=11)
        tk.Label(Ventana.box,text="Numero de pasadas", anchor="e").grid(column=4,row=11)
        tk.Label(Ventana.box,text="Numero de fotos por pasadas", anchor="e").grid(column=0,row=12)
        tk.Label(Ventana.box,text="Numero de fotos por vuelo", anchor="e").grid(column=2,row=12)
        tk.Label(Ventana.box,text="Distancia de vuelo en metros", anchor="e").grid(column=4,row=12)
        tk.Label(Ventana.box,text="Duracion de vuelo en min", anchor="e").grid(column=2,row=13)

    
        Ventana.GSD = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.GSD.grid(column=1,row=9)
        Ventana.EV  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.EV.grid(column=3,row=9)
        Ventana.AIT = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.AIT.grid(column=5,row=9)
        Ventana.HIT = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.HIT.grid(column=1,row=10)
        Ventana.BA  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.BA.grid(column=3,row=10)
        Ventana.DP  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.DP.grid(column=5,row=10)
        Ventana.IF  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.IF.grid(column=1,row=11)
        Ventana.TF  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.TF.grid(column=3,row=11)
        Ventana.NP  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.NP.grid(column=5,row=11)
        Ventana.NFP = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.NFP.grid(column=1,row=12)
        Ventana.NF  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.NF.grid(column=3,row=12) 
        Ventana.dV  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.dV.grid(column=5,row=12)
        Ventana.DV  = tk.Label(Ventana.box,text=" ?????? ")
        Ventana.DV.grid(column=3,row=13)
        Ventana.box.mainloop()


    def Calculos(Ventana): 
        GSD = (Ventana.AV1.get()*100/Ventana.Focal1.get())*Ventana.RSI1.get()      # Resolucion en Terreno centimetro por pixel
        EV  = 1/((Ventana.Focal1.get()/1000))*Ventana.AV1.get()                    # Escala de vuelo
        AIT = (Ventana.AS1.get()*EV)/1000                                          # Ancho de la imagen sobre el terreno en metros
        HIT = (Ventana.HS1.get()*EV)/1000                                          # Alto de la imagen sobre el terreno en metros
        BA  = AIT*(1-(Ventana.SL1.get()/100))                                      # Base area
        DP  = HIT*(1-(Ventana.ST1.get()/100))                                      # Distancia entre pasadas en metros
        IF  = BA/8                                                                 # Intervalo entre fotos
        TF  = 5.2                                                                  # Tiempo entre fotos
        NP  = Ventana.A1.get()/DP                                                  # Numero de pasadas
        NFP = (Ventana.L1.get()/BA)+1                                              # Numero de fotos por pasadas
        NF  = NFP*NP                                                               # Numero de fotos por vuelo
        dV  = (NP*Ventana.L1.get())+Ventana.A1.get()                               # Distancia de  vuelo en metros
        DV  = (NF*IF)/60                                                           # Duracion de vuelo en min
        Ventana.GSD.configure(text=round(GSD,2))
        Ventana.EV.configure(text=round(EV,2))
        Ventana.AIT.configure(text=round(AIT,2))
        Ventana.HIT.configure(text=round(HIT,2))
        Ventana.BA.configure(text=round(BA,0))
        Ventana.DP.configure(text=round(DP,2))
        Ventana.IF.configure(text=round(IF,1))
        Ventana.TF.configure(text=round(TF,1))
        Ventana.NP.configure(text=int(NP))
        Ventana.NFP.configure(text=int(NFP))
        Ventana.NF.configure(text=int(NF))
        Ventana.dV.configure(text=round(dV,2))
        Ventana.DV.configure(text=round(DV,2))
        

Ejecucion=aplication()
