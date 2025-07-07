# FastMCP-Authentication
I will demonstrate on how to implement basic authentication using RSA Key Pair in the FastMCP server for developmental purposes.

# weather_server.py:
It is sample FastMCP server which uses StreamableHttpTransport. I have used in the BearerAuthProvider from FastMCP to introduce authentication for the server. I have used the basic provider which is RSAKeyPair.

# app.py
It is the client application running on a different machine or port. According to the documentation, the client application requires URL to connect to the FastMCP.

# Working
This is for developmental purposes only.
Start up the FastMCP server. The CLI for FastMCP server (weather_server.py) should print the generated token in the CLI. Copy the token on to the app.py {current_token} and run the client application. Simulate by modifying the current_token to invalid or incorrect token will cause FastMCP server throw Unauthorized Error.

You can streamline to save/read the generated token to/from a file. However, for developmental purposes copy the token works fine. You can set auto refresh of token which is time based token (say 24 hours) and in the client application you can run another background job to retrieve the refreshed token. 

To productionize, you can integrate it with OAuth2.1 style authentication or rely on external providers for third party authentication like Google, Meta, etc,. For enterprises, you can integrate it with the LDAP - directory based authentication which can not only based user information but also respective scopes for the users or groups. 

==For any questions or queries, feel free to reach out.==
