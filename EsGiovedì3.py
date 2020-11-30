x = int(input("numero distanza lancio di marco"))
y = int(input("numero distanza lancio di giacomo"))
if x > y:
    print("marco ha vinto con ", x)
elif x == y:
    print("pari")
else:
    print("giacomo ha vinto con ", y)