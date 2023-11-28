# (define (count-change amount)
#   (cc amount 5))

# (define (cc amount kinds-of-coins)
#   (cond ((= amount 0) 1)
#         ((or (< amount 0) (= kinds-of-coins 0)) 0)
#         (else (+ (cc amount
#                      (- kinds-of-coins 1))
#                  (cc (- amount
#                         (first-denomination kinds-of-coins))
#                      kinds-of-coins)))))
                     
# (define (first-denomination kinds-of-coins)
#   (cond ((= kinds-of-coins 1) 1)
#         ((= kinds-of-coins 2) 5)
#         ((= kinds-of-coins 3) 10)
#         ((= kinds-of-coins 4) 25)
#         ((= kinds-of-coins 5) 50)))

def count_change(amount):
    return cc(amount, 5)

def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1:
        return 1
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins == 3:
        return 10
    elif kinds_of_coins == 4:
        return 25
    elif kinds_of_coins == 5:
        return 50

# 示例用法
amount_to_change = 10
ways = count_change(amount_to_change)
print(f"There are {ways} ways to make change for {amount_to_change} cents.")
