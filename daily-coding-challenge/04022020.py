def solution(n):   
    product_digit = 1
    sum_digit = 0
    for i in str(n):
        product_digit *= int(i)
        sum_digit += int(i)
    diff = product_digit - sum_digit
    return diff

print(solution(234))