test = 'aaabbccceeeeeeedd'

# Run time O(n)

def compress_string(string):
    # this variable allows me to know if I have
    # started counting the letters or not
    state = False
    # reverse the string backwards so I do not have
    # to keep track of the length of the array in a while loop
    for i in reversed(range(len(string) - 1)):
        # This if statement identifies a sequence of letters.
        if string[i] == string[i + 1]:
            if state is False:
                # if it is the first letter of the sequence change the right index
                # to the current count of letters and change the state to True
                string = string[:i + 1] + '2' + string[i + 2:]

                state = True
            else:
                # if it is not the first sequence remove the right value
                # and then add 1 to the new right value
                temp = str(int(string[i + 2]) + 1)
                string = string[:i + 1] + temp + string[i + 3:]
        else:
            # if there is no sequence, ensure the state if False
            state = False
    return string
                

print(compress_string(test))