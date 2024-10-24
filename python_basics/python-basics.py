'''
WHAT IS PYTHON
Python is a high-level, general-purpose, and very popular programming language. Python programming language (latest Python 3) is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.

Python language is being used by almost all tech-giant companies like - Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.

The biggest strength of Python is huge collection of standard library which can be used for the following:

Machine Learning
GUI Applications (like Kivy, Tkinter, PyQt etc. )
Web frameworks like Django (used by YouTube, Instagram, Dropbox)
Image processing (like OpenCV, Pillow)
Web scraping (like Scrapy, BeautifulSoup, Selenium)
Test frameworks
Multimedia
Scientific computing
Text processing and many more..

Python is currently the most widely used multi-purpose, high-level programming language, which allows programming in Object-Oriented and Procedural paradigms. Python programs generally are smaller than other programming languages like Java. Programmers have to type relatively less and the indentation requirement of the language, makes them readable all the time.
'''
'''PYTHON COMMENTS and Rules for all of programming
Rule 1: Comments should not duplicate the code.
Rule 2: Good comments do not excuse unclear code.
Rule 3: If you can't write a clear comment, there may be a problem with the code.
Rule 4: Comments should dispel confusion, not cause it.
Rule 5: Explain unidiomatic code in comments.
Rule 6: Provide links to the original source of copied code.
Rule 7: Include links to external references where they will be most helpful.
Rule 8: Add comments when fixing bugs.
Rule 9: Use comments to mark incomplete implementations.

# is a single line comment
Anything between '''''' is a single to multiple line comment
'''

'''VARIABLES: Variables do not need to be declared with any particular type, and can even change type after they have been set. Just start with a initial value or not

VARIABLE NAMES: A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
***A variable name must start with a letter or the underscore character
***A variable name cannot start with a number
***A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
***Variable names are case-sensitive (age, Age and AGE are three different variables)
***A variable name cannot be any of the Python keywords.
MULTI VARIABLE CREATION:
#f_name,l_name,age = "Khadeem","Bernard", 21
print(f_name,l_name,age) or print(f_name+l_name+age)

or
#initialValue = start = i = 0

CASTING VARIABLES:If you want to specify the data type of a variable, this can be done with casting.
'''
'''PYTHON DATATYPES:
Python has the following data types built-in by default, in these categories:

Text Type:  str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:  set, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
None Type:  NoneType
'''

'''Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.'''



'''PYTHON STRING MANIPULATION 
String Slicing returns a piece of a string that is dictated by the inputs.
Ex.'''
test= "This is a test string in Python"
print(test[5]) #how to access a character in a string
print(test[15:35]) #how to access a range of characters in a string

'''String Methods'''
print(test.upper())#uppercase letters
spacey = "   This has a lot of spacey before and after   "
print(spacey.strip().upper()) # Gets rid of the extra spaces
location = (spacey.find('before'))
print(spacey[location:(location*6)])

'''String Concatenation:'''
print(test + " " + spacey)

name = 'Take 5'
amount = 10
cost = 20
statements = "I had my favorite candy {0}, I bought a total of {1} for ${2}"
print(statements.format(name,amount,cost))

#Need to finish string quotes using the escape character

'''Conditionals for Python'''
import math
x = 23
last_name = "Abbas"
first_name = "Karam"
age = 16
fake_age = "21"
patience = 3
verbal_abuse = 50
kenny_is_alive = True
if kenny_is_alive and age > 25 or kenny_is_alive == False:
    print("This is what you are doing. This is what I want you to do.")
if last_name == "Abbas" or last_name == "Karam":
    print("You're a certified 1000 ELO chess enjoyer.")
if last_name == "Abbas" and first_name == "Karam":
    print("It's not over for you yet. Keep it pushing.")
if age > 20:
    print("You old!")
    age += 1
elif age == 19:
    print("Your birthday last year was nice.")
else:
    print("Generation of Social Goblins")
    age = 19
if first_name == "Karam":
    print("NO!")
if not kenny_is_alive:
    print("Kevin Whyyyyyy")
print("Karam Abbas")
print(2**6)
print(math.sqrt(age))
print(math.pow(2,6))
grade = 84
if grade >= 90:
    print("A")
if grade >= 80:
    print("B")
if grade >= 70:
    print("C")
if grade >= 60:
    print("D")
else:
    print("F")
print(math.pi)
print(math.gcd(0, 34))
print(math.isfinite(2000))
print(math.cos(10))
print(math.asin(1))
print(math.cos(3.14159265359))
print("I'm blue da boo de da boo dae")
# Lists In Python
'''Lists are used to store multiple items in a single variable
If you have coded in another language it works the same as an array
'''
food = ["rice", "wheat", "bread", "potatoes", "meat", "water"]

print(food)
print(len(food)) # Length of the list
print(food[2]) # Prints a specific part of the list
print(sorted(food)) # Sorts the list alphabetically
print(food)
food.sort() # Sorts and alters the original list
print(food)
food.reverse() # Reverses the list order
print(food)
food.append("maize") # Added to the end of the list OR
food[6] = "maize" # Added to the end
print(food)
print(food.index("potatoes")) # Returns the index of the item in the list 
del food[4]
print(food)

# Dictionaries - Key value pairs like a dictionary and fefinition
favGames = {"Hussein": "Warframe", "Maryam": "She is not a gamer...", 
"Mom": "Royal Match"}
print(favGames)
print(favGames.keys()) # All of the keys in the dictionary
print(favGames.values()) # All of the values in the dictionary
print(len(favGames))

