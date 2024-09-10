'''
Riley Maurer
9/6/2024

I calculated ages of different species based on the inputed age.
'''

human_age = input("enter age: ")
human_months = float(human_age) / 12
human_days = float(human_age) / 365
print("Your age is", float(human_age), "years, ", float(human_months), "months, and", float(human_days), " days.")

dog_age = float(human_age) * 7
dog_months = dog_age / 12
dog_days = dog_age / 365
print("Your age in dog years is", float(dog_age), "years, ", float(dog_months), "months, and ", float(dog_days), "days.")

cat_age = float(human_age) / 9
cat_months = cat_age / 12
cat_days = cat_age / 365
print("Your age in cat years is", float(cat_age), "years, ", float(cat_months), "months, and ", float(cat_days), "days.")

x = float(human_age)**2
horse_age = 3*(((x-47)/7)+12)
horse_months = horse_age / 12
horse_days = horse_age / 365
print("Your age in horse years is", float(horse_age), "years, ", float(horse_months), "months, and ", float(horse_days), "days.")
