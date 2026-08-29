data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
list_result=[]
for item in data:
    for key,value in item.items():
        if key=="age":
            if value>25:
                list_result.append(item)
print(list_result)