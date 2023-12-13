#comentario 1
palabras_odenadas=str

palabras=[]
for i in range(5):
    palabra=input(f"ingrese la palabra {i+1:} ")
    palabras.append(palabra)
    
    #comentario 2 
    def ordenar_por_tamaño(palabras):
     return sorted(palabras,key=len,reverse=True)

#comentario 3
while True:
 print("\n seleccione una opcion:")
 print("1.Orden alfabetico")
 print("2.Orden de tamaño,de la mas grande a la mas corta")
 print("3 orden aleatorio")
 print("4 orden inverso al ingresado")
 print("5 orden igual al ingresado ")
 print("6 salir")
 
 seleccion=input("Elija una opcion ")
 
 
 
 match seleccion:
     case "1":
         palabras_odenadas = sorted (palabras)
     case "2":
         palabras_odenadas= ordenar_por_tamaño (palabras)
     case "3": 
         import random
         random.shuffle(palabras)
         palabras_ordenadas=palabras
     case "4":
         palabras_odenadas= list(reversed(palabras))
     case "5":
         palabras_odenadas= palabras
     case "6": 
         break
     case "_":
         print("opcion no valida.Elija una opcion del 1 al 6")
         
     # comentario 4
 
 
 print("ordenado segun la la funcion")
 print(f"\n{palabras_odenadas:}")
 for palabra in palabras_odenadas:
    print(palabra)