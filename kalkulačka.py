print("zde jsi v kalkulačce \n pro ukončení programu napiš 'konec' ")

while True:
 cislo1 = float (input("první číslo :"   ))
 cislo2 = float (input("druhé číslo :"   ))

 operace = input ("jakou chceš operaci ? '+, -, *, /, **, odmocneni, konec    :         ")
 if operace == "+" :
  print (cislo1 + cislo2)
 elif operace == "-" :
  print (cislo1 - cislo2)
 elif operace == "*" :
  print (cislo1 * cislo2)
 elif operace == "/" :
  print (cislo1 / cislo2)
 elif operace =="**" :
  print (cislo1 ** cislo2)
 elif operace == "odmocneni":
  print (cislo1 **(1/cislo2))
 elif operace == "konec" :
  print ("kalkulačka se ukončuje")
  break
 else:
  print("napiš správnou operaci")






