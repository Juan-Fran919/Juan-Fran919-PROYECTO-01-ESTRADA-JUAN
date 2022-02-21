from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#Variables para el acceso del usuario
usuario_correcto = "Admin_LifeStore"
contraseña_correcta = "LifeS456"
acceso_usuario = False
intentos_acceso = 0

#Bienvenida 
print("Bienvenido al programa de revisión de la plataforma LifeStore\nIntroduzca el usuario y contraseña para acceder.\n")

#Ciclo del login
while not acceso_usuario:
  #Mensaje de intentos de acceso
  intentos_acceso += 1
  print(f"Nota considere que solo tiene 3 intentos para acceder con el usuario se encuentra en el intento {intentos_acceso}")
  #ingreso de usuario y contraseña
  usuario = input("Ingrese el usuario: ")
  contraseña = input("Ingrese la contraseña: ")
  if usuario == usuario_correcto and contraseña == contraseña_correcta:
    acceso_usuario = True
    print("Ha logrado acceder correctamente\n")
  else:
      if usuario == usuario_correcto:
        print("El usuario es correcto, coloque la contraseña correcta\n")
      else:
        print("Usuario no registrado\n")
  if intentos_acceso >= 3:
    exit()

#Procesos de los diferentes puntos 
#Para ordenar diccionarios
from operator import itemgetter
#Creo un diccionario para poder ver las ventas de cada producto y después lo ordeno
ventas_producto={}
for venta in lifestore_sales:
  id_producto = venta [1]
  realizado = venta[4]
  if realizado == 0:
    if id_producto not in ventas_producto.keys():
      ventas_producto[id_producto]=[]
    ventas_producto[id_producto].append(realizado)
for num_ventas in lifestore_products:
  id_producto = num_ventas[0]
  if id_producto not in ventas_producto.keys():
    ventas_producto[id_producto]=[]
#Esta parte interprete que tenia que sacar los ingresos por producto y ver cuales eran los mayores, pero después lo corregí y ya solo es el diccionario que nos dice la cantidad de ventas por artículo.
ganancias_producto={}
for ganancias in ventas_producto.keys():
  ganancia_producto = 0
  precio = lifestore_products[ganancias-1][2]
  cantidad=len(ventas_producto[ganancias])
  ganancias_producto[lifestore_products[ganancias-1][1]]=[cantidad]
#Ordene el diccionario para que después en el menú pueda imprimir los primeros 5 de la lista y obtener los artículos mas vendidos.
ganancias_producto_ord = sorted(ganancias_producto.items(), key = itemgetter(1), reverse = True)

#Creo un diccionario para poder ver las busquedas de cada producto y después lo ordeno
busqueda_productos = {}
for busqueda in lifestore_searches:
  id_producto = busqueda [1]
  realizado = 1
  if id_producto not in busqueda_productos.keys():
    busqueda_productos[id_producto]=[]
  busqueda_productos[id_producto].append(realizado)
for num_busquedas in lifestore_products:
  id_producto = num_busquedas[0]
  if id_producto not in busqueda_productos.keys():
    busqueda_productos[id_producto]=[]
numBusqueda_productos = {}
for numBusqueda in busqueda_productos.keys():
  cantidad = len(busqueda_productos[numBusqueda])
  numBusqueda_productos[lifestore_products[numBusqueda-1][1]]=[cantidad]
#Ordene el diccionario para que después en el menú pueda imprimir los primeros 10 de la lista y obtener los artículos mas buscados.
numBusqueda_productos_ord = sorted(numBusqueda_productos.items(), key = itemgetter(1), reverse = True)

# Creo un diccionario de ids por categoria
cat_prods = {}
for prod in lifestore_products:
    prod_id = prod[1]
    cat = prod[3]
    if cat not in cat_prods.keys():
        cat_prods[cat] = []
    cat_prods[cat].append(prod_id)
