def count_words(arr):
    new_dic = {}
    count = 1
    for i in arr:
        if i in new_dic:
            new_dic[i] += 1
        else:
            new_dic[i] = count
    return new_dic
