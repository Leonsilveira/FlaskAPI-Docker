# FlaskAPI-Docker

Este repositório contém uma API de recomendação desenvolvida em Flask e encapsulada em um contêiner Docker. O projeto visa demonstrar como construir e executar uma aplicação Flask com Docker, oferecendo uma solução escalável e fácil de implementar para desenvolvedores.

## Funcionalidades

- **API RESTful em Flask:** Permite requisições POST para a rota `/recommend` retornando uma lista de recomendações.
- **Encapsulamento com Docker:** Facilita a construção e execução da aplicação em qualquer ambiente, garantindo consistência e isolação.
- **Código Bem Documentado:** Inclui exemplos de uso, validações de entrada e explicações detalhadas de cada etapa do processo.

## Tecnologias Utilizadas

- **Flask:** Framework web utilizado para desenvolver a API.
- **Docker:** Plataforma utilizada para construir e executar contêineres, garantindo portabilidade e escalabilidade.
- **Python:** Linguagem de programação utilizada para desenvolver a lógica da API.

## Como Usar

### Pré-requisitos

Certifique-se de que possui o Docker instalado em sua máquina. 

### Construir a Imagem Docker

Execute o seguinte comando no terminal para construir a imagem Docker:

```bash
docker build -t flaskapi-docker .

Executar o Contêiner Docker
Após construir a imagem, execute o seguinte comando para rodar o contêiner:

bash
docker run -p 5000:5000 flaskapi-docker
Fazer uma Requisição POST
Utilize ferramentas como Postman ou Insomnia para enviar uma requisição POST para http://127.0.0.1:5000/recommend com o corpo JSON contendo os recursos:

json
{
    "features": [1, 2, 3, 4, 5]
}
Capturas de Tela
As capturas de tela do processo de construção e execução do contêiner Docker, bem como das requisições e respostas no Postman, estão disponíveis na pasta midia.

Código da API
Aqui está o código completo do app.py com as validações:

python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de itens populares (exemplo)
popular_items = [
    {"item_id": 1, "name": "Item A", "popularity_score": 95},
    {"item_id": 2, "name": "Item B", "popularity_score": 90},
    {"item_id": 3, "name": "Item C", "popularity_score": 85},
    {"item_id": 4, "name": "Item D", "popularity_score": 80},
    {"item_id": 5, "name": "Item E", "popularity_score": 75}
]

@app.route('/recommend', methods=['POST'])
def recommend():
    if not request.is_json:
        return jsonify({'error': 'Request body must be JSON'}), 400

    data = request.get_json(force=True)

    if 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    if not isinstance(data['features'], list) or any(x is None for x in data['features']):
        return jsonify({'error': 'Invalid features'}), 400

    recommendations = popular_items[:5]  # Exemplo: pegar os 5 itens mais populares

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
Conclusão
Este projeto demonstra como encapsular uma aplicação Flask em um contêiner Docker e fornece uma API simples de recomendação. Sinta-se à vontade para explorar, modificar e melhorar!

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.