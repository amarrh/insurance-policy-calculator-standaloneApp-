import math
from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter.tix import *
from tkinter import font
from pyscreenshot import grab
from PIL import Image
import os
from pathlib import Path
from resizeimage import resizeimage

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

def defocus(event):
    event.widget.master.focus_set()
#-------------------------------TITLE I POSTAVKE------------------------------------------------------------------------
root=Tk()
root.title("Obračun registracije vozila")

root.configure(background='#e6e6e6')
root.iconbitmap('icons/grawe.ico')
bigfont = font.Font(family="Arial",size=11)
root.option_add("*Font", bigfont)

button2 = PhotoImage(file='icons/save.png')
button3 = PhotoImage(file='icons/print.png')
edit = PhotoImage(file='icons/edit.png')

global newWindow, newWindow1, year_, labelPolica, labelPut60, labelPut40, labelPorez, labelTehnicki, labelPomoc, dodatak, \
       labelZeleni, labelTaksa, labelZastita, labelPotvrdaVl, labelPotvrdaReg, labelStiker, labelRegTab, labelKomUg, \
       labelOkolis, labelFond, labelProvizija, labelCijena, terensko, terenskoV, taxi, taxiV, rentV, rent, kombi, kombiTeret, \
       invalid, ug, label42, ugV, potvrdaVLV, potvrdaRegV, sedlastiTeg, label8, vrTer, label9, nosTer, label10, brOs,\
       label11, maxNos, potvrdaoreg, potvrdaovl, zapaljivi, labeltkstT, labeltkstT1, vrPrik, nosPrik, brOsPrik, kolicaV, \
       maxNosPrik, kat, kolica, rvi, labeltkstM, labeltkstM1, t, p, pr, m, zastavicaP, regz, vlz, polica, rviV, da, db, \
       tehnicki, zeleniKarton, putarina60, putarina40, zastitaVoda, fond, pomocPut, taksa, potvrdaVl, potvrdaReg, an, \
       stiker, regTab, komUg, provizijaB, porez, kombiV, kombiTeretV, invalidV, zeleniK, pravno, okolis, cijena, label401, \
       vrstaGor, label5, zapaljiviPrV, zapaljiviPrV1, godProz, bonus, label6, label7,  sedlasti, zapaljiviV, zast

zast = False
t = False
p = False
pr = False
m = False
regz = False
vlz = False
zastavicaP = False
year_ = date.today().year
sedlasti = IntVar()
potvrdaRegV = IntVar()
potvrdaVlV = IntVar()
terenskoV = IntVar()
taxiV = IntVar()
rentV = IntVar()
kombiV = IntVar()
kombiTeretV = IntVar()
invalidV = IntVar()
pravnoV = IntVar()
kolicaV = IntVar()
rviV = IntVar()
ugV = IntVar()
zapaljiviV = IntVar()
zapaljiviPrV = IntVar()
zapaljiviPrV1 = IntVar()
dodatak = int()
check = PhotoImage(file='icons/check.png')
#----------------------------------------FRAME--------------------------------------------------------------------------
frame = Frame(root, height=400, width=300, bg='#017a3d', bd='2')

logo=PhotoImage(file='icons/grawe.png')
lbl_image = Label(frame, image=logo)
frame.pack(fill=X)
lbl_image.pack(padx=35, side=LEFT)
label=Label(frame, text="   OBRAČUN REGISTRACIJE VOZILA", bg='#017a3d', fg='white') #probati sa colonom
label.config(font=("Arial", 20))
label.pack(side=LEFT)

ime = StringVar()
brTel = StringVar()
adr = StringVar()

#--------------------------------------PARAMETRI------------------------------------------------------------------------
label1=Label(root, text="Vrsta registracije:", bg="#e6e6e6", fg="#222")
label1.place(x=20, y=65)
label1.config(font=("Arial", 12))

vrstaReg = ttk.Combobox(root, textvariable='Odaberite vrstu registracije', state='readonly', width=28,
           values=('    Produženje registracije', '    Prva registracija'))
vrstaReg.place(x=21, y=90)
vrstaReg.set("    Odaberite vrstu registracije")
vrstaReg.bind("<FocusIn>", defocus)

label2=Label(root, text="Vrsta vozila:", bg="#e6e6e6", fg="#222")
label2.place(x=20, y=120)
label2.config(font=("Arial", 12))

vrstaVoz = ttk.Combobox(root, textvariable='Odaberite vrstu vozila', state='readonly', width=28,
           values=('    Putničko', '    Teretno', '    Priključno', '    Motocikl'))
vrstaVoz.place(x=21, y=145)
vrstaVoz.set("    Odaberite vrstu vozila")
vrstaVoz.bind("<FocusIn>", defocus)

global label3
label3=Label(root, text="Zapremina motora:", bg="#e6e6e6", fg="#222")
label3.place(x=20, y=175)
label3.config(font=("Arial", 12))

global zapremina
zapremina = ttk.Entry(root, width=30, justify=CENTER)
zapremina.place(x=21, y=200)
zapremina.config(font=("Arial", 11))

global label4
label4=Label(root, text="Snaga motora:", bg="#e6e6e6", fg="#222")
label4.place(x=20, y=230)
label4.config(font=("Arial", 12))

global snaga
snaga = ttk.Combobox(root, textvariable='Odaberite snagu motora', state='readonly', width=28,
        values=('    do 22 kW', '    23 kW - 33 kW', '    34 kW - 44 kW', '    45 kW - 55 kW', '    56 kW - 66 kW',
        '    67 kW - 84 kW', '    85 kW - 110 kW', '    preko 110 kW'))
snaga.set("    Odaberite snagu motora")
snaga.place(x=21, y=255)
snaga.bind("<FocusIn>", defocus)

label5=Label(root, text="Vrsta goriva:", bg="#e6e6e6", fg="#222")
label5.place(x=20, y=285)
label5.config(font=("Arial", 12))

vrstaGor = ttk.Combobox(root, textvariable='Odaberite vrstu goriva', state='readonly', width=28,
           values=('    Dizel', '    Benzin', '    Plin'))
vrstaGor.place(x=21, y=310)
vrstaGor.set("    Odaberite vrstu goriva")
vrstaGor.bind("<FocusIn>", defocus)

label6=Label(root, text="Godina proizvodnje:", bg="#e6e6e6", fg="#222")
label6.place(x=20, y=340)
label6.config(font=("Arial", 12))

godProz = ttk.Entry(root, width=30, justify=CENTER)
godProz.place(x=21, y=365)
godProz.config(font=("Arial", 11))

label7=Label(root, text="Bonus:", bg="#e6e6e6", fg="#222")
label7.place(x=20, y=395)
label7.config(font=("Arial", 12))

bonus = ttk.Combobox(root, textvariable='Bonus', state='readonly', width=28,
        values=('      0%', '    10%', '    20%', '    30%',
        '    40%', '    50%', '   110%', '   120%', '   130%', '   140%', '   150%', '   160%', '   180%', '   200%'))
bonus.place(x=21, y=420)
bonus.set("    Odaberite iznos bonusa")
bonus.bind("<FocusIn>", defocus)
#---------------------------------------FUNKCIJE------------------------------------------------------------------------

