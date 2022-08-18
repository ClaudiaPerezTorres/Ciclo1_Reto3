# Ciclo1_Reto3
El juego de picas y fijas.
Este juego consiste en adivinar los dígitos  que   componen un numero (normalmente de  4 o 5 digitos)  sin  dígitos que se  repitan  a partir de una serie de  intentos  en los que  se obtiene   como resultado  el numero de fijas y el numero  de picas. 
Fijas.  Son los   dígitos que aparecen  en la posición exacta  dentro del   numero a  adivinar 
Picas. Son los dígitos que   hacen parte del numero  a adivinar  pero no aparecen  en la posición correcta. 
Objetivo. Escribir un programa en Python que reciba una primera   entrada el numero  a adivinar  y en una segunda entrada  correspondiente a los intentos separados por “,”  que utiliza un contrincante a la hora de  adivinar el numero. Por simplicidad solo se procesaran números de 4 digitos 
-Primera   entrada. Numero a adivinar:1874
-Segunda entrada, intentos: 2345,3214,2345,5432
En cada intento  el programa debe imprimir la  salida “[1] – [2] – [3] en donde:
1.	Numero utilizado como intento
2.	La palabra fijas : n,  donde n es el numero de fijas. 
3.	La palabra picas: n,  donde n es el numero de  picas  calculadas  en el intento. 
Ejemplo: [1234] – [fijas:3]-[picas:0]
En el transcurrir  del juego  se pueden dar  2 situaciones. 
1.	El contrincante pierde: cuando el  contrincante haya llevado  a cab0 16 intentos  y aun no tenga   las 4 fijas.  En este   caso se deberá   imprimir: {LO SENTIMOS, PERDIO DESPUES DE [16] INTENTOS}
2.	El contrincante   gana, si el contrincante adivina  las 4  fijas  antes de llegar a los 16 intentos, se  deberá imprimir  adicionalmente  la siguiente  frase. {FELICITACIONES, GANA  DESPUES DE [N] INTENTOS} en  donde n  corresponde a los intentos  que se tuvieron. 
