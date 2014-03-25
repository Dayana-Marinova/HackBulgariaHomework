def sort_fractions(fractions):
    sort_fractions_list = []
    sort_fractions_dic = {}
    result = []
    for items in fractions:
        sort_fractions_dic[float(items[0]) / items[1]] = items
        sort_fractions_list.append(float(items[0]) / items[1])
    sort_fractions_list.sort()
    for item in sort_fractions_list:
        for key in sort_fractions_dic:
            if item == key:
                result.append(sort_fractions_dic[key])
    return result
