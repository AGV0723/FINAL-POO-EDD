class Correo():
    #Constructores
    def __init__(self,id,dificultad, tema, remitente, descripcion, malicioso, verificado):
        self.id = id
        self.dificultad = dificultad
        self.tema = tema
        self.remitente = remitente
        self.descripcion = descripcion
        self.malicioso = malicioso
        self.verificado = verificado
    
    def __init__(self,id = None,dificultad = None, tema = None, remitente = None, descripcion = None, malicioso = None, verificado = None):
        self.id = id
        self.dificultad = dificultad
        self.tema = tema
        self.remitente = remitente
        self.descripcion = descripcion
        self.malicioso = malicioso
        self.verificado = verificado