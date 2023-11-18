"""un programa que al ingresar el usuario un numero romano
 este lo transforma en un numero entero!"""

 
class Solution:
    def __init__(self):
        self.valores = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    def romanToInt(self, s):
        entero = 0
        for i in range(len(s)):
            if i > 0 and self.valores [s[i]]> self.valores[s[i-1]]:
                entero +=self.valores[s[i]]-2 * self.valores[s[i-1]]
            else:
                entero += self.valores[s[i]]
        return entero
        
conversor = Solution()
s= input("ingrese el numero romano a tranformar:\n")
valor_numerico=conversor.romanToInt(s)
print(valor_numerico)