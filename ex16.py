# coding=utf-8

#MÓDULO
from sys import argv

script, filename = argv

print " we're going to erase %r." % filename
print "if you don't want that, hit CTRL- C (^C)."
print "if you want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#VACIANDO ARCHIVO
print "Truncating the file. Goodbye!"
target.truncate()

#ESCRIBIENDO SOBRE EL ARCHIVO
print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
x = line1 + 'n' + line2 + 'n' + line3
target.write(x)  

#AL CERRAR EL ARCHIVO ESTAMOS CREANDO UN ARCHIVO O SOBREESCRIBIENDO
print "And finally, we close it"
target.close()