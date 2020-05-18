#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json

with open ('farmacias.json', encoding = 'utf-8') as file:
    Lista_farm = json.load(file)

#Creación Tk
ventana = Tk()
ventana.geometry('1280x800')
ventana.title('Farmacia')
ventana.configure(bg='light gray')

#Funciones
def Cantidad_Farmacias_por_Prov():
    contador=0
    for farmacia in Lista_farm:
        if farmacia['provincia_nombre'] == entry_ingr_prov_var.get():
            contador+=1
    entry_cant_farm_var.set(contador)    
    
def Datos_por_establecimiento():
    for farmacia in Lista_farm:
        if farmacia["establecimiento_id"]==entry_ingr_id_var.get():
            entry_nombre_var.set(farmacia['establecimiento_nombre'])
            entry_loc_var.set(farmacia['localidad_nombre'])
            entry_prov_var.set(farmacia['provincia_nombre'])
            entry_dep_var.set(farmacia['departamento_nombre'])
            entry_financ_var.set(farmacia['origen_financiamiento'])
            entry_dom_var.set(farmacia['domicilio'])
        break
        
def Cantidad_Farmacias_desde_xCP_hasta_yCP():
    contador=0
    for farmacia in Lista_farm:
        if int(farmacia['cp'])>=int(entry_cp_dsd_var.get()) and int(farmacia['cp'])<=int(entry_cp_hast_var.get()):
            contador+=1
    entry_cant_var.set(contador)

def provincia_con_mas_farmacias_mutual():
    lista_auxiliar=[[],[]]
    for farmacia in Lista_farm:
        if farmacia['provincia_nombre'] not in lista_auxiliar[0]:
            lista_auxiliar[0].append(farmacia['provincia_nombre'])
            lista_auxiliar[1].append(0)
    for farmacia in Lista_farm:
        if farmacia['origen_financiamiento']=='Mutual':
            indice=lista_auxiliar[0].index(farmacia['provincia_nombre'])
            lista_auxiliar[1][indice]+=1
            
    max_farm_indice = lista_auxiliar[1].index(max(lista_auxiliar[1]))
    entry_name_var.set(lista_auxiliar[0][max_farm_indice])
    entry_cant_farm_var_.set(lista_auxiliar[1][max_farm_indice])         
    
def Promedio_por_Dep():
    lista_contadora = [[],[]]
    for farmacia in Lista_farm:
        if farmacia['provincia_nombre']==entry_prov_name_var.get() and farmacia['origen_financiamiento']==financ_var.get():
            lista_contadora[0].append(farmacia)
    for farmacia in Lista_farm:
        if farmacia['provincia_nombre']==entry_prov_name_var.get():
            lista_contadora[1].append(farmacia)
    lista_auxiliar = [[],[],[]]
    for farmacia in lista_contadora[1]:
        if farmacia['departamento_nombre'] not in lista_auxiliar[2]:
            lista_auxiliar[2].append(farmacia['departamento_nombre'])
    for farmacia in lista_contadora[0]:
        if farmacia['departamento_nombre'] not in lista_auxiliar[0]:
            lista_auxiliar[0].append(farmacia['departamento_nombre'])
            lista_auxiliar[1].append(1)
        elif farmacia['departamento_nombre'] in lista_auxiliar[0]:
            for i in lista_auxiliar[0]:
                if i == farmacia['departamento_nombre']:
                    indice=lista_auxiliar[0].index(i)
                    lista_auxiliar[1][indice]+=1
    promedio = sum(lista_auxiliar[1])/len(lista_auxiliar[2])
    cant_var.set(round(promedio,2))                         
        
#Interfaz:
imagen_top = Image.open(r'C:\Users\brian\Downloads\farmacia1.png')
resized = imagen_top.resize((1280,150),Image.ANTIALIAS)
farmacia = ImageTk.PhotoImage(resized, master=ventana)
label_img = Label(ventana, image = farmacia, bd=2)
label_img.pack()
label_img.image = farmacia
    #     Top: calcular cantidad de farmacia x prov 
