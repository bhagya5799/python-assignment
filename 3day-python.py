from multiprocessing.sharedctypes import Value


age={
    "ramya":"24",
    "veena":"28",
    "visnvi":"14",
    "pavan":"18"
}
max_age=max(age,key=age.get)
print(max_age)