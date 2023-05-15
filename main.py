def can_place_flowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
        i += 1
        if count >= n:
            return True
    return False

# Example usage
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(can_place_flowers(flowerbed, n))

flowerbed = [1, 0, 0, 0, 1]
n = 2
print(can_place_flowers(flowerbed, n))