users = {"Karam": 5558840, "Mom": 6666, "Maryam": 1212958186}
user = "starBoy"
password = "theWeeknd"

login_username = input("What is your username?")
login_password = input("What is your password?")
if login_username == user and login_password == password:
    print("Success!")
else:
    print("Failure.")

#To the Loops: For Loops used for sequential loops like a list, dictionary set or even a string
for thing in food:
    print(thing)

for y in favGames:
    print(y)

for thing in food:
    print("When in the Course of human events it becomes necessary for one people to dissolve the political bands which have connected them with another and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. — That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, — That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security. — Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world. He has refused his Assent to Laws, the most wholesome and necessary for the public good. He has forbidden his Governors to pass Laws of immediate and pressing importance, unless suspended in their operation till his Assent should be obtained; and when so suspended, he has utterly neglected to attend to them. He has refused to pass other Laws for the accommodation of large districts of people, unless those people would relinquish the right of Representation in the Legislature, a right inestimable to them and formidable to tyrants only. He has called together legislative bodies at places unusual, uncomfortable, and distant from the depository of their Public Records, for the sole purpose of fatiguing them into compliance with his measures. He has dissolved Representative Houses repeatedly, for opposing with manly firmness his invasions on the rights of the people. He has refused for a long time, after such dissolutions, to cause others to be elected, whereby the Legislative Powers, incapable of Annihilation, have returned to the People at large for their exercise; the State remaining in the mean time exposed to all the dangers of invasion from without, and convulsions within. He has endeavoured to prevent the population of these States; for that purpose obstructing the Laws for Naturalization of Foreigners; refusing to pass others to encourage their migrations hither, and raising the conditions of new Appropriations of Lands. He has obstructed the Administration of Justice by refusing his Assent to Laws for establishing Judiciary Powers. He has made Judges dependent on his Will alone for the tenure of their offices, and the amount and payment of their salaries. He has erected a multitude of New Offices, and sent hither swarms of Officers to harass our people and eat out their substance. He has kept among us, in times of peace, Standing Armies without the Consent of our legislatures. He has affected to render the Military independent of and superior to the Civil Power. He has combined with others to subject us to a jurisdiction foreign to our constitution, and unacknowledged by our laws; giving his Assent to their Acts of pretended Legislation: For quartering large bodies of armed troops among us: For protecting them, by a mock Trial from punishment for any Murders which they should commit on the Inhabitants of these States: For cutting off our Trade with all parts of the world: For imposing Taxes on us without our Consent: For depriving us in many cases, of the benefit of Trial by Jury: For transporting us beyond Seas to be tried for pretended offences: For abolishing the free System of English Laws in a neighbouring Province, establishing therein an Arbitrary government, and enlarging its Boundaries so as to render it at once an example and fit instrument for introducing the same absolute rule into these Colonies For taking away our Charters, abolishing our most valuable Laws and altering fundamentally the Forms of our Governments: For suspending our own Legislatures, and declaring themselves invested with power to legislate for us in all cases whatsoever. He has abdicated Government here, by declaring us out of his Protection and waging War against us. He has plundered our seas, ravaged our coasts, burnt our towns, and destroyed the lives of our people. He is at this time transporting large Armies of foreign Mercenaries to compleat the works of death, desolation, and tyranny, already begun with circumstances of Cruelty & Perfidy scarcely paralleled in the most barbarous ages, and totally unworthy the Head of a civilized nation. He has constrained our fellow Citizens taken Captive on the high Seas to bear Arms against their Country, to become the executioners of their friends and Brethren, or to fall themselves by their Hands. He has excited domestic insurrections amongst us, and has endeavoured to bring on the inhabitants of our frontiers, the merciless Indian Savages whose known rule of warfare, is an undistinguished destruction of all ages, sexes and conditions. In every stage of these Oppressions We have Petitioned for Redress in the most humble terms: Our repeated Petitions have been answered only by repeated injury. A Prince, whose character is thus marked by every act which may define a Tyrant, is unfit to be the ruler of a free people. Nor have We been wanting in attentions to our British brethren. We have warned them from time to time of attempts by their legislature to extend an unwarrantable jurisdiction over us. We have reminded them of the circumstances of our emigration and settlement here. We have appealed to their native justice and magnanimity, and we have conjured them by the ties of our common kindred to disavow these usurpations, which would inevitably interrupt our connections and correspondence. They too have been deaf to the voice of justice and of consanguinity. We must, therefore, acquiesce in the necessity, which denounces our Separation, and hold them, as we hold the rest of mankind, Enemies in War, in Peace Friends. We, therefore, the Representatives of the united States of America, in General Congress, Assembled, appealing to the Supreme Judge of the world for the rectitude of our intentions, do, in the Name, and by Authority of the good People of these Colonies, solemnly publish and declare, That these united Colonies are, and of Right ought to be Free and Independent States, that they are Absolved from all Allegiance to the British Crown, and that all political connection between them and the State of Great Britain, is and ought to be totally dissolved; and that as Free and Independent States, they have full Power to levy War, conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which Independent States may of right do. — And for the support of this Declaration, with a firm reliance on the protection of Divine Providence, we mutually pledge to each other our Lives, our Fortunes, and our sacred Honor.)!")