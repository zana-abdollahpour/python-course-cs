artist = {
    "first": "Neil",
    "last": "Young"
}

# fullName = artist.get("first") + " " + artist.get("last")
fullName = f"{artist.get("first")} {artist.get("last")}"
print(fullName)
