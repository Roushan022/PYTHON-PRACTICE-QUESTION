topics = [
    "Artificial Intelligence",
    "Intelligent Agents",
    "PEAS Framework",
    "Knowledge-Based Agents",
    "Wumpus World"
]
topics.append("Problem-Solving Agents")
topics.remove("PEAS Framework")
topics.sort()
print("Updated AI Topics:")
for i, topic in enumerate(topics, 1):
    print(i, ".", topic)
