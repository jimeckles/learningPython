favPets = list(map(lambda s: "favorite pet is " + s, ["dog", "cat", "squirrel", "hamster"]))
print(favPets)

favPets = list(map(lambda s,y: f"pet {s!r} count {y!s}", 
                   ["dog", "cat", "squirrel", "hamster"], range(1,10)))
print(favPets)
