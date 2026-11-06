valid_dna_sequence = 'AGTCTTCCAAGGCGATCGATTAGC'
invalid_dna_sequence = 'AXCTGHARCXGARGTVCGTAXXA'

print(len(valid_dna_sequence))

#check GC content
g_content = valid_dna_sequence.count('G')
print(g_content)

#Checking for valid DNA

def check_dna(test_dna):
    if set(test_dna).issubset('AGTC'):
        return 'Valid DNA'
    else:
        return 'Invalid DNA'
    
print(check_dna('ASGRTCK'))
print(check_dna('AAGTCAT'))
