

def combinations(items, combination_length):
    if combination_length <=0:
        max_item_position = 0
    else:
        max_item_position= len(items)-combination_length+1
    if max_item_position <=0:
        yield []
    for item_position in range(max_item_position):
        if combination_length == 1:
            yield [items[item_position]]
        else:
            for sub_combination in combinations(items[item_position+1:], combination_length-1):
                max_item_position = [items[item_position]]
                max_item_position.extend(sub_combination)
                yield max_item_position

def power2(items):
    power_count = 2**len(items)
    for power_mask in range(power_count):
        power_mask_string = str(bin(power_mask))[2:].zfill(len(items))
        combination = []
        for position,onoff in enumerate(power_mask_string):
            if onoff=='1':
                combination.append(items[position])
        print (combination)
    
    
            
def power(items):
    for combination_length in range(len(items)+1):
        for single_length_combination in combinations(items,combination_length):
            print(single_length_combination)
            
demo_list = [1,2,3,4,5,6,7]

power(demo_list)
power([])
power2(demo_list)
