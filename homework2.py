# Lesson 2: Assignments: Nested If

# 1. Nested Decisions: The Adventure Game
# Task 1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        action = "cross a river"
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You see the path out!")
    else:
        action = "proceed in the dark"
        print("A swarm of bats encase you!")
else:
    pass

# 2. Quick Decisions: The Event Planner
attendees = int(input("Enter number of attendees"))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

vegeterian_option = "yes"
option = "Veggie Delight Caterers" if vegeterian_option == "yes" else "Gourmet Meals Caterers"
print(option)

