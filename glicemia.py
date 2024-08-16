def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #sintaxe inicial declarando as variaveis

if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: 
return "Diabetes"
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
return "Pré-diabetes"
else:
return "Normal"
#conta para medição da diabates que se caso passar de 200 ja entra como diabetico se der entre 126 e 140 ja sera pré diabetico se caso for abaixo sera considerado normal 
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #sintaxe para declarar a glicemia
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) #sintaxe para declarar a glicemia pos-prandial

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) #resultado final
print(f"O diagnóstico é: {resultado}") #impressao do resultado