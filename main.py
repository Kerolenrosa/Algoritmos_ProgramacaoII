from Aluno import Aluno
from AluEnsinoMedio import AluEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

aluno = Aluno (5, "Ana", "1245")
alu_Ens = AluEnsinoMedio (1, "Pedro", "1365","2021")
alu_Gra = AlunoGraduacao (2, "Luis", "9874","2/2020")

aluno.imprimir()
print()
alu_Ens.imprimir()
print()
alu_Gra.imprimir()