from fastapi import FastAPI

app = FastAPI(title="Mon API pour la promotion JAN22_CDE")

@app.get("/")
def status():
    """
    Cette méthode retourne le dictionnaire {"status":1} si c'est fonctionnel
    """
    return {"status":1}


@app.get("/test")
def test():
    """
    Ceci est une route test
    """
    return "test"

@app.post("/post_test")
def post_test():
    return 25

