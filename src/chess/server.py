from mcp.server.fastmcp import FastMCP
from chess.chessapi import get_player_profile as GetPlayerProfile, get_player_stats as GetPlayerStats


mcp = FastMCP("chess")

@mcp.tool()
def get_player_profile(username: str) -> dict:
    """
    Get the player profile by username.
    :param username: The username of the player.
    :return: A dictionary containing the player profile.
    """
    return GetPlayerProfile(username)

@mcp.tool()
def get_player_stats(username: str) -> dict:
    """
    Get the player statistics by username.
    :param username: The username of the player.
    :return: A dictionary containing the player statistics.
    """
    return GetPlayerStats(username)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    #main()
    get_player_profile("Hikaru")

