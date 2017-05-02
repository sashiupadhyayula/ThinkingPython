import pprint

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(items):
    total = 0
    for k,v in items:
        pprint.pprint(str(v) + ' ' + k)
        total = total + v
    print ('Total items in inventory are: ' + str(total))

displayInventory(inventory.items())