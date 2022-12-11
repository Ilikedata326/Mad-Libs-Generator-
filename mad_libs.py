import tkinter as Tk
from tkinter import *


def madLib_quotes():  
    verb1 = input("Enter correspond verb: ")
    verb2 = input("Enter correspond verb: ")
    adverb = input("Enter correspond adverb: ")
    adjective = input("Enter correspond adjective: ")
    verb3 = input("Enter correspond verb: ")
    noun =  input("Enter correspond noun: ")
    name =  input("Enter correspond name: ")

    print(f"""
    ========================================================================
                                 Quote
                                =======

    Sometimes we {verb1} the process more complicated than we {verb2} to. 
    We will {adverb} make a journey of a thousand miles by fretting about how
    {adjective} it will take or how hard it will be. We {verb3} the journey 
    by taking each day step by step and then repeating it again and again
    until we reach our {noun}. \n 
                                                    {name}
    =========================================================================
    """)

# Calling function
madLib_quotes()