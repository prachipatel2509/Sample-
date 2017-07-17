import collections
st=raw_input("Enter a string: ")
list=st.split(" ")
dict={}
for n in list:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1

od = collections.OrderedDict(sorted(dict.items()))
for k,v in od.iteritems():
    print k,v
