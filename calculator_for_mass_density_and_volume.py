mdv = input("Choose one to calculate M(mass), D(Density), V(Volume):  ")

if mdv == "m" or mdv == "M" or mdv == "mass" or mdv == "Mass" or mdv == "M(mass)":
    d = float(input("Density:  "))
    v = float(input("Volume: "))
    result = d*v # This is for mass only
elif mdv == "d" or mdv == "D" or mdv == "density" or mdv == "Density" or mdv == "D(Density)":
    m = float(input("Mass:  "))
    v = float(input("Volume: "))
    result = m/v # This is for Density only
elif mdv == "v" or mdv == "V" or mdv == "volume" or mdv == "Vomume" or mdv == "V(Volume)":
    m = float(input("Mass:  "))
    d = float(input("Density: "))
    result = m/d # This is for Density only
print("%.2f" % result) 