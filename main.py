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
async def get_docs(quer:str,library:str): # when get_docs is called it return docs_url
    """
    Search docs for given question and library,
    it supports langchain ,openai, and llama.
    
    Args:
    query: query to search ex- Chroma DB
    library: library to search ex-langchain
    
    Returns;
        text from docs
                """
    
    if library not in docs_urls:
        raise ValueError(f"Library {library} not supportedd")

    query=f"{query} site:{docs_urls[library]} {query}"
    results=await search_web(query)
    if len(results["organic"])==0:
        return "No results found"

    text=""
    for result in results["organic"]:
        text+=await fetch_url(result["link"])
    return text



if __name__ == "__main__":
    mcp.run(transport="stdio")
