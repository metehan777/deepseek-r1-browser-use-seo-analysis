import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent

# Load environment
load_dotenv()

async def run_search():
    # Initialize agent with tasks
    agent = Agent(
        task=(
            '1. Go to https://appsamurai.com\n'
            '2. Analyze the page for the best semantic placements of contents\n'
            '3. Extract the current semantic content placements\n'
            '4. Suggest missing semantic long-tail queries'
        ),
        llm=ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-reasoner',
            api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY', '')),
        ),
        use_vision=False,
    )

    # Execute tasks and save raw output
    result = await agent.run()
    
    # Basic text file output
    # with open('output.txt', 'w', encoding='utf-8') as f:
    #   f.write(str(result))

if __name__ == '__main__':
    asyncio.run(run_search())
