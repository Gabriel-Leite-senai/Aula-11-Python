import sqlite3


def input_int(mensagen, mensagen_erro="entrada precisa ser um numero"):
    while True:
        num = input(mensagen)
        try:
            return int(num)
        except ValueError:
            print(mensagen_erro)

def input_int(mensagen, mensagen_erro="entrada precisa ser um numero"):
    while True:
        num = input(mensagen)
        try:
            return int(num)
        except ValueError:
            print(mensagen_erro)

#estou orgulhoso dessa função
def menu(lista,mensagen,zero_m,zero_f,mostrar_zero=True):
    while True:
        for opcao in lista:
            x = lista.index(opcao)+1
            print(f"{x} - {opcao["m"]}")

        if mostrar_zero:
            print(f"0 - {zero_m}")
        print("")
        
        opt = input_int(mensagen)
        
        if opt <= len(lista) and opt >0:
            fun = lista[opt-1]["f"]
            try:
                return fun()
            except TypeError:
                return fun
            
        elif opt == 0 and mostrar_zero:
            fun = lista[opt-1]["f"]
            try:
                return fun()
            except TypeError:
                return fun            
        else:
            print("opção invalida")
    
def fun_construcao():
    print("essa função não esta pronta")

def abrir_chamado():
    con = sqlite3.connect('chamados.db')
    cur = con.cursor()
    titulo = input("insira o nome do chamado: ")
    lista = [
     {"m":"Baixa","f":"Baixa"},
     {"m":"Media","f":"Media"},
     {"m":"Alta","f":"Alta"},
     {"m":"Critica","f":"Critica"}]
    prioridade = menu(lista, "escolha a prioridade: ","não" ,"-1", False)
    print(prioridade)
    
    
menu_pricinal = [
    {"m":"procurar chamado por usuario","f":fun_construcao},
    {"m":"procurar chamado por prioridade","f":fun_construcao},
    {"m":"pesquisa por status","f":fun_construcao},
    {"m":"chamados urgentes","f":fun_construcao},
    {"m":"abrir chamado","f":abrir_chamado},
    {"m":"resolver chamado","f":fun_construcao},
    {"m":"fechar chamdo","f":fun_construcao}
    ]

menu(
    menu_pricinal,
    "escola uma opção: ",
    "sair do sitema",
    "Saindo do sistema"
    )