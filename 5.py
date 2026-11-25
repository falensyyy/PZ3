scores = {"Alice":85, "Bob":90}
scores["Charlie"] = 78
print(scores)
scores["Bob"] = 95
print(scores)
print(scores.get("Dave", "не найден"))
print(scores.get("Bob"))
scores.pop("Alice")
print(scores)