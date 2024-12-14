Descrição
Crie uma solução para analisar uma lista de e-mails recebidos, verificando padrões comuns de phishing nas 
mensagens. Se um e-mail contiver palavras suspeitas como "ganhe", "prêmio", "urgente", "desconto", "click"
e "promoção" ele deve ser classificado como "Phishing" e "Seguro".

Entrada
Uma String contendo um conteúdo único representando o corpo do e-mail.

Saída
"Phishing" ou "Seguro" para cada e-mail.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    # Converter a mensagem para minúsculas para verificar de forma insensível a maiúsculas/minúsculas
    mensagem = mensagem.lower()

    # Verificar se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem:
            return "Phishing"
    
    # Se nenhuma palavra suspeita foi encontrada, classificar como "Seguro"
    return "Seguro"

# Receber o corpo do e-mail como entrada
email_usuario = input().strip()

# Chamar a função para verificar o e-mail
resultado = verificar_phishing(email_usuario)

# Imprimir o resultado
print(f"Classificação: {resultado}")
