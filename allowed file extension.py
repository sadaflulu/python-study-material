allowed=["jpg","png","pdf","docx"]
file=input("enter file extension")
if file in allowed:
    print("allowed")
else:
    print('not allowed')