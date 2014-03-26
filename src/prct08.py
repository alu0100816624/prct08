import modulo
Pi=3.141592653589
def error(nro_intervalos,nro_test, umbral):
  contador=0
  for i in range(nro_test):
    apri=modulo.aproximacion(nro_intervalos)
    error=abs(Pi-apri)
    if error>umbral:
      numero=numero+1
  fallo=(nro_test/numero)*100
  return fallo
import sys
if(len(sys.argv)==4):
   nro_intervalos=int(sys.argv[1])
   veces=int(sys.argv[2])
   umbral=float(sys.argc[3])
else:
  print("Como no ha introducido ningun valor de asignaran por defecto")
  nro_intervalos=5
  nro_test=5
  umbral=0.0005
Equivocacion=error(nro_itnervalos,nro_test,umbral)
print("El porcentaje de error es %5.3f" %Equivocacion)
  
   