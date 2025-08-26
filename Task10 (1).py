# Treasure Dictionary Challenge
# step 1 : Start the dictionary
treasure = {
    "clues": ["beach", "cave", "waterfall"],
    "locations": {
        "beach": {
            "items": ["compass", "shovel"],
            "hint": "dig here"
        },
        "cave": {
            "items": ["lantern", "gold coin"],
            "hint": "look behind rocks"
        }
    },
    "crew": ["First Mate", "Navigator"]
}

# step 2 : Make changes to the dictionary
treasure["crew"].append("cook")
treasure["locations"]["volcano"] = {
    "items":["diamond", "lava boots"],
    "hint":"wear protection"
}
treasure["clues"].append("valcano")
treasure["crew"].remove("Navigator")

# step 3 : Look for gold
for location, info in treasure["locations"].items():
    if "gold coin" in ["location"]:
        print(f"Treasure! In location_name")
# 4Count and list all items
for location, info in treasure["locations"].items():
    print(f"{location} : {' , '.join(info['items'])}")