def vrstaVozila(eventObject):
    global t, p, pr, m, snaga, label4, label3, zapremina, regz, vlz, invalidV, label401, an, vrstaGor, label5, da, db, zast
    global terensko, terenskoV, taxi, taxiV, rentV, rent, kombi, kombiTeret, invalid, ug, ugV, potvrdaVlV, potvrdaRegV, kombiV, kombiTeretV
    global sedlastiTeg, label8, vrTer, label9, nosTer, label10, brOs, label11, maxNos, potvrdaoreg, potvrdaovl, zapaljivi, labeltkstT, labeltkstT1, pravno
    global vrPrik, nosPrik, brOsPrik, maxNosPrik, zapaljiviPr1, zapaljiviPr, labeltkstPr2, labeltkstPr1, labeltkstPr, labeltkstPr3
    global kat, kolica, rvi, labeltkstM, labeltkstM1, zapaljiviPrV, zapaljiviPrV1, godProz, bonus, label6, label7, sedlasti, zapaljiviV

    potvrdaRegV.set(value=0)
    taxiV.set(value=0)
    rentV.set(value=0)
    kombiV.set(value=0)
    kombiTeretV.set(value=0)
    potvrdaVlV.set(value=1)
    invalidV.set(value=0)
    pravnoV.set(value=0)
    ugV.set(value=0)
    zapaljiviPrV.set(value=0)
    zapaljiviPrV1.set(value=0)
    sedlasti.set(value=0)

    if vlz is True:
        potvrdaovl.destroy()
        vlz = False
    if regz is True:
        potvrdaoreg.destroy()
        regz = False

    if m == True:
        label6.destroy()
        godProz.destroy()
        godProz.destroy()
        bonus.destroy()
        label6 = Label(root, text="Godina proizvodnje:", bg="#e6e6e6", fg="#222")
        label6.place(x=20, y=340)
        label6.config(font=("Arial", 12))

        godProz = ttk.Entry(root, width=30, justify=CENTER)
        godProz.place(x=21, y=365)
        godProz.config(font=("Arial", 11))

        label7 = Label(root, text="Bonus:", bg="#e6e6e6", fg="#222")
        label7.place(x=20, y=395)
        label7.config(font=("Arial", 12))

        bonus = ttk.Combobox(root, textvariable='Bonus', state='readonly', width=28,
                             values=('      0%', '    10%', '    20%', '    30%',
                                     '    40%', '    50%', '   110%', '   120%', '   130%', '   140%', '   150%',
                                     '   160%', '   180%', '   200%'))
        bonus.place(x=21, y=420)
        bonus.set("    Odaberite iznos bonusa")
        bonus.bind("<FocusIn>", defocus)

    if vrstaVoz.get() == '    Teretno':

        if pr is False:
            label3.place(x=20, y=205)
            zapremina.place(x=21, y=230)
        label4.destroy()
        snaga.destroy()
        label6.place(x=20, y=370)
        godProz.place(x=21, y=395)
        label7.place(x=20, y=425)
        bonus.place(x=21, y=450)

        if vrstaReg.get() == '    Produženje registracije':
            potvrdaoreg = Checkbutton(root, text='Potvrda o registraciji', variable=potvrdaRegV, font='Arial 12',
                                      bg="#e6e6e6",
                                      fg="#222")
            potvrdaoreg.place(x=18, y=745)
            regz = True
        elif vrstaReg.get() == '    Prva registracija':
            potvrdaovl = Checkbutton(root, text='Potvrda o vlasništvu', variable=potvrdaVlV, font='Arial 12',
                                     bg="#e6e6e6",
                                     fg="#222")
            potvrdaovl.place(x=18, y=745)
            vlz = True
        if t is True:
            sedlastiTeg.destroy()
            label8.destroy()
            vrTer.destroy()
            label9.destroy()
            nosTer.destroy()
            label10.destroy()
            brOs.destroy()
            label11.destroy()
            maxNos.destroy()
            zapaljivi.destroy()
            labeltkstT.destroy()
            labeltkstT1.destroy()

        if m is True:
            label5 = Label(root, text="Vrsta goriva:", bg="#e6e6e6", fg="#222")
            label5.place(x=20, y=285)
            label5.config(font=("Arial", 12))

            vrstaGor = ttk.Combobox(root, textvariable='Odaberite vrstu goriva', state='readonly', width=28,
                                    values=('    Dizel', '    Benzin', '    Plin'))
            vrstaGor.place(x=21, y=310)
            vrstaGor.set("    Odaberite vrstu goriva")
            vrstaGor.bind("<FocusIn>", defocus)
            kat.destroy()
            label10.destroy()
            kolica.destroy()
            rvi.destroy()
            labeltkstM.destroy()
            labeltkstM1.destroy()
            pravno.destroy()
            ug.destroy()
            m = False

        if p is True:
            terensko.destroy()
            taxi.destroy()
            rent.destroy()
            kombi.destroy()
            kombiTeret.destroy()
            invalid.destroy()
            ug.destroy()
            pravno.destroy()
            label401.destroy()
            an.destroy()
            p = False

        if pr is True:
            if zast is True:
                da.destroy()
                db.destroy()
                zast = False
            label3 = Label(root, text="Zapremina motora:", bg="#e6e6e6", fg="#222")
            label3.place(x=20, y=205)
            label3.config(font=("Arial", 12))

            zapremina = ttk.Entry(root, width=30, justify=CENTER)
            zapremina.place(x=21, y=230)
            zapremina.config(font=("Arial", 11))

            label5 = Label(root, text="Vrsta goriva:", bg="#e6e6e6", fg="#222")
            label5.config(font=("Arial", 12))

            vrstaGor = ttk.Combobox(root, textvariable='Odaberite vrstu goriva', state='readonly', width=28,
                                    values=('    Dizel', '    Benzin', '    Plin'))
            vrstaGor.set("    Odaberite vrstu goriva")
            vrstaGor.bind("<FocusIn>", defocus)

            vrPrik.destroy()
            label8.destroy()
            nosPrik.destroy()
            label9.destroy()
            brOsPrik.destroy()
            label10.destroy()
            maxNosPrik.destroy()
            label11.destroy()
            pravno.destroy()
            zapaljiviPr.destroy()
            zapaljiviPr1.destroy()
            labeltkstPr2.destroy()
            labeltkstPr1.destroy()
            labeltkstPr.destroy()
            labeltkstPr3.destroy()
            pr = False

        t = True

        label4 = Label(root, text="Snaga motora:", bg="#e6e6e6", fg="#222")
        label4.place(x=20, y=260)
        label4.config(font=("Arial", 12))
        snaga = ttk.Combobox(root, textvariable='Odaberite snagu motora', state='readonly', width=28,
                             values=('    do 18 kW', '    19 kW - 25 kW', '    26 kW - 33 kW', '    34 kW - 44 kW',
                                     '    45 kW - 73 kW',
                                     '    74 kW - 110 kW', '    111 kW - 147 kW', '    preko 147 kW'))
        snaga.set("    Odaberite snagu motora")
        snaga.place(x=21, y=285)
        snaga.bind("<FocusIn>", defocus)

        label5.place(x=20, y=315)
        vrstaGor.place(x=21, y=340)

        sedlastiTeg = Checkbutton(root, text='Sedlasti tegljač', variable=sedlasti, font='Arial 12', bg="#e6e6e6",
                                  fg="#222")
        sedlastiTeg.place(x=20, y=175)

        label8 = Label(root, text="Vrsta teretnog vozila:", bg="#e6e6e6", fg="#222")
        label8.place(x=20, y=480)
        label8.config(font=("Arial", 12))

        vrTer = ttk.Combobox(root, textvariable='Vrsta teretnog vozila', state='readonly', width=28, values=(
            '    N1', '    N2', '    N3'))
        vrTer.place(x=21, y=505)
        vrTer.set("    Odaberite vrstu teretnog vozila")
        vrTer.bind("<FocusIn>", defocus)

        label9 = Label(root, text="Nosivost teretnog vozila:", bg="#e6e6e6", fg="#222")
        label9.place(x=20, y=535)
        label9.config(font=("Arial", 12))

        nosTer = ttk.Combobox(root, textvariable='Nosivost teretnog vozila', state='readonly', width=28, values=(
            '    do 0.5 t', '    preko 0.5 - 1.0 t', '    preko 1.0 - 2.0 t', '    preko 2.0 - 3.0 t',
            '    preko 3.0 - 5.0 t', '    preko 5.0 - 7.0 t', '    preko 7.0 - 10.0 t', '    preko 10.0 - 15.0 t',
            '    preko 15.0 t'))
        nosTer.place(x=21, y=560)
        nosTer.set("    Odaberite nosivost vozila")
        nosTer.bind("<FocusIn>", defocus)

        label10 = Label(root, text="Broj osovina:", bg="#e6e6e6", fg="#222")
        label10.place(x=20, y=590)
        label10.config(font=("Arial", 12))

        brOs = ttk.Combobox(root, textvariable='Broj osovina', state='readonly', width=28, values=(
            '    Dvije osovine', '    Tri osovine', '    Četiri i više osovina'))
        brOs.place(x=21, y=615)
        brOs.set("    Odaberite broj osovina")
        brOs.bind("<FocusIn>", defocus)

        label11 = Label(root, text="Najveća dopuštena masa:", bg="#e6e6e6", fg="#222")
        label11.place(x=20, y=645)
        label11.config(font=("Arial", 12))

        maxNos = ttk.Combobox(root, textvariable='Dopuštena masa', state='readonly', width=28, values=(
            '    do 1000 kg', '    1001 - 2000 kg', '    2001 - 3000 kg', '    3001 - 3500 kg', '    3501 - 5000 kg',
            '    5001 - 6000 kg', '    6001 - 7000 kg', '    7001 - 8000 kg', '    8001 - 9000 kg',
            '    9001 - 10000 kg', '    10001 - 11000 kg', '    11001 - 12000 kg', '    12001 - 13000 kg',
            '    13001 - 14000 kg', '    14001 - 15000 kg', '    15001 - 16000 kg', '    16001 - 17000 kg',
            '    17001 - 18000 kg', '    18001 - 19000 kg', '    19001 - 20000 kg', '    20001 - 21000 kg',
            '    21001 - 22000 kg', '    22001 - 23000 kg', '    23001 - 24000 kg', '    24001 - 25000 kg',
            '    25001 - 26000 kg', '    26001 - 27000 kg', '    27001 - 28000 kg', '    28001 - 29000 kg',
            '    29001 - 30000 kg', '    30001 - 31000 kg', '    31001 - 32000 kg', '    preko 32000 kg'))
        maxNos.place(x=21, y=670)
        maxNos.set("    Najveća dopuštena masa")
        maxNos.bind("<FocusIn>", defocus)

        zapaljivi = Checkbutton(root, height=2, text='', variable=zapaljiviV, font='Arial 11', bg="#e6e6e6",
                                fg="#222")
        zapaljivi.place(x=18, y=700)

        tkstT = "Vozilo povremeno ili stalno služi za prijevoz"
        tkstT1 = "eksplozivnih i lako zapaljivih tvari"

        labeltkstT = Label(root, text=tkstT, bg="#e6e6e6", fg="#222")
        labeltkstT.place(x=40, y=699)
        labeltkstT.config(font=("Arial", 12))

        labeltkstT1 = Label(root, text=tkstT1, bg="#e6e6e6", fg="#222")
        labeltkstT1.place(x=40, y=719)
        labeltkstT1.config(font=("Arial", 12))

        btn.place(x=96, y=780)

    elif vrstaVoz.get() == '    Putničko':

        if vrstaReg.get() == '    Produženje registracije':
            potvrdaoreg = Checkbutton(root, text='Potvrda o registraciji', variable=potvrdaRegV, font='Arial 12',
                                      bg="#e6e6e6",
                                      fg="#222")
            potvrdaoreg.place(x=18, y=505)
            regz = True
        elif vrstaReg.get() == '    Prva registracija':
            potvrdaovl = Checkbutton(root, text='Potvrda o vlasništvu', variable=potvrdaVlV, font='Arial 12',
                                     bg="#e6e6e6",
                                     fg="#222")
            potvrdaovl.place(x=18, y=505)
            vlz = True

        if m is True:
            label4 = Label(root, text="Snaga motora:", bg="#e6e6e6", fg="#222")
            label4.place(x=20, y=230)
            label4.config(font=("Arial", 12))

            snaga = ttk.Combobox(root, textvariable='Odaberite snagu motora', state='readonly', width=28, values=(
                '    do 22 kW', '    23 kW - 33 kW', '    34 kW - 44 kW', '    45 kW - 55 kW',
                '    56 kW - 66 kW',
                '    67 kW - 84 kW', '    85 kW - 110 kW', '    preko 110 kW'))
            snaga.set("    Odaberite snagu motora")
            snaga.place(x=21, y=255)
            snaga.bind("<FocusIn>", defocus)

            label5 = Label(root, text="Vrsta goriva:", bg="#e6e6e6", fg="#222")
            label5.place(x=20, y=285)
            label5.config(font=("Arial", 12))

            vrstaGor = ttk.Combobox(root, textvariable='Odaberite vrstu goriva', state='readonly', width=28,
                                    values=('    Dizel', '    Benzin', '    Plin'))
            vrstaGor.place(x=21, y=310)
            vrstaGor.set("    Odaberite vrstu goriva")
            vrstaGor.bind("<FocusIn>", defocus)
            kat.destroy()
            label10.destroy()
            kolica.destroy()
            rvi.destroy()
            labeltkstM.destroy()
            labeltkstM1.destroy()
            pravno.destroy()
            ug.destroy()
            m = False

        if p is True:
            terensko.destroy()
            taxi.destroy()
            rent.destroy()
            kombi.destroy()
            kombiTeret.destroy()
            invalid.destroy()
            ug.destroy()
            pravno.destroy()
            label401.destroy()
            an.destroy()

        if t is True:
            label3.place(x=20, y=175)
            zapremina.place(x=21, y=200)
            label4.place(x=20, y=230)
            snaga.destroy()
            vrstaGor.destroy()
            label5.destroy()
            snaga = ttk.Combobox(root, textvariable='Odaberite snagu motora', state='readonly', width=28,
                                 values=('    do 22 kW', '    23 kW - 33 kW', '    34 kW - 44 kW', '    45 kW - 55 kW',
                                         '    56 kW - 66 kW',
                                         '    67 kW - 84 kW', '    85 kW - 110 kW', '    preko 110 kW'))
            snaga.set("    Odaberite snagu motora")
            snaga.place(x=21, y=255)
            snaga.bind("<FocusIn>", defocus)
            label5 = Label(root, text="Vrsta goriva:", bg="#e6e6e6", fg="#222")
            label5.place(x=20, y=285)
            label5.config(font=("Arial", 12))

            vrstaGor = ttk.Combobox(root, textvariable='Odaberite vrstu goriva', state='readonly', width=28,
                                    values=('    Dizel', '    Benzin', '    Plin'))
            vrstaGor.place(x=21, y=310)
            vrstaGor.set("    Odaberite vrstu goriva")
            vrstaGor.bind("<FocusIn>", defocus)
            label6.place(x=20, y=340)
            godProz.place(x=21, y=365)
            label7.place(x=20, y=395)
            bonus.place(x=21, y=420)
            sedlastiTeg.destroy()
            label8.destroy()
            vrTer.destroy()
            label9.destroy()
            nosTer.destroy()
            label10.destroy()
            brOs.destroy()
            label11.destroy()
            maxNos.destroy()
            zapaljivi.destroy()
            labeltkstT.destroy()
            labeltkstT1.destroy()
            t = False

        if pr is True:
            label6.place(x=20, y=340)
            godProz.place(x=21, y=365)
            label7.place(x=20, y=395)
            bonus.place(x=21, y=420)
            label3 = Label(root, text="Zapremina motora:", bg="#e6e6e6", fg="#222")
            label3.place(x=20, y=175)
            label3.config(font=("Arial", 12))

            zapremina = ttk.Entry(root, width=30, justify=CENTER)
            zapremina.place(x=21, y=200)
            zapremina.config(font=("Arial", 11))

            label4 = Label(root, text="Snaga motora:", bg="#e6e6e6", fg="#222")
            label4.place(x=20, y=230)
            label4.config(font=("Arial", 12))

            snaga = ttk.Combobox(root, textvariable='Odaberite snagu motora', state='readonly', width=28, values=(
                '    do 22 kW', '    23 kW - 33 kW', '    34 kW - 44 kW', '    45 kW - 55 kW',
                '    56 kW - 66 kW',
                '    67 kW - 84 kW', '    85 kW - 110 kW', '    preko 110 kW'))
            snaga.set("    Odaberite snagu motora")
            snaga.place(x=21, y=255)
            snaga.bind("<FocusIn>", defocus)

            label5 = Label(root, text="Vrsta goriva:", bg="#e6e6e6", fg="#222")
            label5.place(x=20, y=285)
            label5.config(font=("Arial", 12))
            vrstaGor = ttk.Combobox(root, textvariable='Odaberite vrstu goriva', state='readonly', width=28,
                                    values=('    Dizel', '    Benzin', '    Plin'))
            vrstaGor.place(x=21, y=310)
            vrstaGor.set("    Odaberite vrstu goriva")
            vrstaGor.bind("<FocusIn>", defocus)
            if zast is True:
                da.destroy()
                db.destroy()
                zast = False
            vrPrik.destroy()
            label8.destroy()
            nosPrik.destroy()
            label9.destroy()
            brOsPrik.destroy()
            label10.destroy()
            maxNosPrik.destroy()
            label11.destroy()
            pravno.destroy()
            zapaljiviPr.destroy()
            zapaljiviPr1.destroy()
            labeltkstPr2.destroy()
            labeltkstPr1.destroy()
            labeltkstPr.destroy()
            labeltkstPr3.destroy()
            pr = False

        p = True

        label401 = Label(root, text="Osiguranje autonezgode (AN):", bg="#e6e6e6", fg="#222")
        label401.place(x=20, y=450)
        label401.config(font=("Arial", 12))

        an = ttk.Combobox(root, textvariable='Odaberite premiju', state='readonly', width=28, values=('    Bez premije',
                                                                                                      '    2.85 KM',
                                                                                                      '    5.70 KM',
                                                                                                      '    8.55 KM',
                                                                                                      '  11.40 KM',
                                                                                                      '  14.25 KM',
                                                                                                      '  17.10 KM',
                                                                                                      '  19.95 KM',
                                                                                                      '  22.80 KM',
                                                                                                      '  25.65 KM',
                                                                                                      '  28.50 KM',
                                                                                                      '  31.35 KM',
                                                                                                      '  34.20 KM',
                                                                                                      '  39.90 KM',
                                                                                                      '  42.75 KM',
                                                                                                      '  45.60 KM',
                                                                                                      '  48.45 KM',
                                                                                                      '  51.30 KM',
                                                                                                      '  54.15 KM',
                                                                                                      '  57.00 KM',
                                                                                                      '  59.85 KM',
                                                                                                      '  62.70 KM',
                                                                                                      '  65.55 KM',
                                                                                                      '  68.40 KM',
                                                                                                      '  71.25 KM'))
        an.set("    Bez premije")
        an.place(x=21, y=475)
        an.bind("<FocusIn>", defocus)

        terensko = Checkbutton(root, text='Terensko vozilo', variable=terenskoV, font='Arial 12', bg="#e6e6e6",
                               fg="#222")
        terensko.place(x=18, y=535)

        pravno = Checkbutton(root, text='Pravno lice', variable=pravnoV, font='Arial 12', bg="#e6e6e6",
                             fg="#222")
        pravno.place(x=18, y=565)

        ug = Checkbutton(root, text="Komisioni ugovor", variable=ugV,
                         font='Arial 12', bg="#e6e6e6", fg="#222")
        ug.place(x=18, y=595)

        taxi = Checkbutton(root, text='Taxi', variable=taxiV, font='Arial 12', bg="#e6e6e6", fg="#222")
        taxi.place(x=18, y=625)

        rent = Checkbutton(root, text='Rent a car', variable=rentV, font='Arial 12', bg="#e6e6e6", fg="#222")
        rent.place(x=18, y=655)

        kombi = Checkbutton(root, text='Kombi vozila sa 7 i više mjesta', variable=kombiV, font='Arial 12',
                            bg="#e6e6e6", fg="#222")
        kombi.place(x=18, y=685)

        kombiTeret = Checkbutton(root, text='Kombi vozila namijenjena prijevozu tereta', variable=kombiTeretV,
                                 font='Arial 12', bg="#e6e6e6", fg="#222")
        kombiTeret.place(x=18, y=715)

        invalid = Checkbutton(root, text='Osobe sa 80% i više tjelesnim oštećenjem', variable=invalidV,
                              font='Arial 12', bg="#e6e6e6", fg="#222")
        invalid.place(x=18, y=745)

        btn.place(x=96, y=785)

    elif vrstaVoz.get() == '    Priključno':
        label3.destroy()
        zapremina.destroy()
        vrstaGor.destroy()
        label5.destroy()
        label4.destroy()
        snaga.destroy()
        pravnoV.set(value=1)
        label6.place(x=20, y=285)
        godProz.place(x=21, y=310)
        label7.place(x=20, y=340)
        bonus.place(x=21, y=365)

        if pr is True:
            if zast is True:
                da.destroy()
                db.destroy()
                zast = False
            vrPrik.destroy()
            label8.destroy()
            nosPrik.destroy()
            label9.destroy()
            brOsPrik.destroy()
            label10.destroy()
            maxNosPrik.destroy()
            label11.destroy()
            pravno.destroy()
            zapaljiviPr.destroy()
            zapaljiviPr1.destroy()
            labeltkstPr2.destroy()
            labeltkstPr1.destroy()
            labeltkstPr.destroy()
            labeltkstPr3.destroy()

        if m is True:
            kat.destroy()
            label10.destroy()
            kolica.destroy()
            rvi.destroy()
            labeltkstM.destroy()
            labeltkstM1.destroy()
            pravno.destroy()
            ug.destroy()
            m = False

        if p is True:
            terensko.destroy()
            taxi.destroy()
            rent.destroy()
            kombi.destroy()
            kombiTeret.destroy()
            invalid.destroy()
            ug.destroy()
            pravno.destroy()
            label401.destroy()
            an.destroy()
            p = False

        if t is True:
            sedlastiTeg.destroy()
            label8.destroy()
            vrTer.destroy()
            label9.destroy()
            nosTer.destroy()
            label10.destroy()
            brOs.destroy()
            label11.destroy()
            maxNos.destroy()
            zapaljivi.destroy()
            labeltkstT.destroy()
            labeltkstT1.destroy()
            t = False

        pr = True

        if vrstaReg.get() == '    Produženje registracije':
            potvrdaoreg = Checkbutton(root, text='Potvrda o registraciji', variable=potvrdaRegV, font='Arial 12',
                                      bg="#e6e6e6",
                                      fg="#222")
            potvrdaoreg.place(x=20, y=505)
            regz = True
        elif vrstaReg.get() == '    Prva registracija':
            potvrdaovl = Checkbutton(root, text='Potvrda o vlasništvu', variable=potvrdaVlV, font='Arial 12',
                                     bg="#e6e6e6",
                                     fg="#222")
            potvrdaovl.place(x=20, y=505)
            vlz = True

        pravno = Checkbutton(root, text='Pravno lice', variable=pravnoV, font='Arial 12', bg="#e6e6e6",
                             fg="#222")
        pravno.place(x=20, y=535)

        label8 = Label(root, text="Vrsta priključnog vozila:", bg="#e6e6e6", fg="#222")
        label8.place(x=20, y=175)
        label8.config(font=("Arial", 12))

        vrPrik = ttk.Combobox(root, textvariable='Vrsta priključnog vozila', state='readonly', width=28, values=(
            '    O1', '    O2', '    O3', '    O4'))

        vrPrik.set("    Vrsta priključnog vozila")
        vrPrik.bind("<FocusIn>", defocus)
        vrPrik.place(x=21, y=200)
        label9 = Label(root, text="Nosivost priključnog vozila:", bg="#e6e6e6", fg="#222")
        label9.place(x=20, y=395)
        label9.config(font=("Arial", 12))

        nosPrik = ttk.Combobox(root, textvariable='Nosivost priključnog vozila', state='readonly', width=28, values=(
            '    do 1 t', '    preko 1 - 3 t', '    preko 3 - 5 t', '    preko 5 - 10 t', '    preko 10 - 15 t',
            '    preko 15 - 20 t', '    preko 20 t'))
        nosPrik.place(x=21, y=420)
        nosPrik.set("    Odaberite nosivost vozila")
        nosPrik.bind("<FocusIn>", defocus)

        label10 = Label(root, text="Broj osovina:", bg="#e6e6e6", fg="#222")
        label10.place(x=20, y=230)
        label10.config(font=("Arial", 12))

        brOsPrik = ttk.Combobox(root, textvariable='Broj osovina', state='readonly', width=28, values=(
            '    Jedna osovina', '    Dvije osovine', '    Tri osovine', '    Četiri osovine', '    Pet osovina',
            '    Šest i više osovina'))
        brOsPrik.place(x=21, y=255)
        brOsPrik.set("    Odaberite broj osovina")
        brOsPrik.bind("<FocusIn>", defocus)

        label11 = Label(root, text="Najveća dopuštena masa:", bg="#e6e6e6", fg="#222")
        label11.place(x=20, y=450)
        label11.config(font=("Arial", 12))

        maxNosPrik = ttk.Combobox(root, textvariable='Dopuštena masa', state='readonly', width=28, values=(
            '    do 750 kg', '    751 - 1000 kg', '    1001 - 2000 kg', '    2001 - 3000 kg', '    3001 - 3500 kg',
            '    3501 - 5000 kg', '    5001 - 6000 kg', '    6001 - 7000 kg', '    7001 - 8000 kg',
            '    8001 - 9000 kg',
            '    9001 - 10000 kg', '    10001 - 11000 kg', '    11001 - 12000 kg', '    12001 - 13000 kg',
            '    13001 - 14000 kg', '    14001 - 15000 kg', '    15001 - 16000 kg', '    16001 - 17000 kg',
            '    17001 - 18000 kg', '    18001 - 19000 kg', '    19001 - 20000 kg', '    20001 - 21000 kg',
            '    21001 - 22000 kg', '    22001 - 23000 kg', '    23001 - 24000 kg', '    preko 24000 kg'))
        maxNosPrik.place(x=21, y=475)
        maxNosPrik.set("    Najveća dopuštena masa")
        maxNosPrik.bind("<FocusIn>", defocus)

        zapaljiviPrV = IntVar()
        zapaljiviPr = Checkbutton(root, height=2, text='', variable=zapaljiviPrV, font='Arial 12', bg="#e6e6e6",
                                  fg="#222")
        zapaljiviPr.place(x=18, y=565)
        tkstPr = "Teretna prikolica povremeno ili stalno služi"
        tkstPr1 = "za prijevoz eksplozivnih i lako zapaljivih tvari"

        labeltkstPr = Label(root, text=tkstPr, bg="#e6e6e6", fg="#222")
        labeltkstPr.place(x=40, y=564)
        labeltkstPr.config(font=("Arial", 12))

        labeltkstPr1 = Label(root, text=tkstPr1, bg="#e6e6e6", fg="#222")
        labeltkstPr1.place(x=40, y=584)
        labeltkstPr1.config(font=("Arial", 12))

        zapaljiviPrV1 = IntVar()
        zapaljiviPr1 = Checkbutton(root, height=2, text='', variable=zapaljiviPrV1, font='Arial 12', bg="#e6e6e6",
                                   fg="#222")
        zapaljiviPr1.place(x=18, y=615)

        tkstPr = "Prikolica služi za prijevoz oštećenih i"
        tkstPr1 = "neispravnih osobnih automobila"

        labeltkstPr2 = Label(root, text=tkstPr, bg="#e6e6e6", fg="#222")
        labeltkstPr2.place(x=40, y=614)
        labeltkstPr2.config(font=("Arial", 12))

        labeltkstPr3 = Label(root, text=tkstPr1, bg="#e6e6e6", fg="#222")
        labeltkstPr3.place(x=40, y=634)
        labeltkstPr3.config(font=("Arial", 12))

        btn.place(x=96, y=669)

        def vrstaPrik(eventObject):
            if vrPrik.get() == '    O4':
                global da, db, zast
                da = Label(root, text="Prikolica / poluprikolica:", bg="#e6e6e6", fg="#222")
                da.place(x=20, y=230)
                da.config(font=("Arial", 12))

                db = ttk.Combobox(root, textvariable='Odaberite', state='readonly', width=28, values=(
                    '    Poluprikolica DA', '    Prikolice DB i DC', '    Poluprikolica DA, prikolice DB, DC'))
                db.set("    Odaberite")
                db.place(x=20, y=255)
                db.bind("<FocusIn>", defocus)
                if vlz is True:
                    potvrdaovl.place(x=20, y=560)
                elif regz is True:
                    potvrdaoreg.place(x=20, y=560)
                label6.place(x=20, y=340)
                godProz.place(x=21, y=365)
                label7.place(x=20, y=395)
                bonus.place(x=21, y=420)
                pravno.place(x=20, y=590)
                label9.place(x=20, y=450)
                nosPrik.place(x=21, y=475)
                label10.place(x=20, y=285)
                brOsPrik.place(x=21, y=310)
                label11.place(x=20, y=505)
                maxNosPrik.place(x=21, y=530)
                zapaljiviPr.place(x=18, y=620)
                labeltkstPr.place(x=40, y=619)
                labeltkstPr1.place(x=40, y=639)
                zapaljiviPr1.place(x=18, y=670)
                labeltkstPr2.place(x=40, y=669)
                labeltkstPr3.place(x=40, y=689)
                btn.place(x=96, y=724)

                zast = True
            else:
                if zast is True:
                    da.destroy()
                    db.destroy()
                zast = False
                if vlz is True:
                    potvrdaovl.place(x=20, y=505)
                elif regz is True:
                    potvrdaoreg.place(x=20, y=505)
                pravno.place(x=20, y=535)
                label9.place(x=20, y=395)
                nosPrik.place(x=21, y=420)
                label10.place(x=20, y=230)
                brOsPrik.place(x=21, y=255)
                label11.place(x=20, y=450)
                maxNosPrik.place(x=21, y=475)
                zapaljiviPr.place(x=18, y=565)
                labeltkstPr.place(x=40, y=564)
                labeltkstPr1.place(x=40, y=584)
                zapaljiviPr1.place(x=18, y=615)
                labeltkstPr2.place(x=40, y=614)
                labeltkstPr3.place(x=40, y=634)
                label6.place(x=20, y=285)
                godProz.place(x=21, y=310)
                label7.place(x=20, y=340)
                bonus.place(x=21, y=365)
                btn.place(x=96, y=669)

        vrPrik.bind("<<ComboboxSelected>>", vrstaPrik)

    elif vrstaVoz.get() == '    Motocikl':
        label4.destroy()
        snaga.destroy()
        vrstaGor.destroy()
        label5.destroy()
        if vrstaReg.get() == '    Produženje registracije':
            potvrdaoreg = Checkbutton(root, text='Potvrda o registraciji', variable=potvrdaRegV, font='Arial 12',
                                      bg="#e6e6e6",
                                      fg="#222")
            potvrdaoreg.place(x=18, y=395)
            regz = True
        elif vrstaReg.get() == '    Prva registracija':
            potvrdaovl = Checkbutton(root, text='Potvrda o vlasništvu', variable=potvrdaVlV, font='Arial 12',
                                     bg="#e6e6e6",
                                     fg="#222")
            potvrdaovl.place(x=18, y=395)
            vlz = True

        if m is True:
            kat.destroy()
            label10.destroy()
            kolica.destroy()
            rvi.destroy()
            labeltkstM.destroy()
            labeltkstM1.destroy()
            pravno.destroy()
            ug.destroy()

        if p is True:
            terensko.destroy()
            taxi.destroy()
            rent.destroy()
            kombi.destroy()
            kombiTeret.destroy()
            invalid.destroy()
            ug.destroy()
            pravno.destroy()
            label401.destroy()
            an.destroy()

        if pr is True:
            if zast is True:
                label6.place(x=20, y=285)
                godProz.place(x=21, y=310)
                label7.place(x=20, y=340)
                bonus.place(x=21, y=365)
                da.destroy()
                db.destroy()
                zast = False
            label3 = Label(root, text="Zapremina motora:", bg="#e6e6e6", fg="#222")
            label3.place(x=20, y=175)
            label3.config(font=("Arial", 12))

            zapremina = ttk.Entry(root, width=30, justify=CENTER)
            zapremina.place(x=21, y=200)
            zapremina.config(font=("Arial", 11))

            vrPrik.destroy()
            label8.destroy()
            nosPrik.destroy()
            label9.destroy()
            brOsPrik.destroy()
            label10.destroy()
            maxNosPrik.destroy()
            label11.destroy()
            pravno.destroy()
            zapaljiviPr.destroy()
            zapaljiviPr1.destroy()
            labeltkstPr2.destroy()
            labeltkstPr1.destroy()
            labeltkstPr.destroy()
            labeltkstPr3.destroy()
            pr = False

        if t is True:
            label3.place(x=20, y=175)
            zapremina.place(x=21, y=200)
            sedlastiTeg.destroy()
            label8.destroy()
            vrTer.destroy()
            label9.destroy()
            nosTer.destroy()
            label10.destroy()
            brOs.destroy()
            label11.destroy()
            maxNos.destroy()
            zapaljivi.destroy()
            labeltkstT.destroy()
            labeltkstT1.destroy()
            t = False

        m = True

        pravno = Checkbutton(root, text='Pravno lice', variable=pravnoV, font='Arial 12', bg="#e6e6e6",
                             fg="#222")
        pravno.place(x=18, y=425)

        ug = Checkbutton(root, text="Komisioni ugovor", variable=ugV,
                         font='Arial 12', bg="#e6e6e6", fg="#222")
        ug.place(x=18, y=455)

        label10 = Label(root, text="Kategorija motocikla:", bg="#e6e6e6", fg="#222")
        label10.place(x=20, y=230)
        label10.config(font=("Arial", 12))

        kat = ttk.Combobox(root, textvariable='Kategorija motocikla', state='readonly', width=28, values=(
            '    L1', '    L2', '    L3', '    L4', '    L5', '    L6',
            '    L7'))
        kat.place(x=21, y=255)
        kat.set("    Odaberite kategoriju motocikla")
        kat.bind("<FocusIn>", defocus)

        label6.place(x=20, y=285)
        godProz.place(x=21, y=310)
        label7.place(x=20, y=340)
        bonus.place(x=21, y=365)

        kolica = Checkbutton(root, text='Invalidska kolica sa motorom', variable=kolicaV, font='Arial 12', bg="#e6e6e6",
                             fg="#222")
        kolica.place(x=18, y=485)

        tkstM = "RVI, civilni invalidi i invalidi rada, minimalno"
        tkstM1 = "80% tjelesnih oštećenja"

        rvi = Checkbutton(root, height=2, text="", variable=rviV, font='Arial 12', bg="#e6e6e6", fg="#222")
        rvi.place(x=18, y=515)

        labeltkstM = Label(root, text=tkstM, bg="#e6e6e6", fg="#222")
        labeltkstM.place(x=40, y=514)
        labeltkstM.config(font=("Arial", 12))

        labeltkstM1 = Label(root, text=tkstM1, bg="#e6e6e6", fg="#222")
        labeltkstM1.place(x=40, y=534)
        labeltkstM1.config(font=("Arial", 12))

        btn.place(x=96, y=569)

