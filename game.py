import random


# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]


# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_failures = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []


print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

#seleccion nivel de dificultad
diffuculty="""******Dificultad******
        1.Facil
        2.Media
        3.Dificil
********************** 
                        """
print(diffuculty)

while True:
    level_difficulty= input("Ingrese el nivel de dificultad(1,2 o 3): ")
    if (level_difficulty >="1")and (level_difficulty <= "3"):
        break
    print("No has ingresa una opcion correcta, vuelva a ingresar la dificultad")
    
match  int(level_difficulty):
    case 1:
        vocals= []
        for letter in secret_word:
            if letter in "aeiou":
                vocals.append(letter)
                guessed_letters.append(letter)
            else:
                vocals.append("_")
        word_displayed="".join(vocals)
    case 2 : 
        word_displayed= secret_word[0] + "_" *(len(secret_word)-2)+ secret_word[-1]
        guessed_letters.append(secret_word[0])
        guessed_letters.append(secret_word[-1])
    case 3:
        word_displayed= "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

failures = 0
while failures < max_failures:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #Veirifico que se haya ingresado una letra
    if (letter==""):
        print("Error: No se ha ingresado una letra")
        failures += 1
        continue
    
    # Verificar si la letra ya ha sido adivinada(cuento como fallo solo si esa letra no estaba en la palabra a adivinar)
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        if letter not in secret_word :
            failures+=1
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures +=1
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanza tus {max_failures} permitidos.")
    print(f"La palabra secreta era: {secret_word}")
