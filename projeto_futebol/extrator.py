from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def coletar_classificacao():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.sofascore.com")
        time.sleep(5)
        script = """
        return fetch("https://www.sofascore.com/api/v1/unique-tournament/325/season/87678/standings/total")
            .then(res => res.json());
        """
        data = driver.execute_script(script)
        if "standings" not in data:
            print("❌ Erro: dados não encontrados")
            return pd.DataFrame()
        rows = data['standings'][0]['rows']
        dados = []
        for t in rows:
            dados.append({
                "equipe": t.get("team", {}).get("name"),
                "posicao": t.get("position"),
                "jogos": t.get("matches"),
                "vitorias": t.get("wins"),
                "empates": t.get("draws"),
                "derrotas": t.get("losses"),
                "gols_pro": t.get("scoresFor"),
                "gols_contra": t.get("scoresAgainst"),
                "saldo": t.get("scoreDiffFormatted"),
                "pontos": t.get("points")
            })

        df = pd.DataFrame(dados)
        df = df.sort_values(by="posicao")

        return df

    except Exception as e:
        print("❌ Erro:", e)
        return pd.DataFrame()

    finally:
        driver.quit()