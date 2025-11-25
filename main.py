from dotenv import load_dotenv

load_dotenv()

#agent dediğimiz varlık 2 şeyden oluşur: 1-LLM ve 2-Toolkit. LLMlere toolkit veririz ve spesifik gorevleri yerine getirmesini sağlarız.
from langchain.agents import create_agent 
from langchain.tools import tool #A tool is a function that an agent can execute. It can be any function we give to an agent.
from langchain_core.messages import HumanMessage #HumanMessage'ı kullanip agent'ı invoke edeceğiz
from langchain_ollama import ChatOllama
from tavily import TavilyClient #İnternet üzerinden arama yapmak için kullanırız
from langchain_tavily import TavilySearch


#tavily = TavilyClient()

#@tool #bu satırdakini yazarak normal bir python fonksiyonunu llmin kullanacağı bir langchain tool'a donusturuyoruz. 
      #Langchain bu toolun metadatasını(isim ve parametreler tanımı filan) alıp formatlar ve llm cagrısına koymamızı saglar.
#def search(query: str) -> str:
#    """
#    Tool that searches over internet
#    Args:
#        query: The query to search for
#    Returns:
#        The search result
#    """
#    print(f"Searching for {query}")
#    return tavily.search(query=query)


llm = ChatOllama(model="llama3.1:8b")
#tools = [search] #toolların listesi
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course-aiagents!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
