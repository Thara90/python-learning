stuff = {"food":15, "energy":100, "enemies":3}

print(stuff.get("food"))
print(stuff.items())
print(stuff.keys())

#last item of the dictionary
#print(stuff.popitem())
#print(stuff)

print(stuff.setdefault("friends",22))
#print(stuff)

#add another dictionary to existing one
new_items= {"rocks":4, "arrows": 90}
stuff.update(new_items)
print(stuff)

#update values in dictionary
new_items= {"rocks":1, "arrows": 10}
stuff.update(new_items)
print(stuff)

stuff.update(food=0, energy=11, sun=71)
print(stuff)