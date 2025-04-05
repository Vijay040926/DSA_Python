def merge_three_dictionaries(dict1, dict2, dict3):
    merge_dict={**dict1,**dict2,**dict3}
    return merge_dict
dict1={'a': 1, 'b': 2}
dict2={'c': 3, 'd': 4}
dict3={'e': 5, 'f': 6}
res=merge_three_dictionaries(dict1,dict2,dict3)
print(res)