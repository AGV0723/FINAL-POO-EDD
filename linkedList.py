class Nodo():
    #Constructores
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    #Constructores
    def __init__(self, head):
        self.head = head
    
    def __init__(self, head = None):
        self.head = head
        
    def addDatoFin(self, dato):
        if self.head == None:
            self.head = Nodo(dato)
            return
        else:
            pivot = self.head
            while pivot.next != None:
                pivot = pivot.next
            
            pivot.next = Nodo(dato)
    
    def mostrarLinked(self):
        pivot = self.head
        while pivot != None:
            if(pivot.data.nivelesCompletados.head.data != None):
                print(pivot.data.nivelesCompletados.head.data.nombre)
            pivot = pivot.next
    
    def mostrarLogros(self):
        pivot = self.head
        while pivot != None:
            print(pivot.data.nombre)
            pivot = pivot.next
            
    def mostrarNiveles(self):
        pivot = self.head
        while pivot != None:
            print(pivot.data.nombre)
            pivot = pivot.next