shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total= 0
    for x in food:
       if stock[y]>0:
                total += prices[x]
    return total


print compute_bill(['apple',1])

#['pear',2],['orange',3])
