# DAY 12

# Local vs Global
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function {enemies}")


increase_enemies()
print(f"Enemies outside function {enemies}")


# Local scope only exists inside the function, unless returned
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)  # this is not referenced

# Global Scope
player_health = 10


def drink_mix():
    print(player_health)  # this is ok, since player_health is assigned outside function, in the global scope


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()  # inside the scope of function drink_potion -> OK

drink_potion()  # outside the scope of function drink_potion -> ERROR


#   There is no block Scope
game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)    # this is fine, indentation has no block scope


# Setting a function variable a global one
enemies = 1


def increase_enemies():
    global enemies  # access global variable enemies
    enemies += 1
    print(f"Enemies inside function {enemies}")


# Global scope and CONST
PI = 3.14159    # convention is that the name of the const var is all UPPERCASE
