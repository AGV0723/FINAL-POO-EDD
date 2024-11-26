class Jugador():
    
    #Constructores
    def __init__(self,nombre,contrasena,logrosConseguidos,nivelesCompletados, mejorMarca):
        self.nombre = nombre
        self.contrasena = contrasena
        self.logrosConseguidos = logrosConseguidos
        self.nivelesCompletados = nivelesCompletados
        self.mejorMarca = mejorMarca
        
    def __init__(self,nombre = None,contrasena = None, logrosConseguidos = None,nivelesCompletados = None, mejorMarca = None):
        self.nombre = nombre
        self.contrasena = contrasena
        self.logrosConseguidos = logrosConseguidos
        self.nivelesCompletados = nivelesCompletados
        self.mejorMarca = mejorMarca
    
    #Dado un nivel se verifica si este ha sido pasado o no
    def verificarEstadoNivel(self, nivel_nombre):
        pivot = self.nivelesCompletados.head
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