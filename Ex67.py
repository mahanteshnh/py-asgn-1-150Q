'''kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))'''

kpa = float(input("Input the pressure in kilopascals > "))
pressure_in_psi = round(kpa * 0.145038,3)
pressure_in_mmHg = round(kpa * 7.50062, 3)
pressure_in_atmp = round(kpa * 0.0098692382432766,3)
print(f"Pressure = {pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")

