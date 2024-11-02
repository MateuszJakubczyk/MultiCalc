from fractions import Fraction

def calculationDelta(valueA, valueB, valueC):
    global deltaElement
    delta = valueB ** 2 - (4 * valueA * valueC)
    deltaElement = round(delta ** 0.5)

def calculationX1(valueA, valueB, deltaElement):
    global x1, x2
    x1 = Fraction((-valueB) - deltaElement, (2 * valueA))
    x2 = Fraction((-valueB) + deltaElement, (2 * valueA))

valueA = int(input("Podaj współczynnik A równania kwadratowego: "))

while valueA <= 0:
    print('Wartość A nie moze być zerem!')
    valueA = int(input("Podaj współczynnik A równania kwadratowego, który nie jest zerem: "))

valueB = int(input("Podaj współczynnik B równania kwadratowego: "))
valueC = int(input("Podaj współczynnik C równania kwadratowego: "))

if valueB < 0:
    print(f"Równanie kwadratowe wyglada tak: {valueA}x² - {valueB}x + {valueC} = 0")
    calculationDelta(valueA, valueB, valueC)
    calculationX1(valueA, valueB, deltaElement)
    print("Wartość x1 to:", x1)
    print("Wartość x2 to:", x2)
else:
    print(f"Równanie kwadratowe wyglada tak: {valueA}x² + {valueB}x + {valueC} = 0")
    calculationDelta(valueA, valueB, valueC)
    calculationX1(valueA, valueB, deltaElement)
    print("Wartość x1 to:", x1)
    print("Wartość x2 to:", x2)