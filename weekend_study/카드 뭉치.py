def solution(cards1, cards2 ,goal):
    used_cards1 = []
    used_cards2 = []
    for word in goal:
        if word in cards1:
            used_cards1.append(word)
        if word in cards2:
            used_cards2.append(word)
    for i, word in enumerate(used_cards1):
        if word != cards1[i]:
            return "No"
    for i, word in enumerate(used_cards2):
        if word != cards2[i]:
            return "No"
    return "Yes"