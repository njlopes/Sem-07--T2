nome = input().strip()

def estadocivil(x):
    caract_nome = len(nome)
    if x==1:
        nome_conj = input().strip()
        caract_conj=len(nome_conj)
        return print(caract_conj+caract_nome)
    elif x==2:
        return print(caract_nome)


es_civ = int(input())
x = estadocivil(es_civ)
