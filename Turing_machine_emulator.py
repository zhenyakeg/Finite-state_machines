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
print(' '.join(emulate_turing_machine('input.txt', 'rule.txt')))
