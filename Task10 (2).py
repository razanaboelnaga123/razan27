# 4 Word Flipper Mission!
sentence = "The sky is blue"
flipped = ' '.join([word[::-1]for word in sentence.split()])
print(flipped)


# Help Desk Hero
customers = [
    ("Alex", "VIP"),
    ("Bob", "Regular"),
    ("Sarah", "Regular"),
    ("Maria", "VIP"),
    ("Mike", "Regular")
]
vip_queue = []
regular_queue = []
for name, status in customers:
    if status == "VIP":
        vip_queue.append(name)
    else:
        regular_queue.append(name)
order = vip_queue + regular_queue
print("Serve Order:", order)

#School Club Signup Mission
signups = [
    ("Liam", "Science"),
    ("Emma", "Art"),
    ("Olivia", "Science"),
    ("Liam", "Art"),  # Duplicate - ignore this one!
    ("Noah", "Art"),
    ("Emma", "Science")  # Duplicate - ignore this one too!
]
science_club = set()
art_club = set()
already_signed_up = set()
for name, club in signups:
    if name is not already_signed_up:
        already_signed_up.add(name)
        if club == "Science":
            science_club.add(name)
        else:
            art_club.add(name)
print("Science Club:", science_club)
print("Art Club:", art_club)
