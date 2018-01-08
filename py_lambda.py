
seq = [1,2,3,4]

#map
map_fun = list(map(lambda num: num*3, seq))
print('seq times 3 is {}'.format(map_fun))

#filter
fil_fun = list(filter(lambda num: num%2==0, seq))
print('seq remainder 2 is 0: {}'.format(fil_fun))
    
