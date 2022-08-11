results = []
for i in data:
    y = delayed(inc)(i)    
    results.append(y)
    
total = delayed(sum)(results)