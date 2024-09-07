school = "west-mec"
# Snake Case Example
first_name = "Karam"
last_name = "Abbas"

print(first_name)
print(school)
print(type(first_name))
print("Hello World!")

message = """This is a multi line message saying that
you should look more often
when turning right on red
or when doing unprotected left turns"""

print(message)

name = "Karam"
age = 16
alive = True
fav_foods = ['Italian', "Japanese", 'Arabian']
# Do this instead
print(name + " " + str(age) + " " + str(alive) + " " + str(fav_foods))

print(int(True))

print(int(False))

print(float("55.5"))

age_1 = 23
age_2 = 56

if age_2 > 45:
    print("They OLD")
elif age < 30:
    print("Babies am I right?")
else:
    print("They are getting there")

bf = "Jesse Pinkman"
thinks_bf = "Badger Mayhew"

if bf == thinks_bf:
    print("You need more Friends.")

if bf != thinks_bf:
    print("You must have plenty of friends.")

alive = True
year = 2024

if alive == True:
    if year == 2024:
        print("Yay!")


money = 100

if money < 21:
    print("Broke Netflix")
elif 21 < money < 41:
    print("Movie Theatre")
elif 41 < money < 61:
    print("Dinner")
elif 81 < money < 151:
    print("Sky Diving")
