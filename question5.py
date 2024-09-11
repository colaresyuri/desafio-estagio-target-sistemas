def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Teste com string

string = input("Digite uma string: ")
print(f"String invertida: {inverter_string(string)}")
