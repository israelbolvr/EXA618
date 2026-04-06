from sqlalchemy import create_engine

# Configurações extraídas do seu my.cnf
usuario = "root"
senha = "" # Por padrão o XAMPP vem sem senha
host = "127.0.0.1" # ou localhost
porta = "3306"
nome_banco = "projeto_futebol" # O nome que você criar no phpMyAdmin

# A string de conexão final
engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{nome_banco}?charset=utf8mb4")