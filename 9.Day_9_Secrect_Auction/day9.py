    # DAY 9

#    Dictionaries

empty_dictionary = {}

example_dictionary = {"Bug": "An error in program.", "Function": "A piece of code you can call and reuse."}

#   Get something from a dictionary by key
# print(example_dictionary["Bug"])
# print(example_dictionary["Function"])

#   Add to dictionary
example_dictionary["Loop"] = "The action of doing something over and over again."
# print(example_dictionary)

#   Wipe an existing dictionary
full = {"hello": "there"}
full = {}
# print(full)

#   Edit a dictionary
example_dictionary["Bug"] = "A new definition of a bug." # if this key does not exist, it will create a new item

#   Access all keys
for thing in example_dictionary:
    print(thing)

for thing in example_dictionary.keys():
    print(thing)

#   Access all values
for thing in example_dictionary:
    print(example_dictionary[thing])

for thing in example_dictionary.values():
    print(thing)

for key, value in example_dictionary.items():
    print(key, "-->", value)


#   Nesting dictionary in a dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

travel_experience = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "activities": ["Sightseeing", "Skydiving"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "activities": ["Museum", "Beer"]}
}

#   Nesting a dictionary in a list
travel_list = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "activities": ["Sightseeing", "Skydiving"]
    },
    {
     "country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "activities": ["Museum", "Beer"]
    },
]
print(travel_list)