

#Creo un objeto
class Pokemon():
    def __init__(self, nombre, habilidad, fuerza, inteligencia, vida):
        self.pokemon_elegido = nombre
        self.habilidad = habilidad
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida

class NuestroPokemon(Pokemon):
    def __init__(self, nombre, habilidad, fuerza, inteligencia, vida):
        self.pokemon_elegido = nombre
        self.habilidad = habilidad
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
    
    #Interacción con el usuario
    def election(self):
        print("Selecciona un Pokemon")
        print("1.Pikachu")
        print("2.Charizard")
        print("Ingresa el numero de tu eleccion")
        opcion = input(">>>  ")

        if opcion == '1':
            self.pokemon_elegido = "Pikachu"
            self.habilidad = "Rayo"
            self.fuerza = 90
            self.inteligencia = "80"
            self.vida = 1000
        elif opcion == '2':
            self.pokemon_elegido = "Charizard"
            self.habilidad = "fuego"
            self.fuerza = 110
            self.inteligencia = "90"
            self.vida = 800
        else:
            print("Type again")
            
    #Se imprime la opcion elegida    
    def meeting(self):
        if self.pokemon_elegido:
            print(f"Hola, me presento soy {self.pokemon_elegido} espero que nos llevemos bien.")
            print(f"Poseo una habilidad {self.habilidad}, una fuerza de {self.fuerza} puntos una inteligencia de {self.inteligencia} puntos y unos {self.vida} puntos de vida")
            print(" ")
    
class Enemigo(Pokemon):
    def __init__(self, nombre, habilidad, fuerza, inteligencia, vida):
        self.pokemon_elegido = nombre
        self.habilidad = habilidad
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida

    #Interaccion con el usuario
    def  election2(self):
        print("Selecciona un Pokemon con el que quieras luchar")
        print("1.Pikachu")
        print("2.Charizard")
        print("Ingresa el numero de tu eleccion")
        opcion = input(">>>  ")

        if opcion == '1':
            self.pokemon_elegido = "Pikachu"
            self.habilidad = "Rayo"
            self.fuerza = 90
            self.inteligencia = "80"
            self.vida = 100
        elif opcion == '2':
            self.pokemon_elegido = "Charizard"
            self.habilidad = "fuego"
            self.fuerza = 85
            self.inteligencia = "90"
            self.vida = 100
        else:
            print("Type again")

    #Se imprime la opcion eligida
    def meeting2(self):
        if self.pokemon_elegido:
            print(f"Hola, me presento soy {self.pokemon_elegido} espero que nos llevemos bien.")
            print(f"Poseo una habilidad {self.habilidad}, una fuerza de {self.fuerza} puntos una inteligencia de {self.inteligencia} puntos y unos {self.vida} puntos de vida")
            print(" ")
    
    


print("Bienvenido a mi juego!!!")
nombre_usuario = input("¿Cuál es tu nombre?: ")

first_pokemon = NuestroPokemon("", "", "", "", "")
second_pokemon = Enemigo("", "", "", "", "")

first_pokemon.election()
first_pokemon.meeting()
second_pokemon.election2()
second_pokemon.meeting2()

print("Ahora es el comienzo de la lucha!!!")
print("¿Quién ganará?")

print(f"Nuestro Pokemon {first_pokemon.pokemon_elegido} va a luchar contra {second_pokemon.pokemon_elegido}")
print("")

vida_mia = first_pokemon.vida
vida_enemiga = second_pokemon.vida

fuerza_mia = first_pokemon.fuerza
fuerza_enemiga = second_pokemon.fuerza


while vida_mia > 0 and vida_enemiga > 0:
    
    #Ataque al enemigo
    vida_enemiga = vida_enemiga - fuerza_mia

    print(f"Nuestro pokemon {first_pokemon.pokemon_elegido} ha atacado a {second_pokemon.pokemon_elegido} ahora {second_pokemon.pokemon_elegido} tiene una vida de {vida_enemiga}")

    #Comprobacion si el enemigo ha sido derrotado
    if vida_enemiga <= 0:
        print(f"{first_pokemon.pokemon_elegido} ha ganado!")
        break

    vida_mia = vida_mia - fuerza_enemiga

    print(f"El enemigo {second_pokemon.pokemon_elegido} ha atacado a nuestro pokemon {first_pokemon.pokemon_elegido} ahora {first_pokemon.pokemon_elegido} tiene una vida de {vida_mia}")

    if vida_mia <= 0:
        print("Nuestro pokemon ha sido derrotado")
    

print("")

print(f"Ha sido un placer conocerte {nombre_usuario} espero que te haya gustado mi juego ")