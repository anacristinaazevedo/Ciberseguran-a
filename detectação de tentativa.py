Descrição
Você é responsável por implementar um sistema de monitoramento de segurança para um sistema de acesso.
 Seu objetivo é analisar registros de log de tentativas de acesso para detectar possíveis invasões. 
 Cada registro contém um identificador de usuário e um status que indica se a tentativa de acesso foi bem-sucedida ou falhou.

A detecção de tentativas de invasão é essencial para a segurança do sistema, e a análise de logs é uma prática comum para identificar comportamentos suspeitos. O sistema deve emitir um alerta se detectar 
mais de 3 tentativas consecutivas de falha para o mesmo usuário.

Entrada
Uma lista de registros de log no formato id_usuario:status, onde:

id_usuario é uma string que representa o identificador do usuário (exemplo: "user1").

status pode ser uma das seguintes strings:
- "sucesso" – indica que a tentativa de acesso foi bem-sucedida.
- "falha" – indica que a tentativa de acesso falhou.

A lista pode conter qualquer número de registros.

Saída
O sistema deve retornar:

O id_usuario que teve mais de 3 tentativas consecutivas de falha.

Se nenhum usuário tiver mais de 3 tentativas de falha consecutivas, o sistema deve retornar a 
mensagem "Nenhum invasor detectado".

# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):
    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    # Percorrer cada registro de log
    for registro in registros:
        # Separe o ID do usuário e o status do registro (sucesso ou falha)
        usuario, status = registro.split(":")

        # Verificar se o usuário atual é o mesmo da iteração anterior
        if usuario == usuario_atual:
            # Se o status é "falha", incremente o contador de tentativas falhas
            if status == "falha":
                tentativas_consecutivas += 1
                # Se o contador de falhas for maior que 3, detectamos uma invasão
                if tentativas_consecutivas > 3:
                    invasor_detectado = usuario
                    break
            else:
                # Se o status for "sucesso", resetamos o contador de falhas
                tentativas_consecutivas = 0
        else:
            # Se mudar de usuário, verificamos se o usuário anterior teve mais de 3 falhas consecutivas
            if tentativas_consecutivas > 3:
                invasor_detectado = usuario_atual
                break
            # Atualize para o novo usuário e reinicie a contagem de tentativas falhas
            usuario_atual = usuario
            tentativas_consecutivas = 1 if status == "falha" else 0  # Inicia a contagem para o novo usuário

    # Após o loop, verifica se o último usuário teve mais de 3 tentativas de falha
    if tentativas_consecutivas > 3:
        invasor_detectado = usuario_atual

    # Retorna o resultado final
    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"

# Função principal para executar o programa
def main():
    # Solicita ao usuário que insira os registros de log
    entrada = input()
    
    # Divide os registros de log pela vírgula e limpa espaços extras
    registros = [registro.strip() for registro in entrada.split(",")]

    # Chama a função para detectar tentativas de invasão
    resultado = detectar_invasao(registros)

    # Imprime o resultado
    print(resultado)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
