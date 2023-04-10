is_male = False
is_tall = True

if is_male:
    if is_tall:
        print("Yo! You are a guy! and you can get mansi")
else:
    print("You are a not a guy nor tall")

if is_male or is_tall:
    print("LOL.. male or tall.")
else:
    print("Not male or tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("LOL.. male and tall. Jackpot!")
elif is_male and not(is_tall):
    print("Tiny guy")