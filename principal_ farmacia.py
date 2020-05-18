from tkinter import*
from tkinter import ttk
import json

with open('farmaciass.json', encoding = 'utf-8') as file:
    lst_farmacias = json.load(file)

def calcular_prov():
    global lst_provincias
    lst_provincias = list()
    for una_prov in lst_farmacias:
        if una_prov['provincia_nombre'] not in lst_provincias:
            lst_provincias.append(una_prov['provincia_nombre'])
    return lst_provincias

def calcular_prom():
    global lst_financiamientos
    lst_financiamientos = list()
    for una_prov in lst_farmacias:
        if una_prov['origen_financiamiento'] not in lst_financiamientos:
            lst_financiamientos.append(una_prov['origen_financiamiento'])
    return lst_financiamientos

ventana = Tk()
ventana.title('Farmacia Fantin')
ventana.geometry('1000x526')
ventana.resizable(0,0)
Canvas(ventana, relief="groove", borderwidth=2, width=993, height=70).place(x=0, y=0)
Canvas(ventana, relief="groove", borderwidth=2, width=993, height=220).place(x=0, y=75)
Canvas(ventana, relief="groove", borderwidth=2, width=993, height=80).place(x=0, y=300)
Canvas(ventana, relief="groove", borderwidth=2, width=993, height=70).place(x=0, y=385)
Canvas(ventana, relief="groove", borderwidth=2, width=993, height=60).place(x=0, y=460)
#Labels Fijos
Label(ventana, text="Ingrese una provincia:", font=("Arial", 12)).place(x=20, y=25)
Label(ventana, text="Cantidad de farmacias:", font=("Arial", 12)).place(x=701, y=25)
Label(ventana, text="ID del establecimiento:", font=("Arial", 12)).place(x=20, y=85)
Label(ventana, text="Nombre:", font=("Arial", 12)).place(x=20, y=125)
Label(ventana, text="Localidad:", font=("Arial", 12)).place(x=20, y=155)
Label(ventana, text="Provincia:", font=("Arial", 12)).place(x=20, y=185)
Label(ventana, text="Departamento:", font=("Arial", 12)).place(x=20, y=215)
Label(ventana, text="Financiamiento:", font=("Arial", 12)).place(x=400, y=125)
Label(ventana, text="Domicilio:", font=("Arial", 12)).place(x=400, y=155)
Label(ventana, text="Codigo Postal Desde:", font=("Arial", 12)).place(x=10, y=315)
Label(ventana, text="Codigo Postal Hasta:", font=("Arial", 12)).place(x=10, y=345)
Label(ventana, text="Cantidad:", font=("Arial", 12)).place(x=670, y=327)
Label(ventana, text="Provincias con mas farmacias cuyo origen de financiamiento sea mutual", font=("Arial", 12)).place(x=10, y=410)
Label(ventana, text="Nombre:", font=("Arial", 12)).place(x=670, y=395)
Label(ventana, text="Cantidad:", font=("Arial", 12)).place(x=670, y=425)
Label(ventana, text="Ingrese una provincia:", font=("Arial", 12)).place(x=10, y=465)
Label(ventana, text="Un financiamiento:", font=("Arial", 12)).place(x=10, y=495)
Label(ventana, text="Cantidad:", font=("Arial", 12)).place(x=650, y=478)
#Lables cambiantes
global lbl_cmb1
lbl_cmb1 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=10)
lbl_cmb1.place(x=881, y=25)
lbl_cmb2 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=28)
lbl_cmb2.place(x=140, y=125)
lbl_cmb3 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=28)
lbl_cmb3.place(x=140, y=155)
lbl_cmb4 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=28)
lbl_cmb4.place(x=140, y=185)
lbl_cmb5 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=28)
lbl_cmb5.place(x=140, y=215)
lbl_cmb6 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=20)
lbl_cmb6.place(x=530, y=125)
lbl_cmb7 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=15)
lbl_cmb7.place(x=781, y=327)
lbl_cmb8 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=22)
lbl_cmb8.place(x=780, y=425)
lbl_cmb9 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=20)
lbl_cmb9.place(x=750, y=478)
lbl_cmb10 = Label(ventana, text="---", font=("Arial", 12), borderwidth=2, relief="groove", bg="white", width=22)
lbl_cmb10.place(x=780, y=395)
#Entrys
primer_entry=Entry(ventana, width=30, relief="groove")
primer_entry.place(x=201, y=88)
segundo_entry=Entry(ventana, width=30, relief="groove")
segundo_entry.place(x=180, y=317)
tercer_entry=Entry(ventana, width=30, relief="groove")
tercer_entry.place(x=180, y=347)
#Lisbox
global list_box1
list_box1 = Label(ventana, text="---", width=40, height=6, font=("Arial", 12), borderwidth=2, relief="groove", bg="white")
list_box1.place(x=530, y=155)
#Comboboxes
global combo_provincias
global combo_provincias2
global combo_financiamientos
combo_provincias = ttk.Combobox(ventana, width = 30)
combo_provincias.configure(values=calcular_prov())
combo_provincias.place(x=201, y=26)
combo_provincias2 = ttk.Combobox(ventana, width = 30)
combo_provincias2.configure(values=calcular_prov())
combo_provincias2.place(x=170, y=468)
combo_financiamientos = ttk.Combobox(ventana, width = 30)
combo_financiamientos.configure(values=calcular_prom())
combo_financiamientos.place(x=170, y=498)
#Funciones
def buscar_datos():
    p_entry = primer_entry.get()
    for un_id in lst_farmacias:
        if p_entry == un_id['establecimiento_id']:
            lbl_cmb2.config(text=un_id['establecimiento_nombre'])
            lbl_cmb3.config(text=un_id['localidad_nombre'])
            lbl_cmb4.config(text=un_id['provincia_nombre'])
            lbl_cmb5.config(text=un_id['departamento_nombre'])
            lbl_cmb6.config(text=un_id['origen_financiamiento'])
            list_box1.config(text=un_id['domicilio'])

