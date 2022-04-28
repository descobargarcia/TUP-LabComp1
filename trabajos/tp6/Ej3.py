materiasCurso = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
materiasReprob = []

print('\nINGRESE LAS NOTAS OBTENIDAS EN CADA MATERIA\n')
for asignatura in materiasCurso:
    while True:
        nota = int(input(f'Nota de {asignatura}: '))
        if nota >=0 and nota <=10:
            break
        print('\nLa nota debe estar entre 0 y 10')
    if nota < 6:
        materiasReprob.append(asignatura)

print(f'\nDebe recursar las siguientes materias: {materiasReprob}\n')
