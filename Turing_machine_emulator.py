def emulate_turing_machine(input_file, rules):
    turing_line = {}
    turing_rules = {}
    state = 'q1'
    pos = 0
    my_input = open(input_file, encoding='UTF-8')
    input_line = my_input.readline().rstrip()

    for i in range(len(input_line)):
        turing_line[i] = input_line[i]

    turing_rule_file = open(rules, encoding='UTF-8')

    for line in turing_rule_file:
        current_rule = line.split()
        turing_rules[(current_rule[0], current_rule[1])] = \
            (current_rule[2], current_rule[3], int(current_rule[4]))

    while state != 'STOP':
        new_state, new_pos = turing_rules[(state, turing_line[pos])][0], \
                             pos + turing_rules[(state, turing_line[pos])][2]
        turing_line[pos] = turing_rules[(state, turing_line[pos])][1]
        state, pos = new_state, new_pos
        if new_pos not in turing_line:
            turing_line[new_pos] = 'B'

    result = []

    for i in sorted(turing_line.keys()):
        if turing_line[i] != 'B':
            result.append(turing_line[i])
    return result


def generate_rule_for_deleting():
    output_file = open('delete_if_first==last_rule.txt', 'w',)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter1 in alphabet + ['B']:
        print('q1', letter1, 'q' + letter1, letter1, 1, file=output_file)
        if letter1 == 'B':
            print('q1', letter1, 'STOP', 'B', 0, file=output_file)
        for letter2 in alphabet:
            print('q' + letter2, letter1, 'q' + letter2, letter1, 1, file=output_file)
            if letter1 == 'B':
                print('q' + letter2, letter1, 'q' + letter2 + letter2, 'B', -1, file=output_file)
            if letter2 == letter1:
                print('q' + letter2 + letter2, letter1, 'qdel', 'B', -1, file=output_file)
            else:
                print('q' + letter2 + letter2, letter1, 'STOP', letter1, 0, file=output_file)
        if letter1 != 'B':
            print('qdel', letter1, 'qdel', 'B', -1, file=output_file)
        else:
            print('qdel', letter1, 'STOP', 'B', 0, file=output_file)
    output_file.close()

print(' '.join(emulate_turing_machine('input.txt', 'delete_if_first==last_rule.txt')))
