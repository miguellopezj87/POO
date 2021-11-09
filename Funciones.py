from Usuario import Usuario
from Noticia import Noticia
from Comentario import Comentario
from DAO import DAO
from beautifultable import BeautifulTable
from os import system
import os

class Funciones:

    d = DAO()
    sesion = Usuario()

    def __init__(self):
        pass

    
    def menuInicial(self):
        while True:
            try:
                system("cls")
                print("--- MENU INICIAL ---")
                print("1.Iniciar Sesion")
                print("2.Ver Comentarios")
                print("3.Salir")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    self.__login()
                elif op==2:
                    self.__listarComentarios()
                    self.menuInicial()
                elif op==3:
                    print("\n--- OK. ADIOS!! ---")
                    system("pause")
                    os._exit(1)
                else:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!! ---")
                system("pause")

#----------------------------------------------------------------------

    def menuAdmin(self):
        while True:
            try:
                system("cls")
                print("--- MENU DE ADMIN ---")
                print("1.Crear Nuevo Usuario")
                print("2.Deshabilitar Usuario")
                print("3.Crear Nueva Noticia")
                print("4.Deshabilitar Noticias")
                print("5.Cerrar Sesion")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    pass
                elif op==2:
                    pass
                elif op==3:
                    pass
                elif op==4:
                    pass
                elif op==5:
                    self.menuInicial()
                else:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!! ---")
                system("pause")

#----------------------------------------------------------------------

    def menuUsuarios(self):
        while True:
            try:
                system("cls")
                print("--- MENU DE",self.sesion.getNomUsuario().upper(),"---")
                print("1.Comentar Noticia")
                print("2.Ver Mis Comentarios")
                print("3.Ver Todos Los Comentarios")
                print("4.Cerrar Sesion (Logout)")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    pass
                elif op==2:
                    pass
                elif op==3:
                    pass
                elif op==4:
                    self.menuInicial()
                else:
                    print("\n--- Error De Opcion De Menu Usuario!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!! ---")
                system("pause")

#----------------------------------------------------------------------

    def __listarComentarios(self):
        respuesta = self.d.obtenerComentarios()
        tabla = BeautifulTable()
        for x in respuesta:
            tabla.rows.append([x[0], x[1], x[2]])
        tabla.column_headers = ["USUARIO", "COMENTARIO", "NOTICIA"]
        system("cls")
        print(tabla)
        system("pause")

#----------------------------------------------------------------------

    def __login(self):
        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                nom = input("Digite El Nombre de Usuario : ")
                if len(nom)<1 or len(nom)>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nombre De Usuario (LOGIN)!! ---")
                system("pause")

        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                pas = input("Digite La Contraseña Del Usuario ("+nom.upper()+") : ")
                if len(pas)<1 or len(pas)>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Ingresar Contraseña (LOGIN)!! ---")
                system("pause")
    
        system("cls")
        r = self.d.iniciarSesion(nom, pas)
        if r is None:
            print("\n--- Error De Usuario y/o Contraseña!! ---\n")
            system("pause")
        elif r[3] != 1:
            print("\n--- Usuario Deshabilitado. Contactese Con El Admin!! ---\n")
            system("pause")
        else:
            self.sesion.setIdUsuario(r[0])
            self.sesion.setNomUsuario(r[1])
            self.sesion.setPasUsuario(r[2])
            self.sesion.setIdEstado(r[3])
            if self.sesion.getNomUsuario() == "ADMIN":
                print("\n--- Bienvenido Usuario ADMIN!! ---\n")
                system("pause")
                self.menuAdmin()
            else:
                print("\n--- Bienvenido Usuario "+self.sesion.getNomUsuario().upper()+" !! ---\n")
                system("pause")
                self.menuUsuarios()

# ---------------------------------------------------------------------