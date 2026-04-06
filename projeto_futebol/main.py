from extrator import coletar_classificacao
from banco import engine

# coleta os dados
df = coletar_classificacao()

if not df.empty:
    # salva no banco
    df.to_sql(
        name="classificacao_futebol",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("✅ Dados inseridos no banco com sucesso!")

else:
    print("❌ Falha na coleta")