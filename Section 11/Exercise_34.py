def merge_dicts_with_overlapping_keys(dicts):
    dict={}
    for i in dicts:
        for key,val in i.items():
            if key in dict:
                dict[key]+=val
            else:
                dict[key]=val
    return dict
dicts=[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
res=merge_dicts_with_overlapping_keys(dicts)
print(res)