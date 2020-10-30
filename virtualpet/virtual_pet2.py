from virtual_pet import VirtualPet


class VirtualPet2(VirtualPet):
    def learn(self):
        if self.status == "awake":
            print("Estudando Python...")
        else:
            print("ZzZzZzZz...")


pet = VirtualPet2()
option = ""
while option != "s":
    print()
    option = input(
        "(C)omer, (A)cordar, (D)ormir, (E)studar ou (S)air: ").lower()
    if option == "c":
        food_name = input("Comida: ")
        pet.eat(food_name)
    elif option == "a":
        pet.wake_up()
    elif option == "d":
        pet.sleep()
    elif option == "e":
        pet.learn()
