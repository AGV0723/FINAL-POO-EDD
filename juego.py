# -*- coding: utf-8 -*-
from jugador import Jugador
from correo import Correo
from linkedList import *
from logro import Logro
from historia import Historia
from nivel import Nivel
from sinFin import SinFin
from tutorial import Tutorial
from video import Video
import csv
import pygame
import pyttsx3



class Juego:
    #todos estos atributos son de tipo LinkedList de nodos con data de su respectiva clase(usuario, nivel, etc)
    #niveles, usuario, correos y logros se crean a partir de un csv
    #jugadores se crea a partir de usuarios
    
    #Constructores
    def __init__(self,niveles,jugadores,correos,logros,historia,sin_fin,tutorial):
        self.niveles = niveles
        self.jugadores =jugadores
        self.correos = correos
        self.logros = logros
        self.historia = historia
        self.sin_fin = sin_fin
        self.tutorial = tutorial
    
    def __init__(self,niveles = None,jugadores = None,correos = None,logros = None, historia = None,sin_fin = None,tutorial = None):
        self.niveles = niveles
        self.jugadores =jugadores
        self.correos = correos
        self.logros = logros
        self.historia = historia
        self.sin_fin = sin_fin
        self.tutorial = tutorial
    
    
    #Métodos del jugador
    def comprobarNivelPasado(self,jugador_nombre, nivel_nombre):
        player = self.getJugador(jugador_nombre)
        pivot = player.nivelesCompletados.head
        sw = 0
        while pivot != None and sw == 0:
            if(pivot.data.nombre == nivel_nombre):
                sw = 1
            else:
                pivot = pivot.next
        
        if(sw == 1):
            return True
        else:
            return False
    
    def jugarNivelElegido(self,jugador_nombre,nivel_nombre):
        if(self.comprobarNivelPasado(jugador_nombre,nivel_nombre)):
            nivel = self.getNivel(nivel_nombre)
            jugador = self.getJugador(jugador_nombre)
            fallas = 0
            
        else:
            print("Aún no completas los niveles necesarios para jugar este nivel")
      
    #Comprobar logros
    #def cincoSeguidosHistoria(self):
        
    #Logro1 = 5 correos seguidos, habría que hacer un contador de aciertos y que cada vez que se equivoque o termine el nivel se reinicie  
    #Logro2 = Completar modo historia, cuando la linkedList de niveles del jugador esté completa 
    #Logro3 = Hacer 10 correos, cuando el contador de aciertos sea igual a 10
    #Logro4 = Hacer 20 correos, cuando el contado de acierto sea igual a 20
    #Logro5 = Hacer 30 correos, cuando el contado de acierto sea igual a 20
    #Logro6 = Perder por primera vez en modo historia, que tenga un correo mal identificado
     
         
    #Modifica la LinkedList usuarios y luego el csv, tambien crea un objeto de Jugador
    def crearJugador(self, nombre, contrasena):
        jugador = Jugador(nombre = nombre, contrasena = contrasena, logrosConseguidos=LinkedList(), nivelesCompletados=LinkedList(), mejorMarca=0)
        self.jugadores.addDatoFin(jugador)
        self.actualizarJugadoresArchivo()
        
    #Actualiza los .csv con la info de las LinkedList
    def actualizarJugadoresArchivo(self):
        with open("ArchivosCSV//Jugadores.csv", "w", encoding="UTF-8") as p:
            writer = csv.writer(p, delimiter = ";")
            nuevo = self.linkedListAListJugadores()
            writer.writerows(nuevo)
      
      
        
    #De LinkedList() a list()
    def linkedListAListJugadores(self):
        pivot = self.jugadores.head
        lista = list()
        while(pivot != None):
            n_lista = list()
            n_lista.append(str(pivot.data.nombre))
            n_lista.append(str(pivot.data.contrasena))
            n_lista.append(str(self.linkedListAListLogrosJug(pivot.data)))
            n_lista.append(str(self.linkedListAListNivelesJug(pivot.data)))
            n_lista.append(str(pivot.data.mejorMarca))
            lista.append(n_lista)
            pivot = pivot.next
        return lista
    
    def linkedListAListLogrosJug(self,jugador):
        pivot = jugador.logrosConseguidos.head
        lista = list()
        while(pivot!=None):
            if(isinstance(pivot.data, Logro)):
                lista.append(pivot.data.nombre)
            elif pivot == jugador.logrosConseguidos.head:
                lista.append("Logros")
            else:
                lista.append(pivot.data)
            pivot = pivot.next
        return lista

    def linkedListAListNivelesJug(self,jugador):
        pivot = jugador.nivelesCompletados.head
        lista = list()
        while(pivot!=None):
            if(isinstance(pivot.data,Nivel)):
                lista.append(pivot.data.nombre)
            elif pivot == jugador.nivelesCompletados.head:
                lista.append("Niveles")
            else:
                lista.append(pivot.data)
            pivot = pivot.next
        return lista
    
    
    
    #Verifica si tu decision(si el correo es malicioso o no) es correcta o no
    def validarCorreo(self, correo, decision):
        if(decision == self.correos.getCorreo(correo).malicioso):
            print("Bien hecho!")
        else:
            print("Oh no")
             
    def leerCorreo(self, correo_id, nivel_nombre):
        
        body_mal = self.getNivel(nivel_nombre).getCorreo(correo_id).descripcion
        body = body_mal.replace(r"\n","")
        lector = pyttsx3.init()
        voces = lector.getProperty('voices')
        #Voces en español 8,14,15,29,31
        lector.setProperty('voice', voces[15].id)     
        lector.say(body)
        lector.runAndWait()
        
        
        
    #Métodos para pasar de csv a LinkedList
    def crearNivelesLinked(self):
        levels = LinkedList()
        with open("ArchivosCSV//Niveles.csv",encoding = "UTF-8") as niv:
            archivo = csv.reader(niv, delimiter = ";")
            for fila in archivo:
                nombre = fila[0]
                dificultad = fila[1]
                nivel = Nivel(nombre = nombre,dificultad = dificultad)
                levels.addDatoFin(nivel)
        
        self.niveles = levels
        pivot = levels.head
        i = 1
        while pivot != None:
            if(i <= 5):
                with open("ArchivosCSV//Nivel" + str(i) + ".csv",encoding = "UTF-8") as corr:
                    archivo = csv.reader(corr, delimiter = ";")
                    for fila in archivo:
                        id = fila[0]
                        dificultad = fila[1]
                        tema = fila[2]
                        remitente = fila[3]
                        descripcion = fila[4]
                        malicioso = fila[5]
                        mail = Correo(id, dificultad, tema, remitente, descripcion, malicioso)
                        pivot.data.correos.addDatoFin(mail)                    
            i += 1
            pivot = pivot.next
        self.niveles = levels
        self.historia = levels
    
    def crearSinFinLinked(self):
        sinFin = LinkedList()
        with open("ArchivosCSV//CorreosSinFin.csv",encoding = "UTF-8") as mail:
            archivo = csv.reader(mail, delimiter = ";")
            for fila in archivo:
                id = fila[0]
                dificultad = fila[1]
                tema = fila[2]
                remitente = fila[3]
                descripcion = fila[4]
                malicioso = fila[5]
                mail = Correo(id, dificultad, tema, remitente, descripcion, malicioso)
                sinFin.addDatoFin(mail)
            self.sin_fin = sinFin
    
    def crearLogrosLinked(self):   
        logros = LinkedList()
        with open("ArchivosCSV//Logros.csv",encoding = "UTF-8") as log:
            archivo = csv.reader(log, delimiter = ";")
            for fila in archivo:
                nombre = fila[0]
                descripcion = fila[1]
                logro = Logro(descripcion,nombre )
                logros.addDatoFin(logro)
            self.logros = logros
             
    def crearJugadoresLinked(self):
        players = LinkedList()
        with open("ArchivosCSV//Jugadores.csv",encoding = "UTF-8") as usu:
            archivo = csv.reader(usu, delimiter = ";")
            
            for fila in archivo:
                nombre = fila[0]
                contrasena = fila[1]
                logrosConseguidos = fila[2].split(",")
                nivelesCompletados = fila[3].split(",")
                mejorMarca = fila[4]
                jugador = Jugador(nombre, contrasena, self.listALinkedListLogrosJugador(logrosConseguidos), self.listALinkedListNivelesJugador(nivelesCompletados), mejorMarca)
                players.addDatoFin(jugador)
            self.jugadores = players
    
    def crearCorreosLinked(self):
        mails = LinkedList()
        i = 1
        while i < 6:
            with open("ArchivosCSV//Nivel" + str(i) + ".csv",encoding = "UTF-8") as corr:
                archivo = csv.reader(corr, delimiter = ";")
                for fila in archivo:
                    id = fila[0]
                    dificultad = fila[1]
                    tema = fila[2]
                    remitente = fila[3]
                    descripcion = fila[4]
                    malicioso = fila[5]
                    mail = Correo(id, dificultad, tema, remitente, descripcion, malicioso)
                    mails.addDatoFin(mail)                    
            i += 1
        with open("ArchivosCSV//CorreosSinFin.csv",encoding = "UTF-8") as cor:
            archivo = csv.reader(cor, delimiter = ";")
            for fila in archivo:
                id = fila[0]
                dificultad = fila[1]
                tema = fila[2]
                remitente = fila[3]
                descripcion = fila[4]
                malicioso = fila[5]
                mail = Correo(id, dificultad, tema, remitente, descripcion, malicioso)
                mails.addDatoFin(mail)
        self.correos = mails
      


    #Pasar de list() a LinkedList()   
    def listALinkedListLogrosJugador(self,logros_lista):
        if len(logros_lista) > 0:
            logrosLinked = LinkedList()
            logrosLinked.head = Nodo(self.getLogro(logros_lista[0]))
            pivot = logrosLinked.head
            i = 1
            while i < len(logros_lista):
                pivot.next = Nodo(self.getLogro(logros_lista[i]))
                pivot = pivot.next
                i += 1
            return logrosLinked
        else:
            return
            
    def listALinkedListNivelesJugador(self, niveles_lista):
        if(len(niveles_lista) > 0):
            nivelesLinked = LinkedList()
            nivelesLinked.head = Nodo(self.getNivel(niveles_lista[0]))
            pivot = nivelesLinked.head
            i = 1
            while i < len(niveles_lista):
                pivot.next = Nodo(self.getNivel(niveles_lista[i]))
                pivot = pivot.next
                i += 1
            return nivelesLinked
        else: 
            return
            
            
            
    #Métodos get, todos funcionan ingresando un nombre o id y retornan un objeto
    def getCorreo(self, correo_id):
        pivot = self.correos.head
        sw = 0
        while pivot != None and sw == 0:
            if(pivot.data.id == correo_id):
                sw = 1
            else:
                pivot = pivot.next
        
        if sw == 1:
            return pivot.data
        else:
            return 
    
    def getJugador(self, jugador):
        pivot = self.jugadores.head
        sw = 0
        while pivot != None and sw == 0:
            if(pivot.data.nombre == jugador):
                sw = 1
            else:
                pivot = pivot.next
        
        if sw == 1:
            return pivot.data
        else:
            return 
        
    def getNivel(self, nombre):
        pivot = self.niveles.head
        sw = 0
        while pivot != None and sw == 0:
            if(pivot.data.nombre == nombre):
                sw = 1
            else:
                pivot = pivot.next
        
        if sw == 1:
            return pivot.data
        else:
            return 
    
    def getLogro(self, logro):
        pivot = self.logros.head
        sw = 0
        while pivot != None and sw == 0:
            if(pivot.data.nombre == logro):
                sw = 1
            else:
                pivot = pivot.next
        
        if sw == 1:
            return pivot.data
        else:
            return 
    
    def getCorreoNivel(self,correo_id,nivel_nombre):
        pivot = self.getNivel(nivel_nombre).head
        sw = 0
        while sw == 0 and pivot != None:
            if(pivot.data.getCorreo(correo_id).id == correo_id):
                sw = 1
            else:
                pivot = pivot.next
        
        if(sw == 1):
            return pivot.data.getCorreo(correo_id)
        else:
            return
  
    #Métodos mostrar, sirven para mostrar los nombres de los elementos en las linkedLists
    
    def mostrarNiveles(self):
        pivot = self.niveles.head
        while pivot != None:
            print("El nivel es : " + pivot.data.nombre + ", su dificultad es: " + pivot.data.dificultad)
            pivot = pivot.next
    
    def mostrarJugadores(self):
        pivot = self.jugadores.head
        while pivot != None:
            print("El nombre es : " + pivot.data.nombre + ", su contraseña es: " + pivot.data.contrasena + ", su mejor marca es: " + pivot.data.mejorMarca)
            pivot = pivot.next
    
    def mostrarLogros(self):
        pivot = self.logros.head
        while pivot != None:
            print("El nombre es : " + pivot.data.nombre + ", su descripcion es: " + pivot.data.descripcion)
            pivot = pivot.next      
    
    def mostrarCorreos(self):
        pivot = self.correos.head
        while pivot != None:
            print("El tema del correo es: " + pivot.data.tema + "La descripcion del correo es : " + pivot.data.descripcion)
            pivot = pivot.next


    def intro(video):
        video.set_size((1200,700))
        while True:
            video.draw(SCREEN,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTON:
                    video.close()
                    #se pone el juego

game = Juego()
game.crearNivelesLinked()
game.crearLogrosLinked()
game.crearJugadoresLinked()
game.crearCorreosLinked()
game.crearSinFinLinked()
game.intro(Video("Vids//Nivel1"))