import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_diameter(self):
        return 2 * self.radius
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def grow(self):
        self.radius *= 2
    def get_radius(self):
        return self.radius


def get_valid_radius():
   #Prompt the user to enter a valid radius until a valid number is provided.
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius > 0:
                return radius
            else:
                print("Please enter a positive number for the radius.")
        except ValueError:
            print("Invalid input. Please enter a number with decimals.")

def main():
    print("Circle Calculator")

    # Get a valid radius from the user
    radius = get_valid_radius()

    # Create a Circle object with the provided radius
    circle = Circle(radius)

    while True:
        # Display the calculated properties
        print(f"Diameter: {circle.calculate_diameter():.2f}")
        print(f"Circumference: {circle.calculate_circumference():.2f}")
        print(f"Area: {circle.calculate_area():.2f}")

        # Ask if the user wants to grow the circle
        choice = input("Do you want the circle to grow? (yes/no): ").strip().lower()

        if choice == "yes":
            circle.grow()
        elif choice == "no":
            print(f"Goodbye! The final radius of the circle is: {circle.get_radius():.2f}")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
