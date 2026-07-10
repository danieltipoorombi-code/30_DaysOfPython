# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Linkedin', 'Snapchat', 'Pinterest'])
print(it_companies)

it_companies.remove('Twitter')
print(it_companies)

it_companies.discard('Pinterest')
print(it_companies)

A . union(B)
print(A.union(B))

A.intersection(B)
print(A.intersection(B))

print(A.issubset(B))
print(A.union(B))
print(A.symmetric_difference(B))

print(A.clear())
print(B.clear())
print(it_companies.clear())

age_set = set(age)
print(age_set)
print(len(age_set))

print(len(age_set) == len(age))

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")