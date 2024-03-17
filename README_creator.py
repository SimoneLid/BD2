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
    out.write("|Progetto|Testo e Soluzione Mancini|Testo e Soluzione Mia|\n|--------|:-----------------------:|:-------------------:|\n")
    for name in listdir:
        file=name[0]
        sysfile=name[1]
        out.write(f'|{file}|[Testo e Soluzione](../../raw/main/{dir}/{sysfile}/{sysfile}%20-%20Testo%20e%20Soluzione.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return

def writeProve(listdir,dir,out):
    out.write("|Progetto|Data|Testo|Soluzione|\n|--------|:--:|:---:|:-------:|\n")
    for name in listdir:
        year=name[0]
        month=name[1]
        file=name[2]
        sysfile=name[3]
        out.write(f'|{file}|{month}-{year}|[Testo](../../raw/main/{dir}/{year}-{month}-{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{sysfile}/{sysfile}.pdf)|\n')
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
            elif len(dirsplit)==3:
                dirsplit=[int(dirsplit[0]),int(dirsplit[1]),dirsplit[2]]
                dirsplit.append(dirsplit[2].replace(" ","%20"))
            else:
                dirsplit.append(dirsplit[0].replace(" ","%20"))
            listdir.append(dirsplit)
    if dir=="ProveD'Esame":
        listdir.sort(reverse=True)
        writeProve(listdir,dir,out)
    listdir.sort()
    if dir=="Esercizi":
        writeEsercizi(listdir,dir,out)
    elif dir=="ProgettiNuovi":
        writeProgNew(listdir,dir,out)
    elif dir=="ProgettiVecchi":
        writeProgOld(listdir,dir,out)

if __name__=="__main__":
    with open(OUT,mode="w",encoding="utf-8") as out:
        out.write("# BD2\nRepository contenente tutti gli esercizi e progetti del corso Basi Di Dati 2\n\n")
        for dir in LISTDIR:
            if dir=="ProgettiNuovi":
                dirsplit="Progetti Nuovi"
            elif dir=="ProgettiVecchi":
                dirsplit="Progetti Vecchi"
            elif dir=="ProveD'Esame":
                dirsplit="Prove D'Esame"
            else:
                dirsplit=dir
            out.write(f'## {dirsplit}\n\n<details>\n\n<summary>{dirsplit}</summary>\n\n')
            searchDir(dir,out)
            out.write("\n</details>\n\n")