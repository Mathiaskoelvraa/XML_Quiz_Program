import os
os.chdir('/Users/anderskolvraa/Documents/GitRepos/XML quiz')

os.listdir()

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