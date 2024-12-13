# Use a imagem base oficial do Python
FROM python:3.11.0-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação para o diretório de trabalho do contêiner
COPY . .

# Torna o script start.sh executável
RUN chmod +x start.sh

# Expõe a porta em que a aplicação irá rodar
EXPOSE 8080

# Define o comando para iniciar a aplicação
CMD ["sh", "start.sh"]