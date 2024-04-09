def msg(nome):
  print('executando nome')
  return f'oi {nome}'

def mensagem(nome):
  print('executando msg longa')
  return f'ola, tudo bom {nome}?'

def executar(funcao, nome):
  print('executando executar')
  return funcao(nome)

print(executar(mensagem, "Big"))