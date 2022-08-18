#5726
#5623,5624,0526,5627,5728,5926,5721,0726,4726,5726
numero=input()
intentos=input()

#FUNCION QUE CONVIERTE LAS ENTRADAS A LISTAS
def convierte(num,intentos):
  numero = [int(k) for k in str(num)]
  intentos = [y for y in intentos.split(",")]
  intento=[]
  for i in intentos:
    intento.append([int(x) for x in str(i)] )
  return numero, intento

#FUNCION QUE COMPARA DOS LISTAS Y DEVUELVE FIJAS Y PICAS
def comparar(numero,intento):
  picas: int =0
  fijas: int =0
  for i in range(0,len(numero)):
    if(numero[i]==intento[i]):
      fijas+=1
    elif numero[i] in intento:
      picas+=1 
  return fijas,picas

#JUEGO PICAS FIJAS  
def juguemos_picas_fijas(numero, intentos):
  cont: int = 0
  num, lista = convierte(numero,intentos)
  for i in lista:
    fij,pic = comparar(num,i)
    cont+=1
    print("%s-[Fijas: %d]-[Picas: %d]" % (str(i).replace(", ", ""),fij,pic))
  if fij==4 and cont<= 16:
    print("{FELICITACIONES, GANA DESPUÉS DE [%d] INTENTOS}" % cont)
  else:
    print("{LO SENTIMOS, PERDIÓ DESPUÉS DE [%d] INTENTOS}" % cont) 

juguemos_picas_fijas(numero,intentos)