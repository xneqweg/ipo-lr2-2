n = int(input(("школьник:")))
k = int(input("яблоки:"))
applesForPupil = k // n 
applesInBasket = k % n
print("яблок достанется школьнику:", applesForPupil)
print("яблок останется в корзине:", applesInBasket)
