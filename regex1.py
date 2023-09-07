import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( ) 

coreyms.com

800-555-4231
900.890.7539
578*698*4582
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
urls = 'https://www.google.com,' 'http://coreyms.com,' 'https://youtube.com,' 'https://www.nasa.gov'

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)


#matches = pattern.finditer(urls)

#for match in matches:
 #   print(match.group(3))

num = "123 12345 123456 1234567"

print("matches:", len(re.findall("\d{5,7}", num)))