vrstaVoz.bind("<<ComboboxSelected>>", vrstaVozila)
vrstaReg.bind("<<ComboboxSelected>>", vrstaVozila)

#---------------------------------Izlazni dio---------------------------------------------------------------------------
w = Canvas(root, width=400, bg="#ffffff", height=667, highlightthickness=0)
w.place(x=351, y=81)

w.create_line(1, 1, 399, 1, 399, 1, 399, 667, 399, 667, 1, 667, 1, 667, 1, 1, fill="#222")

w.create_line(1, 36, 399, 36, 399, 71, 1, 71, 1, 106, 399, 106, 399, 141, 1, 141, fill="#222")
w.create_line(1, 176, 399, 176, 399, 211, 1, 211, 1, 246, 399, 246, 399, 281, 1, 281, fill="#222")
w.create_line(1, 316, 399, 316, 399, 351, 1, 351, 1, 386, 399, 386, 399, 421, 1, 421, fill="#222")
w.create_line(1, 456, 399, 456, 399, 491, 1, 491, 1, 526, 399, 526, 399, 561, 1, 561, 1, 596, 399, 596, fill="#222")
w.create_line(1, 631, 399, 631, 399, 666, 1, 666, fill="#222")

w.create_line(50, 36, 50, 631, fill="#222")
w.create_line(250, 36, 250, 666, fill="#222")

label21 = Label(root, text="Klijent: ", bg="#ffffff", fg="#222")
label21.place(x=380, y=88)
label21.config(font=("Arial", 12, 'bold'))

klijent = ttk.Entry(root, width=28, justify=CENTER)
klijent.place(x=450, y=88)
klijent.config(font=("Arial", 12, 'bold'))

label21 = Label(root, text="1.", bg="#ffffff", fg="#222")
label21.place(x=368, y=123)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Tehnički pregled", bg="#ffffff", fg="#222")
label21.place(x=440, y=123)
label21.config(font=("Arial", 12))

label21 = Label(root, text="2.", bg="#ffffff", fg="#222")
label21.place(x=368, y=158)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Polica osiguranja", bg="#ffffff", fg="#222")
label21.place(x=438, y=158)
label21.config(font=("Arial", 12))

label21 = Label(root, text="3.", bg="#ffffff", fg="#222")
label21.place(x=368, y=193)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Zeleni karton", bg="#ffffff", fg="#222")
label21.place(x=452, y=193)
label21.config(font=("Arial", 12))

label21 = Label(root, text="4.", bg="#ffffff", fg="#222")
label21.place(x=368, y=228)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Putarina 60%", bg="#ffffff", fg="#222")
label21.place(x=451, y=228)
label21.config(font=("Arial", 12))

label21 = Label(root, text="5.", bg="#ffffff", fg="#222")
label21.place(x=368, y=263)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Putarina 40%", bg="#ffffff", fg="#222")
label21.place(x=451, y=263)
label21.config(font=("Arial", 12))

label21 = Label(root, text="6.", bg="#ffffff", fg="#222")
label21.place(x=368, y=298)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Zaštita voda", bg="#ffffff", fg="#222")
label21.place(x=454, y=298)
label21.config(font=("Arial", 12))

label21 = Label(root, text="7.", bg="#ffffff", fg="#222")
label21.place(x=368, y=333)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Fond za izgradnju", bg="#ffffff", fg="#222")
label21.place(x=439, y=333)
label21.config(font=("Arial", 12))

label21 = Label(root, text="8.", bg="#ffffff", fg="#222")
label21.place(x=368, y=368)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Pomoć na putu", bg="#ffffff", fg="#222")
label21.place(x=446, y=368)
label21.config(font=("Arial", 12))

label21 = Label(root, text="9.", bg="#ffffff", fg="#222")
label21.place(x=368, y=403)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Taksa", bg="#ffffff", fg="#222")
label21.place(x=475, y=403)
label21.config(font=("Arial", 12))

label21 = Label(root, text="10.", bg="#ffffff", fg="#222")
label21.place(x=364, y=438)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Potvrda o vlasništvu", bg="#ffffff", fg="#222")
label21.place(x=432, y=438)
label21.config(font=("Arial", 12))

label21 = Label(root, text="11.", bg="#ffffff", fg="#222")
label21.place(x=364, y=473)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Potvrda o registraciji", bg="#ffffff", fg="#222")
label21.place(x=431, y=473)
label21.config(font=("Arial", 12))

label21 = Label(root, text="12.", bg="#ffffff", fg="#222")
label21.place(x=364, y=508)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Stiker naljepnica", bg="#ffffff", fg="#222")
label21.place(x=444, y=508)
label21.config(font=("Arial", 12))

label21 = Label(root, text="13.", bg="#ffffff", fg="#222")
label21.place(x=364, y=543)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Porez na imovinu", bg="#ffffff", fg="#222")
label21.place(x=442, y=543)
label21.config(font=("Arial", 12))

label21 = Label(root, text="14.", bg="#ffffff", fg="#222")
label21.place(x=364, y=578)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Zaštita okoliša", bg="#ffffff", fg="#222")
label21.place(x=447, y=578)
label21.config(font=("Arial", 12))

label21 = Label(root, text="15.", bg="#ffffff", fg="#222")
label21.place(x=364, y=613)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Registarske tablice", bg="#ffffff", fg="#222")
label21.place(x=432, y=613)
label21.config(font=("Arial", 12))

label21 = Label(root, text="16.", bg="#ffffff", fg="#222")
label21.place(x=364, y=648)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Komisioni ugovor", bg="#ffffff", fg="#222")
label21.place(x=437, y=648)
label21.config(font=("Arial", 12))

label21 = Label(root, text="17.", bg="#ffffff", fg="#222")
label21.place(x=364, y=683)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Provizija banke", bg="#ffffff", fg="#222")
label21.place(x=442, y=683)
label21.config(font=("Arial", 12))

label21 = Label(root, text="Cijena registracije vozila", bg="#ffffff", fg="#222")
label21.place(x=382, y=718)
label21.config(font="Arial 12 bold")


