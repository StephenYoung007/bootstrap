def longest(s):
    """
    :type s: str
    :rtype: int
    """
    max_before = max_now = start = 0
    dict = {}
    for index, i in enumerate(s):
        if i in dict and dict[i] >= start:
            max_before = max(max_before, max_now)
            max_now = index - start - 1
            start = dict[i] + 1
        else :
            max_now = max_now + 1
        dict[i] = index
    count = max(max_before, max_now)
    return count


if __name__ == '__main__':
    s = "aflhdjkcdgaiucv;weklq.fdvcxio;lkw.efbvdsu"
    print(longest(s))