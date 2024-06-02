import os


LISTDIR=["Progetti","Prove D'Esame"]
ROOT=os.getcwd()
OUT="README.md"



def writeProgOld(listdir,dir,out):
    out.write("|Progetto|Testo e/o Soluzione|Soluzione Mia|\n|--------|:-----------------:|:-----------:|\n")
    for name in listdir:
        file=name[0]
        sysfile=name[1]
        out.write(f'|{file}|[Testo](../../raw/main/{dir}/{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{dir}/{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return


def writeProve(listdir,dir,out):
    sysdir=dir.replace(" ","%20")
    out.write("|Progetto|Data|Testo|Soluzione|\n|--------|:--:|:---:|:-------:|\n")
    for name in listdir:
        year=name[0]
        month=name[1]
        day=name[2]
        file=name[3]
        sysfile=name[4]
        out.write(f'|{file}|{day}/{month}/{year}|[Testo](../../raw/main/{sysdir}/{year}-{month}-{day}-{sysfile}/{sysfile}%20-%20Testo.pdf)|')
        if os.path.exists(f'{ROOT}/{dir}/{year}-{month}-{day}-{file}/{file}.pdf'):
            out.write(f'[Soluzione](../../raw/main/{sysdir}/{year}-{month}-{day}-{sysfile}/{sysfile}.pdf)|\n')
        else:
            out.write("-|\n")
    return


def searchDir(dir,out):
    listdir=[]
    for subdir in os.listdir(dir):
        if os.path.isdir(f'{ROOT}/{dir}/{subdir}/'):
            dirsplit=subdir.split("-")
            if len(dirsplit)==4:
                dirsplit=[int(dirsplit[0]),int(dirsplit[1]),int(dirsplit[2]),dirsplit[3]]
                dirsplit.append(dirsplit[3].replace(" ","%20"))
            else:
                dirsplit.append(dirsplit[0].replace(" ","%20"))
            listdir.append(dirsplit)
    if dir=="Prove D'Esame":
        listdir.sort(reverse=True)
        writeProve(listdir,dir,out)
    elif dir=="Progetti":
        listdir.sort(key= lambda x: x[0].lower())
        writeProgOld(listdir,dir,out)


if __name__=="__main__":
    with open(OUT,mode="w",encoding="utf-8") as out:
        out.write("# BD2\nRepository contenente tutti i progetti e le prove d'esame svolti da me durante il corso Basi Di Dati 2.\n")
        out.write("### Informazioni sui progetti\nIl testo viene sottolineato con diversi colori ognuno indicante una parte specifica dell'analisi:\n")
        out.write("|Colore|Significato|\n|:----:|:---------:|\n|${\color{blue}\\text{BLU}}$|Classi|\n|${\color{red}\\text{ROSSO}}$|Attributi|\n|${\color{yellow}\\text{GIALLO}}$|Associazioni|\n|${\color{green}\\text{VERDE}}$|Use-case|\n\n")
        for dir in LISTDIR:
            out.write(f'## {dir}\n\n')
            searchDir(dir,out)
            out.write("\n\n")