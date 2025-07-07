from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from fastmcp.server.dependencies import get_access_token, AccessToken
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair

key_pair = RSAKeyPair.generate()

auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    audience="my-weather-server"
)

mcp = FastMCP("Weather", auth=auth)

token = key_pair.create_token(
    subject="Rajesh",
    audience="my-weather-server",
    scopes=["read", "write"]
)

print(f"Token: {token}")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get weather for the location."""
    access_token: AccessToken | None = get_access_token()

    if access_token is None:
        raise ToolError("No access token found")

    user_id = access_token.client_id
    user_scopes = access_token.scopes

    if "read" not in user_scopes:
        raise ToolError("Insufficient permissions to access weather data")

    return f"Weather data for {location}. User: {user_id}, Scopes: {', '.join(user_scopes)}"

if __name__ == "__main__":
  mcp.run(transport="streamable-http")
