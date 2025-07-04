Install this MCP server by adding the following json code to your JSON config file.

```json
{
    "mcpServers": {
        "server":{
            "command": "uv",
            "args": [
                "--from",
                "git+https://github.com/jainnitin2411/ChessMCPServer.git",
                "chess"
            ]
        }
    }
}
```