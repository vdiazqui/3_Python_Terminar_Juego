import random
import time


# FUNCIONES

# Funcion que carga las mejores puntuaciones
def best_scores(): 
    return {}
SCORE_BOARD = best_scores()

# Funcion que enseña las mejores puntuaciones
def show_best_scores():
    print ("The best scores registered are:")
    for name, number_of_attempts in SCORE_BOARD.items():
        print(f"{name}: {number_of_attempts} attempt")


# Funcion que tiene como variable nivel y devuelve un valor minimo y uno maximo.
def choose_range(nivel):
    max_values = [100, 1000, 1000000, 1000000000000]

    min_value = 0
    max_value = max_values[nivel-1]

    return min_value, max_value

# Funcion que con los valores devueltos por la anterior selecciona un entero aleatorio dentro de ese rango.
def choose_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Inicio del juego, se le pide al jugador que seleccione su nivel
level = int(input("Choose the difficulty level, the eassiest level being 1 and the hardest 4. Please enter a number from 1 to 4: "))
time.sleep(0.5)
print("You have chosen level " + str(level)+".")

# Se hace uso de los outputs de las funciones previamente definidas
min_value, max_value = choose_range(level)
target = choose_number(min_value, max_value)

# El proprio jugador determina su numero maximo de intentos
time.sleep(0.5)
maximum_attempts = int(input("Determine how many attempts do you want to have (you should enter an integer): "))

number_of_attempts = 0 #Contador de intentos

# Bucle que tiene lugar cuando los intentos son menores del maximo establecido por el jugador
while number_of_attempts < maximum_attempts:
    attempt = int(input(f"Enter a number inside the interval ({min_value}, {max_value}): " ))

    if attempt < min_value or attempt > max_value:
        print("You didn't pay attention. The number you entered is not in the chosen interval. Either way I will give you a clue: ")
    if attempt < target:
        print("Your number is too small.")
        number_of_attempts += 1
    elif attempt > target:
        print("Your number is too big.")
        number_of_attempts += 1
    else: #attempt == target:
        number_of_attempts +=1
        print("Good job! You were able to find the right number in " +str(number_of_attempts)+" attempts.")
        # Guardar los datos del jugador
        time.sleep(1)
        print ("We are going to record this score")
        time.sleep(0.5)
        Name = input("Please enter your name: ")
        SCORE_BOARD[Name] = number_of_attempts
        break
    print ("The number of attempts is "+ str(number_of_attempts)+".")
else: 
    print ("You have reached the maximum value of attempts")

show_best_scores()