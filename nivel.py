from linkedList import LinkedList 
class Nivel():
    #Constructores
    def __init__(self,nombre, correos, dificultad):
        self.nombre = nombre
        self.correos = correos
        self.dificultad = dificultad
    
    def __init__(self,nombre = None, correos = LinkedList(), dificultad = None):
        self.nombre = nombre
        self.correos = correos
        self.dificultad = dificultad

    def getCorreo(self, id):
        pivot = self.correos.head
        sw = 0
        while pivot != None and sw ==0:
            if(pivot.data.id == id):
                sw = 1
            else:
                pivot = pivot.next
        
        if(sw == 1):
            return pivot.data
        else:
            return