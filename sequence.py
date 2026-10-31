valid_dna_sequence = 'AGTCTTCCAAGGCGATCGATTAGC'
invalid_dna_sequence = 'AXCTGHARCXGARGTVCGTAXXA'

print(len(valid_dna_sequence))

#check GC content
g_content = valid_dna_sequence.count('G')
print(g_content)