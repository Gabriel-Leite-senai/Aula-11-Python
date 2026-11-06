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
    con.close()

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
    con = sqlite3.connect("chamados.db")
    cur = con.cursor()
    usuario = input("insira o nome do usuario: ")

    sql = "SELECT * FROM chamados WHERE usuario LIKE ?"
    tabela = cur.execute(sql, (usuario,))

    n = 0
    for x in tabela:
        print(f"id: {x[0]} | titulo: {x[1]} | status: {x[2]} | prioridade: {x[3]} | usuario: {x[4]}")
        n+=1
    print(f"{n} chamado(s) com o usuario: {usuario} encontrado(s)")

def busca_prioridade():
    con = sqlite3.connect("chamados.db")
    cur = con.cursor()
    menu_prioridade = [
    {"m":"Baixa","f":"Baixa"},
    {"m":"Media","f":"Media"},
    {"m":"Alta","f":"Alta"},
    {"m":"Critica","f":"Critica"}]
    
    prioridade = menu(menu_prioridade,"Selecione a prioridade: ","none",-1,False)

    sql = "SELECT * FROM chamados WHERE prioridade LIKE ?"
    tabela = cur.execute(sql, (prioridade,))

    n = 0
    for x in tabela:
        print(f"id: {x[0]} | titulo: {x[1]} | status: {x[2]} | prioridade: {x[3]} | usuario: {x[4]}")
        n+=1
    print(f"{n} chamados encontrados com a prioridade: {prioridade}")

def busca_status():
    con = sqlite3.connect("chamados.db")
    cur = con.cursor()
    menu_status = [
    {"m":"Aberto","f":"Aberto"},
    {"m":"Em progresso","f":"Em progresso"},
    {"m":"Fechado","f":"Fechado"},]
    
    status = menu(menu_status,"Selecione o Status: ","none",-1,False)

    sql = "SELECT * FROM chamados WHERE status LIKE ?"
    tabela = cur.execute(sql, (status,))
    con.close()
    n = 0
    for x in tabela:
        print(f"id: {x[0]} | titulo: {x[1]} | status: {x[2]} | prioridade: {x[3]} | usuario: {x[4]}")
        n+=1
    print(f"{n} chamados encontrados com o status: {status}")

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
    print(prioridade)
    mostrar_chamado(titulo,prioridade,status,usuario)
    opt = sim_ou_não()
    if opt == 1:
        sql = """
        INSERT INTO chamados (titulo, status, prioridade, usuario)
        VALUES (?, ?, ?, ?)
        """
        cur.execute(sql, (titulo, status, prioridade, usuario))
        con.commit()
        con.close
        return 0
    elif opt == 0:
        return 1
    else:
        print("erro ao processar entrada")

def resolver_chamado():
    con = sqlite3.connect("chamados.db")
    cur = con.cursor()
    chamado = input("insira o id ou o nome do chamado: ")
    try:
        chamdo = int(chamdo)
        sql_update = "UPDATE chamados SET status=? WHERE id = ?"
        sql_quarry = "SELECT * FROM chamados WHARE id = ?"
    except ValueError:
        sql_update = "UPDATE chamados SET status=? WHARE nome LIKE ?"
        sql_quarry = "SELECT * FROM chamados WHERE nome LIKE ?"
    
    lista = cur.execute(sql_quarry, (chamado,))

    opt = sim_ou_não()
    
    
    

criar_tabela()

menu_pricinal = [
    {"m":"procurar chamado por usuario","f":busca_usuario},
    {"m":"procurar chamado por prioridade","f":busca_prioridade},
    {"m":"pesquisa por status","f":busca_status},
    {"m":"chamados urgentes","f":fun_construcao},
    {"m":"abrir chamado","f":abrir_chamado},
    {"m":"resolver chamado","f":fun_construcao},
    {"m":"fechar chamdo","f":fun_construcao}
    ]
while True:
    menu(menu_pricinal,"escolha uma opção: ","sair do sitema",exit)
    input("aperte ENTER para continuar")