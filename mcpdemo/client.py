from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"], #Ensure correct absolute path
                "transport": "stdio"
            },

            "weather":{
                            "url": "http://localhost:8000/mcp",
                            "transport": "streamable_http"
                        }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model = "llama-3.1-8b-instant")
    agent = create_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's the answer of (5+3)*12?"}]}
    )

    print("Math Response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "What's the weather in Hartford?"}]}
        )
    
    print("Weather Response:", weather_response['messages'][-1].content)

asyncio.run(main())