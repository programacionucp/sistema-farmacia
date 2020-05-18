from tkinter import *
from tkinter import messagebox
import json
import futbol_support
with open("Equipos.json", encoding = 'utf-8') as archivo:
    listaEquipos = json.load(archivo)

listaNombre_equipo = []  #Lista de Strings que sirve para mostrar los equipos en la Listbox.
listaDatos = []  #Lista de Strings que sirve para mostrar los datos del equipo en la Listbox.
equipo1 = listaEquipos[0]
equipo2 = listaEquipos[1]
equipo3 = listaEquipos[2]
equipo4 = listaEquipos[3]
equipo5 = listaEquipos[4]

listaModificable = listaEquipos

def guardar ():
    with open ("Equipos.json","w") as archivo:
        json.dump(listaEquipos,archivo)

def ventana_cargar_equipos(top,equipos,datos,Yequipo1_n,Yequipo2_n,Yequipo3_n,Yequipo4_n,Yequipo5_n,Xequipo1_n,Xequipo2_n,Xequipo3_n,Xequipo4_n,Xequipo5_n):
    global listaModificable
    ventanaCargar = Toplevel(top)
    ventanaCargar.geometry("400x230")
    ventanaCargar.title("Cargar Equipos")
    lblEquipo1 = Label(ventanaCargar, text="Equipo 1:", font=("Arial Bold", 16))
    lblEquipo1.place(x=10, y=20)
    txtEquipo1 = Entry(ventanaCargar)
    txtEquipo1.place(x=200, y=25)

    lblEquipo2 = Label(ventanaCargar, text="Equipo 2:", font=("Arial Bold", 16))
    lblEquipo2.place(x=10, y=50)
    txtEquipo2 = Entry(ventanaCargar)
    txtEquipo2.place(x=200, y=55)

    lblEquipo3 = Label(ventanaCargar, text="Equipo 3:", font=("Arial Bold", 16))
    lblEquipo3.place(x=10, y=80)
    txtEquipo3 = Entry(ventanaCargar)
    txtEquipo3.place(x=200, y=85)

    lblEquipo4 = Label(ventanaCargar, text="Equipo 4:", font=("Arial Bold", 16))
    lblEquipo4.place(x=10, y=110)
    txtEquipo4 = Entry(ventanaCargar)
    txtEquipo4.place(x=200, y=115)

    lblEquipo5 = Label(ventanaCargar, text="Equipo 5:", font=("Arial Bold", 16))
    lblEquipo5.place(x=10, y=140)
    txtEquipo5 = Entry(ventanaCargar)
    txtEquipo5.place(x=200, y=145)

    def guardarEquipo():
        N_equipo1 = txtEquipo1.get()
        N_equipo2 = txtEquipo2.get()
        N_equipo3 = txtEquipo3.get()
        N_equipo4 = txtEquipo4.get()
        N_equipo5 = txtEquipo5.get()
        equipo1 = listaEquipos[0]
        if N_equipo1 == "" or N_equipo2 == "" or N_equipo3 == "" or N_equipo4 == "" or N_equipo5 == "":
            messagebox.showerror(message="Debe rellenar todos los campos", title="Error")
        else:
            equipo1["Equipo"] = N_equipo1
            equipo1["Puntos"] = 0
            equipo1["Jugados"] = 0
            equipo1["Ganados"] = 0
            equipo1["Empatados"] = 0
            equipo1["Perdidos"] = 0
            equipo1["Goles a Favor"] = 0
            equipo1["En Contra"] = 0

            equipo2["Equipo"] = N_equipo2
            equipo2["Puntos"] = 0
            equipo2["Jugados"] = 0
            equipo2["Ganados"] = 0
            equipo2["Empatados"] = 0
            equipo2["Perdidos"] = 0
            equipo2["Goles a Favor"] = 0
            equipo2["En Contra"] = 0

            equipo3["Equipo"] = N_equipo3
            equipo3["Puntos"] = 0
            equipo3["Jugados"] = 0
            equipo3["Ganados"] = 0
            equipo3["Empatados"] = 0
            equipo3["Perdidos"] = 0
            equipo3["Goles a Favor"] = 0
            equipo3["En Contra"] = 0

            equipo4["Equipo"] = N_equipo4
            equipo4["Puntos"] = 0
            equipo4["Jugados"] = 0
            equipo4["Ganados"] = 0
            equipo4["Empatados"] = 0
            equipo4["Perdidos"] = 0
            equipo4["Goles a Favor"] = 0
            equipo4["En Contra"] = 0

            equipo5["Equipo"] = N_equipo5
            equipo5["Puntos"] = 0
            equipo5["Jugados"] = 0
            equipo5["Ganados"] = 0
            equipo5["Empatados"] = 0
            equipo5["Perdidos"] = 0
            equipo5["Goles a Favor"] = 0
            equipo5["En Contra"] = 0

            listarEquipos()
            equipos.set(listaNombre_equipo)
            datos.set(listaDatos)
            Yequipo1_n.configure(text=N_equipo1)
            Yequipo2_n.configure(text=N_equipo2)
            Yequipo3_n.configure(text=N_equipo3)
            Yequipo4_n.configure(text=N_equipo4)
            Yequipo5_n.configure(text=N_equipo5)
            Xequipo1_n.configure(text=N_equipo1)
            Xequipo2_n.configure(text=N_equipo2)
            Xequipo3_n.configure(text=N_equipo3)
            Xequipo4_n.configure(text=N_equipo4)
            Xequipo5_n.configure(text=N_equipo5)
            futbol_support.w.btnRegistrar_partido.configure(state='normal')
            futbol_support.w.btnCargar_equipos.configure(state="disable")
            ventanaCargar.destroy()
            guardar()
            listaModificable = listaEquipos


    btnGuardar = Button(ventanaCargar,text="GUARDAR", command=guardarEquipo)
    btnGuardar.place(x=200, y=200)

