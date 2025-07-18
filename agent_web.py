import asyncio
import os
from browser_use import Agent
from browser_use.llm import ChatOllama

async def main():
    
    agent = Agent(
        task="""
        Faça login nesse site 'https://practicetestautomation.com/practice-test-login/'.
        As informações para acesso: Username = student e Password = Password123
        """,
        llm=ChatOllama(
            model="mistral:7b-instruct",
            host=os.getenv("HOST_LLM"),
        )
    )

    await agent.run()
    
if __name__ == '__main__':
    asyncio.run(main())
