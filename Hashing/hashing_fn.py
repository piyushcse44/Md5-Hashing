import hashlib

def vigenere_encrypt(plaintext, key):


    # Obtengo la longitud de la clave para ayudar con el For y para la operación modular
    key_length = len(key)

    # Convierto la clave a una lista de valores enteros usando la función ord()
    # La función ord() en Python se utiliza para obtener el valor entero del código Unicode del carácter.
    key_as_int = [ord(i) for i in key]

    # Convirtiendo el texto plano a una lista de valores enteros usando la función ord()
    plaintext_int = [ord(i) for i in plaintext]

    # Inicializando la cadena que contendrá el texto cifrado
    ciphertext = ''

    # Iterando sobre cada carácter en el texto plano
    for i in range(len(plaintext_int)):
        # Calculando el valor cifrado usando la fórmula del cifrado de Vigenère, se usa 65536 porque es un número primo que es mayor que el tamaño del alfabeto ASCII
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 65536

        # Concatenando el carácter cifrado a la cadena cifrada
        ciphertext += chr(value)

    ciphertext_invertido = ciphertext[::-1] #Invierto la cadena de texto

    clave_invertida = key[::-1] #Invierto la cadena de texto


    hash_md5 = hashlib.md5(ciphertext_invertido.encode()).hexdigest() #Genero el hash MD5 de la cadena invertida


    #Recojo la longitud de la clave y la casteo a str para unirla a la cadena final
    longitudclave = str(key_length)

    #Uno la longitud, el texto cifrado, la clave original, y el hash:

    ciphertext_invertido_conclave_conhash = longitudclave + ciphertext_invertido + clave_invertida + hash_md5

    # Devolviendo el texto cifrado
    return ciphertext_invertido_conclave_conhash

def vigenere_decrypt(ciphertexto):


    numero_str = ""

    #Bucle para separar la longitud de la clave del parametro recibido, esto servirá después para extraer la clave de la cadena

    for caracter in ciphertexto:
        if caracter.isdigit():
            # Verificar si el carácter actual es un dígito
            numero_str += caracter
        else:
            # Si el carácter no es un dígito, salir del bucle
            break

    longitud_de_clave = int(numero_str)
    ayuda_para_recorte = len(str(longitud_de_clave))

    #Quito la longitud de la clave del texto cifrado que contiene el resto de datos
    ciphertexto = ciphertexto[ayuda_para_recorte:]


    #Separo el texto cifrado que aún está invertido, la clave y el hash.

    ciphertext = ciphertexto[:-32-longitud_de_clave]
    key = ciphertexto[-32-longitud_de_clave:-32]
    hash_md5 = ciphertexto[-32:]

    # Compara el hash MD5 generado en la función anterior y el hash MD5 calculado a partir del valor recibido
    if hashlib.md5(ciphertext.encode()).hexdigest() != hash_md5:
        return "Error: El texto cifrado ha sido modificado"


    #Regreso la cadena de texto invertida a su estado original
    ciphertext_invertido = ciphertext[::-1]

    #Regreso la clave invertida a su estado original
    key_invertida = key[::-1]

    # Obteniendo la longitud de la clave
    key_length = len(key_invertida)

    # Convirtiendo la clave a una lista de valores enteros usando la función ord()
    key_as_int = [ord(i) for i in key_invertida]

    # Convirtiendo el texto cifrado a una lista de valores enteros usando la función ord()
    ciphertext_int = [ord(i) for i in ciphertext_invertido]

    # Inicializando la cadena que contendrá el texto descifrado
    plaintext = ''

    # Iterando sobre cada carácter en el texto cifrado
    for i in range(len(ciphertext_int)):
        # Calculando el valor descifrado usando la fórmula del cifrado de Vigenère
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 65536

        # Concatenando el caráctertext descifrado a la cadena descifrada
        plaintext += chr(value)

    # Devolviendo el texto descifrado
    return plaintext

