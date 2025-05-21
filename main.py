import os
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic caalculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a+b}"

@tool
def say_hello(name: str) -> str:
    """useful for greeting a user"""
    print("tool has been called. ")
    return f"Hello {name} , I hope you are well today"



def main():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama3-70b-8192"
    llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL)

    tools = [calculator, say_hello]
    agent_executor = create_react_agent(llm, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        print("\nAssistant: ", end="")

        try:
            for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
                if "messages" in chunk.get("agent", {}):
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="", flush=True)
                elif "output" in chunk:
                    print(chunk["output"], end="", flush=True)
        except Exception as e:
            print(f"\n[Error] {str(e)}")

        print()  # for newline after assistant response

if __name__ == "__main__":
    main()








