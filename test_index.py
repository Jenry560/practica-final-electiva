def test_hola_mundo():
    with open("index.html", encoding="utf-8") as f:
        contenido = f.read()
    assert "<h1>Hola Mundo</h1>" in contenido
