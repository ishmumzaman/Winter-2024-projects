from Numbers import *

x = P_generator()
y = M_Generator()
z = C_Generator()
while True:

    def redirect(x, y , z):
        while True:
            choice = (input("""Welcome to The Drug Store. There are 3 areas and you need tickets to get in. 
        Choose the number according to the area that you want to go:
        1. Perfumes
        2. Medicines
        3. Cosmetics
        Choose 1,2 or 3: """))
            if choice.isdigit() == True and (len(choice) == 1):
                choice = int(choice)

                if choice == 1:
                    Perfumes(x)
                if choice == 2:
                    Medicines(y)
                if choice == 3:
                    Cosmetics(z)

            else:
                print("Please enter only a letter")
                continue

    @greeting
    def Perfumes(x):

        print(f"P - {next(x)}")



    @greeting
    def Medicines(y):

        print(f"M - {next(y)}")

    @greeting
    def Cosmetics(z):

        print(f"C - {next(z)}")


    redirect(x, y, z)







