def estado_atribuicoes(utilis):
    estado = ["Ativa", "Devolvida", "Cancelada"]
    op = utilis.validar_entrada("escolha uma opcao: ", len(estado)) -1
    return estado[op]

def adicionar_atribuicoes(banco, boreg):
    "em desenvolvimento"
