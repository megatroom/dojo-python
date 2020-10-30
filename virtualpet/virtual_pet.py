class VirtualPet:
    status = "awake"

    def eat(self, food_name):
        print(f"Comendo {food_name}...")

    def sleep(self):
        if self.status == "awake":
            print("Dormindo...")
            self.status = "sleeping"
        else:
            print("Você me acordou! :(")
            self.status = "awake"

    def wake_up(self):
        if self.status == "awake":
            print("Já estou acordado!")
        else:
            print("Acordei :)")


pet = VirtualPet()
option = ""
while option != "s":
    print()
    option = input("(C)omer, (A)cordar, (D)ormir ou (S)air: ").lower()
    if option == "c":
        food_name = input("Comida: ")
        pet.eat(food_name)
    elif option == "a":
        pet.wake_up()
    elif option == "d":
        pet.sleep()
