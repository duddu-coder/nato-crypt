from nato import NATO

text = '''
The quick brown fox jumps over the lazy dog
'''

nato = NATO()

stage_1_hash = nato.alter_chars(text)

print(stage_1_hash)