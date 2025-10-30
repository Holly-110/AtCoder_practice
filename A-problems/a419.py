data = {
    "red":"SSS",
    "blue":"FFF",
    "green":"MMM"
}

S = input()

if data.get(S, 0) == 0:
    print("Unknown")
else :
    print(data[S])
    