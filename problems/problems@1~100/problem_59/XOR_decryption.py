import itertools

base = ord('a')
with open('./p059_cipher.txt') as f:
    encrypted_code = [int(s) for s in f.read().strip().split(',')]

for i, j, k in itertools.permutations(range(base, base + 26), 3):
    encryption_key = [i, j, k] * (len(encrypted_code) // 3)
    plain_text = "".join(
        [chr(n1 ^ n2) for n1, n2 in zip(encrypted_code, encryption_key)])
    common_words = [
        ' the ', ' to ', ' of ', ' and ', ' a ', ' in ', ' that ', ' for '
    ]

    if sum([s == ' ' for s in plain_text]) > 10 and \
            sum(w in plain_text for w in common_words) > 5:
        print([chr(i), chr(j), chr(k)])
        print(plain_text)
        input()

# encryption_key = [ord('e'), ord('x'), ord('p')] * (len(encrypted_code) // 3)
# res = sum([n1 ^ n2 for n1, n2 in zip(encrypted_code, encryption_key)])
# print(res)
