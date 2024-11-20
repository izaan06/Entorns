

codi_postal = input("Introdueix un codi postal: ")

if codi_postal == "08001":
    print("El codi postal 08001 correspon a la ciutat: Barcelona.")
elif codi_postal == "28001":
    print("El codi postal 28001 correspon a la ciutat: Madrid.")
elif codi_postal == "46001":
    print("El codi postal 46001 correspon a la ciutat: València.")
elif codi_postal == "41001":
    print("El codi postal 41001 correspon a la ciutat: Sevilla.")
else:
    print(f"No s'ha trobat cap ciutat amb el codi postal {codi_postal}.")
