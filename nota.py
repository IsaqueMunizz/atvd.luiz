def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): #sintaxe inicial declarando as variaveis 

num_alunos = len(notas)
aprovados = []
reprovados = []

for aluno, nota in notas.items():
total_notas += nota
if nota >= nota_minima_aprovacao:
aprovados.append(aluno)
else:
reprovados.append(aluno)
#declarando nota dos alunos 
media_turma = total_notas / num_alunos #conta para a media das notas da sala 

return media_turma, aprovados, reprovados #lista dos aprovados

notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70 #sintaxe declarando a nota minima para pasaar

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)#conta para calcular a media de aprovaçoes

print(f"Média da turma: {media_turma:.2f}") #impressao da media da turma 
print(f"Alunos aprovados: {', '.join(aprovados)}")#lista dos aprovados
print(f"Alunos reprovados: {', '.join(reprovados)}") #lista dos reprovados