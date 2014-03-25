def slope_style_score(scores):
    max_num = scores[0]
    min_num = scores[0]
    for i in range(1, len(scores)):
        if scores[i] < min_num:
            min_num = scores[i]
        elif scores[i] > max_num:
            max_num = scores[i]
    scores.remove(min_num)
    scores.remove(max_num)
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]
    result = float(sum) / len(scores)
    return round(result, 2)
