key1=['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
value1=[20, 3, 1, 88, 55, 92, 6, 90, 910]
key2=['u', 'b', 'o', 'x',  'e', 'a']
value2=[200, 30, 10, 88, 55, 920]

dic1={k:v for k,v in zip(key1,value1) if v%2==1}
dic2={k:v for k,v in zip(key2,value2) if v%2==1}
merged_dic={**dic1,**dic2}
print(merged_dic)