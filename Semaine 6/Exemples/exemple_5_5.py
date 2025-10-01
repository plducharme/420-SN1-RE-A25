def plus_petit_diviseur_autre_que_un(nombre: int):
    div_pot = 2
    while nombre % div_pot != 0:
        div_pot += 1
    return div_pot


print(plus_petit_diviseur_autre_que_un(42))
print(plus_petit_diviseur_autre_que_un(77))
print(plus_petit_diviseur_autre_que_un(101))

