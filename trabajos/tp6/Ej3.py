materiasCurso = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
materiasReprob = []

print('\nINGRESE LAS NOTAS OBTENIDAS EN CADA MATERIA\n')
for asignatura in materiasCurso:
    nota = int(input(f'Nota de {asignatura}: '))
    if nota < 6:
        materiasReprob.append(asignatura)

print(f'\nDebe recursar las siguientes materias: {materiasReprob}\n')
