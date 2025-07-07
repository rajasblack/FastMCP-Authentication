from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

current_token = "Insert your token here..."

transport = StreamableHttpTransport(
    url="http://127.0.0.1:8000/mcp/",
    headers={
        "Authorization": f"Bearer {current_token}",
        "Accept": "application/json, text/event-stream"
    }
)

async def main():
    async with Client(transport) as client:
        await client.ping()
        tools = await client.list_tools()
        result = await client.call_tool("get_weather", {"location": "Delhi"})
        print(f"Result: {result}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
