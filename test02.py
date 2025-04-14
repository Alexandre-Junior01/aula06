
# receber numeros de alunos e fazer a media aritmetica da turma#
i=0
soma=0
alunos=int(input("Digite o numero de alunos: "))
while i<= alunos:
    numb = int(input("digite a nota: "))
    soma += numb
    i += 1
media= soma/alunos
print(f"A media da turma é{media}")
