from math import log

with open('p099_base_exp.txt', 'r') as f:
    max_log = -1
    max_line = None

    for idx, line in enumerate(f.readlines(), 1):
        a, b = line.strip().split(',')
        log_exp = int(b) * log(int(a))
        if log_exp > max_log:
            max_log = log_exp
            max_line = idx

    print(max_line)
