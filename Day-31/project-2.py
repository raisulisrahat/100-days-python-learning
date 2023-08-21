# Here i am showing the Day 22 practice project

# Geometry Calculator
import math

class GeometryCalculator:
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def calculate_rectangle_area(width, height):
        return width * height

    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

def main():
    print("Welcome to the Geometry Calculator!")

    while True:
        print("\nMenu:")
        print("1. Calculate the area of a circle")
        print("2. Calculate the area of a rectangle")
        print("3. Calculate the area of a triangle")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            area = GeometryCalculator.calculate_circle_area(radius)
            print(f"The area of the circle is: {area}")
        elif choice == '2':
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            area = GeometryCalculator.calculate_rectangle_area(width, height)
            print(f"The area of the rectangle is: {area}")
        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = GeometryCalculator.calculate_triangle_area(base, height)
            print(f"The area of the triangle is: {area}")
        elif choice == '4':
            print("Exiting the Geometry Calculator.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
