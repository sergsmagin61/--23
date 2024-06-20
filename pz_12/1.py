'''
1.Дана последовательность целых чисел. Поменять местами ее первую и
последнюю трети. 
'''
sequence = [x for x in range(1, 18)]

third_length = len(sequence) // 3

first_third = sequence[:third_length]
middle_third = sequence[third_length:2*third_length]
last_third = sequence[2*third_length:]
new_sequence = last_third + middle_third + first_third

print(new_sequence)
