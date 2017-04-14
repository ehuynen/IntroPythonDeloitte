from Mymodule import Animal

zebra = Animal("Zoe", 23)

zebra.description()

lion = Animal("Harry", 11)
print(lion.description())

#als ge een functie wilt kunt ge elke keer import math doen en dan functies binnen math gebruiken
import math
print(math.sqrt(36))

#als ge een specifieke functie daarvan vaak gebruikt kan dit ook:
from math import sqrt
print(sqrt(36))

#als ge gwn alle functies wilt importeren omdat dat makkelijker is
from math import *
print(acos(1))
#maar pas op want dan kan het dat ge functies importeert met dezelfde naam als uw functies!!
#Als ge dan al die functies overschrijft worden die van u overschreven!