def merge_lists_to_dictionary(keys, values):
    dict={}
    if len(keys)!=len(values):
        return False
    else:
        for i in range(len(keys)):
            dict[keys[i]]=values[i]
        return dict
keys = ['a', 'b', 'c']
values = [1, 2, 3]
res=merge_lists_to_dictionary(keys,values)
print(res)