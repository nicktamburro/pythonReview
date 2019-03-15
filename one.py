print("Welcome back to your old friend Python.")

#remember no semi-colons, and indentation actually matters!

if 5 > 2
    print("You bet it is, buddy.")

"""and remember this is for
multiline comments"""

#you don't have to specify a variable type, just name it and define it
band = "Mudhoney"
previousBand = "Green River"
print(band)
print(previousBand)

#var types can change, no problem
album = 2112
print(album)
album = "Permanent Waves"
print(album)

#concat is same as js
print("He was in " + previousBand + " before he was in " + band + "."

# + will also add, if you give it numbers
x = 100
y = 1
print(x + y)

#but, thankfully, you'll get an error if you do:
print(x + album)

"""NUMBER TYPES- python has int, float, and complex
but you don't have to name them, it will just sort it out itself"""
x = 1000
y = 1.123
z = 1j
#j is the imaginary part of the number

#and you can ask it what number class you have
print(type(x))
print(type(z))

#if we want to specify a variable type, we use casting
first = int(1)
second = str("Lemmy")
third = float(1.34)

#also it will change it for you
fourth = int("1")
#will show 1
fifth = str(1)
#will be "1"
sixth = float(3)
#will be 3.0

#for strings, single quotes = double quotes
a = "hi how are you"
print(a) #prints the string
print(a[1]) #prints just letter i, index 1
print(a[2:5]) #prints that range of indicies

#strip is like trim in JS
print(a.strip())  #takes off white space at front and back

# len is like .length
print(len(a))

print(a.lower())  # .toLowerCase
print(a.upper()) # .toUpperCase

#replace
print(a.replace("h", "j"))  #"ji jow are you"

#split
print(a.split(","))  #wherever there's a comma, it splits into separate strings on either side







