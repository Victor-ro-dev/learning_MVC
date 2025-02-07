def introduciton_page():
    message = '''
    Sistema Cadastral

    Bem-vindo ao sistema de cadastro de pessoas.

    Escolha uma das opções abaixo:

    1 - Cadastrar pessoa
    2 - Listar pessoas
    3 - Sair
    
    '''

    print(message)
    command = input('Digite o número da opção desejada: ')
    
    return command