#Comienzo a separar por categorías para que en cada categoría crear un diccionario con los 5 menos vendidos y un diccionario con los menos 10 buscados. Dicho proceso lo repito con cada categoría.
#procesadores
venProcesadores={}
repeticiones_Vproce=0
for categoria in cat_prods["procesadores"]:
  venProcesadores[categoria]=[]
  venProcesadores[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venProcesadores_ord = sorted(venProcesadores.items(), key = itemgetter(1))
busProcesadores={}
repeticiones_Proce=0
for categoria in cat_prods["procesadores"]:
  busProcesadores[categoria]=[]
  busProcesadores[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busProcesadores_ord = sorted(busProcesadores.items(), key = itemgetter(1))

#Tarjetas de video
venTarjetasVideo={}
repeticiones_VtarjeV=0
for categoria in cat_prods["tarjetas de video"]:
  venTarjetasVideo[categoria]=[]
  venTarjetasVideo[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venTarjetasVideo_ord = sorted(venTarjetasVideo.items(), key = itemgetter(1))
busTarjetasVideo={}
repeticiones_TarjeV=0
for categoria in cat_prods["tarjetas de video"]:
  busTarjetasVideo[categoria]=[]
  busTarjetasVideo[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busTarjetasVideo_ord = sorted(busTarjetasVideo.items(), key = itemgetter(1))

#Tarjetas madre
venTarjetasMadre={}
repeticiones_VtarjeM=0
for categoria in cat_prods["tarjetas madre"]:
  venTarjetasMadre[categoria]=[]
  venTarjetasMadre[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venTarjetasMadre_ord = sorted(venTarjetasMadre.items(), key = itemgetter(1))
busTarjetasMadre={}
repeticiones_TarjeM=0
for categoria in cat_prods["tarjetas madre"]:
  busTarjetasMadre[categoria]=[]
  busTarjetasMadre[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busTarjetasMadre_ord = sorted(busTarjetasMadre.items(), key = itemgetter(1))

#Discos Duros
venDiscoD={}
repeticiones_Vdisco=0
for categoria in cat_prods["discos duros"]:
  venDiscoD[categoria]=[]
  venDiscoD[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venDiscoD_ord = sorted(venDiscoD.items(), key = itemgetter(1))
busDiscoD={}
repeticiones_Disco=0
for categoria in cat_prods["discos duros"]:
  busDiscoD[categoria]=[]
  busDiscoD[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busDiscoD_ord = sorted(busDiscoD.items(), key = itemgetter(1))

#Memorias usb
venMemoriasUSB={}
repeticiones_VmeUSB=0
for categoria in cat_prods["memorias usb"]:
  venMemoriasUSB[categoria]=[]
  venMemoriasUSB[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venMemoriasUSB_ord = sorted(venMemoriasUSB.items(), key = itemgetter(1))
busMemoriasUSB={}
repeticiones_MeUSB=0
for categoria in cat_prods["memorias usb"]:
  busMemoriasUSB[categoria]=[]
  busMemoriasUSB[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busMemoriasUSB_ord = sorted(busMemoriasUSB.items(), key = itemgetter(1))

#Pantallas
venPantallas={}
repeticiones_Vpanta=0
for categoria in cat_prods["pantallas"]:
  venPantallas[categoria]=[]
  venPantallas[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venPantallas_ord = sorted(venPantallas.items(), key = itemgetter(1))
busPantallas={}
repeticiones_Panta=0
for categoria in cat_prods["pantallas"]:
  busPantallas[categoria]=[]
  busPantallas[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busPantallas_ord = sorted(busPantallas.items(), key = itemgetter(1))

#Bocinas
venBocinas={}
repeticiones_Vboci=0
for categoria in cat_prods["bocinas"]:
  venBocinas[categoria]=[]
  venBocinas[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venBocinas_ord = sorted(venBocinas.items(), key = itemgetter(1))
busBocinas={}
repeticiones_Boci=0
for categoria in cat_prods["bocinas"]:
  busBocinas[categoria]=[]
  busBocinas[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busBocinas_ord = sorted(busBocinas.items(), key = itemgetter(1))

#Audifonos
venAudifonos={}
repeticiones_Vaudif=0
for categoria in cat_prods["audifonos"]:
  venAudifonos[categoria]=[]
  venAudifonos[categoria].append(ganancias_producto[categoria])
#Ordeno el diccionario de los menos vendidos de esta categoría para luego imprimir los primeros 5 en el menú.
venAudifonos_ord = sorted(venAudifonos.items(), key = itemgetter(1))
busAudifonos={}
repeticiones_Audif=0
for categoria in cat_prods["audifonos"]:
  busAudifonos[categoria]=[]
  busAudifonos[categoria].append(numBusqueda_productos[categoria])
#Ordeno el diccionario de los menos buscados de esta categoría para luego imprimir los primeros 10 en el menú.
busAudifonos_ord = sorted(busAudifonos.items(), key = itemgetter(1))

# Creo un diccionario con los productos y sus reseñas recibidas de cada uno.
prods_reviews = {}
for sale in lifestore_sales:
    prod_id = sale[1]
    review = sale[2]
    if prod_id not in prods_reviews.keys():
        prods_reviews[prod_id] = []
    prods_reviews[prod_id].append(review)
#Creo un diccionario con el promedio de reseñas de cada producto y su número de reseñas.
reseñaProductos={}
for id, reviews in prods_reviews.items():
  reseñaProductos[lifestore_products[id-1][1]]=[]
  calificacion=0
  entre=len(prods_reviews[id])
  for review in reviews:
    calificacion += review
  reseñaProductos[lifestore_products[id-1][1]].append(round((calificacion/entre), 1))
  reseñaProductos[lifestore_products[id-1][1]].append((entre))
#Ordenó el diccionario para poder imprimir en el menú los 5 productos con mejores y peores reseñas.
reseñaProductos_ord = sorted(reseñaProductos.items(), key = itemgetter(1))
mejoresReseñas=0
peoresReseñas=0

#Creo un diccionario que me diga que ventas se realizaron por mes.
ventas_mes={}
for meses in lifestore_sales:
  if meses[4] == 0:
    producto=meses[1]
    fecha = meses[3]
    _, mes,_ = meses[3].split("/")
    if mes not in ventas_mes.keys():
          ventas_mes[mes] = []
    ventas_mes[mes].append(producto)
  else:
    producto=meses[1]
    fecha = meses[3]
    _, mes,_ = meses[3].split("/")
    if mes not in ventas_mes.keys():
          ventas_mes[mes] = []  
#Creo un diccionario que me diga la suma de los ingresos por mes y numero de ventas por mes
suma_ventas_mes={}
for mes, ids in ventas_mes.items():
  suma_ventas_mes[mes]=[]
  suma=0
  numVentas=len(ventas_mes[mes])
  for id in ids:
    suma += lifestore_products[id-1][2]
  suma_ventas_mes[mes].append(suma)
  suma_ventas_mes[mes].append((numVentas))
#Ordeno el diccionario para imprimirlo en el menú de forma cronológica.
suma_ventas_mes_ord = sorted(suma_ventas_mes.items(), key = itemgetter(0))
suma_anual = 0

# Ordeno el diccionario para imprimirlo en el menú de forma que van primero los meses con más venta.
num_ventas_mes_ord = sorted(suma_ventas_mes.items(), key = itemgetter(1))
suma_anual2=0


#Ciclo del menu
acceso_menu = False
while not acceso_menu:
  print("Se encuentra dentro del menú de revisión de la plataforma LifeStore")
  print("Ingrese que dato quiere conocer de la plataforma o si desea terminar su consulta.")
  print("1: Productos más vendidos y productos rezagados.")
  print("2: Productos por reseña.")
  print("3: Numero de ventas y total de ingresos.")
  print("4: Salir.")
  apartado = input("Ingrese el numero de la consulta que quiere hacer: ")
  if apartado == "1":
    print("Estos son los 5 productos mas vendidos de la plataforma: ")
    #Impresión de los 5 artículos mas vendidos 
    for primeros5 in ganancias_producto_ord:
      print(primeros5[0])
      print("Unidades vendidas:",primeros5[1][0],"\n")
      if primeros5 == ganancias_producto_ord[4]:
        break
    print("Estos son los 10 productos mas buscados de la plataforma:")
    #Impresión de los 10 artículos mas buscados 
    for primeros10 in numBusqueda_productos_ord:
      print(primeros10[0])
      print("Busquedas: ",primeros10[1][0],"\n")
      if primeros10 == numBusqueda_productos_ord[9]:
        break
    print("Ahora por categoría se mostrarán los 5 productos menos vendidos y los 10 menos buscados:")
    print("Procesadores\n")
    print("Numero de ventas:")
    for primeros5 in venProcesadores_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_Vproce += 1
      if 5 == repeticiones_Vproce:
        break
    print("Numero de busquedas:")
    for primeros10 in busProcesadores_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_Proce += 1
      if 10 == repeticiones_Proce:
        break
    print("Tarjetas de video\n")
    print("Numero de ventas:")
    for primeros5 in venTarjetasVideo_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_VtarjeV += 1
      if 5 == repeticiones_VtarjeV:
        break
    print("Numero de busquedas:")
    for primeros10 in busTarjetasVideo_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_TarjeV += 1
      if 10 == repeticiones_TarjeV:
        break
    print("Tarjetas madre\n")
    print("Numero de ventas:")
    for primeros5 in venTarjetasMadre_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_VtarjeM += 1
      if 5 == repeticiones_VtarjeM:
        break
    print("Numero de busquedas:")
    for primeros10 in busTarjetasMadre_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_TarjeM += 1
      if 10 == repeticiones_TarjeM:
        break
    print("Discos duros")
    print("Numero de ventas:")
    for primeros5 in venDiscoD_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_Vdisco += 1
      if 5 == repeticiones_Vdisco:
        break
    print("Numero de busquedas:")
    for primeros10 in busDiscoD_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_Disco += 1
      if 10 == repeticiones_Disco:
        break
    print("Memorias USB")
    print("Numero de ventas:")
    for primeros5 in venMemoriasUSB_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_VmeUSB += 1
      if 5 == repeticiones_VmeUSB:
        break
    print("Numero de busquedas:")
    for primeros10 in busMemoriasUSB_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_MeUSB += 1
      if 10 == repeticiones_MeUSB:
        break
    print("Pantallas")
    print("Numero de ventas:")
    for primeros5 in venPantallas_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_Vpanta += 1
      if 5 == repeticiones_Vpanta:
        break
    print("Numero de busquedas:")
    for primeros10 in busPantallas_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_Panta += 1
      if 10 == repeticiones_Panta:
        break
    print("Bocinas")
    print("Numero de ventas:")
    for primeros5 in venBocinas_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_Vboci += 1
      if 5 == repeticiones_Vboci:
        break
    print("Numero de busquedas:")
    for primeros10 in busBocinas_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_Boci += 1
      if 10 == repeticiones_Boci:
        break
    print("Audifonos")
    print("Numero de ventas:")
    for primeros5 in venAudifonos_ord:
      print("\t",primeros5[0])
      print("\tVentas: ",primeros5[1][0],"\n")
      repeticiones_Vaudif += 1
      if 5 == repeticiones_Vaudif:
        break
    print("Numero de busquedas:")
    for primeros10 in busAudifonos_ord:
      print("\t",primeros10[0])
      print("\tBusquedas: ",primeros10[1][0],"\n")
      repeticiones_Audif += 1
      if 10 == repeticiones_Audif:
        break
  elif apartado == "2":
    print("A continuación, se muestran los 5 productos mejor y peor reseñados con su cantidad de reseñas:")
    print("Productos con mejor reseña")
    for primeros5 in reversed(reseñaProductos_ord):
      mejoresReseñas +=1
      print(primeros5[0])
      print("Reseña promedio:",primeros5[1][0],"\t Numero de reseñas: ",primeros5[1][1],"\n")
      if 5 == mejoresReseñas:
        break
    print("Productos con peor reseña")
    for primeros5 in reseñaProductos_ord:
      peoresReseñas +=1
      print(primeros5[0])
      print("Reseña promedio:",primeros5[1][0],"\t Numero de reseñas: ",primeros5[1][1],"\n")
      if 5 == peoresReseñas:
        break
  elif apartado == "3":
    print("A continuación, puede ver primero en orden cronológico y después en orden de meses con mayores ventas la cantidad de ingresos y ventas generados mensualmente, y por último el ingreso anual:")
    print("Orden cronológico")
    for mes, ventas in suma_ventas_mes_ord:
      print("Mes: ",mes," Numero de ventas: ",ventas[1]," Ingresos: $",ventas[0])
      suma_anual += ventas[0]
    print("Ingresos anuales: ", suma_anual)
    print("Orden de meses con mayores ventas")
    for mes, ventas in reversed(num_ventas_mes_ord):
      print("Mes: ",mes," Numero de ventas: ",ventas[1]," Ingresos: $",ventas[0])
      suma_anual2 += ventas[0]
    print("Ingresos anuales: ", suma_anual2)
  elif apartado == "4":
    acceso_menu = True
  else:
    print("No introdujo una opción válida intente de nuevo.\n")
print("Usted ha salido del programa.")

