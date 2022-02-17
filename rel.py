def rel_tmp(string):
    result, tmp, count = '', '', 1
    for i in string:
        if tmp == '':
            result += i
        elif tmp != i:
            if count != 1:
                result += str(count)
                count = 1
            result += i
        if tmp == i:
            count += 1
        tmp = i
    if count != 1:
        result += str(count)
    return result


def rel_list(string):
    result = []
    for i in range(0, len(string)):
        if not result:
            result.append(string[i])
        elif string[i] != string[i-1]:
            result.append(string[i])
        else:
            if not result[-1].isdigit():
                result.append('2')
            else:
                result[-1] = str(1 + int(result[-1]))
    return ''.join(result)
    
