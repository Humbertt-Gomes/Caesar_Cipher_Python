# Cifra de César - Implementação em Python

Este projeto implementa uma Cifra de César para criptografia e descriptografia, focando em eficiência e interação robusta com o usuário.

## Lógica e Arquitetura

Em vez de usar loops complexos para substituição de caracteres, esta implementação utiliza os métodos nativos `str.maketrans` e `translate` para garantir uma eficiência de  Big O(n).

## Funcionalidades Principais

* **Deslocamento Bidirecional**: Para lidar com a descriptografia de forma precisa, a fórmula $26 - deslocamento$ é aplicada quando `encrypt=False`. Isso garante que a rotação do alfabeto seja sempre matematicamente correta.
* **Validação de Entrada**: O sistema utiliza blocos `try/except` para lidar com entradas não inteiras e garante que o valor do deslocamento permaneça dentro do intervalo válido de 1 a 25.
* **Interação Persistente**: Possui um loop de execução contínuo, permitindo que o usuário realize múltiplas operações em uma única sessão sem a necessidade de reiniciar o script.

##  Como Executar o Projeto

Para testar o projeto localmente, siga estes passos:

1. **Pré-requisitos**: Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. **Download**: Você pode baixar o arquivo `Caesar_Cipher.py` diretamente ou clonar este repositório:
   ```bash
   git clone [ https://github.com/Humbertt-Gomes/Caesar_Cipher_Python.git ]
   
## Testar Online
Se você não tem o Python instalado, pode executar o código diretamente no seu navegador através do Google Colab:

[Clique aqui para rodar o projeto online]  (  https://colab.research.google.com/drive/1EzLd-IyTizAOP5mSsFA_IW8_svrgAgOj?usp=sharing  )
