#!/usr/bin/env python3

str = "Q}|u`sfg~sf{}|a3"
final = "Congratulations!"

val = int(ord(str[0]) ^ ord(final[0]))

password = 0x1337D00D - val

print("Password: {}".format(password))
