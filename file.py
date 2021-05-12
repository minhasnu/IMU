
values = []
def load_value(value,buff):
    values.append(value)
    while(len(values)>=buff):
        values.pop(0)
    return values


def write_file(values):
    with open('log.txt','w') as f:
        for i in range(98):
            f.write(str(values[i])+','+str(i/98)+'\n')
               
