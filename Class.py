class personaje():
   
    
    #__init__ sirve para inicializar los atributos de la clase
    # self es el metodo para poder acceder a los parametros del objeto y su clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print("|",self.nombre, ":")
        print("|",self.fuerza)
        print("|",self.inteligencia)
        print("|",self.defensa)
        print("|",self.vida)
        
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def estar_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
        
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a ", enemigo.nombre)
        
        if enemigo.estar_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)

        else:
            enemigo.morir()



guerrero = personaje("chronos", 10, 1, 5, 100)
enemigo = personaje("aldebaran", 8, 5, 3, 5)
guerrero.atacar(enemigo)
enemigo.atributos()

