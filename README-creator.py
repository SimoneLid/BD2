import os


LISTDIR=["Esercizi","ProgettiNuovi","ProgettiVecchi","ProveD'Esame"]
ROOT=os.getcwd()
OUT="README.md"


def writeEsercizi(listdir,dir,out):
    out.write("|Esercizio|Testo|Soluzione|\n|---------|:---:|:-------:|\n")
    for name in listdir:
        num=name[0]
        file=name[1]
        sysfile=name[2]
        out.write(f'|{file}|[Testo](../../raw/main/{dir}/{num}-{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{num}-{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{num}-{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return

def writeProgNew(listdir,dir,out):
    out.write("|Progetto|Testo|Soluzione|\n|--------|:---:|:-------:|\n")
    for name in listdir:
        num=name[0]
        file=name[1]
        sysfile=name[2]
        out.write(f'|{file}|[Testo](../../raw/main/{dir}/{num}-{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{num}-{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{num}-{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return

def writeProgOld(listdir,dir,out):
    out.write("|Progetto|Testo e/o Soluzione Mancini|Soluzione Mia|\n|--------|:-----------------------:|:-------------------:|\n")
    for name in listdir:
        print(name)
        file=name[0]
        sysfile=name[1]
        if os.path.exists(f'{ROOT}/{dir}/{file}/{file} - Testo e Soluzione.pdf'):
            out.write(f'|{file}|[Testo e Soluzione](../../raw/main/{dir}/{sysfile}/{sysfile}%20-%20Testo%20e%20Soluzione.pdf)|')
        elif os.path.exists(f'{ROOT}/{dir}/{file}/{file} - Testo.pdf'):
            out.write(f'|{file}|[Testo](../../raw/main/{dir}/{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return

def writeProve(listdir,dir,out):
    out.write("|Progetto|Data|Testo|Soluzione|\n|--------|:----:|:---:|:-------:|\n")
    for name in listdir:
        year=name[0]
        month=name[1]
        day=name[2]
        file=name[3]
        sysfile=name[4]
        out.write(f'|{file}|{day}/{month}/{year}|[Testo](../../raw/main/{dir}/{year}-{month}-{day}-{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{year}-{month}-{day}-{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return

def searchDir(dir,out):
    listdir=[]
    for subdir in os.listdir(dir):
        if os.path.isdir(f'{ROOT}/{dir}/{subdir}/'):
            dirsplit=subdir.split("-")
            if len(dirsplit)==2:
                dirsplit=[int(dirsplit[0]),dirsplit[1]]
                dirsplit.append(dirsplit[1].replace(" ","%20"))
            elif len(dirsplit)==4:
                dirsplit=[int(dirsplit[0]),int(dirsplit[1]),int(dirsplit[2]),dirsplit[3]]
                dirsplit.append(dirsplit[3].replace(" ","%20"))
            else:
                dirsplit.append(dirsplit[0].replace(" ","%20"))
            listdir.append(dirsplit)
    if dir=="ProveD'Esame":
        listdir.sort(reverse=True)
        writeProve(listdir,dir,out)
    elif dir=="ProgettiVecchi":
        listdir.sort(key= lambda x: x[0].lower())
        writeProgOld(listdir,dir,out)
    elif dir=="Esercizi":
        listdir.sort()
        writeEsercizi(listdir,dir,out)
    elif dir=="ProgettiNuovi":
        listdir.sort()
        writeProgNew(listdir,dir,out)

if __name__=="__main__":
    with open(OUT,mode="w",encoding="utf-8") as out:
        out.write("# BD2\nRepository contenente tutti gli esercizi e progetti del corso Basi Di Dati 2.<br>\nIn particolare ci sono:\n- Esercizi 2023/2024\n- Progetti 2023/2024\n- Progetti 2022/2023 con soluzione (non tutti) di Toni Mancini\n- Prove D'Esame fino al 2021\n\n")
        for dir in LISTDIR:
            if dir=="ProgettiNuovi":
                dirsplit="Progetti Nuovi"
            elif dir=="ProgettiVecchi":
                dirsplit="Progetti Vecchi"
            elif dir=="ProveD'Esame":
                dirsplit="Prove D'Esame"
            else:
                dirsplit=dir
            out.write(f'## {dirsplit}\n\n<details open>\n\n<summary>{dirsplit}</summary>\n\n')
            searchDir(dir,out)
            out.write("\n</details>\n\n")