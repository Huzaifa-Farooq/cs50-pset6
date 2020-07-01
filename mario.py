
height = int(input("Height: "))
spaces = height


for i in range(0, height):

    # inner loop to manage number spaces
    for j in range(0, spaces):
        print("  ", end="")

    # decrementing spaces
    spaces -= 1

    iteration = 0

    for k in range(i+1):
        print("#", end=" ")

    # Adding two spaces b/w pyramids
    print("  ", end="")

    for k in range(i+1):
        print("#", end=" ")
    # ending line after each row
    print("")
