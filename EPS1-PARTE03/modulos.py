# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:03:02 2022
@author: alumno
"""


def listar_producto():
    f = open("nombre.txt", "r")
    g = open("dni.txt", "r")
    h = open("apellido.txt", "r")
    print("\n***LISTANDO DNI,NOMBRE Y APELLIDO respectivamente.***\n")
    print("\n***DNI   --   NOMBRE   --   APELLIDO***\n")
    while(True):
    
     dni = g.readline()
     nombre = f.readline()
     apellido = h.readline()
     nombre=nombre.strip('\n')
     dni=dni.strip('\n')
     apellido=apellido.strip('\n')
     print ("{:<10} {:<15} {:<15}".format(dni,nombre,apellido))
     if not nombre:
       break
    
    

def agregar_producto():
    
    contenido2 = input("dni: ")
    archivo2 = open("dni.txt","at")
    archivo2.write("\n"+ contenido2)
    contenido1 = input("Nombre: ")
    archivo1 = open("nombre.txt","at")
    archivo1.write("\n"+ contenido1)
    contenido3 = input("Apellido: ")
    archivo3 = open("apellido.txt","at")
    archivo3.write("\n"+ contenido3)
    archivo1.close()
    archivo2.close()
    archivo3.close()

def salir():
    print("Vuelva pronto...")