def calcular_farm():
    selec_prov = combo_provincias.get()
    contador = 0
    for una_farm in lst_farmacias:
        if una_farm['provincia_nombre'] == selec_prov:
            contador+=1
    lbl_cmb1.config(text=contador)
    return contador

def cp():
    desde = int(segundo_entry.get())
    hasta = int(tercer_entry.get())
    contador = 0
    for una_farm in lst_farmacias:
        if int(una_farm['cp'])>=desde and int(una_farm['cp'])<=hasta:
            contador+=1
    lbl_cmb7.config(text=contador)
    return contador

def mutual():
    cont_bsas = 0
    cont_caba = 0
    for una_farm in lst_farmacias:
        if una_farm['origen_financiamiento'] == "Mutual":
            if una_farm['provincia_nombre'] == "BUENOS AIRES":
                cont_bsas+=1
            else:
                cont_caba+=1
    if cont_bsas>cont_caba:
        lbl_cmb8.config(text=cont_bsas)
        lbl_cmb10.config(text="BUENOS AIRES")
    else:
        lbl_cmb8.config(text=cont_caba)
        lbl_cmb10.config(text="CABA")

def promedio():
    prov = combo_provincias2.get()
    financia = combo_financiamientos.get()
    departamentos = list()
    cont = 0
    for una_farm in lst_farmacias:
        if una_farm['provincia_nombre'] == prov:
            if una_farm['departamento_nombre'] not in departamentos:
                departamentos.append(una_farm['departamento_nombre'])
    cont = 0
    for una_farm in lst_farmacias:
        if una_farm['provincia_nombre'] == prov and una_farm['origen_financiamiento'] == financia:
            cont+=1
    prome = cont/len(departamentos)
    lbl_cmb9.config(text=prome)

#Botones
Button(ventana, text="Calcular", cursor="hand2", borderwidth=3, relief="ridge", width=30, command=calcular_farm).place(x=451, y=23)
Button(ventana, text="Buscar", cursor="hand2", borderwidth=3, relief="ridge", width=30, command=buscar_datos).place(x=411, y=83)
Button(ventana, text="Buscar", cursor="hand2", borderwidth=3, relief="ridge", width=30, command=cp).place(x=411, y=327)
Button(ventana, text="Buscar", cursor="hand2", borderwidth=3, relief="ridge", width=15, command=mutual).place(x=540, y=408)
Button(ventana, text="Promedio Por Departamento", cursor="hand2", borderwidth=3, relief="ridge", width=30, command=promedio).place(x=400, y=478)

calcular_prov()
calcular_prom()

ventana.mainloop()