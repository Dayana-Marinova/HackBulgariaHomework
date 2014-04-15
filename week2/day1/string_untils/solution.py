def lines(text):
    array_text = text.split('\n')
    return array_text


def unlines(elements):
    return " ".join(elements)


def words(text):
    list_of_chars = []
    for ch in text:
        list_of_chars.append(ch)
    return list_of_chars


def unwords(elements):
    return " ".join(elements)


def tabs_to_spaces(string, one_tab_n_spaces):
    spaces = " " * one_tab_n_spaces
    new_string = string.replace("\t", spaces)
    return new_string


#print lines('hi may name is dayana. \n your name is \n nice too meet you')
#print unlines(['hi', 'my', 'name', 'is', 'dayana.'])
#print words("dayana marinova")
#print unwords(['d', 'a', 'n', 'e'])
#print tabs_to_spaces("\tdayana\t")
