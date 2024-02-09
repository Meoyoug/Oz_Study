def solution(food):
    answer = ''
    for i,f in enumerate(food):
        answer += (str(i) * (f//2))   
    answer = answer + '0' + answer[::-1]
#111
    return answer