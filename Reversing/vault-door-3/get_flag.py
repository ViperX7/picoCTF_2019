# Scrambled Password
buffer = "jU5t_a_sna_3lpm11ga4e_u_4_m9rf48"

# A place To store the password
password = [
    '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
    '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
    '@', '@'
]

# Reversed Loops
# i buffer replaced by password and vice versa

for i in range(0, 8):
    password[i] = buffer[i]

for i in range(8, 16):
    password[i] = buffer[23 - i]

for i in range(16, 32, 2):
    password[i] = buffer[46 - i]

i = 31
while (i >= 17):
    password[i] = buffer[i]
    i = i - 2
print('picoCTF{' + ''.join(password) + '}')
