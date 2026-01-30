def get_sum(a, b):
    return a + b

def count_capital_letters(text):
    a = 0
    for i in text:
        if i.isupper():
            a = a + 1
    return a




def decode_string(words):
    words_lower = words.lower()
    result = ''
    
    for i in range(len(words_lower)):
        char = words_lower[i]
        count = 0
        for j in range(len(words_lower)):
            if words_lower[j] == char:
                count += 1
        if count > 1:
            result += ')'
        else:
            result += '('
    
    return result

def get_odd_count(count):
    digits = list(map(int, str(count)))
    res = 0
    for i in digits:
        if i == 0:
            continue
        elif i % 2 == 0:
            res = res + 1
        else:
            continue

    return res



def check_access(has_keycard, has_fingerprint, is_alarm, is_daylight):
    if is_alarm:
        return False
    
    if has_fingerprint:
        return True
    
    if has_keycard and is_daylight:
        return True
    
    return False

