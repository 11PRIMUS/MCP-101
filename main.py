from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import httpx
import json
from bs4 import BeautifulSoup

load_dotenv()

mcp=FastMCP()

USER_AGENT="docs-app/2.o"
SERPER_URL="https://google.serper.dev/search"

docs_url={
    "llama-index": "https://docs.llama.com",
    "openai": "https://docs.openai.com",
    "langchain": "https://docs.langchain.com",

}

async def search_web(query:str) ->dict |None:
    payload=json.dumps({"q":query,"num":2})

    headers={
        "X-API-KEY":os.getenv("SERPER_API_KEY"),
        "Content-Type":"application/json",
    }

async def fetch_url():
    async with httpx.AsyncClient() as Client:
        try:
            response =await client.get(url,timeout=30.0)  #gets title and url
            soup=BeautifulSoup(response.text,"html.parser")
            text=soup.get_text()
            return text
        except httpx.TimeoutExceptions:
            return "Timeout error"

@mcp.tool()
def get_docs(): # when get_docs is called it return docs_url
    ...

def main():
    print("Hello from mcp1!")


if __name__ == "__main__":
    main()
