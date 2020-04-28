# islower - determines letter case
# @c: the lette rto test
# Return: true or false
def islower(c):
    if ord(c) > 96 and ord(c) < 124:
        return(True)
    return(False)
