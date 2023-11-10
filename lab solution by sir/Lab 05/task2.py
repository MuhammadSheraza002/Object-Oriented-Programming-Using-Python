def read_file(rollnos, names, cgpas):
    rollnos_f = open("rollnos.txt","r")
    names_f = open("names.txt","r")
    cgpas_f = open("cgpas.txt","r")
    for r in rollnos_f:
        rollnos.append(r.replace("\n",""))
    for n in names_f:
        names.append(n.replace("\n",""))
    for cgpa in cgpas_f:
        cgpas.append(cgpa)

def write_file(rollnos, names, cgpas):
    file = open("record.txt","w")
    for i in range(len(rollnos)):
        file.write(f'{rollnos[i]} ')
        file.write(f'{names[i]} ')
        file.write(f'{cgpas[i]} ')

def task2():
    rollnos=[]
    names=[]
    cgpas=[]
    read_file(rollnos, names, cgpas)
    write_file(rollnos, names, cgpas)

task2()
