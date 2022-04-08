# inspiration code for Python Unit Testing Project
import math
def surfaceArea():
    pass

def volume(rad):
    volume = math.pi * rad * rad * 4
    return volume
def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    print("\nThe Volume of a Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
