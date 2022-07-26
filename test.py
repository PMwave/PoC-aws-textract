

with open('data/'+'texte-manuscrit'+'/'+'constat'+'/output_'+'constatbleubrouillon.pdf'+'.txt', 'r') as f:
    n = f.readlines()

for k in range(len(n)):
    if n[k] == 'NOT_SELECTED\n':
        print(n[k])