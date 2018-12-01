#!/usr/bin/env python3

import string

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print('Test of reverse() function on string \'example\': ')
	print(reverse('example'))

	print('Test of acronym() function on phrase \'Graphical User Interface\': ')
	print(acronym('Graphical User Interface'))

	print('Test of whichTriangle() function on triangles: 3,3,3 4,4,5 3,4,5: ')
	print(whichTriangle(3,3,3))
	print(whichTriangle(4,4,5))
	print(whichTriangle(3,4,5))
	
	print('Test of scrabble() function on the word \'oxyphenbutazone\': ')
	print(scrabble('oxyphenbutazone'))

	print('Test of armstrong() function on the numbers 8208 and 294: ')
	print(armstrong(8208))
	print(armstrong(294))

	print('Test of primeFactors() function on the number 1234: ')
	for number in primeFactors(1234):
		print(number, end=' ')
	print()
	
	print('Test of pangram() function on \"Sphinx of black quartz, judge my vow\": ')
	print(pangram('Sphinx of black quartz, judge my vow'))

	print('Test of sort() function on list [9, 4, 6, 12, 1, 34]: ')
	for number in sort([9, 4, 6, 12, 1, 34]):
		print(number, end=' ')
	print()

	print('Test of rotate() function on sentence \"Python is fun\" with key 13: ')
	print(rotate(13, 'Python is fun'))

	print('Test of evenAndOdds() function: ')
	evenAndOdds()

	
'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	return string[::-1]
'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	words = phrase.split()
	acronym = ''
	for word in words:
		acronym = acronym + word[0]
	return acronym
'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	if sideOne == sideTwo or sideTwo == sideThree:
		if sideOne == sideThree:
			return 'equilateral'
		else: 
			return 'isoceles'
	else:
		return 'scalene'
'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	score = 0
	values = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h': 4, 'i':1, 
			'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 
			'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
	for letter in word:
		score += values.get(letter)
	return score
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
	numDigits = len(str(abs(number)))
	temp = number
	sumDigits = 0
	while temp != 0:
		digit = temp % 10
		sumDigits += (digit ** numDigits)
		temp /= 10
	return sumDigits == number
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):
	factors = []
	while number % 2 == 0:
		factors.append(2)
		number /= 2
	factor = 3
	while factor ** 2 <= number:
		if number % factor == 0:
			factors.append(factor)
			number /= factor
		else:
			factor += 2
	if number != 2:
		factors.append(number)
	return factors
'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
	letters = {}
	for letter in sentence.lower():
		if letter in string.ascii_lowercase:
			letters[letter] = 1
	if len(letters) == 26:
		return True
	else:
		return False
'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
	quicksort(numbers, 0, len(numbers) - 1)
	return numbers

def quicksort(array, low, high):
	if low < high:
		split = partition(array, low, high)
		quicksort(array, low, split)
		quicksort(array, split+1, high)

def partition(array, low, high):
	pivot = array[low]
	i = low - 1
	j = high + 1
	while True:
		while True:
			i = i + 1
			if array[i] >= pivot:
				break
		while True:
			j = j - 1
			if array[j] <= pivot:
				break
		if i >= j:
			return j
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
	encoded = ''
	
	for char in string:
		if char.isalpha():
			asc = ord(char)
			asc += key

			if char.isupper():
				if asc > ord('Z'):
					asc -= 26
				elif asc < ord('A'):
					asc += 26
			elif char.islower():
				if asc > ord('z'):
					asc -= 26
				elif asc < ord('a'):
					asc += 26

			encoded += chr(asc)
	else:
		encoded += char
	return encoded
'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
	odd = open('odd.txt', 'w')
	even = open('even.txt', 'w')
	inputString = input('Enter 10 numbers, separated by spaces: ')
	inputList = inputString.split(',')
	
	for number in inputList:
		if int(number) % 2 == 0:
			even.write(number + ' ')
		else:
			odd.write(number + ' ')

	odd.close()
	even.close()

if __name__ == "__main__":
    main()
