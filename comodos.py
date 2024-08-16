def calcular_area_comodos(): #sintaxe inicial
total_area = 0

while True:

largura = float(input("Digite a largura do cômodo (em metros): ")) #sintaxe para escrever a medida utilizando o float puxando o imput
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

area_comodo = largura * comprimento #conta da area do comodo 
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") #impressao de toda a conta puxando a sintaxa formantando com duas casas decimais

total_area += area_comodo # conta para o total_area mais a area do comodo

mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() # sintaxe para adicionar mais comodos ao codigo
if mais_comodos != 's': # se caso a resposta for "s" continuara rodando
break #parar se caso nao for adicionados mais comodos

return total_area 

area_total = calcular_area_comodos()
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")