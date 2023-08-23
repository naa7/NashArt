import api2
import os, re

while True:
    prompt = input("Programming prompt: ")

    if prompt == 'q' or prompt == 'Q':
        break
    elif prompt == 'c' or prompt == 'C': 
        if os.name == 'nt':
            os.system('cls')
            continue
        else:
            os.system('clear')
            continue

    result = api2.Completion.create(
        model  = 'gpt-4',
        prompt = prompt,
        results     = api2.Search.create(prompt, actualSearch = False), # create search (set actualSearch to False to disable internet)
        creative    = False,
        detailed    = True,
        codeContext = '') # up to 3000 chars of code
    
    print("\nprogrammingGPT >>> ", re.sub(r"(?s).*?" + re.escape("</PHIND_METADATA>"), "", result.completion.choices[0].text))
    print("----------------")
    print("[c]lear - [q]uit")
    print("----------------")