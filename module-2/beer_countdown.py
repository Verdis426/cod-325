# Name: Verdis
# Course: CSD-325
# Assignment: Module 2 - Documented Debugging

def countdown(bottles):
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around.")
        bottles -= 1
        print(f"{bottles} bottles of beer on the wall.\n")


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown(bottles)


if __name__ == "__main__":
    main()