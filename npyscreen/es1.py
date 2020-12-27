#!/usr/bin/env python3
import npyscreen

def simple_function(*arguments):
    form = npyscreen.Form(name = "npyscreen form!")                 #creazione del form
    form.add(npyscreen.TitleText, name="First Widget")              #titolo della schermata
    form.edit()                                                     #fa rimanere la schermata
    pass

if (__name__ == "__main__"):
    npyscreen.wrapper_basic(simple_function)                        #chiamata della funzione nel main
