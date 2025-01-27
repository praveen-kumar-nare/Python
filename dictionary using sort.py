d = {'praveen': 10, 'kumar': 9, 'rose': 15}

myKeys = list(d.keys())
myKeys.sort()

sd = {i: d[i] for i in myKeys}
print(sd)