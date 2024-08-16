def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): ##inicio do code, sintaxe para as variaves
taxa_juros_diaria = taxa_juros_anual / 365 / 100: ##Conta para as taxas de juros anuais e diarias 

juros = valor_principal * taxa_juros_diaria * dias_atraso ##conta com o valor principal com juros e atrasos

valor_total = valor_principal + juros #conta total com juros 
return valor_total, juros

valor_principal = 1000.00 
taxa_juros_anual = 5.0
dias_atraso = 30       #valores declarados para o code
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) #conta final u
print(f"Valor total a ser pago: R${valor_total:.2f}") # impressão do valor total puxando o resultado com o a sintaxa
print(f"Valor dos juros: R${juros:.2f}") # impressão do valor dos juros totais puxando o resultado com a sintaxa