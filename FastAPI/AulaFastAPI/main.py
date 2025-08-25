from fastapi import FastAPI, HTTPException, status
from models import PersonagensOnePiece

app = FastAPI()

personagens = {
    1: {
        "nome": "Monkey D. Luffy",
        "fruta": "Gomu Gomu no Mi",
        "recompensa": 3000000,
        "funcao": "Capitão",
        "foto": "https://i.pinimg.com/736x/4c/43/dc/4c43dc07adaf545a35e2ce41d8706fae.jpg",
    },
    2: {
        "nome": "Trafalgar D. Water Law",
        "fruta": "Ope Ope no Mi",
        "recompensa": 3000000,
        "funcao": "Capitão",
        "foto": "https://i.pinimg.com/736x/f4/8d/ca/f48dca93b826bdc17cbf50e13fe3083a.jpg",
    }
}

@app.get("/")
def teste():
    return {"Mensagem": "Arrasou"}

@app.get("/personagens")
async def get_personagens():
    return personagens

@app.get("/personagens/{personagem_id}")
async def get_personagem(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Personagem não encontrado")
    
@app.post("/personagens", status_code=201)
async def post_personagens(personagem: PersonagensOnePiece):
    next_id = len(personagens) + 1

    personagens[next_id] = personagem
    del personagem.id
    return personagem

@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensOnePiece):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Personagem não encontrado")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", 
                port=8001, log_level="info", reload=True)

