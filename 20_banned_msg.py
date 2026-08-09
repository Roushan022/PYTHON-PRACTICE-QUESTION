def ProfanityFilter(msg, banned):
    words = msg.split()
    filtered = []

    for word in words:
        if word not in banned:
            filtered.append(word)
        if word in banned:
            filtered.append("*"*len(word))
    return " ".join(filtered)

msg = "this is a bad and ugly example"
banned = ["bad", "ugly"]

print(ProfanityFilter(msg, banned))
