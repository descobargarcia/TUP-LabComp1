# 3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
# cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
# mostrar por pantalla las asignaturas que el usuario tiene que repetir

materiasCurso = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
materiasReprob = []

print('\nINGRESE LAS NOTAS OBTENIDAS EN CADA MATERIA\n')
for asignatura in materiasCurso:
    nota = int(input(f'Nota de {asignatura}: '))
    if nota < 6:
        materiasReprob.append(asignatura)

print(f'\nDebe recursar las siguientes materias: {materiasReprob}\n')
