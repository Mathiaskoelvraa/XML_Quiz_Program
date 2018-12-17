import os
os.chdir('/Users/anderskolvraa/Documents/GitRepos/XML quiz')

os.listdir()

#hvis der indgår danske bogstaver: aaa= os.listdir()
#print([aaaa.encode('latin_1') for aaaa in aaa])
fil=open('Test of push-pull.txt')

content=fil.read()

print(content)

print(repr(content))

contents=content

contents=contents.replace('\n\t\t','INNERMOST BREAK')

contents=contents.replace('\n\t','MIDDLE BREAK')

contents=contents.replace('\n\n\n','OUTER BREAK')

for stt in contents.split('Sygdom'):
    print(repr(stt[-10:]))

In [119]: contents=content

In [120]: contents=contents.replace('\n\n','OUTER')

In [121]: contents=contents.replace('\n\t\n','OUTER')

In [122]: contents=contents.replace('\n\n\n','OUTER')

dicc=dict()

for elt in contents:
    sp=elt.split('\n\t', maxsplit=1)
    dicc[sp[0]]=sp[1]

def split_to_dict(stt):
    innerdic=dict()
    innerdic["Symptomer"]=stt[len('Symptomer'):stt.find('Diagnostisk')].split('\n\t\t')#.strip(['\n','\t'])
    innerdic["Diagnostisk"]=stt[stt.find('Diagnostisk')+len('Disagnostisk'):stt.find('Behandling')].split('\n\t\t')
    innerdic["Behandling"]=stt[stt.find('Behandling')+len('Behandling'):stt.find('Prognose')].split('\n\t\t')
    innerdic["Prognose"]=stt[stt.find('Prognose')+len('prognose'):].split('\n\t\t')
    return innerdic


def recursinvsplit(stri, splitters):
    if len(splitters)==1:
        liss = stri.split(splitters[0])
        return liss
    liss= stri.split(splitters[0])


In [123]: contents2=contents.split('OUTER')

 contents3=contents2[0]

In [128]: contents3
Out[128]: 'sygdom A\n\tSymptomer\n\t\tA-S1\n\t\tA-S2\n\t\tA-S3\n\t\tA-S4\n\tDiagnostisk\n\t\tA-D1\n\t\tA-D2\n\t\tA-D3\n\t\tA-D4\n\tBehandling\n\t\tA-B1\n\t\tA-B2\n\t\tA-B3\n\t\tA-B4\n\tPrognose\n\t\tA-P1\n\t\tA-P2\n\t\tA-P3\n\t\tA-P4'
contents3 =contents3.replace('\n\t\t','INNER')

In [133]: contents3
Out[133]: 'sygdom A\n\tSymptomerINNERA-S1INNERA-S2INNERA-S3INNERA-S4\n\tDiagnostiskINNERA-D1INNERA-D2INNERA-D3INNERA-D4\n\tBehandlingINNERA-B1INNERA-B2INNERA-B3INNERA-B4\n\tPrognoseINNERA-P1INNERA-P2INNERA-P3INNERA-P4'

In [134]: contents4=contents3.split('\n\t')

In [135]: contents4
Out[135]:
['sygdom A',
 'SymptomerINNERA-S1INNERA-S2INNERA-S3INNERA-S4',
 'DiagnostiskINNERA-D1INNERA-D2INNERA-D3INNERA-D4',
 'BehandlingINNERA-B1INNERA-B2INNERA-B3INNERA-B4',
 'PrognoseINNERA-P1INNERA-P2INNERA-P3INNERA-P4']

