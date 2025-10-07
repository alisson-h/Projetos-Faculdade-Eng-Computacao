import copy

Estoque = {}

Produto  = {
    "key" : None,
    "value" : {
        "amount" : None,
        "price" : None,
    }
}

def ListarEstoque(OrdemEstoque):
    """Exibe o estoque de acordo com a ordem que foi passada"""
    global Estoque
    if OrdemEstoque == {}:
        print("Não há nada no estoque :( \n")
        return
    
    for key in OrdemEstoque:
        print("========================================= ")
        print(f"  Nome : {key}")
        print(f"  Quantidade no Estoque: {Estoque[key]['value']['amount']}")
        print(f"  Valor Unitário: {Estoque[key]['value']['price']}")
    
    print()

def ListarEstoqueOrdenadoPorNome():
    """Exibe o estoque ordenado por nome"""
    global Estoque
    sortedEstoque = sorted(Estoque)
    ListarEstoque(sortedEstoque)

    
def CriarProduto():
    """Cria um novo produto

    Pergunta o nome, quantidade e o preço

    ao final retorna o produto criado"""
    global Produto
    novoProduto = copy.deepcopy(Produto)

    while (True):
        nome = ""
        quantidade = 0
        preco = 0
        try:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a  quantidade no estoque: "))
            preco = float(input("Digite o  preço unitário: "))
        except:
            print(" -> Dados incompativeís ... tente novamente")
        else:
            if (nome in Estoque):
                print(" -> Ops, Há um produto cadastrado no estoque com o mesmo nome! tente outro...")
            else:
                novoProduto["key"] = nome
                novoProduto["value"]["amount"] = quantidade
                novoProduto["value"]["price"] = preco
                print("\nProduto criado com sucesso!")
                break
    print()
    return novoProduto

def AdcionarProduto(novoProduto):
    """Adiciona um produto no estoque atual"""
    global Estoque
    Estoque[novoProduto["key"]] = novoProduto


def AtualizarProduto():
    """Pede o usuário um nome e logo após atualiza o preco e a quantidade e salva no estoque"""
    global Estoque
    if Estoque == {}:
        print("Nao há produto para atualizar :(\n")
        return
    
    for Produto in Estoque:
        print(f"({Produto}) ")
    print()

    procurarProduto = input("Digite o nome do produto para atualizar: ")

    if procurarProduto in Estoque:
        novaQuantidade = 0
        novoPreco = 0
        while True:
            
            try:
                novaQuantidade = int(input(f"Digite a nova quantidade do produto no estoque; atual :({Estoque[procurarProduto]['value']['amount']}): "))
                novoPreco = float(input(f"Digite a novo preco unitário do produto; atual :({Estoque[procurarProduto]['value']['price']}): "))
            except:
                print(" -> Dados incompativeís ... tente novamente")
            else:
                break
        
        Estoque[procurarProduto]['value']['amount'] = novaQuantidade
        Estoque[procurarProduto]['value']['price'] = novoPreco

        print("\nProduto atualizado com sucesso...")
    else:
        print("\nProduto não encontado!")
    print()

def RemoverProduto():
    """Pede um nome ao usario e remove-o do estoque"""
    global Estoque
    if Estoque == {}:
        print("Nao há produto para remover :(\n")
        return
    
    for Produto in Estoque:
        print(f"({Produto}) ")
    print()

    procurarProduto = input("Digite o nome do produto para remover: ")

    if procurarProduto in Estoque:
        del Estoque[procurarProduto]
        print("\nProduto removido com sucesso!")
    else:
        print("\nProduto não encontado!")
    print()

def CalcularOvalorTotal():
    """ Passa por cada elemento e calcula seu preço e no final imprime o valor total do estoque"""
    global Estoque
    if Estoque == {}:
        print("Não há nada no estoque :( \n")
        return
    
    soma = 0
    for Produto in Estoque:
        soma += Estoque[Produto]['value']['amount'] * Estoque[Produto]['value']['price']
    print(f"Valor Total do Estoque: {soma} \n")

def MenuPrincipal():
    """Menu Principal da Aplicação

        Este menu é responsável por chamar todas as funções do codigo, é nele onde o código começa e termina
    """
    while True:
        print("1. Ver Estoque")
        print("2. Adcionar Produto ao Estoque")
        print("3. Atualizar Produto no Estoque")
        print("4. Calcular o valor total do estoque")
        print("5. Exibir Estoque Ordenado por Nome")
        print("6. Remover Produto no Estoque")
        print("7. Sair")

        resposta = 0
        while True:
            try:
                resposta = int(input("Reposta: "))
            except:
                print(" -> Dados inválidos... Tente novamente")
            else:
                if resposta <= 0 or resposta >= 8:
                    print(f"  -> Resposta inválida... Tente novamente")
                else:
                    break     

        print()
        match resposta:
            case 1:
                ListarEstoque(Estoque)
            case 2:   
                novoProduto  = CriarProduto()
                AdcionarProduto(novoProduto)
            case 3:
                AtualizarProduto()
            case 4:
                CalcularOvalorTotal()
            case 5:
                ListarEstoqueOrdenadoPorNome()
            case 6:
                RemoverProduto()
            case 7:
                #Sair
                break

    print("Encerrando o programa...")

MenuPrincipal()
