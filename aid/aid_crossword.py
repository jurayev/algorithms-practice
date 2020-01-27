def findMatch(possibleMatches, crossword):
    for match in possibleMatches:
        is_matched = True
        match_length = len(match)
        if match_length == len(crossword):
            for i in range(match_length):
                if crossword[i] not in ['.', match[i]]:
                    is_matched = False
                    break
            if is_matched:
                return match

matches = [
'vaporeon',
'jolteon',
'flareon',
"espeon",
"umbreon",
"leafeon",
"glaceon",
"sylveon"
]

crossword = 'g...eon'
match = findMatch(matches, crossword)
print(match)