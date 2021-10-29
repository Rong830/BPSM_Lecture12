input_txt_contents = open('input.txt').read().upper().replace('ATTCGATTATAAGC','').split()
input_txt_contents2 = open('input.txt').read().upper().split()
for cleanones in input_txt_contents :
    cleanseqs.write(cleanones + '\n')
    cleanones
cleanseqs.close()

with open('input.txt') as mylines :
    my_file_contents = mylines.read().upper().split()
    with open('Cleaned_sequences.txt','w') as cleanedseqs :
       for cleanones in my_file_contents :
          cleanedseqs.write(cleanones[14:] + '\n')
          f'{cleanones[14 :]}'

