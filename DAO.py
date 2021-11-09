from Usuario import Usuario
from Noticia import Noticia
from Comentario import Comentario
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass

#--------------------------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost", 
            user = "root",
            password = "",
            db = "bd7"
        )

        self.cursor = self.con.cursor()

#--------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

#--------------------------------------------------------------------

    def obtenerComentarios(self):
        try:
            self.conectar()
            # Con Equi-Join.
            sql = "select nom_usu, des_com, tit_not from usuarios, comentarios, noticias where comentarios.id_usu=usuarios.id_usu and comentarios.id_not=noticias.id_not and comentarios.id_est=1"
            
            # Con Inner Join.
            #sql = "select nom_usu, des_com, tit_not from usuarios u inner join comentarios c on c.id_usu=u.id_usu inner join noticias n on c.id_not=n.id_not and c.id_est=1"
        
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Comentarios (DAO)!! ---")
            system("pause")

#--------------------------------------------------------------------

    def iniciarSesion(self, nom, pas):
        u = Usuario()
        try:
            self.conectar()
            sql = "select * from usuarios where nom_usu=%s and pas_usu=%s"
            val = (nom, pas)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            return rs 
            # retorna None o una tupla con los datos.
        except:
            print("\n--- Error Al Obtener Usuario (LOGIN)!! ---")

# ---------------------------------------------------------------------
