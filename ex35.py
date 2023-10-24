from sys import exit

#NOS LLEVA FINALMENTE A ESTA FUNCION
def gold_room():
    print " This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")
        
    if how_much < 50:
        print "Nice you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
        
#SI ELEGIMOS LA PUERTA IZQUIERDA NOS LLEVA
#A ESTA FUNCION, QUE SEGUN QUE TECLEEMOS NOS
#LLEVA A OTRA FUNCION.
#HAY ALGO CURIOSO EN ESTE BLOQUE DE CODIGO DONDE EN LA SECUENCIA IF,
#EXACTAMENTE EN "TAUNT BEAR" YA QUE SI LO TECLEEAMOS 2 VECES MORIREMOS
#Y SI LO TECLEAMOS SOLO 1 NO, YA QUE LE DAMOS A LA VARIANTE BEAR_MOVED
#EL ATRIBUTO NOT(FALSE) = TRUE, Y DESPUES DIRECTAMENTE SEA TRUE
#ESTO ES PARA QUE SI TECLEEAMOS 2 VECES LO MISMO MUERA 
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front another door."
    print "how are you going to move the bear?"
    bear_moved = False 
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True 
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
        
#SI ELEGIMOS LA PUERTA DERECHA NOS LLEVA 
#A ESTA FUNCION 
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
#FUNCION MUERTO + LA RAZON
def dead(why):
    print why, "Good job!"
    exit(0)
    
#AQUI ES DONDE COMIENZA CON LA FUNCION START
#SEGUIDAMENTE LLAMA A OTRA FUNCION SEGUN QUE
#HAS ELEGIDO SI RIGHT OR LEFT
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Wich one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()