# VARIABLES

alfanumerico = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'á', 'é', 'í', 'ó', 'ú',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'Á', 'É', 'Í', 'Ó', 'Ú',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

# FUNCIONES


def quitar_espcacios(cadena):
    '''Elimina los espacios de una cadena de caracteres'''
    cadena = cadena.replace(" ", "")
    return cadena


def quitar_no_alfanumericos(cadena):
    '''Elimina los caracteres no alfanumericos de una cadena de caracteres'''
    for c in cadena:
        if c not in alfanumerico:  # si no es un caracter alfanumerico
            cadena = cadena.replace(c, "")  # lo eliminamos
    return cadena


def todo_mayusculas(cadena):
    '''Pasa una cadena de caracteres a mayusculas'''
    cadena = cadena.upper()
    return cadena


def sustituir_tildes(cadena):
    '''Sustituye las letras con tilde de una cadena de caracteres por sus respectivas letras sin tilde'''
    cadena = cadena.replace("Á", "A")
    cadena = cadena.replace("É", "E")
    cadena = cadena.replace("Í", "I")
    cadena = cadena.replace("Ó", "O")
    cadena = cadena.replace("Ú", "U")
    return cadena


def palindromo(cadena):
    '''Comprueba si una cadena de caracteres es un palindromo'''
    cadena = quitar_espcacios(cadena)
    cadena = quitar_no_alfanumericos(cadena)
    cadena = todo_mayusculas(cadena)
    cadena = sustituir_tildes(cadena)
    if cadena == cadena[::-1]:
        return True
    else:
        return False


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    cadena = input("Introduce una cadena de caracteres: ")
    if palindromo(cadena):  # si es un palindromo
        print("Es un palindromo")
    else:  # si no lo es
        print("No es un palindromo")
