import os

print("Complete File path with filename", __file__)
print("Complete File path of foler", os.path.dirname(__file__))
print(os.path.abspath(__file__))