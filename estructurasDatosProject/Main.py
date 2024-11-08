tupla=()#tuypla
print(tupla)
tupla2 = ("apple",2018,"samsung",4.9,"t", True)
"las tuplas son inmutables"
print(tupla2)

print(tupla2[1])
print(tupla2[3])

tupla3="a","b","c","d"
tupla4= (1,2,3,4)
#concatenar tuplas
tupla5 = tupla3+ tupla4
print(tupla5)
#repetir
tupla6=tupla3*3
print(tupla6)

#Enlazada
tupla7 =(0,1,2,3)
tupla8=("A","B","C")
tupla9= (tupla7,tupla8)
print(tupla9)
print(tupla9[1][1])


#comparar
tupla10=("Rojas")
tupla11=(123)
tupla12=("Rosas")
tupla13=("rosas")
print(tupla10 <tupla12)