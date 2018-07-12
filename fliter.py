# 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_palindrome(n):
    normalString = str(n);
    reverseString = normalString[::-1]
    return normalString == reverseString
output = filter(is_palindrome, range(1, 5000))
print('1~1000:', list(output))