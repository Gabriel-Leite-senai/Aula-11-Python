import sqlite3

def criar_tabela():
    con = sqlite3.connect("chamados.db")
    cur = con.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS chamados
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    status TEXT NOT NULL,
    prioridade TEXT NOT NULL,
    usuario TEXT NOT NULL)"""

    cur.execute(sql)
    con.commit()

def input_int(mensagen, mensagen_erro="entrada precisa ser um numero inteiro"):
    while True:
        num = input(mensagen)
        try:
            return int(num)
        except ValueError:
            print(mensagen_erro)

def input_float(mensagen, mensagen_erro="entrada precisa ser um numero"):
    while True:
        num = input(mensagen)
        try:
            return float(num)
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
            fun = zero_f 
            try:
                return fun()
            except TypeError:
                return fun            
        else:
            print("opção invalida")

def sim_ou_não(mensagen="deseja comfirmar a operação[S/N]? ", mensagen_erro="opção invalida"):
    opt = input(mensagen)
    if opt.lower() in ["sim","s","si"]:
        return 1
    elif opt.lower() in ["não", "nao", "n", "no"]:
        return 0
    else:
        print(mensagen_erro)
         
def fun_construcao():
    print("essa função não esta pronta")

def mostrar_chamado(titulo,prioridade,status,usuario):
    print(f"titulo: {titulo} | prioridade: {prioridade} | status: {status} | usuario: {usuario}")

def busca_usuario():
    usuario = input("insira o nome do usuario: ")

    sql = """
    SELECT usuario FROM chamados
    """

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
    status = "Aberto"
    usuario= input("insira o usuario que está fazendo o chamado: ")

    mostrar_chamado(titulo,prioridade,status,usuario)
    opt = sim_ou_não()
    if opt == 1:
        sql = """
        INSERT INTO chamados (titulo, status, prioridade, usuario)
        VALUES (?, ?, ?, ?)
        """
        cur.execute(sql, (titulo, prioridade, status, usuario))
        con.commit()
        return opt
    elif opt == 0:
        return opt
    else:
        print("erro ao processar entrada")

criar_tabela()

menu_pricinal = [
    {"m":"procurar chamado por usuario","f":fun_construcao},
    {"m":"procurar chamado por prioridade","f":fun_construcao},
    {"m":"pesquisa por status","f":fun_construcao},
    {"m":"chamados urgentes","f":fun_construcao},
    {"m":"abrir chamado","f":abrir_chamado},
    {"m":"resolver chamado","f":fun_construcao},
    {"m":"fechar chamdo","f":fun_construcao}
    ]
while True:
    print(menu(menu_pricinal,"escolha uma opção: ","sair do sitema",exit))