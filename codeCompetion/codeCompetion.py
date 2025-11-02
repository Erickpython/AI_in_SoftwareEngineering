# manual code completeion 

def sort_dict_manual (data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

# exampe usage
data = [{'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}]

print (sort_dict_manual(data, 'age'))

# AI powered ode completion  -- GITHUB COPILOT

def sort_dict_ai(data, key):
    return sorted(data, key=lambda x: x[key])

# example usage
data = [{'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}]

print(sort_dict_ai(data, 'age')) 