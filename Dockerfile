# Usar a imagem base do Python
FROM python:3.8

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar as dependências
RUN pip install -r requirements.txt

# Expor a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
