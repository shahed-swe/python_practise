import base64

MESSAGE = '''CE8SHQYHERIfUkteRVVSQxYJFU9JRFMCAxkHAQQVQFRUSFtIQgEHFQkQBgEBVRkRVA0HDgoWABJL VVFEQhtbUgENBQEHCBFGQFVMBQYaXFQFDQwNCxBTQVZVTBELHlpSGA0FT0lEUxMNFwkNEQESEUlI RhsEAhFGQFVMAgodEhFJSEYfDApVRhE='''

KEY = 'shahedtalukder51'


result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
