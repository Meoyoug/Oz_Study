def solution(s, n):
    result = ''
    for i in s:
        if i.isalpha(): 
            start = ord('a') if i.islower() else ord('A') 
            # 받은 값이 대문자이냐 소문자냐 따라서 기준점을 a 또는 A의 아스키값으로 설정
            change_i = chr((ord(i) - start + n) % 26 + start)
            # 입력받은 알파벳의 (아스키값 - 기준점 + n 은) % 26 + 기준점 => 시저암호화
            
            result += change_i
        else:
            result += i 