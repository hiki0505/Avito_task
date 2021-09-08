import aiohttp
from fastapi import FastAPI
from matrix_manipulation import GetMatrix
from exceptions import handle_server_exceptions

app = FastAPI()


@handle_server_exceptions
@app.get("/get_matrix/")
async def get_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            get_matrix = GetMatrix(await resp.text())
            spiral_list = await get_matrix.get_final_matrix()
            return spiral_list
