def solution(keymap, targets):
    answer = []
    key_dict = {}
    for key in keymap:
        for idx, char in enumerate(key):
            if char not in key_dict:
                key_dict[char]  = idx + 1
            key_dict[char] = min(key_dict[char], idx + 1)
    for target in targets:
        count = 0
        for char in target:
            if char not in key_dict:
                count = -1
                break
            count += key_dict[char]
        answer.append(count)
    return answer