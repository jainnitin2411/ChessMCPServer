import json
import sys

# Example request for get_player_stats
request = {
    "tool": "get_player_stats",
    "args": {"username": "sampleuser"}
}
print(json.dumps(request))
sys.stdout.flush()