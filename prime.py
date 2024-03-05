def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    # 素数かどうかを判定したい数を入力します
    num = int(input("素数かどうかを判定したい数を入力してください: "))

    if is_prime(num):
        print(num, "は素数です")
    else:
        print(num, "は素数ではありません")
