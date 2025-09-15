from fastapi import FastAPI, HTTPException, status
from models import PersonagensUrsinhoPooh

app = FastAPI()

personagens = {
    1: {
        "nome": "Ursinho Pooh",
        "raca": "Urso de Pelúcia",
        "traco": "Amigável",
        "filmes": [
            "As Muitas Aventuras do Ursinho Pooh",
            "A Maior Aventura do Ursinho Pooh",
            "Ursinho Pooh: Tempo de Dividir",
            "Tigrão O Filme",
            "O Natal Mágico na Casa do Mickey: Nevou na Casa do Mickey",
            "Ursinho Pooh: Um Ano Muito Feliz",
            "Os Vilões da Disney",
            "Leitão O Filme",
            "Ursinho Pooh: A Páscoa de Guru",
            "Pooh e o Elefante",
            "Christopher Robin: Um Reencontro Inesquecível",
        ],
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNkC3WYGLeLR44u52zD_-doX8B-FUdRDSJw5mu6wmyi2ctUoNmHJCB646USI32GVvuP9U&usqp=CAU",
    },
    2: {
        "nome": "Leitão",
        "raca": "Porco",
        "traco": "Medroso",
        "filmes": [
            "As Muitas Aventuras do Ursinho Pooh",
            "A Maior Aventura do Ursinho Pooh",
            "Ursinho Pooh: Tempo de Dividir",
            "Tigrão O Filme",
            "Leitão O Filme",
            "Ursinho Pooh: A Páscoa de Guru",
            "Pooh e o Elefante",
            "Christopher Robin: Um Reencontro Inesquecível",
        ],
        "foto": "https://static.wikia.nocookie.net/disney/images/b/bb/Free_walt_disney_piglet_wallpaper.jpg/revision/latest?cb=20150516024733&path-prefix=pt-br",
    }
}

@app.get("/")
async def root():
    return {"msg": 'Funcionou bb'}

# GET - Lista de Personagens
@app.get("/personagens")
async def get_personagens():
    return personagens

# GET - Pesquisa de personagem pelo ID
@app.get("/personagens/{personagem_id}")
async def get_personagem(personagem_id: int):
    try: 
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Personagem não encontrado")
    
# POST - Adicionar outros personagens
@app.post("/personagens", status_code=201)
async def post_personagens(personagem: PersonagensUrsinhoPooh):
    next_id = len(personagens) + 1

    personagens[next_id] = personagem
    del personagem.id
    return personagem

# PUT - Atualização dos personagens por ID
@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensUrsinhoPooh):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Personagem não encontrado")

# DELETE - Deletar personagem por ID
@app.delete("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def del_personagem(personagem_id: int, personagem: PersonagensUrsinhoPooh):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return {"message" : "O personagem foi apagado"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Personagem não encontrado")
    
# PATCH - Atualizar itens especificos do personagem


# SETUP Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1",
                port=8001, log_level="info", reload=True)