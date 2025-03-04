commands = [
    {
        "requires": [["ciao", "buongiorno"]],
        "function": print,
        "parameters": ["Ciao mondo!"]
    },
    {
        "requires": [["come"], ["stai", "va"]],
        "function": print,
        "parameters": ["Stavo bene prima che mi parlassi"]
    }
]

def executeCommand(words):
    for command in commands:
        foundAlternative = False
        for alternatives in command["requires"]:
            foundAlternative = False
            for word in alternatives: 
                if word in words:
                    foundAlternative = True
                    break
            if not foundAlternative: break
        if foundAlternative:
            commands[0]["function"](commands[0]["parameters"])
            return
executeCommand(["ciao"])