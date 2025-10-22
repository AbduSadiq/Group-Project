def flip_string(s):
    if len(s) == 0:
        print("Please do not enter an empty string!")
    else:
        s_backwards = s[::-1]
        print(s_backwards)

flip_string("toad")