def removeDuplicateData(list_):
    duplicate = []
    for each in list_:
        if each in duplicate:
            list_.remove(each)
        else:
            duplicate.append(each)

dict_ = {'a':1, 'b':2, 'b':2, 'b':2}
dict2 = {'a':1, 'b':2, 'b':2, 'b':2}
dict3 = {'a':1, 'b':2, 'b':2, 'b':1}

list_ = [dict_, dict2, dict3]

removeDuplicateData(list_)

print(list_) #result: [{'a': 1, 'b': 2}, {'a': 1, 'b': 1}]
