import tiktoken
enc = tiktoken.encoding_for_model('gpt-4o')
text = "hey there !my name is turab"

tokens = enc.encode(text)

print(tokens)

decoded = enc.decode([48467, 1354, 1073, 3825, 1308, 382, 7369, 378])
print(decoded)