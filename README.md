Install this MCP server by adding the following json code to your JSON config file.

```json
{
    "server": {
        "name": "Chess-Server",
        "host": "localhost",
        "port": 8080,
        "type": "mcp",
        "enabled": true,
        "settings": {
            "maxPlayers": 2,
            "gameType": "chess",
            "logging": true
        }
    }
}
```