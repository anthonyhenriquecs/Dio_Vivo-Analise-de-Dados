def principal():
    print('executando a função principal')

    def funcao_interna():
        print('executando a função interna ou mais de uma ')
    
    funcao_interna()

principal()