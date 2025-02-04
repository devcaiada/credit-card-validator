# Credit Card Validator

Este repositório contém um validador de cartão de crédito que identifica automaticamente a bandeira do cartão através do seu número e valida o número do cartão usando o algoritmo de Luhn.

## Funcionalidades

- Identificação da bandeira do cartão (Visa, MasterCard, American Express, Discover, JCB, Diners Club)
- Validação do número do cartão utilizando o algoritmo de Luhn

## Requisitos

- Python 3.x

## Como usar

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/credit-card-validator.git
    cd credit-card-validator
    ```

2. Execute o script `main.py`:
    ```sh
    python main.py
    ```

3. Insira o número do cartão de crédito que deseja validar e identificar a bandeira.

## Estrutura do Projeto

- `main.py`: Contém a lógica principal para validação e identificação da bandeira do cartão.
- [README.md](http://_vscodecontentref_/0): Este arquivo, contendo informações sobre o projeto.

## Exemplo de Uso

```python
# Exemplo de uso no script main.py
card_number = "4111 1111 1111 1111"
print(validate_credit_card(card_number))
```

## Contribuição <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />

Este projeto foi desenvolvido como parte de um desafio utilizando Github Copilot. Contribuições e sugestões são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório do GitHub.