frame_cf = Frame(ventana, width=1280, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_cf.pack()
        #Labels:   
lbl_ingr_prov = Label(frame_cf, text='Ingrese una provincia:', width=20, height=2, bg='light gray').place(x=150, y=70)
lbl_cant_farm = Label(frame_cf, text='Cantidad de farmacias:', width=20, height=2, bg='light gray').place(x=830, y=70)
        #Entrys:
entry_ingr_prov_var = StringVar(frame_cf)
entry_ingr_prov = Entry(frame_cf, relief=SUNKEN, bg= 'light gray', bd=3,textvariable=entry_ingr_prov_var)
entry_ingr_prov.place(x=320, y=70,width=150,height=35)
entry_cant_farm_var = IntVar(frame_cf)
entry_cant_farm = Entry(frame_cf, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_farm_var)
entry_cant_farm.place(x=975, y=70,width=150,height=35)
        #Button:
btn_calcular = Button(frame_cf, text='Calcular', width=8, height=2, bg='light gray',command=Cantidad_Farmacias_por_Prov).place(x=630,y=65)
    #Top: Busqueda mediante ID 
frame_busc = Frame(ventana, width=1280, height=200, relief=SUNKEN, bg='light gray', bd=3)
frame_busc.pack()
        #labels izquierda
lbl_ingr_id = Label(frame_busc, text='Establecimiento_id:', width=20, height=2, bg='light gray').place(x=150, y=20)
lbl_nombre = Label(frame_busc, text='Nombre:', width=15, height=1, bg='light gray',bd=2).place(x=170, y=55)
lbl_loc = Label(frame_busc, text='Localidad:', width=15, height=1, bg='light gray').place(x=170, y=85)
lbl_prov = Label(frame_busc, text='Provincia:', width=15, height=1, bg='light gray').place(x=170, y=115)
lbl_dep = Label(frame_busc, text='Departamento:', width=15, height=1, bg='light gray').place(x=170, y=145)
lbl_financ = Label(frame_busc, text='Financiamiento:', width=15, height=1, bg='light gray',bd=2).place(x=830, y=55)
lbl_dom =  Label(frame_busc, text='Domicilio:', width=15, height=1, bg='light gray',bd=1).place(x=830, y=85)
        #Entrys de labels
entry_ingr_id_var = StringVar(frame_busc)
entry_ingr_id = Entry(frame_busc, relief=SUNKEN, bg= 'light gray', bd=2, textvariable=entry_ingr_id_var)
entry_ingr_id.place(x=320, y=18,width=150,height=27)
entry_nombre_var = StringVar(frame_busc)
entry_nombre = Entry(frame_busc, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_nombre_var)
entry_nombre.place(x=320, y=50,width=150,height=27)
entry_loc_var = StringVar(frame_busc)
entry_loc = Entry(frame_busc, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_loc_var)
entry_loc.place(x=320, y=82,width=150,height=27)
entry_prov_var = StringVar(frame_busc)
entry_prov = Entry(frame_busc, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_prov_var)
entry_prov.place(x=320, y=114,width=150,height=27)
entry_dep_var = StringVar(frame_busc)
entry_dep = Entry(frame_busc, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_dep_var)
entry_dep.place(x=320, y=146,width=150,height=27)
entry_financ_var = StringVar(frame_busc)
entry_financ = Entry(frame_busc, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_financ_var)
entry_financ.place(x=975, y=52,width=100,height=20)
entry_dom_var = StringVar(frame_busc)
entry_dom = Entry(frame_busc, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_dom_var)
entry_dom.place(x=975, y=90,width=200,height=70)
        #Button
btn_buscar_id = Button(frame_busc, text='→ Buscar ←', width=8, height=2, bg='light gray', command=Datos_por_establecimiento).place(x=630, y=85)
    #Top: calculo de CP:
frame_calc_cp = Frame(ventana, width=1280, height=130, relief=SUNKEN, bg='light gray', bd=3)
frame_calc_cp.pack()
        #Labels:
lbl_cp_dsd = Label(frame_calc_cp, text='Código Postal desde:', width=15, height=2, bg='light gray').place(x=170, y=10)
lbl_cp_hast = Label(frame_calc_cp, text='Código Postal hasta:', width=15, height=2, bg='light gray').place(x=170, y=50)
lbl_cant = Label(frame_calc_cp, text='Cantidad:', width=15, height=2, bg='light gray').place(x=830, y=25)
        #Entrys:
entry_cp_dsd_var = StringVar(frame_calc_cp)
entry_cp_dsd= Entry(frame_calc_cp, relief=SUNKEN, bg= 'light gray', bd=2, textvariable=entry_cp_dsd_var)
entry_cp_dsd.place(x=320, y=10,width=150,height=27)
entry_cp_hast_var = StringVar(frame_calc_cp)
entry_cp_hast = Entry(frame_calc_cp, relief=SUNKEN, bg= 'light gray', bd=2, textvariable=entry_cp_hast_var)
entry_cp_hast.place(x=320, y=55,width=150,height=27)
entry_cant_var = StringVar(frame_calc_cp)
entry_cant = Entry(frame_calc_cp, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_cant_var)
entry_cant.place(x=975, y=25,width=150,height=27)
        #Button:
btn_calc_cp = Button(frame_calc_cp, text='Calcular', width=8, height=2, bg='light grey', command=Cantidad_Farmacias_desde_xCP_hasta_yCP).place(x=630, y=25)   
    #Top calc de farmacias (x prov) que sean del estado:
frame_calc_farm_est = Frame(ventana, width=1280, height=100, relief=SUNKEN, bg='light gray', bd=3)
frame_calc_farm_est.pack()
        #Label:
lbl_req = Label(frame_calc_farm_est, text='Provincia con más farmacias cuyo\n       origen de Financiamiento sea "Mutual":', bg='light grey', bd=2).place(x=150, y=40)
lbl_name = Label(frame_calc_farm_est, text='Nombre:', width=15, height=2, bg='light gray').place(x=830, y=15)
lbl_cant_farm = Label(frame_calc_farm_est, text='Cantidad:', width=15, height=2, bg='light gray').place(x=830, y=50)
        #Entrys:
entry_name_var = StringVar(frame_calc_farm_est)
entry_name = Entry(frame_calc_farm_est, relief=SUNKEN, bg= 'light gray', bd=2, text=entry_name_var)
entry_name.place(x=975, y=15,width=150,height=27)
entry_cant_farm_var_ = StringVar(frame_calc_farm_est)
entry_cant_farm = Entry(frame_calc_farm_est, relief=SUNKEN, bd=2, state=DISABLED, textvariable=entry_cant_farm_var_)
entry_cant_farm.place(x=975, y=50,width=150,height=27)
        #Button:
btn_calc_cp_ = Button(frame_calc_farm_est, text='Calcular', width=8, height=2, bg='light grey', command=provincia_con_mas_farmacias_mutual).place(x=630, y=25)
    #Top promedio por departamento de prov (elegiendo un tipo de Financiamiento)
frame_prom = Frame(ventana, width=1280, height=100, relief=SUNKEN, bg='light gray', bd=3)
frame_prom.pack()
        #Labels:
lbl_ing_prov = Label(frame_prom, text=' Ingrese una provincia:', width=15, height=2, bg='light grey').place(x=170, y=10)
lbl_tip_fin = Label(frame_prom, text='Ingrese un Financiamiento:', width=20, height=2, bg='light gray').place(x=166, y=45)
lbl_cant_prom = Label(frame_prom, text='Cantidad:', width=15, height=2, bg='light gray').place(x=830, y=25)
#         #Entry:
cant_var=IntVar(frame_prom)
entry_cant = Entry(frame_prom, relief=SUNKEN, bg= 'light gray', bd=2, state = DISABLED, textvariable=cant_var)
entry_cant.place(x=975, y=25,width=150,height=27)
entry_prov_name_var=StringVar(frame_prom)
entry_prov_name = Entry(frame_prom, relief=SUNKEN, bg= 'light gray', bd=2, textvariable=entry_prov_name_var)
entry_prov_name.place(x=310, y=10,width=150,height=27)

#         #Combobox:
financ_var = StringVar(frame_prom)
cmb = ttk.Combobox(frame_prom, values=['Mutual','Privado'], textvariable=financ_var)
cmb.place(x=320, y=55)
#         #Button
btn_calc_cp = Button(frame_prom, text='Promedio por Departamento ', width=25, height=2, bg='light gray', command=Promedio_por_Dep).place(x=570, y=25)

ventana.mainloop()


# In[ ]:




