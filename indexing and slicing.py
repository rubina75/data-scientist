Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='TECHNOLOGYANDINNOVATION'
a[2:5:]
'CHN'
a[19:12:-1]
'TAVONNI'
a[-4:-11:-1]
'TAVONNI'
a[4:10:]
'NOLOGY'
a[0:4:], a[6:10:]
('TECH', 'LOGY')
a='computer'
a[0]
'c'
a[-8]
'c'
>>> a='computer '
>>> a[8]
' '
>>> a[0:4:1]
'comp'
>>> a[4:0:-1]
'upmo'
>>> a[-4:-8:-1]
'tupm'
>>> a[5::]
'ter '
>>> a[4]
'u'
>>> a[4::]
'uter '
>>> a='TECHNOLOGYANDINNOVATION'
>>> a[0:4]+' of '+a[6:10]
'TECH of LOGY'
>>> a='computer'
>>> len(a)
8
>>> a='TECHNOLOGYANDINNOVATION'
>>> len(a)
23
>>> a.index('D')
12
>>> a.index('T')
0
>>> a='PROGRAMMINGWITHPYTHON'
>>> a[4:6:]+'H'
'RAH'
>>> a[15:17]+a[11:14]
'PYWIT'
>>> a[15:17]+a[11:14]
'PYWIT'
>>> a[11:15]+' OF '+a[0:3]
'WITH OF PRO'
>>> a[3:8]
'GRAMM'
