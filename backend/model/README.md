
# Pet Shop API

Este é um projeto de uma API simples de Pet Shop construída com Flask. A API permite o gerenciamento de pets, com operações de listagem, cadastro e exclusão.

## Tecnologias utilizadas
- Python 3.x
- Flask
- Flask-Cors
- Flasgger
- SQLite

## Endpoints da API

### `GET /pets`
Lista todos os pets cadastrados no banco de dados.

**Resposta**: Lista de objetos JSON representando os pets.

### `POST /pets`
Cadastra um novo pet no banco de dados.

**Corpo da requisição** (JSON):
```json
{
  "nome": "Nome do Pet",
  "tipo": "Tipo do Pet",
  "idade": 3
}
```

**Resposta**:
```json
{
  "message": "Pet cadastrado com sucesso!"
}
```

### `DELETE /pets/<id>`
Deleta um pet pelo ID.

**Resposta**:
```json
{
  "message": "Pet com ID <id> deletado."
}
```

## Como executar o projeto

1. Clone o repositório:
    ```bash
    git clone <URL do repositório>
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

4. A API estará disponível em `http://127.0.0.1:5000`.

## Logs

Toda requisição será registrada no terminal e no arquivo `petshop.log`.

## Banco de Dados

O banco de dados SQLite será criado automaticamente ao rodar o projeto, armazenando informações dos pets na tabela `pets`.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias.
