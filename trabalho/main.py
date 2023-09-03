from trabalho.model.contato import Contato

def gravar_dados():
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    twitter = input("Digite o twitter: ")
    instagram = input("Digite o instagram: ")
    facebook = input("Digite o facebook: ")


def imprimir_menu():
    print("\n\nDigite:")
    print("1 para inserir um novo contato;")
    print("2 para fazer uma consulta;")
    print("3 para remover um contato;")
    print("4 para editar um contato;")
    print("5 para sair.")


def conferir_entrada(entrada: int):
    if entrada == 1:
        gravar_dados()
    elif entrada == 2:
        pass
    elif entrada == 3:
        pass
    elif entrada == 4:
        pass


def menu_agenda():
    imprimir_menu()
    try:
        entrada = 0
        while (entrada != 5):
            entrada = int(input())
            conferir_entrada(entrada)
            imprimir_menu()
    except:
        print("Esta entrada não é válida\n")
        menu_agenda()


if __name__ == '__main__':
    menu_agenda()
    contato = Contato("123123123", "teste@mail.com", "oioi", "oioi", "oioi")
    print(contato.facebook)
