#2.Swap two variables without using a temporary variable
a=int(input('Enter Value for a:'))
b=int(input('Enter Value for b:'))
#show original values
print("\nBefore swap:")
print("a =", a)
print("b =", b)
# Swapping without a temporary variable using tuple unpacking
a, b = b, a
# Show swapped values
print("\nAfter swap:")
print("a =", a)
print("b =", b)