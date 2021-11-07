# METHOD 1
def reverse(strng):
    def g(n, trc):
        if n < 0:
            return trc
        trc += strng[n]
        trc = g(n - 1, trc)
        return trc

    return g(len(strng) - 1, '')


s = input('Enter the string: ')
print(reverse(s))


# METHOD 2
def reverse(strng, n, trc):
    if n < 0:
        return trc
    trc += strng[n]
    trc = reverse(strng, n - 1, trc)
    return trc


s = input('Enter the string: ')
print(reverse(s, len(s) - 1, ''))
