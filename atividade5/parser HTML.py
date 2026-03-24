import requests
from bs4 import BeautifulSoup

dados = []

with open("seeds.txt", "r") as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()
    
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        titulo = soup.title.string.strip() if soup.title else "Sem título"

        img_tag = soup.find("img")
        img_src = ""

        if img_tag and img_tag.has_attr("src"):
            img_src = img_tag["src"]

            if not img_src.startswith("http"):
                img_src = url.rstrip("/") + "/" + img_src.lstrip("/")

        dados.append((url, titulo, img_src))

    except:
        print(f"Erro ao acessar: {url}")

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Coleta de Dados - EXA618</title>
    <style>
        body { font-family: Arial; background: #f5f5f5; }
        .card {
            background: white;
            margin: 20px;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        img { width: 200px; border-radius: 10px; }
    </style>
</head>
<body>

<h1>Dados dos Estudantes</h1>
"""

for url, titulo, img in dados:
    html += f"""
    <div class="card">
        <h2>{titulo}</h2>
        <p><a href="{url}" target="_blank">{url}</a></p>
        <img src="{img}">
    </div>
    """

html += """
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Página HTML gerada com sucesso!")