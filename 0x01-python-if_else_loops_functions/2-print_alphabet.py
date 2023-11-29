#!/usr/bin/python3
#Print the alphabet in lowercase, not followed by a new line.
print(''.join(chr(97 + i) for i in range(26)), end='')