#----------------------------------------KALKULACIJE--------------------------------------------------------------------
def checkcmbo():

    global sedlasti, polica, tehnicki, zeleniKarton, zeleniK, putarina60, putarina40, zastitaVoda, fond, pomocPut, taksa, dodatak, \
           potvrdaVl, potvrdaReg, stiker, regTab, komUg, provizijaB, potvrdaVlV, potvrdaRegV, terenskoV, taxiV, zastavicaP, label42,\
           year_, labelPolica, labelPut60, labelPut40, labelPorez, labelTehnicki, labelPomoc, labelZeleni, labelTaksa, \
           labelZastita, labelPotvrdaVl, labelPotvrdaReg, labelStiker, labelRegTab, labelKomUg, labelFond, labelOkolis,\
           labelProvizija, labelCijena, rentV, kombiTeretV, kombiV, invalidV, okolis, porez, cijena, tehnicki, an, \
           zapaljiviPrV, zapaljiviPrV1, kat

    if zastavicaP is True:
        label42.destroy()
        labelPolica.destroy()
        labelPut60.destroy()
        labelPut40.destroy()
        labelPorez.destroy()
        labelTehnicki.destroy()
        labelPomoc.destroy()
        labelZeleni.destroy()
        labelTaksa.destroy()
        labelZastita.destroy()
        labelPotvrdaVl.destroy()
        labelPotvrdaReg.destroy()
        labelStiker.destroy()
        labelRegTab.destroy()
        labelKomUg.destroy()
        labelFond.destroy()
        labelCijena.destroy()
        labelOkolis.destroy()
        labelProvizija.destroy()

    polica = float()
    tehnicki = float()
    zeleniKarton = float()
    putarina60 = float()
    putarina40 = float()
    zastitaVoda = float()
    fond = float()
    pomocPut = float()
    taksa = float()
    potvrdaVl = float()
    potvrdaReg = float()
    stiker = float()
    porez = float()
    okolis = float()
    regTab = float()
    komUg = float()
    provizijaB = float()

    zastitaVoda = 20
    stiker = 5
    zeleniK = 4
    dodatak = 0
    if pravnoV.get() == 1:
        fond = 20
    else:
        fond = 10

    if vrstaReg.get() == '    Prva registracija':
        taksa = 20
        regTab = 20
        potvrdaReg = 5
        if potvrdaVlV.get() == 1:
            potvrdaVl = 5
        else:
            potvrdaVl = 0
    elif vrstaReg.get() == '    Produženje registracije':
        taksa = 10
        if potvrdaRegV.get() == 1:
            potvrdaReg = 5

    if vrstaVoz.get() == '    Teretno':
        zastitaVoda = 40
        fond = 20
        pomocPut = 15
        if vrTer.get() == '    N1':
            if vrstaGor.get() == '    Benzin' or vrstaGor.get() == '    Plin':
                tehnicki = 97.33
            else:
                tehnicki = 101.33
        elif vrTer.get() == '    N2':
            tehnicki = 125.83
        elif vrTer.get() == '    N3':
            tehnicki = 135.16

        if maxNos.get() == '    do 1000 kg':
            putarina60 = 32.94
            putarina40 = 21.96
        elif maxNos.get() == '    1001 - 2000 kg':
            putarina60 = 48.6
            putarina40 = 32.4
        elif maxNos.get() == '    2001 - 3000 kg':
            putarina60 = 63
            putarina40 = 42
        elif maxNos.get() == '    3001 - 3500 kg':
            putarina60 = 70.56
            putarina40 = 47.04
        elif maxNos.get() == '    3501 - 5000 kg':
            putarina60 = 72
            putarina40 = 48
        elif maxNos.get() == '    5001 - 6000 kg':
            putarina60 = 84.06
            putarina40 = 56.04
        elif maxNos.get() == '    6001 - 7000 kg':
            putarina60 = 95.94
            putarina40 = 63.96
        elif maxNos.get() == '    7001 - 8000 kg':
            putarina60 = 108
            putarina40 = 72
        elif maxNos.get() == '    8001 - 9000 kg':
            putarina60 = 131.94
            putarina40 = 87.96
        elif maxNos.get() == '    9001 - 10000 kg':
            putarina60 = 149.94
            putarina40 = 99.96
        elif maxNos.get() == '    10001 - 11000 kg':
            putarina60 = 171
            putarina40 = 114
        elif maxNos.get() == '    11001 - 12000 kg':
            putarina60 = 192.06
            putarina40 = 128.04
        elif maxNos.get() == '    12001 - 13000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 216
                putarina40 = 144
            else:
                putarina60 = 214.2
                putarina40 = 142.8
        elif maxNos.get() == '    13001 - 14000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 239.94
                putarina40 = 159.96
            else:
                putarina60 = 238.14
                putarina40 = 158.76
        elif maxNos.get() == '    14001 - 15000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 264.06
                putarina40 = 176.04
            else:
                putarina60 = 262.26
                putarina40 = 174.84
        elif maxNos.get() == '    15001 - 16000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 288
                putarina40 = 192
            else:
                putarina60 = 286.2
                putarina40 = 190.8
        elif maxNos.get() == '    16001 - 17000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 311.94
                putarina40 = 207.96
            else:
                putarina60 = 310.14
                putarina40 = 206.76
        elif maxNos.get() == '    17001 - 18000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 336.06
                putarina40 = 224.04
            else:
                putarina60 = 334.26
                putarina40 = 222.84
        elif maxNos.get() == '    18001 - 19000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 358.2
                putarina40 = 238.8
        elif maxNos.get() == '    19001 - 20000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 382.14
                putarina40 = 254.76
        elif maxNos.get() == '    20001 - 21000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 406.26
                putarina40 = 270.84
        elif maxNos.get() == '    21001 - 22000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 430.2
                putarina40 = 286.8
        elif maxNos.get() == '    22001 - 23000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 454.14
                putarina40 = 302.76
        elif maxNos.get() == '    23001 - 24000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 478.26
                putarina40 = 318.84
        elif maxNos.get() == '    24001 - 25000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 504
                putarina40 = 336
        elif maxNos.get() == '    25001 - 26000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 527.94
                putarina40 = 351.96
        elif maxNos.get() == '    26001 - 27000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            else:
                putarina60 = 552.06
                putarina40 = 368.04
        elif maxNos.get() == '    27001 - 28000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            elif brOs.get() == '    Tri osovine':
                putarina60 = 552.06
                putarina40 = 368.04
            else:
                putarina60 = 576
                putarina40 = 384
        elif maxNos.get() == '    28001 - 29000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            elif brOs.get() == '    Tri osovine':
                putarina60 = 552.06
                putarina40 = 368.04
            else:
                putarina60 = 599.94
                putarina40 = 399.96
        elif maxNos.get() == '    29001 - 30000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            elif brOs.get() == '    Tri osovine':
                putarina60 = 552.06
                putarina40 = 368.04
            else:
                putarina60 = 624.06
                putarina40 = 416.04
        elif maxNos.get() == '    30001 - 31000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            elif brOs.get() == '    Tri osovine':
                putarina60 = 552.06
                putarina40 = 368.04
            else:
                putarina60 = 648
                putarina40 = 432
        elif maxNos.get() == '    31001 - 32000 kg':
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            elif brOs.get() == '    Tri osovine':
                putarina60 = 552.06
                putarina40 = 368.04
            else:
                putarina60 = 671.94
                putarina40 = 447.96
        else:
            if brOs.get() == '    Dvije osovine':
                putarina60 = 360
                putarina40 = 240
            elif brOs.get() == '    Tri osovine':
                putarina60 = 552.06
                putarina40 = 368.04
            else:
                putarina60 = 696.06
                putarina40 = 464.04

        if nosTer.get() == '    do 0.5 t' or nosTer.get() == '    preko 0.5 - 1.0 t' or nosTer.get() == '    preko 1.0 - 2.0 t' \
                or nosTer.get() == '    preko 2.0 - 3.0 t':
            porez = 70
        elif nosTer.get() == '    preko 3.0 - 5.0 t' or nosTer.get() == '    preko 5.0 - 7.0 t' or nosTer.get() == '    preko 7.0 - 10.0 t':
            porez = 100
        elif nosTer.get() == '    preko 10.0 - 15.0 t':
            porez = 130
        else:
            porez = 170
        if sedlasti.get() != 1:
            if nosTer.get() == '    do 0.5 t':
                polica = 487.00
                if bonus.get() == '    10%':
                    polica = 438.00
                elif bonus.get() == '    15%':
                    polica = 414.00
                elif bonus.get() == '    20%':
                    polica = 389.00
                elif bonus.get() == '    25%':
                    polica = 365.00
                elif bonus.get() == '    30%':
                    polica = 341.00
                elif bonus.get() == '    35%':
                    polica = 316.00
                elif bonus.get() == '    40%':
                    polica = 292.00
                elif bonus.get() == '    45%':
                    polica = 268.00
                elif bonus.get() == '    50%':
                    polica = 243.00
                elif bonus.get() == '   110%':
                    polica = 536.00
                elif bonus.get() == '   120%':
                    polica = 584.00
                elif bonus.get() == '   130%':
                    polica = 633.00
                elif bonus.get() == '   140%':
                    polica = 682.00
                elif bonus.get() == '   150%':
                    polica = 731.00
                elif bonus.get() == '   160%':
                    polica = 779.00
                elif bonus.get() == '   180%':
                    polica = 877.00
                elif bonus.get() == '   200%':
                    polica = 974.00

            elif nosTer.get() == '    preko 0.5 - 1.0 t':
                polica = 513.00
                if bonus.get() == '    10%':
                    polica = 462.00
                elif bonus.get() == '    15%':
                    polica = 436.00
                elif bonus.get() == '    20%':
                    polica = 411.00
                elif bonus.get() == '    25%':
                    polica = 385.00
                elif bonus.get() == '    30%':
                    polica = 359.00
                elif bonus.get() == '    35%':
                    polica = 334.00
                elif bonus.get() == '    40%':
                    polica = 308.00
                elif bonus.get() == '    45%':
                    polica = 282.00
                elif bonus.get() == '    50%':
                    polica = 257.00
                elif bonus.get() == '   110%':
                    polica = 564.00
                elif bonus.get() == '   120%':
                    polica = 616.00
                elif bonus.get() == '   130%':
                    polica = 667.00
                elif bonus.get() == '   140%':
                    polica = 718.00
                elif bonus.get() == '   150%':
                    polica = 770.00
                elif bonus.get() == '   160%':
                    polica = 821.00
                elif bonus.get() == '   180%':
                    polica = 923.00
                elif bonus.get() == '   200%':
                    polica = 1026.00

            elif nosTer.get() == '    preko 1.0 - 2.0 t':
                polica = 692.00
                if bonus.get() == '    10%':
                    polica = 623.00
                elif bonus.get() == '    15%':
                    polica = 588.00
                elif bonus.get() == '    20%':
                    polica = 554.00
                elif bonus.get() == '    25%':
                    polica = 519.00
                elif bonus.get() == '    30%':
                    polica = 485.00
                elif bonus.get() == '    35%':
                    polica = 450.00
                elif bonus.get() == '    40%':
                    polica = 415.00
                elif bonus.get() == '    45%':
                    polica = 381.00
                elif bonus.get() == '    50%':
                    polica = 346.00
                elif bonus.get() == '   110%':
                    polica = 761.00
                elif bonus.get() == '   120%':
                    polica = 830.00
                elif bonus.get() == '   130%':
                    polica = 900.00
                elif bonus.get() == '   140%':
                    polica = 969.00
                elif bonus.get() == '   150%':
                    polica = 1038.00
                elif bonus.get() == '   160%':
                    polica = 1107.00
                elif bonus.get() == '   180%':
                    polica = 1246.00
                elif bonus.get() == '   200%':
                    polica = 1384.00

            elif nosTer.get() == '    preko 2.0 - 3.0 t':
                polica = 800.00
                if bonus.get() == '    10%':
                    polica = 720.00
                elif bonus.get() == '    15%':
                    polica = 680.00
                elif bonus.get() == '    20%':
                    polica = 640.00
                elif bonus.get() == '    25%':
                    polica = 600.00
                elif bonus.get() == '    30%':
                    polica = 560.00
                elif bonus.get() == '    35%':
                    polica = 520.00
                elif bonus.get() == '    40%':
                    polica = 480.00
                elif bonus.get() == '    45%':
                    polica = 440.00
                elif bonus.get() == '    50%':
                    polica = 400.00
                elif bonus.get() == '   110%':
                    polica = 880.00
                elif bonus.get() == '   120%':
                    polica = 960.00
                elif bonus.get() == '   130%':
                    polica = 1040.00
                elif bonus.get() == '   140%':
                    polica = 1120.00
                elif bonus.get() == '   150%':
                    polica = 1200.00
                elif bonus.get() == '   160%':
                    polica = 1280.00
                elif bonus.get() == '   180%':
                    polica = 1440.00
                elif bonus.get() == '   200%':
                    polica = 1600.00

            elif nosTer.get() == '    preko 3.0 - 5.0 t':
                polica = 1011.00
                if bonus.get() == '    10%':
                    polica = 910.00
                elif bonus.get() == '    15%':
                    polica = 859.00
                elif bonus.get() == '    20%':
                    polica = 808.00
                elif bonus.get() == '    25%':
                    polica = 758.00
                elif bonus.get() == '    30%':
                    polica = 707.00
                elif bonus.get() == '    35%':
                    polica = 657.00
                elif bonus.get() == '    40%':
                    polica = 606.00
                elif bonus.get() == '    45%':
                    polica = 556.00
                elif bonus.get() == '    50%':
                    polica = 505.00
                elif bonus.get() == '   110%':
                    polica = 1112.00
                elif bonus.get() == '   120%':
                    polica = 1213.00
                elif bonus.get() == '   130%':
                    polica = 1314.00
                elif bonus.get() == '   140%':
                    polica = 1415.00
                elif bonus.get() == '   150%':
                    polica = 1517.00
                elif bonus.get() == '   160%':
                    polica = 1618.00
                elif bonus.get() == '   180%':
                    polica = 1820.00
                elif bonus.get() == '   200%':
                    polica = 2022.00

            elif nosTer.get() == '    preko 5.0 - 7.0 t':
                polica = 1319.00
                if bonus.get() == '    10%':
                    polica = 1187.00
                elif bonus.get() == '    15%':
                    polica = 1121.00
                elif bonus.get() == '    20%':
                    polica = 1055.00
                elif bonus.get() == '    25%':
                    polica = 989.00
                elif bonus.get() == '    30%':
                    polica = 923.00
                elif bonus.get() == '    35%':
                    polica = 857.00
                elif bonus.get() == '    40%':
                    polica = 791.00
                elif bonus.get() == '    45%':
                    polica = 725.00
                elif bonus.get() == '    50%':
                    polica = 659.00
                elif bonus.get() == '   110%':
                    polica = 1451.00
                elif bonus.get() == '   120%':
                    polica = 1583.00
                elif bonus.get() == '   130%':
                    polica = 1715.00
                elif bonus.get() == '   140%':
                    polica = 1847.00
                elif bonus.get() == '   150%':
                    polica = 1979.00
                elif bonus.get() == '   160%':
                    polica = 2110.00
                elif bonus.get() == '   180%':
                    polica = 2374.00
                elif bonus.get() == '   200%':
                    polica = 2638.00

            elif nosTer.get() == '    preko 7.0 - 10.0 t':
                polica = 1907.00
                if bonus.get() == '    10%':
                    polica = 1716.00
                elif bonus.get() == '    15%':
                    polica = 1621.00
                elif bonus.get() == '    20%':
                    polica = 1525.00
                elif bonus.get() == '    25%':
                    polica = 1430.00
                elif bonus.get() == '    30%':
                    polica = 1335.00
                elif bonus.get() == '    35%':
                    polica = 1239.00
                elif bonus.get() == '    40%':
                    polica = 1144.00
                elif bonus.get() == '    45%':
                    polica = 1049.00
                elif bonus.get() == '    50%':
                    polica = 953.00
                elif bonus.get() == '   110%':
                    polica = 2098.00
                elif bonus.get() == '   120%':
                    polica = 2288.00
                elif bonus.get() == '   130%':
                    polica = 2479.00
                elif bonus.get() == '   140%':
                    polica = 2670.00
                elif bonus.get() == '   150%':
                    polica = 2861.00
                elif bonus.get() == '   160%':
                    polica = 3051.00
                elif bonus.get() == '   180%':
                    polica = 3433.00
                elif bonus.get() == '   200%':
                    polica = 3814.00

            elif nosTer.get() == '    preko 10.0 - 15.0 t':
                polica = 2499.00
                if bonus.get() == '    10%':
                    polica = 2249.00
                elif bonus.get() == '    15%':
                    polica = 2124.00
                elif bonus.get() == '    20%':
                    polica = 1999.00
                elif bonus.get() == '    25%':
                    polica = 1874.00
                elif bonus.get() == '    30%':
                    polica = 1749.00
                elif bonus.get() == '    35%':
                    polica = 1624.00
                elif bonus.get() == '    40%':
                    polica = 1499.00
                elif bonus.get() == '    45%':
                    polica = 1375.00
                elif bonus.get() == '    50%':
                    polica = 1250.00
                elif bonus.get() == '   110%':
                    polica = 2749.00
                elif bonus.get() == '   120%':
                    polica = 2999.00
                elif bonus.get() == '   130%':
                    polica = 3249.00
                elif bonus.get() == '   140%':
                    polica = 3499.00
                elif bonus.get() == '   150%':
                    polica = 3749.00
                elif bonus.get() == '   160%':
                    polica = 3998.00
                elif bonus.get() == '   180%':
                    polica = 4498.00
                elif bonus.get() == '   200%':
                    polica = 4998.00
            elif nosTer.get() == '    preko 15.0 t':
                polica = 3239.00
                if bonus.get() == '    10%':
                    polica = 2915.00
                elif bonus.get() == '    15%':
                    polica = 2753.00
                elif bonus.get() == '    20%':
                    polica = 2591.00
                elif bonus.get() == '    25%':
                    polica = 2429.00
                elif bonus.get() == '    30%':
                    polica = 2267.00
                elif bonus.get() == '    35%':
                    polica = 2105.00
                elif bonus.get() == '    40%':
                    polica = 1943.00
                elif bonus.get() == '    45%':
                    polica = 1781.00
                elif bonus.get() == '    50%':
                    polica = 1619.00
                elif bonus.get() == '   110%':
                    polica = 3563.00
                elif bonus.get() == '   120%':
                    polica = 3887.00
                elif bonus.get() == '   130%':
                    polica = 4211.00
                elif bonus.get() == '   140%':
                    polica = 4535.00
                elif bonus.get() == '   150%':
                    polica = 4859.00
                elif bonus.get() == '   160%':
                    polica = 5182.00
                elif bonus.get() == '   180%':
                    polica = 5830.00
                elif bonus.get() == '   200%':
                    polica = 6478.00
        else:
            if snaga.get() == '    do 18 kW':
                polica = 452.00
                if bonus.get() == '    10%':
                    polica = 407.00
                elif bonus.get() == '    15%':
                    polica = 384.00
                elif bonus.get() == '    20%':
                    polica = 362.00
                elif bonus.get() == '    25%':
                    polica = 339.00
                elif bonus.get() == '    30%':
                    polica = 317.00
                elif bonus.get() == '    35%':
                    polica = 294.00
                elif bonus.get() == '    40%':
                    polica = 271.00
                elif bonus.get() == '    45%':
                    polica = 249.00
                elif bonus.get() == '    50%':
                    polica = 226.00
                elif bonus.get() == '   110%':
                    polica = 497.00
                elif bonus.get() == '   120%':
                    polica = 542.00
                elif bonus.get() == '   130%':
                    polica = 588.00
                elif bonus.get() == '   140%':
                    polica = 633.00
                elif bonus.get() == '   150%':
                    polica = 678.00
                elif bonus.get() == '   160%':
                    polica = 723.00
                elif bonus.get() == '   180%':
                    polica = 814.00
                elif bonus.get() == '   200%':
                    polica = 904.00

            elif snaga.get() == '    19 kW - 25 kW':
                polica = 648.00
                if bonus.get() == '    10%':
                    polica = 583.00
                elif bonus.get() == '    15%':
                    polica = 551.00
                elif bonus.get() == '    20%':
                    polica = 518.00
                elif bonus.get() == '    25%':
                    polica = 486.00
                elif bonus.get() == '    30%':
                    polica = 453.00
                elif bonus.get() == '    35%':
                    polica = 421.00
                elif bonus.get() == '    40%':
                    polica = 389.00
                elif bonus.get() == '    45%':
                    polica = 356.00
                elif bonus.get() == '    50%':
                    polica = 324.00
                elif bonus.get() == '   110%':
                    polica = 713.00
                elif bonus.get() == '   120%':
                    polica = 778.00
                elif bonus.get() == '   130%':
                    polica = 842.00
                elif bonus.get() == '   140%':
                    polica = 907.00
                elif bonus.get() == '   150%':
                    polica = 972.00
                elif bonus.get() == '   160%':
                    polica = 1037.00
                elif bonus.get() == '   180%':
                    polica = 1166.00
                elif bonus.get() == '   200%':
                    polica = 1296.00
            elif snaga.get() == '    26 kW - 33 kW':
                polica = 743.00
                if bonus.get() == '    10%':
                    polica = 668.00
                elif bonus.get() == '    15%':
                    polica = 631.00
                elif bonus.get() == '    20%':
                    polica = 594.00
                elif bonus.get() == '    25%':
                    polica = 557.00
                elif bonus.get() == '    30%':
                    polica = 520.00
                elif bonus.get() == '    35%':
                    polica = 483.00
                elif bonus.get() == '    40%':
                    polica = 446.00
                elif bonus.get() == '    45%':
                    polica = 408.00
                elif bonus.get() == '    50%':
                    polica = 371.00
                elif bonus.get() == '   110%':
                    polica = 817.00
                elif bonus.get() == '   120%':
                    polica = 892.00
                elif bonus.get() == '   130%':
                    polica = 966.00
                elif bonus.get() == '   140%':
                    polica = 1040.00
                elif bonus.get() == '   150%':
                    polica = 1115.00
                elif bonus.get() == '   160%':
                    polica = 1189.00
                elif bonus.get() == '   180%':
                    polica = 1337.00
                elif bonus.get() == '   200%':
                    polica = 1486.00
            elif snaga.get() == '    34 kW - 44 kW':
                polica = 908.00
                if bonus.get() == '    10%':
                    polica = 818.00
                elif bonus.get() == '    15%':
                    polica = 772.00
                elif bonus.get() == '    20%':
                    polica = 727.00
                elif bonus.get() == '    25%':
                    polica = 681.00
                elif bonus.get() == '    30%':
                    polica = 636.00
                elif bonus.get() == '    35%':
                    polica = 590.00
                elif bonus.get() == '    40%':
                    polica = 545.00
                elif bonus.get() == '    45%':
                    polica = 500.00
                elif bonus.get() == '    50%':
                    polica = 454.00
                elif bonus.get() == '   110%':
                    polica = 999.00
                elif bonus.get() == '   120%':
                    polica = 1090.00
                elif bonus.get() == '   130%':
                    polica = 1180.00
                elif bonus.get() == '   140%':
                    polica = 1271.00
                elif bonus.get() == '   150%':
                    polica = 1362.00
                elif bonus.get() == '   160%':
                    polica = 1453.00
                elif bonus.get() == '   180%':
                    polica = 1634.00
                elif bonus.get() == '   200%':
                    polica = 1816.00
            elif snaga.get() == '    45 kW - 73 kW':
                polica = 1269.00
                if bonus.get() == '    10%':
                    polica = 1142.00
                elif bonus.get() == '    15%':
                    polica = 1079.00
                elif bonus.get() == '    20%':
                    polica = 1015.00
                elif bonus.get() == '    25%':
                    polica = 952.00
                elif bonus.get() == '    30%':
                    polica = 888.00
                elif bonus.get() == '    35%':
                    polica = 825.00
                elif bonus.get() == '    40%':
                    polica = 762.00
                elif bonus.get() == '    45%':
                    polica = 698.00
                elif bonus.get() == '    50%':
                    polica = 635.00
                elif bonus.get() == '   110%':
                    polica = 1396.00
                elif bonus.get() == '   120%':
                    polica = 1523.00
                elif bonus.get() == '   130%':
                    polica = 1650.00
                elif bonus.get() == '   140%':
                    polica = 1777.00
                elif bonus.get() == '   150%':
                    polica = 1904.00
                elif bonus.get() == '   160%':
                    polica = 2030.00
                elif bonus.get() == '   180%':
                    polica = 2284.00
                elif bonus.get() == '   200%':
                    polica = 2538.00
            elif snaga.get() == '    74 kW - 110 kW':
                polica = 1861.00
                if bonus.get() == '    10%':
                    polica = 1675.00
                elif bonus.get() == '    15%':
                    polica = 1582.00
                elif bonus.get() == '    20%':
                    polica = 1489.00
                elif bonus.get() == '    25%':
                    polica = 1396.00
                elif bonus.get() == '    30%':
                    polica = 1303.00
                elif bonus.get() == '    35%':
                    polica = 1210.00
                elif bonus.get() == '    40%':
                    polica = 1117.00
                elif bonus.get() == '    45%':
                    polica = 1024.00
                elif bonus.get() == '    50%':
                    polica = 931.00
                elif bonus.get() == '   110%':
                    polica = 2047.00
                elif bonus.get() == '   120%':
                    polica = 2233.00
                elif bonus.get() == '   130%':
                    polica = 2419.00
                elif bonus.get() == '   140%':
                    polica = 2605.00
                elif bonus.get() == '   150%':
                    polica = 2792.00
                elif bonus.get() == '   160%':
                    polica = 2978.00
                elif bonus.get() == '   180%':
                    polica = 3350.00
                elif bonus.get() == '   200%':
                    polica = 3722.00
            elif snaga.get() == '    111 kW - 147 kW':
                polica = 2524.00
                if bonus.get() == '    10%':
                    polica = 2271.00
                elif bonus.get() == '    15%':
                    polica = 2145.00
                elif bonus.get() == '    20%':
                    polica = 2019.00
                elif bonus.get() == '    25%':
                    polica = 1893.00
                elif bonus.get() == '    30%':
                    polica = 1767.00
                elif bonus.get() == '    35%':
                    polica = 1640.00
                elif bonus.get() == '    40%':
                    polica = 1514.00
                elif bonus.get() == '    45%':
                    polica = 1388.00
                elif bonus.get() == '    50%':
                    polica = 1262.00
                elif bonus.get() == '   110%':
                    polica = 2776.00
                elif bonus.get() == '   120%':
                    polica = 3029.00
                elif bonus.get() == '   130%':
                    polica = 3281.00
                elif bonus.get() == '   140%':
                    polica = 3534.00
                elif bonus.get() == '   150%':
                    polica = 3786.00
                elif bonus.get() == '   160%':
                    polica = 4038.00
                elif bonus.get() == '   180%':
                    polica = 4543.00
                elif bonus.get() == '   200%':
                    polica = 5048.00
            elif snaga.get() == '    preko 147 kW':
                polica = 3185.00
                if bonus.get() == '    10%':
                    polica = 2866.00
                elif bonus.get() == '    15%':
                    polica = 2707.00
                elif bonus.get() == '    20%':
                    polica = 2548.00
                elif bonus.get() == '    25%':
                    polica = 2388.00
                elif bonus.get() == '    30%':
                    polica = 2229.00
                elif bonus.get() == '    35%':
                    polica = 2070.00
                elif bonus.get() == '    40%':
                    polica = 1911.00
                elif bonus.get() == '    45%':
                    polica = 1752.00
                elif bonus.get() == '    50%':
                    polica = 1592.00
                elif bonus.get() == '   110%':
                    polica = 3504.00
                elif bonus.get() == '   120%':
                    polica = 3822.00
                elif bonus.get() == '   130%':
                    polica = 4141.00
                elif bonus.get() == '   140%':
                    polica = 4459.00
                elif bonus.get() == '   150%':
                    polica = 4778.00
                elif bonus.get() == '   160%':
                    polica = 5096.00
                elif bonus.get() == '   180%':
                    polica = 5733.00
                elif bonus.get() == '   200%':
                    polica = 6370.00

        if zapaljiviV.get() == 1:
            dodatak = polica * 15 / 100

        polica += dodatak

        if int(zapremina.get()) < 1401:
            okolis = 0
        elif 2001 > int(zapremina.get()) > 1400:
            if year_ - int(godProz.get()) > 30:
                okolis = 144
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 126
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 108
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 99
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 90
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 85.5
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 81

        elif 4001 > int(zapremina.get()) > 2000:
            if year_ - int(godProz.get()) > 30:
                okolis = 172.8
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 151.2
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 129.6
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 118.8
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 108
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 102.6
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 97.2

        elif 8001 > int(zapremina.get()) > 4000:
            if year_ - int(godProz.get()) > 30:
                okolis = 201.6
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 176.4
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 151.2
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 138.6
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 126
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 119.7
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 113.4
        elif 12001 > int(zapremina.get()) > 8000:
            if year_ - int(godProz.get()) > 30:
                okolis = 230.4
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 201.6
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 172.8
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 158.4
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 144
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 136.8
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 129.6
        elif 16001 > int(zapremina.get()) > 12000:
            if year_ - int(godProz.get()) > 30:
                okolis = 259.2
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 226.8
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 194.4
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 178.2
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 162
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 153.9
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 145.8
        elif int(zapremina.get()) > 16000:
            if year_ - int(godProz.get()) > 30:
                okolis = 288
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 252
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 216
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 198
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 180
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 171
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 162

    if vrstaVoz.get() == '    Putničko':

        pomocPut = 8

        if ugV.get() == 1:
            komUg = 20

        if vrstaGor.get() == '    Dizel':
            tehnicki = 91
        else:
            tehnicki = 87
            if int(godProz.get()) > 1992:
                tehnicki = 87
            else:
                tehnicki = 77

        if 751 > int(zapremina.get()) > 250:
            if year_ - int(godProz.get()) > 30:
                okolis = 21.60
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 18.90
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 16.20
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 14.85
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 13.50
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 12.83
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 12.15

        elif 1401 > int(zapremina.get()) > 750:
            if year_ - int(godProz.get()) > 30:
                okolis = 22.8
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 19.95
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 17.10
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 15.68
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 14.25
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 13.55
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 12.83

        elif 2001 > int(zapremina.get()) > 1400:
            if year_ - int(godProz.get()) > 30:
                okolis = 24
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 21
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 18
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 16.5
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 15
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 14.25
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 13.5

        elif 4001 > int(zapremina.get()) > 2000:
            if year_ - int(godProz.get()) > 30:
                okolis = 28.8
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 25.2
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 21.6
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 19.8
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 18
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 17.1
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 16.2

        elif 8001 > int(zapremina.get()) > 4000:
            if year_ - int(godProz.get()) > 30:
                okolis = 33.6
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 29.4
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 25.2
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 23.1
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 21
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 19.95
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 18.9

        if snaga.get() == '    do 22 kW':
            polica = 230.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 196.00
            if bonus.get() == '    10%':
                polica = 207.00
                if invalidV.get() == 1:
                    polica = 196.00
            elif bonus.get() == '    15%':
                polica = 196.00
            elif bonus.get() == '    20%':
                polica = 184.00
            elif bonus.get() == '    25%':
                polica = 173.00
            elif bonus.get() == '    30%':
                polica = 161.00
            elif bonus.get() == '    35%':
                polica = 150.00
            elif bonus.get() == '    40%':
                polica = 138.00
            elif bonus.get() == '    45%':
                polica = 127.00
            elif bonus.get() == '    50%':
                polica = 115.00
            elif bonus.get() == '   110%':
                polica = 253.00
            elif bonus.get() == '   120%':
                polica = 276.00
            elif bonus.get() == '   130%':
                polica = 299.00
            elif bonus.get() == '   140%':
                polica = 322.00
            elif bonus.get() == '   150%':
                polica = 345.00
            elif bonus.get() == '   160%':
                polica = 368.00
            elif bonus.get() == '   180%':
                polica = 414.00
            elif bonus.get() == '   200%':
                polica = 460.00

        elif snaga.get() == '    23 kW - 33 kW':
            polica = 328.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 279.00
            if bonus.get() == '    10%':
                polica = 295.00
                if invalidV.get() == 1:
                    polica = 279.00
            elif bonus.get() == '    15%':
                polica = 279.00
            elif bonus.get() == '    20%':
                polica = 263.00
            elif bonus.get() == '    25%':
                polica = 246.00
            elif bonus.get() == '    30%':
                polica = 230.00
            elif bonus.get() == '    35%':
                polica = 213.00
            elif bonus.get() == '    40%':
                polica = 197.00
            elif bonus.get() == '    45%':
                polica = 181.00
            elif bonus.get() == '    50%':
                polica = 164.00
            elif bonus.get() == '   110%':
                polica = 361.00
            elif bonus.get() == '   120%':
                polica = 394.00
            elif bonus.get() == '   130%':
                polica = 426.00
            elif bonus.get() == '   140%':
                polica = 459.00
            elif bonus.get() == '   150%':
                polica = 492.00
            elif bonus.get() == '   160%':
                polica = 525.00
            elif bonus.get() == '   180%':
                polica = 590.00
            elif bonus.get() == '   200%':
                polica = 656.00


        elif snaga.get() == '    34 kW - 44 kW':
            polica = 396.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 337.00
            if bonus.get() == '    10%':
                polica = 356.00
                if invalidV.get() == 1:
                    polica = 337.00
            elif bonus.get() == '    15%':
                polica = 337.00
            elif bonus.get() == '    20%':
                polica = 317.00
            elif bonus.get() == '    25%':
                polica = 297.00
            elif bonus.get() == '    30%':
                polica = 277.00
            elif bonus.get() == '    35%':
                polica = 257.00
            elif bonus.get() == '    40%':
                polica = 238.00
            elif bonus.get() == '    45%':
                polica = 218.00
            elif bonus.get() == '    50%':
                polica = 198.00
            elif bonus.get() == '   110%':
                polica = 436.00
            elif bonus.get() == '   120%':
                polica = 475.00
            elif bonus.get() == '   130%':
                polica = 515.00
            elif bonus.get() == '   140%':
                polica = 554.00
            elif bonus.get() == '   150%':
                polica = 594.00
            elif bonus.get() == '   160%':
                polica = 634.00
            elif bonus.get() == '   180%':
                polica = 713.00
            elif bonus.get() == '   200%':
                polica = 792.00

        elif snaga.get() == '    45 kW - 55 kW':
            polica = 461.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 391.00
            if bonus.get() == '    10%':
                polica = 414.00
                if invalidV.get() == 1:
                    polica = 391.00
            elif bonus.get() == '    15%':
                polica = 391.00
            elif bonus.get() == '    20%':
                polica = 368.00
            elif bonus.get() == '    25%':
                polica = 345.00
            elif bonus.get() == '    30%':
                polica = 322.00
            elif bonus.get() == '    35%':
                polica = 299.00
            elif bonus.get() == '    40%':
                polica = 276.00
            elif bonus.get() == '    45%':
                polica = 253.00
            elif bonus.get() == '    50%':
                polica = 230.00
            elif bonus.get() == '   110%':
                polica = 507.00
            elif bonus.get() == '   120%':
                polica = 553.00
            elif bonus.get() == '   130%':
                polica = 599.00
            elif bonus.get() == '   140%':
                polica = 645.00
            elif bonus.get() == '   150%':
                polica = 692.00
            elif bonus.get() == '   160%':
                polica = 738.00
            elif bonus.get() == '   180%':
                polica = 830.00
            elif bonus.get() == '   200%':
                polica = 922.00

        elif snaga.get() == '    56 kW - 66 kW':
            polica = 525.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 446.00
            if bonus.get() == '    10%':
                polica = 473.00
                if invalidV.get() == 1:
                    polica = 446.00
            elif bonus.get() == '    15%':
                polica = 446.00
            elif bonus.get() == '    20%':
                polica = 420.00
            elif bonus.get() == '    25%':
                polica = 394.00
            elif bonus.get() == '    30%':
                polica = 368.00
            elif bonus.get() == '    35%':
                polica = 341.00
            elif bonus.get() == '    40%':
                polica = 315.00
            elif bonus.get() == '    45%':
                polica = 289.00
            elif bonus.get() == '    50%':
                polica = 263.00
            elif bonus.get() == '   110%':
                polica = 578.00
            elif bonus.get() == '   120%':
                polica = 630.00
            elif bonus.get() == '   130%':
                polica = 683.00
            elif bonus.get() == '   140%':
                polica = 735.00
            elif bonus.get() == '   150%':
                polica = 788.00
            elif bonus.get() == '   160%':
                polica = 840.00
            elif bonus.get() == '   180%':
                polica = 945.00
            elif bonus.get() == '   200%':
                polica = 1050.00

        elif snaga.get() == '    67 kW - 84 kW':
            polica = 578.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 491.00
            if bonus.get() == '    10%':
                polica = 520.00
                if invalidV.get() == 1:
                    polica = 491.00
            elif bonus.get() == '    15%':
                polica = 491.00
            elif bonus.get() == '    20%':
                polica = 463.00
            elif bonus.get() == '    25%':
                polica = 434.00
            elif bonus.get() == '    30%':
                polica = 405.00
            elif bonus.get() == '    35%':
                polica = 376.00
            elif bonus.get() == '    40%':
                polica = 347.00
            elif bonus.get() == '    45%':
                polica = 318.00
            elif bonus.get() == '    50%':
                polica = 289.00
            elif bonus.get() == '   110%':
                polica = 636.00
            elif bonus.get() == '   120%':
                polica = 694.00
            elif bonus.get() == '   130%':
                polica = 751.00
            elif bonus.get() == '   140%':
                polica = 809.00
            elif bonus.get() == '   150%':
                polica = 867.00
            elif bonus.get() == '   160%':
                polica = 925.00
            elif bonus.get() == '   180%':
                polica = 1040.00
            elif bonus.get() == '   200%':
                polica = 1156.00

        elif snaga.get() == '    85 kW - 110 kW':
            polica = 692.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 588.00
            if bonus.get() == '    10%':
                polica = 623.00
                if invalidV.get() == 1:
                    polica = 588.00
            elif bonus.get() == '    15%':
                polica = 588.00
            elif bonus.get() == '    20%':
                polica = 553.00
            elif bonus.get() == '    25%':
                polica = 519.00
            elif bonus.get() == '    30%':
                polica = 484.00
            elif bonus.get() == '    35%':
                polica = 450.00
            elif bonus.get() == '    40%':
                polica = 415.00
            elif bonus.get() == '    45%':
                polica = 380.00
            elif bonus.get() == '    50%':
                polica = 346.00
            elif bonus.get() == '   110%':
                polica = 761.00
            elif bonus.get() == '   120%':
                polica = 830.00
            elif bonus.get() == '   130%':
                polica = 900.00
            elif bonus.get() == '   140%':
                polica = 969.00
            elif bonus.get() == '   150%':
                polica = 1038.00
            elif bonus.get() == '   160%':
                polica = 1107.00
            elif bonus.get() == '   180%':
                polica = 1246.00
            elif bonus.get() == '   200%':
                polica = 1384.00

        elif snaga.get() == '    preko 110 kW':
            polica = 831.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if invalidV.get() == 1:
                    polica = 707.00
            if bonus.get() == '    10%':
                polica = 748.00
                if invalidV.get() == 1:
                    polica = 707.00
            elif bonus.get() == '    15%':
                polica = 707.00
            elif bonus.get() == '    20%':
                polica = 665.00
            elif bonus.get() == '    25%':
                polica = 623.00
            elif bonus.get() == '    30%':
                polica = 582.00
            elif bonus.get() == '    35%':
                polica = 540.00
            elif bonus.get() == '    40%':
                polica = 499.00
            elif bonus.get() == '    45%':
                polica = 457.00
            elif bonus.get() == '    50%':
                polica = 416.00
            elif bonus.get() == '   110%':
                polica = 914.00
            elif bonus.get() == '   120%':
                polica = 997.00
            elif bonus.get() == '   130%':
                polica = 1080.00
            elif bonus.get() == '   140%':
                polica = 1163.00
            elif bonus.get() == '   150%':
                polica = 1247.00
            elif bonus.get() == '   160%':
                polica = 1330.00
            elif bonus.get() == '   180%':
                polica = 1496.00
            elif bonus.get() == '   200%':
                polica = 1662.00

        if taxiV.get() == 1:
            dodatak = polica * 40 / 100
        elif rentV.get() == 1:
            dodatak = polica * 125 / 100
        elif kombiV.get() == 1 or kombiTeretV.get() == 1:
            dodatak = polica * 10 / 100
        else:
            dodatak = 0.00

        polica += dodatak

        if an.get() == '    2.85 KM':
            polica += 2.85
        elif an.get() == '    5.70 KM':
            polica += 5.70
        elif an.get() == '    8.55 KM':
            polica += 8.55
        elif an.get() == '  11.40 KM':
            polica += 11.40
        elif an.get() == '  14.25 KM':
            polica += 14.25
        elif an.get() == '  17.10 KM':
            polica += 17.10
        elif an.get() == '  19.95 KM':
            polica += 19.95
        elif an.get() == '  22.80 KM':
            polica += 22.80
        elif an.get() == '  25.65 KM':
            polica += 25.65
        elif an.get() == '  28.50 KM':
            polica += 28.50
        elif an.get() == '  31.35 KM':
            polica += 31.35
        elif an.get() == '  34.20 KM':
            polica += 34.20
        elif an.get() == '  39.90 KM':
            polica += 39.90
        elif an.get() == '  42.75 KM':
            polica += 42.75
        elif an.get() == '  45.60 KM':
            polica += 45.60
        elif an.get() == '  48.45 KM':
            polica += 48.45
        elif an.get() == '  51.30 KM':
            polica += 51.30
        elif an.get() == '  54.15 KM':
            polica += 54.15
        elif an.get() == '  57.00 KM':
            polica += 57.00
        elif an.get() == '  59.85 KM':
            polica += 59.85
        elif an.get() == '  62.70 KM':
            polica += 62.70
        elif an.get() == '  65.55 KM':
            polica += 65.55
        elif an.get() == '  68.40 KM':
            polica += 68.40
        elif an.get() == '  71.25 KM':
            polica += 71.25

        if int(zapremina.get()) < 1001:
            putarina60 = 28.8
            putarina40 = 19.2
        elif 1601 > int(zapremina.get()) > 1000:
            putarina60 = 36
            putarina40 = 24
        elif 2001 > int(zapremina.get()) > 1600:
            putarina60 = 45
            putarina40 = 30
        elif 2501 > int(zapremina.get()) > 2000:
            putarina60 = 84.06
            putarina40 = 56.04
        elif int(zapremina.get()) > 2500:
            putarina60 = 126
            putarina40 = 84

        tmpT60 = 0
        tmpT40 = 0
        tmpP60 = 0
        tmpP40 = 0

        if terenskoV.get() == 1:
            if int(zapremina.get()) > 2500 or int(zapremina.get()) < 2001:
                tmpT60 = (putarina60 * 20) / 100
                tmpT40 = (putarina40 * 20) / 100
            else:
                tmpT60 = 16.74
                tmpT40 = 11.16

        if vrstaGor.get() == '    Plin':
            tmpP60 = (putarina60 * 25) / 100
            tmpP40 = (putarina40 * 25) / 100

        putarina60 += tmpT60
        putarina60 += tmpP60

        putarina40 += tmpT40
        putarina40 += tmpP40

        if int(zapremina.get()) < 1601:
            if year_ - int(godProz.get()) > 9:
                porez = 10
            elif 10 > year_ - int(godProz.get()) > 4:
                porez = 25
            elif 5 > year_ - int(godProz.get()) > 1:
                porez = 35
            elif 2 > year_ - int(godProz.get()) >= 0:
                porez = 50

        if int(zapremina.get()) > 1600:
            if year_ - int(godProz.get()) > 9:
                porez = 20
            elif 10 > year_ - int(godProz.get()) > 4:
                porez = 40
            elif 5 > year_ - int(godProz.get()) > 1:
                porez = 50
            elif 2 > year_ - int(godProz.get()) >= 0:
                porez = 70

    if vrstaVoz.get() == '    Priključno':
        porez = 0
        okolis = 0
        pomocPut = 15

        if vrstaReg.get() == '    Prva registracija':
            regTab = 10

        if vrPrik.get() == '    O1':
            tehnicki = 19.83
        elif vrPrik.get() == '    O2':
            tehnicki = 50.16
        elif vrPrik.get() == '    O3':
            tehnicki = 70
        elif vrPrik.get() == '    O4':
            tehnicki = 79.33

        if maxNosPrik.get() == '    do 750 kg' and vrPrik.get() == '    O1':
            putarina60 = 13.5
            putarina40 = 9

        if vrPrik.get() == '    O2':
            if maxNosPrik.get() == '    751 - 1000 kg':
                putarina60 = 30.06
                putarina40 = 20.04
            elif maxNosPrik.get() == '    1001 - 2000 kg':
                putarina60 = 41.94
                putarina40 = 27.96
            elif maxNosPrik.get() == '    2001 - 3000 kg':
                putarina60 = 54
                putarina40 = 36
            elif maxNosPrik.get() == '    3001 - 3500 kg':
                putarina60 = 66.06
                putarina40 = 44.04
        if vrPrik.get() == '    O3':
            if maxNosPrik.get() == '    3501 - 5000 kg':
                putarina60 = 90
                putarina40 = 60
            elif maxNosPrik.get() == '    5001 - 6000 kg':
                putarina60 = 102.06
                putarina40 = 68.04
            elif maxNosPrik.get() == '    6001 - 7000 kg':
                putarina60 = 113.94
                putarina40 = 75.96
            elif maxNosPrik.get() == '    7001 - 8000 kg':
                putarina60 = 126
                putarina40 = 84
            elif maxNosPrik.get() == '    8001 - 9000 kg':
                putarina60 = 138.06
                putarina40 = 92.04
            elif maxNosPrik.get() == '    9001 - 10000 kg':
                putarina60 = 149.94
                putarina40 = 99.96
            else:
                putarina60 = 171
                putarina40 = 114
        if vrPrik.get() == '    O4':
            if db.get() == '    Prikolice DB i DC':
                if brOsPrik.get() == '    Dvije osovine':
                    if maxNosPrik.get() == '    10001 - 11000 kg':
                        putarina60 = 171
                        putarina40 = 114
                    elif maxNosPrik.get() == '    11001 - 12000 kg':
                        putarina60 = 192.06
                        putarina40 = 128.04
                    elif maxNosPrik.get() == '    12001 - 13000 kg':
                        putarina60 = 212.94
                        putarina40 = 141.96
                    elif maxNosPrik.get() == '    13001 - 14000 kg':
                        putarina60 = 234
                        putarina40 = 156
                    elif maxNosPrik.get() == '    14001 - 15000 kg':
                        putarina60 = 255.06
                        putarina40 = 170.04
                    elif maxNosPrik.get() == '    15001 - 16000 kg':
                        putarina60 = 275.94
                        putarina40 = 183.96
                    elif maxNosPrik.get() == '    16001 - 17000 kg':
                        putarina60 = 297
                        putarina40 = 198
                    elif maxNosPrik.get() == '    17001 - 18000 kg':
                        putarina60 = 316.80
                        putarina40 = 211.2
                    else:
                        putarina60 = 338.94
                        putarina40 = 225.96
                else:
                    if maxNosPrik.get() == '    10001 - 11000 kg':
                        putarina60 = 188.1
                        putarina40 = 125.4
                    elif maxNosPrik.get() == '    11001 - 12000 kg':
                        putarina60 = 211.32
                        putarina40 = 140.88
                    elif maxNosPrik.get() == '    12001 - 13000 kg':
                        putarina60 = 234.18
                        putarina40 = 156.12
                    elif maxNosPrik.get() == '    13001 - 14000 kg':
                        putarina60 = 257.4
                        putarina40 = 171.6
                    elif maxNosPrik.get() == '    14001 - 15000 kg':
                        putarina60 = 280.44
                        putarina40 = 186.96
                    elif maxNosPrik.get() == '    15001 - 16000 kg':
                        putarina60 = 303.48
                        putarina40 = 202.32
                    elif maxNosPrik.get() == '    16001 - 17000 kg':
                        putarina60 = 326.7
                        putarina40 = 217.8
                    elif maxNosPrik.get() == '    17001 - 18000 kg':
                        putarina60 = 348.48
                        putarina40 = 232.32
                    elif maxNosPrik.get() == '    18001 - 19000 kg':
                        putarina60 = 358.2
                        putarina40 = 238.8
                    elif maxNosPrik.get() == '    19001 - 20000 kg':
                        putarina60 = 360
                        putarina40 = 240
                    elif maxNosPrik.get() == '    20001 - 21000 kg':
                        putarina60 = 381.06
                        putarina40 = 254.04
                    elif maxNosPrik.get() == '    21001 - 22000 kg':
                        putarina60 = 401.94
                        putarina40 = 267.96
                    elif maxNosPrik.get() == '    22001 - 23000 kg':
                        putarina60 = 423
                        putarina40 = 282
                    elif maxNosPrik.get() == '    23001 - 24000 kg':
                        putarina60 = 444.06
                        putarina40 = 296.04
                    elif maxNosPrik.get() == '    preko 24000 kg':
                        putarina60 = 464.94
                        putarina40 = 309.96
            elif db.get() == '    Poluprikolica DA':
                if brOsPrik.get() == '    Jedna osovina':
                    putarina60 = 171
                    putarina40 = 114
                elif brOsPrik.get() == '    Dvije osovine':
                    if maxNosPrik.get() == '    10001 - 11000 kg':
                        putarina60 = 171
                        putarina40 = 114
                    elif maxNosPrik.get() == '    11001 - 12000 kg':
                        putarina60 = 192.06
                        putarina40 = 128.04
                    elif maxNosPrik.get() == '    12001 - 13000 kg':
                        putarina60 = 212.94
                        putarina40 = 141.96
                    elif maxNosPrik.get() == '    13001 - 14000 kg':
                        putarina60 = 234
                        putarina40 = 156
                    elif maxNosPrik.get() == '    14001 - 15000 kg':
                        putarina60 = 255.06
                        putarina40 = 170.04
                    elif maxNosPrik.get() == '    15001 - 16000 kg':
                        putarina60 = 275.94
                        putarina40 = 183.96
                    elif maxNosPrik.get() == '    16001 - 17000 kg':
                        putarina60 = 297
                        putarina40 = 198
                    elif maxNosPrik.get() == '    17001 - 18000 kg':
                        putarina60 = 318.06
                        putarina40 = 212.04
                    else:
                        putarina60 = 338.94
                        putarina40 = 225.96
                elif brOsPrik.get() == '    Tri osovine':
                    if maxNosPrik.get() == '    10001 - 11000 kg':
                        putarina60 = 171
                        putarina40 = 114
                    elif maxNosPrik.get() == '    11001 - 12000 kg':
                        putarina60 = 192.06
                        putarina40 = 128.04
                    elif maxNosPrik.get() == '    12001 - 13000 kg':
                        putarina60 = 212.94
                        putarina40 = 141.96
                    elif maxNosPrik.get() == '    13001 - 14000 kg':
                        putarina60 = 234
                        putarina40 = 156
                    elif maxNosPrik.get() == '    14001 - 15000 kg':
                        putarina60 = 255.06
                        putarina40 = 170.04
                    elif maxNosPrik.get() == '    15001 - 16000 kg':
                        putarina60 = 275.94
                        putarina40 = 183.96
                    elif maxNosPrik.get() == '    16001 - 17000 kg':
                        putarina60 = 297
                        putarina40 = 198
                    elif maxNosPrik.get() == '    17001 - 18000 kg':
                        putarina60 = 318.06
                        putarina40 = 212.04
                    elif maxNosPrik.get() == '    18001 - 19000 kg':
                        putarina60 = 338.94
                        putarina40 = 225.96
                    elif maxNosPrik.get() == '    19001 - 20000 kg':
                        putarina60 = 360
                        putarina40 = 240
                    elif maxNosPrik.get() == '    20001 - 21000 kg':
                        putarina60 = 381.06
                        putarina40 = 254.04
                    elif maxNosPrik.get() == '    21001 - 22000 kg':
                        putarina60 = 401.94
                        putarina40 = 267.96
                    elif maxNosPrik.get() == '    22001 - 23000 kg':
                        putarina60 = 423
                        putarina40 = 282
                    elif maxNosPrik.get() == '    23001 - 24000 kg':
                        putarina60 = 444.06
                        putarina40 = 296.04
                    elif maxNosPrik.get() == '    preko 24000 kg':
                        putarina60 = 464.94
                        putarina40 = 309.96
                if maxNosPrik.get() == '    9001 - 10000 kg' or maxNosPrik.get() == '    8001 - 9000 kg' \
                        or maxNosPrik.get() == '    7001 - 8000 kg' or maxNosPrik.get() == '    6001 - 7000 kg' or maxNosPrik.get() == '    5001 - 6000 kg':
                    putarina60 = 149.94
                    putarina40 = 99.96
            elif db.get() == '    Poluprikolica DA, prikolice DB, DC':
                if brOsPrik.get() == '    Četiri osovine':
                    putarina60 = 261
                    putarina40 = 174
                elif brOsPrik.get() == '    Pet osovina':
                    putarina60 = 279
                    putarina40 = 186
                elif brOsPrik.get() == '    Šest i više osovina':
                    putarina60 = 297
                    putarina40 = 198
        if nosPrik.get() == '    do 1 t':
            polica = 32.00
            if bonus.get() == '    10%':
                polica = 29.00
            elif bonus.get() == '    15%':
                polica = 27.00
            elif bonus.get() == '    20%':
                polica = 26.00
            elif bonus.get() == '    25%':
                polica = 24.00
            elif bonus.get() == '    30%':
                polica = 22.00
            elif bonus.get() == '    35%':
                polica = 21.00
            elif bonus.get() == '    40%':
                polica = 19.00
            elif bonus.get() == '    45%':
                polica = 18.00
            elif bonus.get() == '    50%':
                polica = 16.00
            elif bonus.get() == '   110%':
                polica = 35.00
            elif bonus.get() == '   120%':
                polica = 38.00
            elif bonus.get() == '   130%':
                polica = 42.00
            elif bonus.get() == '   140%':
                polica = 45.00
            elif bonus.get() == '   150%':
                polica = 48.00
            elif bonus.get() == '   160%':
                polica = 51.00
            elif bonus.get() == '   180%':
                polica = 58.00
            elif bonus.get() == '   200%':
                polica = 64.00
        elif nosPrik.get() == '    preko 1 - 3 t':
            polica = 33.00
            if bonus.get() == '    10%':
                polica = 30.00
            elif bonus.get() == '    15%':
                polica = 28.00
            elif bonus.get() == '    20%':
                polica = 27.00
            elif bonus.get() == '    25%':
                polica = 25.00
            elif bonus.get() == '    30%':
                polica = 23.00
            elif bonus.get() == '    35%':
                polica = 22.00
            elif bonus.get() == '    40%':
                polica = 20.00
            elif bonus.get() == '    45%':
                polica = 18.00
            elif bonus.get() == '    50%':
                polica = 17.00
            elif bonus.get() == '   110%':
                polica = 36.00
            elif bonus.get() == '   120%':
                polica = 40.00
            elif bonus.get() == '   130%':
                polica = 43.00
            elif bonus.get() == '   140%':
                polica = 46.00
            elif bonus.get() == '   150%':
                polica = 50.00
            elif bonus.get() == '   160%':
                polica = 53.00
            elif bonus.get() == '   180%':
                polica = 59.00
            elif bonus.get() == '   200%':
                polica = 66.00
        elif nosPrik.get() == '    preko 3 - 5 t':
            polica = 35.00
            if bonus.get() == '    10%':
                polica = 32.00
            elif bonus.get() == '    15%':
                polica = 30.00
            elif bonus.get() == '    20%':
                polica = 28.00
            elif bonus.get() == '    25%':
                polica = 26.00
            elif bonus.get() == '    30%':
                polica = 25.00
            elif bonus.get() == '    35%':
                polica = 23.00
            elif bonus.get() == '    40%':
                polica = 21.00
            elif bonus.get() == '    45%':
                polica = 19.00
            elif bonus.get() == '    50%':
                polica = 18.00
            elif bonus.get() == '   110%':
                polica = 39.00
            elif bonus.get() == '   120%':
                polica = 42.00
            elif bonus.get() == '   130%':
                polica = 46.00
            elif bonus.get() == '   140%':
                polica = 49.00
            elif bonus.get() == '   150%':
                polica = 53.00
            elif bonus.get() == '   160%':
                polica = 56.00
            elif bonus.get() == '   180%':
                polica = 63.00
            elif bonus.get() == '   200%':
                polica = 70.00
        elif nosPrik.get() == '    preko 5 - 10 t':
            polica = 38.00
            if bonus.get() == '    10%':
                polica = 35.00
            elif bonus.get() == '    15%':
                polica = 33.00
            elif bonus.get() == '    20%':
                polica = 31.00
            elif bonus.get() == '    25%':
                polica = 29.00
            elif bonus.get() == '    30%':
                polica = 27.00
            elif bonus.get() == '    35%':
                polica = 25.00
            elif bonus.get() == '    40%':
                polica = 23.00
            elif bonus.get() == '    45%':
                polica = 21.00
            elif bonus.get() == '    50%':
                polica = 19.00
            elif bonus.get() == '   110%':
                polica = 42.00
            elif bonus.get() == '   120%':
                polica = 46.00
            elif bonus.get() == '   130%':
                polica = 49.00
            elif bonus.get() == '   140%':
                polica = 53.00
            elif bonus.get() == '   150%':
                polica = 57.00
            elif bonus.get() == '   160%':
                polica = 61.00
            elif bonus.get() == '   180%':
                polica = 68.00
            elif bonus.get() == '   200%':
                polica = 76.00
        elif nosPrik.get() == '    preko 10 - 15 t':
            polica = 43.00
            if bonus.get() == '    10%':
                polica = 39.00
            elif bonus.get() == '    15%':
                polica = 37.00
            elif bonus.get() == '    20%':
                polica = 35.00
            elif bonus.get() == '    25%':
                polica = 32.00
            elif bonus.get() == '    30%':
                polica = 30.00
            elif bonus.get() == '    35%':
                polica = 28.00
            elif bonus.get() == '    40%':
                polica = 26.00
            elif bonus.get() == '    45%':
                polica = 24.00
            elif bonus.get() == '    50%':
                polica = 22.00
            elif bonus.get() == '   110%':
                polica = 47.00
            elif bonus.get() == '   120%':
                polica = 52.00
            elif bonus.get() == '   130%':
                polica = 56.00
            elif bonus.get() == '   140%':
                polica = 60.00
            elif bonus.get() == '   150%':
                polica = 65.00
            elif bonus.get() == '   160%':
                polica = 69.00
            elif bonus.get() == '   180%':
                polica = 77.00
            elif bonus.get() == '   200%':
                polica = 86.00
        elif nosPrik.get() == '    preko 15 - 20 t':
            polica = 48.00
            if bonus.get() == '    10%':
                polica = 43.00
            elif bonus.get() == '    15%':
                polica = 40.00
            elif bonus.get() == '    20%':
                polica = 38.00
            elif bonus.get() == '    25%':
                polica = 36.00
            elif bonus.get() == '    30%':
                polica = 33.00
            elif bonus.get() == '    35%':
                polica = 31.00
            elif bonus.get() == '    40%':
                polica = 29.00
            elif bonus.get() == '    45%':
                polica = 26.00
            elif bonus.get() == '    50%':
                polica = 24.00
            elif bonus.get() == '   110%':
                polica = 53.00
            elif bonus.get() == '   120%':
                polica = 58.00
            elif bonus.get() == '   130%':
                polica = 62.00
            elif bonus.get() == '   140%':
                polica = 67.00
            elif bonus.get() == '   150%':
                polica = 72.00
            elif bonus.get() == '   160%':
                polica = 77.00
            elif bonus.get() == '   180%':
                polica = 86.00
            elif bonus.get() == '   200%':
                polica = 96.00
        elif nosPrik.get() == '    preko 20 t':
            polica = 52.00
            if bonus.get() == '    10%':
                polica = 47.00
            elif bonus.get() == '    15%':
                polica = 44.00
            elif bonus.get() == '    20%':
                polica = 42.00
            elif bonus.get() == '    25%':
                polica = 39.00
            elif bonus.get() == '    30%':
                polica = 37.00
            elif bonus.get() == '    35%':
                polica = 34.00
            elif bonus.get() == '    40%':
                polica = 31.00
            elif bonus.get() == '    45%':
                polica = 29.00
            elif bonus.get() == '    50%':
                polica = 26.00
            elif bonus.get() == '   110%':
                polica = 57.00
            elif bonus.get() == '   120%':
                polica = 62.00
            elif bonus.get() == '   130%':
                polica = 68.00
            elif bonus.get() == '   140%':
                polica = 73.00
            elif bonus.get() == '   150%':
                polica = 78.00
            elif bonus.get() == '   160%':
                polica = 83.00
            elif bonus.get() == '   180%':
                polica = 94.00
            elif bonus.get() == '   200%':
                polica = 104.00

        if zapaljiviPrV.get() == 1:
            dodatak = polica * 15 / 100
        elif zapaljiviPrV1.get() == 1:
            dodatak = polica * 10 / 100

        polica += dodatak

    if vrstaVoz.get() == '    Motocikl':
        pomocPut = 4
        if vrstaReg.get() == '    Prva registracija':
            regTab = 10

        if kat.get() == '    L1' or kat.get() == '    L2' or kat.get() == '    L6':
            putarina60 = 21.6
            putarina40 = 14.4
        elif kat.get() == '    L3' or kat.get() == '    L4' or kat.get() == '    L5' or kat.get() == '    L7':
            putarina60 = 28.8
            putarina40 = 19.2

        if kat.get() == "    Odaberite kategoriju motocikla":
            if int(zapremina.get()) < 50:
                putarina60 = 21.6
                putarina40 = 14.4
            else:
                putarina60 = 28.8
                putarina40 = 19.2

        if ugV.get() == 1:
            komUg = 20

        if int(zapremina.get()) < 50:
            tehnicki = 27
        else:
            tehnicki = 31.5

        if int(zapremina.get()) < 51:
            polica = 33.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 28.00
            if bonus.get() == '    10%':
                polica = 30.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 28.00
            elif bonus.get() == '    15%':
                polica = 28.00
            elif bonus.get() == '    20%':
                polica = 26.00
            elif bonus.get() == '    25%':
                polica = 25.00
            elif bonus.get() == '    30%':
                polica = 23.00
            elif bonus.get() == '    35%':
                polica = 21.00
            elif bonus.get() == '    40%':
                polica = 20.00
            elif bonus.get() == '    45%':
                polica = 18.00
            elif bonus.get() == '    50%':
                polica = 16.00
            elif bonus.get() == '   110%':
                polica = 36.00
            elif bonus.get() == '   120%':
                polica = 40.00
            elif bonus.get() == '   130%':
                polica = 43.00
            elif bonus.get() == '   140%':
                polica = 46.00
            elif bonus.get() == '   150%':
                polica = 50.00
            elif bonus.get() == '   160%':
                polica = 53.00
            elif bonus.get() == '   180%':
                polica = 59.00
            elif bonus.get() == '   200%':
                polica = 66.00
        elif 101 > int(zapremina.get()) > 50:
            polica = 63.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 54.00
            if bonus.get() == '    10%':
                polica = 57.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 54.00
            elif bonus.get() == '    15%':
                polica = 54.00
            elif bonus.get() == '    20%':
                polica = 51.00
            elif bonus.get() == '    25%':
                polica = 48.00
            elif bonus.get() == '    30%':
                polica = 44.00
            elif bonus.get() == '    35%':
                polica = 41.00
            elif bonus.get() == '    40%':
                polica = 38.00
            elif bonus.get() == '    45%':
                polica = 35.00
            elif bonus.get() == '    50%':
                polica = 32.00
            elif bonus.get() == '   110%':
                polica = 69.00
            elif bonus.get() == '   120%':
                polica = 76.00
            elif bonus.get() == '   130%':
                polica = 82.00
            elif bonus.get() == '   140%':
                polica = 88.00
            elif bonus.get() == '   150%':
                polica = 95.00
            elif bonus.get() == '   160%':
                polica = 101.00
            elif bonus.get() == '   180%':
                polica = 113.00
            elif bonus.get() == '   200%':
                polica = 126.00
        elif 176 > int(zapremina.get()) > 100:
            polica = 84.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 71.00
            if bonus.get() == '    10%':
                polica = 75.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 71.00
            elif bonus.get() == '    15%':
                polica = 71.00
            elif bonus.get() == '    20%':
                polica = 67.00
            elif bonus.get() == '    25%':
                polica = 63.00
            elif bonus.get() == '    30%':
                polica = 58.00
            elif bonus.get() == '    35%':
                polica = 54.00
            elif bonus.get() == '    40%':
                polica = 50.00
            elif bonus.get() == '    45%':
                polica = 46.00
            elif bonus.get() == '    50%':
                polica = 42.00
            elif bonus.get() == '   110%':
                polica = 92.00
            elif bonus.get() == '   120%':
                polica = 101.00
            elif bonus.get() == '   130%':
                polica = 109.00
            elif bonus.get() == '   140%':
                polica = 118.00
            elif bonus.get() == '   150%':
                polica = 126.00
            elif bonus.get() == '   160%':
                polica = 134.00
            elif bonus.get() == '   180%':
                polica = 151.00
            elif bonus.get() == '   200%':
                polica = 168.00
        elif 251 > int(zapremina.get()) > 175:
            polica = 108.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 92.00
            if bonus.get() == '    10%':
                polica = 97.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 92.00
            elif bonus.get() == '    15%':
                polica = 92.00
            elif bonus.get() == '    20%':
                polica = 86.00
            elif bonus.get() == '    25%':
                polica = 81.00
            elif bonus.get() == '    30%':
                polica = 76.00
            elif bonus.get() == '    35%':
                polica = 70.00
            elif bonus.get() == '    40%':
                polica = 65.00
            elif bonus.get() == '    45%':
                polica = 59.00
            elif bonus.get() == '    50%':
                polica = 54.00
            elif bonus.get() == '   110%':
                polica = 119.00
            elif bonus.get() == '   120%':
                polica = 130.00
            elif bonus.get() == '   130%':
                polica = 140.00
            elif bonus.get() == '   140%':
                polica = 151.00
            elif bonus.get() == '   150%':
                polica = 162.00
            elif bonus.get() == '   160%':
                polica = 173.00
            elif bonus.get() == '   180%':
                polica = 194.00
            elif bonus.get() == '   200%':
                polica = 216.00
        elif 501 > int(zapremina.get()) > 250:
            polica = 189.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 161.00
            if bonus.get() == '    10%':
                polica = 170.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 161.00
            elif bonus.get() == '    15%':
                polica = 161.00
            elif bonus.get() == '    20%':
                polica = 151.00
            elif bonus.get() == '    25%':
                polica = 142.00
            elif bonus.get() == '    30%':
                polica = 133.00
            elif bonus.get() == '    35%':
                polica = 123.00
            elif bonus.get() == '    40%':
                polica = 114.00
            elif bonus.get() == '    45%':
                polica = 104.00
            elif bonus.get() == '    50%':
                polica = 95.00
            elif bonus.get() == '   110%':
                polica = 208.00
            elif bonus.get() == '   120%':
                polica = 227.00
            elif bonus.get() == '   130%':
                polica = 246.00
            elif bonus.get() == '   140%':
                polica = 265.00
            elif bonus.get() == '   150%':
                polica = 284.00
            elif bonus.get() == '   160%':
                polica = 302.00
            elif bonus.get() == '   180%':
                polica = 340.00
            elif bonus.get() == '   200%':
                polica = 378.00
        elif 751 > int(zapremina.get()) > 500:
            polica = 365.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 310.00
            if bonus.get() == '    10%':
                polica = 328.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 310.00
            elif bonus.get() == '    15%':
                polica = 310.00
            elif bonus.get() == '    20%':
                polica = 292.00
            elif bonus.get() == '    25%':
                polica = 274.00
            elif bonus.get() == '    30%':
                polica = 255.00
            elif bonus.get() == '    35%':
                polica = 237.00
            elif bonus.get() == '    40%':
                polica = 219.00
            elif bonus.get() == '    45%':
                polica = 201.00
            elif bonus.get() == '    50%':
                polica = 182.00
            elif bonus.get() == '   110%':
                polica = 402.00
            elif bonus.get() == '   120%':
                polica = 438.00
            elif bonus.get() == '   130%':
                polica = 475.00
            elif bonus.get() == '   140%':
                polica = 511.00
            elif bonus.get() == '   150%':
                polica = 548.00
            elif bonus.get() == '   160%':
                polica = 584.00
            elif bonus.get() == '   180%':
                polica = 657.00
            elif bonus.get() == '   200%':
                polica = 730.00
        elif int(zapremina.get()) > 750:
            polica = 551.00
            if bonus.get() == '      0%' or bonus.get() == "    Odaberite iznos bonusa":
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 469.00
            if bonus.get() == '    10%':
                polica = 496.00
                if rviV.get() == 1 or kolicaV.get() == 1:
                    polica = 469.00
            elif bonus.get() == '    15%':
                polica = 469.00
            elif bonus.get() == '    20%':
                polica = 441.00
            elif bonus.get() == '    25%':
                polica = 413.00
            elif bonus.get() == '    30%':
                polica = 386.00
            elif bonus.get() == '    35%':
                polica = 358.00
            elif bonus.get() == '    40%':
                polica = 331.00
            elif bonus.get() == '    45%':
                polica = 303.00
            elif bonus.get() == '    50%':
                polica = 276.00
            elif bonus.get() == '   110%':
                polica = 606.00
            elif bonus.get() == '   120%':
                polica = 661.00
            elif bonus.get() == '   130%':
                polica = 716.00
            elif bonus.get() == '   140%':
                polica = 771.00
            elif bonus.get() == '   150%':
                polica = 827.00
            elif bonus.get() == '   160%':
                polica = 882.00
            elif bonus.get() == '   180%':
                polica = 992.00
            elif bonus.get() == '   200%':
                polica = 1102.00

        if int(zapremina.get()) > 125:
            porez = 50

        if int(zapremina.get()) < 51:
            if year_ - int(godProz.get()) > 30:
                okolis = 7.68
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 6.72
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 5.76
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 5.28
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 4.8
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 4.56
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 4.32
        elif 50 < int(zapremina.get()) < 251:
            if year_ - int(godProz.get()) > 30:
                okolis = 13.6
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 11.9
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 10.2
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 9.35
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 8.5
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 8.08
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 7.65
        elif 250 < int(zapremina.get()) < 751:
            if year_ - int(godProz.get()) > 30:
                okolis = 14.5
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 12.6
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 10.8
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 9.9
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 9
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 8.55
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 8.1
        elif 750 < int(zapremina.get()) < 1401:
            if year_ - int(godProz.get()) > 30:
                okolis = 15.2
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 13.3
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 11.4
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 10.45
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 9.5
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 9.03
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 8.55
        elif 2001 > int(zapremina.get()) > 1400:
            if year_ - int(godProz.get()) > 30:
                okolis = 16
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 14
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 12
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 11
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 10
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 9.5
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 9
        elif int(zapremina.get()) > 2000:
            if year_ - int(godProz.get()) > 30:
                okolis = 19.2
            elif 31 > year_ - int(godProz.get()) > 20:
                okolis = 16.8
            elif 21 > year_ - int(godProz.get()) > 15:
                okolis = 14.4
            elif 16 > year_ - int(godProz.get()) > 10:
                okolis = 13.2
            elif 11 > year_ - int(godProz.get()) > 8:
                okolis = 12
            elif 9 > year_ - int(godProz.get()) > 5:
                okolis = 11.40
            elif 6 > year_ - int(godProz.get()) >= 0:
                okolis = 10.8

    labelPolica = Label(root, text=format(polica, '.2f'), bg="#ffffff", fg="#222")
    labelPolica.config(font="Arial 12")
    if 99 < polica < 1000:
        labelPolica.place(x=630, y=158)
    elif polica > 999:
        labelPolica.place(x=620, y=158)
    else:
        labelPolica.place(x=640, y=158)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=158)
    label42.config(font="Arial 12")

    labelPut60 = Label(root, text=format(putarina60, '.2f'), bg="#ffffff", fg="#222")
    labelPut60.config(font="Arial 12")
    if putarina60 > 99.99:
        labelPut60.place(x=630, y=228)

    else:
        labelPut60.place(x=640, y=228)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=228)
    label42.config(font="Arial 12")

    labelPut40 = Label(root, text=format(putarina40, '.2f'), bg="#ffffff", fg="#222")
    labelPut40.config(font="Arial 12")
    if putarina40 > 99.99:
        labelPut40.place(x=630, y=263)
    elif putarina40 > 9.99:
        labelPut40.place(x=640, y=263)
    else:
        labelPut40.place(x=650, y=263)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=263)
    label42.config(font="Arial 12")

    labelPorez = Label(root, text=format(porez, '.2f'), bg="#ffffff", fg="#222")
    labelPorez.config(font="Arial 12")
    if 9.9 < porez < 100:
        labelPorez.place(x=640, y=543)
    elif porez > 99.9:
        labelPorez.place(x=630, y=543)
    else:
        labelPorez.place(x=650, y=543)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=543)
    label42.config(font="Arial 12")
    labelTehnicki = Label(root, text=format(tehnicki, '.2f'), bg="#ffffff", fg="#222")
    labelTehnicki.config(font="Arial 12")
    if tehnicki < 99.99:
        labelTehnicki.place(x=640, y=123)
    else:
        labelTehnicki.place(x=630, y=123)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=123)
    label42.config(font="Arial 12")

    labelPomoc = Label(root, text=format(pomocPut, '.2f'), bg="#ffffff", fg="#222")
    labelPomoc.config(font="Arial 12")
    if pomocPut < 15:
        labelPomoc.place(x=650, y=368)
    else:
        labelPomoc.place(x=640, y=368)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=368)
    label42.config(font="Arial 12")

    labelZeleni = Label(root, text=format(zeleniK, '.2f'), bg="#ffffff", fg="#222")
    labelZeleni.place(x=650, y=193)
    labelZeleni.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=193)
    label42.config(font="Arial 12")

    labelTaksa = Label(root, text=format(taksa, '.2f'), bg="#ffffff", fg="#222")
    labelTaksa.place(x=640, y=404)
    labelTaksa.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=404)
    label42.config(font="Arial 12")

    labelZastita = Label(root, text=format(zastitaVoda, '.2f'), bg="#ffffff", fg="#222")
    labelZastita.place(x=640, y=299)
    labelZastita.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=298)
    label42.config(font="Arial 12")

    labelPotvrdaVl = Label(root, text=format(potvrdaVl, '.2f'), bg="#ffffff", fg="#222")
    labelPotvrdaVl.place(x=650, y=438)
    labelPotvrdaVl.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=438)
    label42.config(font="Arial 12")

    labelPotvrdaReg = Label(root, text=format(potvrdaReg, '.2f'), bg="#ffffff", fg="#222")
    labelPotvrdaReg.place(x=650, y=473)
    labelPotvrdaReg.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=473)
    label42.config(font="Arial 12")

    labelStiker = Label(root, text=format(stiker, '.2f'), bg="#ffffff", fg="#222")
    labelStiker.place(x=650, y=508)
    labelStiker.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=508)
    label42.config(font="Arial 12")

    labelRegTab = Label(root, text=format(regTab, '.2f'), bg="#ffffff", fg="#222")
    labelRegTab.config(font="Arial 12")
    if regTab == 0.0:
        labelRegTab.place(x=650, y=613)
    else:
        labelRegTab.place(x=640, y=613)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=613)
    label42.config(font="Arial 12")

    labelKomUg = Label(root, text=format(komUg, '.2f'), bg="#ffffff", fg="#222")
    labelKomUg.config(font="Arial 12")
    if int(ugV.get()) == 0:
        labelKomUg.place(x=650, y=648)
    else:
        labelKomUg.place(x=640, y=648)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=648)
    label42.config(font="Arial 12")

    labelOkolis = Label(root, text=format(okolis, '.2f'), bg="#ffffff", fg="#222")
    labelOkolis.config(font="Arial 12")
    if 99.9 > okolis > 9.99:
        labelOkolis.place(x=640, y=578)
    elif okolis > 99.9:
        labelOkolis.place(x=630, y=578)
    else:
        labelOkolis.place(x=650, y=578)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=578)
    label42.config(font="Arial 12")

    labelFond = Label(root, text=format(fond, '.2f'), bg="#ffffff", fg="#222")
    labelFond.place(x=640, y=333)
    labelFond.config(font="Arial 12")

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=333)
    label42.config(font="Arial 12")

    sumaL = [tehnicki, polica, zeleniK, putarina60, putarina40, zastitaVoda, fond, pomocPut, taksa, potvrdaVl,
             potvrdaReg, stiker, porez, okolis, regTab]

    var = 0
    for i in sumaL:
        if int(i) == 0:
            var += 1

    provizijaB = 15 - var + 1

    labelProvizija = Label(root, text=format(provizijaB, '.2f'), bg="#ffffff", fg="#222")
    labelProvizija.config(font="Arial 12")
    if provizijaB > 9.0:
        labelProvizija.place(x=640, y=683)
    else:
        labelProvizija.place(x=660, y=683)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=683)
    label42.config(font="Arial 12")

    sumaL.append(provizijaB)
    sumaL.append(komUg)

    cijena = math.fsum(sumaL)

    labelCijena = Label(root, text=format(cijena, '.2f'), bg="#ffffff", fg="#222")
    labelCijena.config(font="Arial 13 bold")
    if 99 < cijena < 1000:
        labelCijena.place(x=630, y=718)
    elif cijena < 100:
        labelCijena.place(x=640, y=718)
    else:
        labelCijena.place(x=622, y=718)

    label42 = Label(root, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=685, y=718)
    label42.config(font="Arial 13 bold")

    zastavicaP = True