def listarEquipos():
    global listaNombre_equipo, listaDatos, listaModificable

    listaOrdenada = sorted(listaModificable, key=lambda user: user['Puntos'], reverse=True)

    primero = listaOrdenada[0]
    segundo = listaOrdenada[1]
    tercero = listaOrdenada[2]
    cuarto = listaOrdenada[3]
    quinto = listaOrdenada[4]

    listaNombre_equipo.append(primero["Equipo"])
    txtE1 = (str(primero["Puntos"]) + "        " + str(primero["Jugados"]) + "          " + str(primero["Ganados"]) +
                      "            " + str(primero["Empatados"]) + "            " + str(primero["Perdidos"]) + "          " + str(primero["Goles a Favor"]) +
                      "           " + str(primero["En Contra"]))
    listaDatos.append(txtE1)

    listaNombre_equipo.append(segundo["Equipo"])
    txtE2 = (str(segundo["Puntos"]) + "        " + str(segundo["Jugados"]) + "          " + str(segundo["Ganados"]) +
        "            " + str(segundo["Empatados"]) + "            " + str(segundo["Perdidos"]) + "          " + str(segundo["Goles a Favor"]) +
        "           " + str(segundo["En Contra"]))
    listaDatos.append(txtE2)

    listaNombre_equipo.append(tercero["Equipo"])
    txtE3 = (str(tercero["Puntos"]) + "        " + str(tercero["Jugados"]) + "          " + str(tercero["Ganados"]) +
        "            " + str(tercero["Empatados"]) + "            " + str(tercero["Perdidos"]) + "          " + str(tercero["Goles a Favor"]) +
        "           " + str(tercero["En Contra"]))
    listaDatos.append(txtE3)

    listaNombre_equipo.append(cuarto["Equipo"])
    txtE4 = (str(cuarto["Puntos"]) + "        " + str(cuarto["Jugados"]) + "          " + str(cuarto["Ganados"]) +
        "            " + str(cuarto["Empatados"]) + "            " + str(cuarto["Perdidos"]) + "          " + str(cuarto["Goles a Favor"]) +
        "           " + str(cuarto["En Contra"]))
    listaDatos.append(txtE4)

    listaNombre_equipo.append(quinto["Equipo"])
    txtE5 = (str(quinto["Puntos"]) + "        " + str(quinto["Jugados"]) + "          " + str(quinto["Ganados"]) +
        "            " + str(quinto["Empatados"]) + "            " + str(quinto["Perdidos"]) + "          " + str(quinto["Goles a Favor"]) +
        "           " + str(quinto["En Contra"]))
    listaDatos.append(txtE5)

