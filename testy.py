items = ["bread", "eggs", "milk"]
def spametize(item): return "spam"
spamCafeOrder = map(spametize, items)
print("We need to go to the market and get:")
for it in spamCafeOrder: print(it)

def quest():
    print("You must now cut down the tallest tree in the forest...")
    print("With... A HERRING!!!!!")

# quest()

def theKnightsWhoSayNi(gift):
    """In order to continue your quest for Camelot, you must
    bring the Knights gifts. Do not mess with these guys, for
    they say 'Ni' at the slightest provocation!"""
    if gift == "shrubbery":
        return ("You must now cut down the tallest tree"
        "in the forest... with... A HERRING!!!!")
    else:
        return "You must bring us... A SHRUBBERY!!!"

print(theKnightsWhoSayNi.__doc__)      


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)

parrot(type='Turkish Red', action='caw', voltage=1000)    

d = {"voltage": "a million", "state":"bleedin' demised"}
parrot(**d)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#---------------------
quotes = {
"Moe": "A wise guy, huh?",
"Larry": "Ow!",
"Curly": "Nyuk nyuk!",
}
stooge = "Curly"
print(stooge, "says:", quotes[stooge])


-----------------------------------------------------------

        path = self.directory
        i = 1
        files = [s for s in os.listdir(path) if os.path.isfile(os.path.join(path, s))]
        files.sort(key = lambda s: os.path.getmtime(os.path.join(path, s)))

        for file in files:
            os.rename(path + file, path + str(i) + '.png')
            i = i + 1


nested_list = [ [1, 2], [3, 4] ]
outer_range = range(len(nested_list))
inner_range = range(len(nested_list[i]))
for i in outer_range:
    for j in inner_range:
        print(nested_list[j] [i])