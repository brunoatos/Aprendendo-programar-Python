mesa=['Rodrigo','Rafael','luan']
naopagou=mesa.pop()
print ('O cliente',naopagou,'não pagou a conta')
novapessoa=input('Irei ter que adicionar mais uma pessoa na mesa, Qual seu nome?')
print ('Senhora(o) vai querer se juntar a mesa?')
print ('Ela respondeu: sim')
mesa.append(novapessoa.title())
print (mesa)
               