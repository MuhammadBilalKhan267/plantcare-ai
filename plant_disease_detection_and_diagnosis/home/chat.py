from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1",
    temperature=0
)
def diagnose(disease):
    messages = [
        ("system", """You are a plant doctor. You will be given a disease. 
         You will provide a description, causes, effects and cure of the disease."""),
        ("human", disease),
    ]
    result = llm.invoke(messages)
    return result.content