def ventana_partido(top, datos, nombres):
    ventanaPartido = Toplevel(top)
    ventanaPartido.geometry("400x230")
    ventanaPartido.title("Cargar Partido")
    lblTitulo = Label(ventanaPartido, text="Seleccione los equipos que jugarán", font=("Arial Bold", 16))
    lblTitulo.place(x=30, y=5)
    seleccion = IntVar()
    radE1_1 = Radiobutton(ventanaPartido,text=equipo1["Equipo"], value=1, variable=seleccion)
    radE1_1.place(x=10, y=50)
    radE2_1 = Radiobutton(ventanaPartido, text=equipo2["Equipo"], value=2, variable=seleccion)
    radE2_1.place(x=10, y=70)
    radE3_1 = Radiobutton(ventanaPartido, text=equipo3["Equipo"], value=3, variable=seleccion)
    radE3_1.place(x=10, y=90)
    radE4_1 = Radiobutton(ventanaPartido, text=equipo4["Equipo"], value=4, variable=seleccion)
    radE4_1.place(x=10, y=110)
    radE5_1 = Radiobutton(ventanaPartido, text=equipo5["Equipo"], value=5, variable=seleccion)
    radE5_1.place(x=10, y=130)

    lblVS = Label(ventanaPartido, text="VS", font=("Arial Bold", 16))
    lblVS.place(x=170, y=80)

    seleccion2 = IntVar()
    radE1_2 = Radiobutton(ventanaPartido, text=equipo1["Equipo"], value=1, variable=seleccion2)
    radE1_2.place(x=320, y=50)
    radE2_2 = Radiobutton(ventanaPartido, text=equipo2["Equipo"], value=2, variable=seleccion2)
    radE2_2.place(x=320, y=70)
    radE3_2 = Radiobutton(ventanaPartido, text=equipo3["Equipo"], value=3, variable=seleccion2)
    radE3_2.place(x=320, y=90)
    radE4_2 = Radiobutton(ventanaPartido, text=equipo4["Equipo"], value=4, variable=seleccion2)
    radE4_2.place(x=320, y=110)
    radE5_2 = Radiobutton(ventanaPartido, text=equipo5["Equipo"], value=5, variable=seleccion2)
    radE5_2.place(x=320, y=130)

    def aceptar():
        primer_equipo = seleccion.get()
        segundo_equipo = seleccion2.get()
        if primer_equipo == segundo_equipo:
            messagebox.showerror('Error', 'Un equipo no puede jugar consigo mismo')
        else:
            ventanaPartido.destroy()
            ventana_goles(top,primer_equipo,segundo_equipo, datos, nombres)

    btnAceptar = Button(ventanaPartido,text="Aceptar", command=aceptar)
    btnAceptar.place(x=160, y=170)

