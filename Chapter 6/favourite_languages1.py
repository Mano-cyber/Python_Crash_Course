favourite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print('Key-value pairs:')
for name, language in favourite_languages.items():
	print(f"\t{name.title()}'s favourite_language is {language.title()}.")

print('\nKeys:')
for name in favourite_languages.keys():
	print(f"\t{name.title()}")

print('\nValues:')
for language in favourite_languages.values():
	print(f"\t{language.title()}")