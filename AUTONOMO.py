import random

def main():
    clave = ""
    letMayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letMinus = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    tieneMayus = 0
    tieneMinus = 0
    tieneNumero = 0
    longitud = 0

    while(longitud < 8):
        longitud = int(input("Ingrese la longitud minima de su contraseña:"))
        if(longitud < 8):
            print("La Longitud minima es 8")


    while not(tieneMayus > 0 and tieneMinus > 0 and tieneNumero > 0 and (tieneMayus + tieneMinus + tieneNumero ) > 9):
        aleatorio = random.randint(0,25)
        tipo = random.randint(1,3)

        if(tipo == 1):
            clave = clave + letMayus[aleatorio]
            tieneMayus = tieneMayus + 1
        elif(tipo == 2):
            clave = clave + letMinus[aleatorio]
            tieneMinus = tieneMinus + 1
        else:
            aleatorio = random.randint(0,9)
            clave = clave + numeros[aleatorio]
            tieneNumero = tieneNumero + 1
    
    print("Clave generada:",clave)
            

if __name__ == "__main__":
    main()