def ventana_goles(top,primer_equipo,segundo_equipo, datos, nombres):
    ventanaGoles = Toplevel(top)
    ventanaGoles.geometry("400x280")
    ventanaGoles.title("Cargar Goles")
    def aceptar(E1,E2,FavorE1,FavorE2,boton,lbl_golE1,lbl_golE2):
        global listaModificable
        golFavorE1 = int(FavorE1.get())
        golFavorE2 = int(FavorE2.get())
        boton.destroy()
        totalGolesE1 = golFavorE1
        totalGolesE2 = golFavorE2
        if totalGolesE1 > totalGolesE2:
            puntosE1 = 3
            puntosE2 = 0
            ganadoE1 = 1
            ganadoE2 = 0
            empateE1 = 0
            empateE2 = 0
            perdidoE1 = 0
            perdidoE2 = 1
        elif totalGolesE2 > totalGolesE1:
            puntosE1 = 0
            puntosE2 = 3
            ganadoE1 = 0
            ganadoE2 = 1
            empateE1 = 0
            empateE2 = 0
            perdidoE1 = 1
            perdidoE2 = 0
        elif totalGolesE1 == totalGolesE2:
            puntosE1 = 1
            puntosE2 = 1
            ganadoE1 = 0
            ganadoE2 = 0
            empateE1 = 0
            empateE1 = 1
            empateE2 = 1
            perdidoE1 = 0
            perdidoE2 = 0

        E1["Puntos"] += puntosE1
        E2["Puntos"] += puntosE2
        E1["Jugados"] += 1
        E2["Jugados"] += 1
        E1["Ganados"] += ganadoE1
        E2["Ganados"] += ganadoE2
        E1["Empatados"] += empateE1
        E2["Empatados"] += empateE2
        E1["Perdidos"] += perdidoE1
        E2["Perdidos"] += perdidoE2
        E1["Goles a Favor"] += golFavorE1
        E2["Goles a Favor"] += golFavorE2
        E1["En Contra"] += totalGolesE2
        E2["En Contra"] += totalGolesE1

        lblResultado = Label(ventanaGoles, text="Resultado", font=("Arial Bold", 17))
        lblResultado.place(x=140, y=150)
        lblGoles = Label(ventanaGoles, text=str(E1["Equipo"]) + "(" + str(totalGolesE1) + ")" + " - " + str(E2["Equipo"])
                         + "(" + str(totalGolesE2) + ")",font=("Arial Bold", 16))
        lblGoles.place(x=100, y=190)
        guardar()
        listaModificable = listaEquipos
        actualizarLista(datos,nombres)

        if lbl_golE1.cget("text") == "-":
            lbl_golE1.configure(text=totalGolesE1)
        else:
            golesE1 = int(lbl_golE1.cget("text"))
            golesE1 += totalGolesE1
            lbl_golE1.configure(text=golesE1)

        if lbl_golE2.cget("text") == "-":
            lbl_golE2.configure(text=totalGolesE2)
        else:
            golesE2 = int(lbl_golE2.cget("text"))
            golesE2 += totalGolesE2
            lbl_golE2.configure(text=golesE2)

    def labels_goles(E1,E2,lbl_golE1,lbl_golE2):
        lblEquipo1 = Label(ventanaGoles, text=E1["Equipo"], font=("Arial Bold", 17))
        lblEquipo1.place(x=170, y=10)
        lblEquipo2 = Label(ventanaGoles, text=E2["Equipo"], font=("Arial Bold", 17))
        lblEquipo2.place(x=300, y=10)
        lblGolFavor = Label(ventanaGoles, text="Goles a favor:", font=("Arial Bold", 14))
        lblGolFavor.place(x=5, y=80)

        txtGolFavorE1 = Entry(ventanaGoles, width=10)
        txtGolFavorE1.place(x=173, y=85)
        txtGolFavorE2 = Entry(ventanaGoles, width=10)
        txtGolFavorE2.place(x=303, y=85)

        btnAceptar = Button(ventanaGoles, text="Aceptar",
                            command=lambda: aceptar(E1,E2,txtGolFavorE1, txtGolFavorE2,btnAceptar,lbl_golE1,lbl_golE2))
        btnAceptar.place(x=240, y=150)

    if primer_equipo == 1 and segundo_equipo == 2:
        labels_goles(equipo1,equipo2,futbol_support.w.lbl1v2,futbol_support.w.lbl2v1)
    elif primer_equipo == 1 and segundo_equipo == 3:
        labels_goles(equipo1,equipo3,futbol_support.w.lbl1v3,futbol_support.w.lbl3v1)
    elif primer_equipo == 1 and segundo_equipo == 4:
        labels_goles(equipo1, equipo4,futbol_support.w.lbl1v4,futbol_support.w.lbl4v1)
    elif primer_equipo == 1 and segundo_equipo == 5:
        labels_goles(equipo1,equipo5,futbol_support.w.lbl1v5,futbol_support.w.lbl5v1)
    elif primer_equipo == 2 and segundo_equipo == 1:
        labels_goles(equipo2,equipo1,futbol_support.w.lbl2v1,futbol_support.w.lbl1v2)
    elif primer_equipo == 2 and segundo_equipo == 3:
        labels_goles(equipo2,equipo3,futbol_support.w.lbl2v3,futbol_support.w.lbl3v2)
    elif primer_equipo == 2 and segundo_equipo == 4:
        labels_goles(equipo2,equipo4,futbol_support.w.lbl2v4,futbol_support.w.lbl4v2)
    elif primer_equipo == 2 and segundo_equipo == 5:
        labels_goles(equipo2,equipo5,futbol_support.w.lbl2v5,futbol_support.w.lbl5v2)
    elif primer_equipo == 3 and segundo_equipo == 1:
        labels_goles(equipo3,equipo1,futbol_support.w.lbl3v1,futbol_support.w.lbl1v3)
    elif primer_equipo == 3 and segundo_equipo == 2:
        labels_goles(equipo3,equipo2,futbol_support.w.lbl3v2,futbol_support.w.lbl2v3)
    elif primer_equipo == 3 and segundo_equipo == 4:
        labels_goles(equipo3,equipo4,futbol_support.w.lbl3v4,futbol_support.w.lbl4v3)
    elif primer_equipo == 3 and segundo_equipo == 5:
        labels_goles(equipo3,equipo5,futbol_support.w.lbl3v5,futbol_support.w.lbl5v3)
    elif primer_equipo == 4 and segundo_equipo == 1:
        labels_goles(equipo4,equipo1,futbol_support.w.lbl4v1,futbol_support.w.lbl1v4)
    elif primer_equipo == 4 and segundo_equipo == 2:
        labels_goles(equipo5,equipo2,futbol_support.w.lbl4v2,futbol_support.w.lbl2v4)
    elif primer_equipo == 4 and segundo_equipo == 3:
        labels_goles(equipo4,equipo3,futbol_support.w.lbl4v3,futbol_support.w.lbl3v4)
    elif primer_equipo == 4 and segundo_equipo == 5:
        labels_goles(equipo4,equipo5,futbol_support.w.lbl4v5,futbol_support.w.lbl5v4)
    elif primer_equipo == 5 and segundo_equipo == 1:
        labels_goles(equipo5,equipo1,futbol_support.w.lbl5v1,futbol_support.w.lbl1v5)
    elif primer_equipo == 5 and segundo_equipo == 2:
        labels_goles(equipo5,equipo2,futbol_support.w.lbl5v2,futbol_support.w.lbl2v5)
    elif primer_equipo == 5 and segundo_equipo == 3:
        labels_goles(equipo5,equipo3,futbol_support.w.lbl5v3,futbol_support.w.lbl3v5)
    elif primer_equipo == 5 and segundo_equipo == 4:
        labels_goles(equipo5,equipo4,futbol_support.w.lbl5v4,futbol_support.w.lbl4v5)

def actualizarLista(datos,nombres):
    global listaNombre_equipo, listaDatos
    listaNombre_equipo.clear()
    listaDatos.clear()
    listarEquipos()
    datos.set(listaDatos)
    nombres.set(listaNombre_equipo)

