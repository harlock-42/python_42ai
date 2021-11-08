from decimal import Decimal

t = ( 0, 4, 132.42222, 10000, 12345.67)
nb = float(t[3])
print("module_" + '{:02}'.format(t[0]) + ", ex_" + '{:02}'.format(t[1]) + " : " + "{:.2f}".format(t[2]) + ", " + "{:.2e}".format(Decimal(t[3])) + ", " + '{:.2e}'.format(Decimal(t[4])))