def izvoz():
    if ws == 1680 and hs == 1050:
        im = grab(bbox=(778, 172, 1178, 904), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1400 and hs == 1050:
        im = grab(bbox=(638, 172, 1038, 904), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1280 and hs == 1024:
        im = grab(bbox=(578, 163, 978, 891), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1280 and hs == 960:
        im = grab(bbox=(578, 90, 978, 819), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1152 and hs == 864:
        im = grab(bbox=(514, 42, 914, 773), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1920 and hs == 1080:
        im = grab(bbox=(899, 160, 1298, 889), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1600 and hs == 900:
        im = grab(bbox=(739, 58, 1138, 789), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1440 and hs == 900:
        im = grab(bbox=(659, 58, 1058, 789), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    c = canvas.Canvas('obracun/obracun.pdf')
    c.drawImage('obracun/obracun.png', 155, 170, 10.5 * cm, 19 * cm)
    c.showPage()
    c.save()

    with open('obracun/obracun.png', 'r+b') as f:
        with Image.open(f) as image:
            img = resizeimage.resize_width(image, 360)
            img.save('obracun/obracun.png', img.format)
            f.close()

    global newWindow
    global check
    checkLabel = Label(newWindow, image=check, bg="#e6e6e6")
    checkLabel.place(x=380, y=746)

def printaj():
    if ws == 1680 and hs == 1050:
        im = grab(bbox=(778, 172, 1178, 904), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1400 and hs == 1050:
        im = grab(bbox=(638, 172, 1038, 904), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1280 and hs == 1024:
        im = grab(bbox=(578, 163, 978, 891), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1280 and hs == 960:
        im = grab(bbox=(578, 90, 978, 819), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1152 and hs == 864:
        im = grab(bbox=(514, 42, 914, 773), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1920 and hs == 1080:
        im = grab(bbox=(899, 160, 1298, 889), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1600 and hs == 900:
        im = grab(bbox=(739, 58, 1138, 789), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    elif ws == 1440 and hs == 900:
        im = grab(bbox=(659, 58, 1058, 789), backend="mss", childprocess=False)
        im.save('obracun/obracun.png')

    c = canvas.Canvas('obracun/obracun.pdf')
    c.drawImage('obracun/obracun.png', 155, 170, 10.5 * cm, 19 * cm)
    c.showPage()
    c.save()

    p = Path("obracun/obracun.pdf").resolve()
    os.startfile(str(p), "print")

def izmjena():
    fp = open('podaci/podaci.txt', "w", encoding="utf-8")
    fp.writelines([ime.get()+"\n", brTel.get()+"\n", adr.get()+"\n"])
    fp.close()
    global newWindow1
    checkLabel = Label(newWindow1, image=check, bg="#e6e6e6")
    checkLabel.place(x=330, y=210)

def spremi():
    global newWindow1
    newWindow1 = Toplevel(root)
    w1 = 520  # width for the Tk root
    h1 = 270  # height for the Tk root

    # get screen width and height
    ws1 = root.winfo_screenwidth()  # width of the screen
    hs1 = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x1 = (ws1 / 2) - (w1 / 2)
    y1 = (hs1 / 2) - (h1 / 2) - 60

    if hs1 == 900:
        y1 -= 40
    elif hs1 == 864:
        y1 -= 38

    # set the dimensions of the screen
    # and where it is placed
    newWindow1.geometry('%dx%d+%d+%d' % (w1, h1, x1, y1))
    newWindow1.iconbitmap('icons/grawe.ico')
    newWindow1.title("Podaci o zaposleniku")
    newWindow1.resizable(height=False, width=False)
    newWindow1.configure(background='#e6e6e6')

    label100 = Label(newWindow1, text="Unos podataka o zastupniku", bg='#e6e6e6', fg='#222')  # probati sa colonom
    label100.place(x=86, y=17)
    label100.config(font="Arial 19")

    label116 = Label(newWindow1, text="Ime i prezime:", bg="#e6e6e6", fg="#222")
    label116.place(x=85, y=80)
    label116.config(font=("Arial", 12))

    global ime
    ime = ttk.Entry(newWindow1, width=26)
    ime.place(x=195, y=80)
    ime.config(font=("Arial", 11))

    label117 = Label(newWindow1, text="Broj telefona:", bg="#e6e6e6", fg="#222")
    label117.place(x=85, y=120)
    label117.config(font=("Arial", 12))

    global brTel
    brTel = ttk.Entry(newWindow1, width=26)
    brTel.place(x=195, y=120)
    brTel.config(font=("Arial", 11))

    label119 = Label(newWindow1, text="Adresa:", bg="#e6e6e6", fg="#222")
    label119.place(x=85, y=160)
    label119.config(font=("Arial", 12))

    global adr
    adr = ttk.Entry(newWindow1, width=26)
    adr.place(x=195, y=160)
    adr.config(font=("Arial", 11))

    btn1 = Button(newWindow1, text="Spremi", bg="#222", fg="#ffffff", font="Arial 12", command=izmjena)
    btn1.place(x=255, y=210)
#-----------------------------------------EXPORT------------------------------------------------------------------------
def export():
    global newWindow
    newWindow = Toplevel(root)
    w2 = 432  # width for the Tk root
    h2 = 790  # height for the Tk root

    # get screen width and height
    ws2 = root.winfo_screenwidth()  # width of the screen
    hs2 = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x2 = (ws2 / 2) - (w2 / 2) + 130
    y2 = (hs2 / 2) - (h2 / 2) + 3

    if hs2 == 900 or hs2 == 960:
        y2 -= 40
    elif hs2 == 864:
        y2 -= 38
    elif hs2 == 1080:
        y2 -= 30

    # set the dimensions of the screen
    # and where it is placed
    newWindow.geometry('%dx%d+%d+%d' % (w2, h2, x2, y2))
    newWindow.iconbitmap('icons/grawe.ico')
    newWindow.title("Obračun registracije vozila")
    newWindow.resizable(height=False, width=False)
    newWindow.configure(background='#e6e6e6')

    img = PhotoImage(file='icons/grawe.png')

    label55 = Label(image=img)
    label55.image = img # keep a reference!
    label55.pack()

    w1 = Canvas(newWindow, width=400, bg="#ffffff", height=732, highlightthickness=0)
    w1.place(x=16, y=8)

    w1.create_image(10, 51, image=img, anchor=SW)
    #x=20, y=12
    label55.place(x=37, y=2)
    w1.create_line(1, 65, 399, 65, 399, 65, 399, 731, 399, 731, 1, 731, 1, 731, 1, 65, fill="#222")

    w1.create_line(1, 101, 399, 101, 399, 136, 1, 136)
    w1.create_line(1, 171, 399, 171, 399, 206, 1, 206, 1, 241, 399, 241, 399, 276, 1, 276, fill="#222")
    w1.create_line(1, 311, 399, 311, 399, 346, 1, 346, 1, 381, 399, 381, 399, 416, 1, 416, fill="#222")
    w1.create_line(1, 451, 399, 451, 399, 486, 1, 486, 1, 521, 399, 521, 399, 556, 1, 556, 1, 591, 399, 591, fill="#222")
    w1.create_line(1, 626, 399, 626, 399, 661, 1, 661, 1, 696, 399, 696, fill="#222")
    w1.create_line(1, 731, 399, 731, fill="#222")

    w1.create_line(50, 101, 50, 696, fill="#222")
    w1.create_line(250, 101, 250, 731, fill="#222")

    fp = open('podaci/podaci.txt', 'r', encoding="utf-8")
    line = fp.readline()
    prviRed = "Zastupnik: " + line.strip()
    line1 = fp.readline()
    treciRed = fp.readline()
    fp.close()
    if len(prviRed) < 26 and len(treciRed) < 26:
        label71 = Label(newWindow, text="Zastupnik: ", bg="#ffffff", fg="#222")
        label71.place(x=215, y=8)
        label71.config(font=("Arial", 11, 'bold'))
        label72 = Label(newWindow, text="Tel: ", bg="#ffffff", fg="#222")
        label72.place(x=215, y=28)
        label72.config(font=("Arial", 11, 'bold'))

        label71 = Label(newWindow, text=line.strip(), bg="#ffffff", fg="#222")
        label71.place(x=290, y=8)
        label71.config(font=("Arial", 11, 'bold'))

        label72 = Label(newWindow, text=line1.strip(), bg="#ffffff", fg="#222")
        label72.place(x=250, y=28)
        label72.config(font=("Arial", 11, 'bold'))

        label73 = Label(newWindow, text=treciRed.strip(), bg="#ffffff", fg="#222")
        label73.place(x=215, y=46)
        label73.config(font=("Arial", 11, 'bold'))
    elif len(prviRed) < 31 and len(treciRed) < 31:
        label71 = Label(newWindow, text="Zastupnik: ", bg="#ffffff", fg="#222")
        label71.place(x=200, y=8)
        label71.config(font=("Arial", 10, 'bold'))
        label72 = Label(newWindow, text="Tel: ", bg="#ffffff", fg="#222")
        label72.place(x=200, y=28)
        label72.config(font=("Arial", 10, 'bold'))

        label71 = Label(newWindow, text=line.strip(), bg="#ffffff", fg="#222")
        label71.place(x=267, y=8)
        label71.config(font=("Arial", 10, 'bold'))

        label72 = Label(newWindow, text=line1.strip(), bg="#ffffff", fg="#222")
        label72.place(x=235, y=28)
        label72.config(font=("Arial", 10, 'bold'))

        label73 = Label(newWindow, text=treciRed.strip(), bg="#ffffff", fg="#222")
        label73.place(x=200, y=46)
        label73.config(font=("Arial", 10, 'bold'))
    elif len(prviRed) < 34 and len(treciRed) < 34:
        label71 = Label(newWindow, text="Zastupnik: ", bg="#ffffff", fg="#222")
        label71.place(x=200, y=8)
        label71.config(font=("Arial", 10))
        label72 = Label(newWindow, text="Tel: ", bg="#ffffff", fg="#222")
        label72.place(x=200, y=28)
        label72.config(font=("Arial", 10))

        label71 = Label(newWindow, text=line.strip(), bg="#ffffff", fg="#222")
        label71.place(x=264, y=8)
        label71.config(font=("Arial", 10))

        label72 = Label(newWindow, text=line1.strip(), bg="#ffffff", fg="#222")
        label72.place(x=230, y=28)
        label72.config(font=("Arial", 10))

        label73 = Label(newWindow, text=treciRed.strip(), bg="#ffffff", fg="#222")
        label73.place(x=200, y=46)
        label73.config(font=("Arial", 10))
    else:
        label71 = Label(newWindow, text=line.strip(), bg="#ffffff", fg="#222")
        label71.place(x=198, y=8)
        label71.config(font=("Arial", 10, 'bold'))

        label72 = Label(newWindow, text="Tel: ", bg="#ffffff", fg="#222")
        label72.place(x=198, y=28)
        label72.config(font=("Arial", 10, 'bold'))

        label72 = Label(newWindow, text=line1.strip(), bg="#ffffff", fg="#222")
        label72.place(x=230, y=28)
        label72.config(font=("Arial", 10, 'bold'))

        label73 = Label(newWindow, text=treciRed.strip(), bg="#ffffff", fg="#222")
        label73.place(x=198, y=46)
        label73.config(font=("Arial", 10, 'bold'))

    btn2 = Button(newWindow, image=button2, bg="#e6e6e6", bd=0, command=izvoz)
    btn2.place(x=340, y=746)

    btn6 = Button(newWindow, image=button3, bg="#e6e6e6", bd=0, command=printaj)
    btn6.place(x=280, y=746)

    btn4 = Button(newWindow, image=edit, bg="#e6e6e6", bd=0, font="Arial 12", command=spremi)
    btn4.place(x=25, y=746)

    duzina = "Klijent: " + klijent.get()

    if len(duzina) < 25:
        label21 = Label(newWindow, text="Klijent: ", bg="#ffffff", fg="#222")
        label21.place(x=122, y=79)
        label21.config(font=("Arial", 12, 'bold'))

        label21 = Label(newWindow, text=klijent.get(), bg="#ffffff", fg="#222")
        label21.place(x=183, y=79)
        label21.config(font=("Arial", 12, 'bold'))
    elif len(duzina) < 31:
        label21 = Label(newWindow, text="Klijent: ", bg="#ffffff", fg="#222")
        label21.place(x=99, y=79)
        label21.config(font=("Arial", 12, 'bold'))

        label21 = Label(newWindow, text=klijent.get(), bg="#ffffff", fg="#222")
        label21.place(x=160, y=79)
        label21.config(font=("Arial", 12, 'bold'))
    elif len(duzina) < 38:
        label21 = Label(newWindow, text="Klijent: ", bg="#ffffff", fg="#222")
        label21.place(x=77, y=79)
        label21.config(font=("Arial", 12, 'bold'))

        label21 = Label(newWindow, text=klijent.get(), bg="#ffffff", fg="#222")
        label21.place(x=138, y=79)
        label21.config(font=("Arial", 12, 'bold'))
    else:
        label21 = Label(newWindow, text="Klijent: ", bg="#ffffff", fg="#222")
        label21.place(x=54, y=79)
        label21.config(font=("Arial", 12, 'bold'))

        label21 = Label(newWindow, text=klijent.get(), bg="#ffffff", fg="#222")
        label21.place(x=115, y=79)
        label21.config(font=("Arial", 12, 'bold'))

    label21 = Label(newWindow, text="1.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=114)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Tehnički pregled", bg="#ffffff", fg="#222")
    label21.place(x=104, y=114)
    label21.config(font=("Arial", 12))

    labelTehnicki1 = Label(newWindow, text=format(tehnicki, '.2f'), bg="#ffffff", fg="#222")
    labelTehnicki1.config(font="Arial 12")

    if tehnicki < 99.99:
        labelTehnicki1.place(x=305, y=114)
    else:
        labelTehnicki1.place(x=295, y=114)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=114)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="2.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=149)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Polica osiguranja", bg="#ffffff", fg="#222")
    label21.place(x=103, y=149)
    label21.config(font=("Arial", 12))

    labelPolica1 = Label(newWindow, text=format(polica, '.2f'), bg="#ffffff", fg="#222")
    labelPolica1.config(font="Arial 12")
    if 99 < polica < 1000:
        labelPolica1.place(x=295, y=149)
    elif polica < 100:
        labelPolica1.place(x=305, y=149)
    else:
        labelPolica1.place(x=285, y=149)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=149)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="3.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=184)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Zeleni karton", bg="#ffffff", fg="#222")
    label21.place(x=117, y=184)
    label21.config(font=("Arial", 12))

    labelZeleni1 = Label(newWindow, text=format(zeleniK, '.2f'), bg="#ffffff", fg="#222")
    labelZeleni1.place(x=315, y=184)
    labelZeleni1.config(font="Arial 12")

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=184)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="4.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=219)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Putarina 60%", bg="#ffffff", fg="#222")
    label21.place(x=116, y=219)
    label21.config(font=("Arial", 12))
    labelPut601 = Label(newWindow, text=format(putarina60, '.2f'), bg="#ffffff", fg="#222")
    labelPut601.config(font="Arial 12")
    if putarina60 > 99.99:
        labelPut601.place(x=295, y=219)
    else:
        labelPut601.place(x=305, y=219)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=219)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="5.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=254)
    label21.config(font=("Arial", 12))

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=254)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="Putarina 40%", bg="#ffffff", fg="#222")
    label21.place(x=116, y=254)
    label21.config(font=("Arial", 12))

    labelPut401 = Label(newWindow, text=format(putarina40, '.2f'), bg="#ffffff", fg="#222")
    labelPut401.config(font="Arial 12")
    if putarina40 > 99.99:
        labelPut401.place(x=295, y=254)
    elif putarina40 > 9.99:
        labelPut401.place(x=305, y=254)
    else:
        labelPut401.place(x=315, y=254)

    label21 = Label(newWindow, text="6.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=289)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Zaštita voda", bg="#ffffff", fg="#222")
    label21.place(x=118, y=289)
    label21.config(font=("Arial", 12))

    labelZastita1 = Label(newWindow, text=format(zastitaVoda, '.2f'), bg="#ffffff", fg="#222")
    labelZastita1.place(x=305, y=289)
    labelZastita1.config(font="Arial 12")

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=289)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="7.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=324)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Fond za izgradnju", bg="#ffffff", fg="#222")
    label21.place(x=103, y=324)
    label21.config(font=("Arial", 12))

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=324)
    label42.config(font="Arial 12")

    labelFond1 = Label(newWindow, text=format(fond, '.2f'), bg="#ffffff", fg="#222")
    labelFond1.place(x=305, y=324)
    labelFond1.config(font="Arial 12")

    label21 = Label(newWindow, text="8.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=359)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Pomoć na putu", bg="#ffffff", fg="#222")
    label21.place(x=110, y=359)
    label21.config(font=("Arial", 12))

    labelPomoc1 = Label(newWindow, text=format(pomocPut, '.2f'), bg="#ffffff", fg="#222")
    labelPomoc1.config(font="Arial 12")
    if pomocPut < 15:
        labelPomoc1.place(x=315, y=359)
    else:
        labelPomoc1.place(x=305, y=359)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=359)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="9.", bg="#ffffff", fg="#222")
    label21.place(x=33, y=394)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Taksa", bg="#ffffff", fg="#222")
    label21.place(x=139, y=394)
    label21.config(font=("Arial", 12))

    labelTaksa1 = Label(newWindow, text=format(taksa, '.2f'), bg="#ffffff", fg="#222")
    labelTaksa1.place(x=305, y=394)
    labelTaksa1.config(font="Arial 12")

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=394)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="10.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=429)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Potvrda o vlasništvu", bg="#ffffff", fg="#222")
    label21.place(x=96, y=429)
    label21.config(font=("Arial", 12))

    labelPotvrdaVl1 = Label(newWindow, text=format(potvrdaVl, '.2f'), bg="#ffffff", fg="#222")
    labelPotvrdaVl1.place(x=315, y=429)
    labelPotvrdaVl1.config(font="Arial 12")

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=429)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="11.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=464)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Potvrda o registraciji", bg="#ffffff", fg="#222")
    label21.place(x=95, y=464)
    label21.config(font=("Arial", 12))

    labelPotvrdaReg1 = Label(newWindow, text=format(potvrdaReg, '.2f'), bg="#ffffff", fg="#222")
    labelPotvrdaReg1.place(x=315, y=464)
    labelPotvrdaReg1.config(font="Arial 12")

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=464)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="12.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=499)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Stiker naljepnica", bg="#ffffff", fg="#222")
    label21.place(x=108, y=499)
    label21.config(font=("Arial", 12))

    labelStiker1 = Label(newWindow, text=format(stiker, '.2f'), bg="#ffffff", fg="#222")
    labelStiker1.place(x=315, y=499)
    labelStiker1.config(font="Arial 12")

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=499)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="13.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=534)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Porez na imovinu", bg="#ffffff", fg="#222")
    label21.place(x=106, y=534)
    label21.config(font=("Arial", 12))

    labelPorez1 = Label(newWindow, text=format(porez, '.2f'), bg="#ffffff", fg="#222")
    labelPorez1.config(font="Arial 12")
    if 9.9 < porez < 100:
        labelPorez1.place(x=305, y=534)
    elif porez > 99.9:
        labelPorez1.place(x=295, y=534)
    else:
        labelPorez1.place(x=315, y=534)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=534)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="14.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=569)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Zaštita okoliša", bg="#ffffff", fg="#222")
    label21.place(x=111, y=569)
    label21.config(font=("Arial", 12))

    labelOkolis1 = Label(newWindow, text=format(okolis, '.2f'), bg="#ffffff", fg="#222")
    labelOkolis1.config(font="Arial 12")
    if 99.9 > okolis > 9.9:
        labelOkolis1.place(x=305, y=569)
    elif okolis > 99.9:
        labelOkolis1.place(x=295, y=569)
    else:
        labelOkolis1.place(x=315, y=569)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=569)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="15.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=604)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Registarske tablice", bg="#ffffff", fg="#222")
    label21.place(x=98, y=604)
    label21.config(font=("Arial", 12))

    labelRegTab1 = Label(newWindow, text=format(regTab, '.2f'), bg="#ffffff", fg="#222")
    labelRegTab1.config(font="Arial 12")
    if regTab == 0.0:
        labelRegTab1.place(x=315, y=604)
    else:
        labelRegTab1.place(x=305, y=604)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=604)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="16.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=639)
    label21.config(font=("Arial", 12))

    label21 = Label(newWindow, text="Komisioni ugovor", bg="#ffffff", fg="#222")
    label21.place(x=103, y=639)
    label21.config(font=("Arial", 12))

    labelKomUg1 = Label(newWindow, text=format(komUg, '.2f'), bg="#ffffff", fg="#222")
    labelKomUg1.config(font="Arial 12")
    if komUg == 0.0:
        labelKomUg1.place(x=315, y=639)
    else:
        labelKomUg1.place(x=305, y=639)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=639)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="17.", bg="#ffffff", fg="#222")
    label21.place(x=29, y=674)
    label21.config(font=("Arial", 12))

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=674)
    label42.config(font="Arial 12")

    label21 = Label(newWindow, text="Provizija banke", bg="#ffffff", fg="#222")
    label21.place(x=110, y=674)
    label21.config(font=("Arial", 12))

    labelProvizija1 = Label(newWindow, text=format(provizijaB, '.2f'), bg="#ffffff", fg="#222")
    labelProvizija1.config(font="Arial 12")
    if provizijaB > 9:
        labelProvizija1.place(x=305, y=674)
    else:
        labelProvizija1.place(x=315, y=674)

    label21 = Label(newWindow, text="Cijena registracije vozila", bg="#ffffff", fg="#222")
    label21.place(x=46, y=709)
    label21.config(font="Arial 12 bold")
    labelCijena = Label(newWindow, text=format(cijena, '.2f'), bg="#ffffff", fg="#222")
    labelCijena.config(font="Arial 13 bold")
    if 99 < cijena < 1000:
        labelCijena.place(x=295, y=709)
    elif cijena < 100:
        labelCijena.place(x=305, y=709)
    else:
        labelCijena.place(x=287, y=709)

    label42 = Label(newWindow, text="KM", bg="#ffffff", fg="#222")
    label42.place(x=350, y=709)
    label42.config(font="Arial 13 bold")

