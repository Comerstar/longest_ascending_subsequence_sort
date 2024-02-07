
def merge(comp, lst1, lst2):
    res = []
    lst1.reverse()
    while len(lst1) > 0 and len(lst2) > 0:
        if comp(lst1[-1], lst2[-1]) <= 0:
            res.append(lst1.pop())
        else:
            temp = lst1
            lst1 = lst2
            lst2 = temp
    while len(lst1) > 0:
        res.append(lst1.pop())
    while len(lst2) > 0:
        res.append(lst2.pop())
    return res

def longest_ascending_subsequence_sort(comp, lst, rev = False):
    sorted = []
    copy = lst.copy()
    while len(copy) > 0:
        table = [[0, 0]] * len(copy)
        longest = 0
        length = 1
        for i in range(len(copy)):
            index = -1
            max_len = 1
            for j in range(i):
                if table[j][0] + 1 > max_len and comp(copy[j], copy[i]) <= 0:
                    max_len = table[j][0] + 1
                    index = j
            table[i] = [max_len, index]
            if (max_len > length):
                length = max_len
                longest = i
        index = longest
        longest_subsequence = []
        while longest != -1:
            longest_subsequence.append(copy.pop(longest))
            longest = table[longest][1]
        sorted = merge(comp, sorted, longest_subsequence)
        if rev:
            copy.reverse()
    return sorted

test = []
print("Input the integers of your list, then a non-integer.")
user_in = input()
try:
    while True:
        test.append(int(user_in))
        print("Inputted ", test)
        user_in = input()

except Exception:
    print(test)
    print(longest_ascending_subsequence_sort(lambda x, y: x - y, test))
