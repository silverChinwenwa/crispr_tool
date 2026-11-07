valid_dna_sequence = 'AGTCTTCCAAGGCGATCGATTAGC'
invalid_dna_sequence = 'AXCTGHARCXGCARGTVCGTAXXA'

print(len(valid_dna_sequence))
print(len(invalid_dna_sequence))

#check GC content
g_content = valid_dna_sequence.count('G')
print(g_content)

c_content = valid_dna_sequence.count('C')
print(c_content)

#calculate GC percent
gc_percent = ((g_content + c_content) / 24) * 100
print(f'{gc_percent} %')

#Checking for valid DNA sample

def check_dna(test_dna):
    if set(test_dna).issubset('AGTC'):
        return 'Valid DNA'
    else:
        return 'Invalid DNA'
print(check_dna('AAGTCAT'))    
print(check_dna('ASGRTCK'))

#Using FASTA file from NCBI
fasta_file = 'crispr_tool/data/sequence.fasta.txt'
with open(fasta_file, 'r', encoding='utf-8') as fasta_seq:
    for dna in fasta_seq:
        clean_dna = dna.strip()
        
        if clean_dna or clean_dna.startswith('>'):
            continue

        if set(clean_dna.upper()).issubset('AGTC'):
            print('Valid DNA')
        else:
            print('Invalid DNA')




