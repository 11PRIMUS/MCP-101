from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()

mcp=FastMCP()

USER_AGENT="docs-app/2.o"
SERPER_URL="https://google.serper.dev/search"

docs_url={
    "llama-index": "https://docs.llama.com",
    "openai": "https://docs.openai.com",
    "langchain": "https://docs.langchain.com",

}

def search_web():
    ...
def fetch_url():
    ...

@mcp.tool()
def get_docs():
    ...

def main():
    print("Hello from mcp1!")


if __name__ == "__main__":
    main()
