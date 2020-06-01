secret_word = 12
guess = 0

while int(guess) != secret_word:
    guess = int(input("Találd ki a titkos egész számot: "))
    if guess > secret_word:
        print("Kisebb szám kell!")
    elif guess < secret_word:
        print("Nagyobb szám kell!")

print("Talált!!! Ügyes vagy!")
