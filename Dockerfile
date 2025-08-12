FROM maven:3.9.6-eclipse-temurin-21

WORKDIR /app

COPY . /app

# Compile o projeto
RUN mvn clean package

# Parâmetros via variáveis de ambiente
ENV NUM_NODES=100
ENV SCAN_RATE=0.1
ENV P_EXPLOIT=0.05
ENV PATCH_TIME=0.02
ENV BACKUP_PROB=0.5

CMD ["java", "-cp", "target/classes", "metodosnumerico.com.App"]