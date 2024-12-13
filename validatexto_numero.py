def validar_litros(litros):
  """Valida se a entrada de peso contém apenas dígitos numéricos."""
  return litros.isdigit()
  
def validar_texto(texto):
    """Valida se a entrada de peso contém apenas dígitos numéricos."""
    return texto.isalpha()
    

while True:
  litros_digitado = input("Digite a quantidade de litros: ")
  if validar_litros(litros_digitado):
    break  # Sai do loop se a quantidade de litros for válido
  else:
    print("litros inválido. Digite apenas numeros.")
    
while True:
  texto_digitado = input("Digite o texto: ")
  if validar_texto(texto_digitado):
    print("texto válido!")
    break  # Sai do loop se texto digitado for válido
  else:
    print("texto digitado inválido. Digite apenas texto ")
