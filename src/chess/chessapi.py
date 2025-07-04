import requests

CHESS_API_BASE= "https://api.chess.com/pub"

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "accept": "application/json"
    }

# add a function to get the player profile by username
def get_player_profile(username: str) -> dict:
    """
    Get the player profile by username.
    :param username: The username of the player.
    :return: A dictionary containing the player profile.
    """
    url = f"{CHESS_API_BASE}/player/{username}"
    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
        return {}  # This line ensures a dict is always returned
    
# get player statistics by username
def get_player_stats(username: str) -> dict:
    """
    Get the player statistics by username.
    :param username: The username of the player.
    :return: A dictionary containing the player statistics.
    """
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    response = requests.get(url,headers=headers )

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
        return {}  # This line ensures a dict is always returned
    