#-----------------------------------------BUTTON------------------------------------------------------------------------

btn = Button(text="Izračunaj!", bg="#017a3d", fg="white", font="Arial 12", command=checkcmbo)
btn.place(x=96, y=460)

button=PhotoImage(file='icons/share.png')

btn1 = Button(image=button, bd=0, bg="#e6e6e6", fg="#ffffff", font="Arial 12", command=export)
btn1.place(x=659, y=757)

#------------------------------ZAVRŠNE POSTAVKE I POZIVANJE LOOP-a------------------------------------------------------


root.resizable(height=False, width=False)

w = 812 # width for the Tk root
h = 835 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

if hs == 900:
    y -= 40

elif hs == 864:
    y -= 33
elif hs == 1080:
    y -= 30
elif hs == 960:
    y -= 40

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
labelC = Label(root, text="Copyright", bg="#e6e6e6", fg="#222")
labelC.place(x=273, y=810)
labelC.config(font="Arial 10 bold")
labelC = Label(root, text="©", bg="#e6e6e6", fg="#222")
labelC.place(x=340, y=810)
labelC.config(font="Arial 11 bold")
labelC1 = Label(root, text="Amar Hodžić, BA ing. el.", bg="#e6e6e6", fg="#222")
labelC1.place(x=356, y=810.5)
labelC1.config(font="Arial 10 bold")
root.mainloop()
