from collections import Counter
str = raw_input('please write some letters:')
counter = Counter(str)
Result = [
('a', counter['a']),
('b', counter['b']),
('c', counter['c']),
('d', counter['d']),
('e', counter['e']),
('f', counter['f']),
('g', counter['g']),
('h', counter['h']),
('i', counter['i']),
('j', counter['j']),
('k', counter['k']),
('l', counter['l']),
('m', counter['m']),
('n', counter['n']),
('o', counter['o']),
('p', counter['p']),
('q', counter['q']),
('r', counter['r']),
('s', counter['s']),
('t', counter['t']),
('u', counter['u']),
('v', counter['v']),
('w', counter['w']),
('x', counter['x']),
('y', counter['y']),
('z', counter['z']),
('A', counter['A']),
('B', counter['B']),
('C', counter['C']),
('D', counter['D']),
('E', counter['E']),
('F', counter['F']),
('G', counter['G']),
('H', counter['H']),
('I', counter['I']),
('J', counter['J']),
('K', counter['K']),
('L', counter['L']),
('M', counter['M']),
('N', counter['N']),
('O', counter['O']),
('P', counter['P']),
('Q', counter['Q']),
('R', counter['R']),
('S', counter['S']),
('T', counter['T']),
('U', counter['U']),
('V', counter['V']),
('W', counter['W']),
('X', counter['X']),
('Y', counter['Y']),
('Z', counter['Z']),
(' ', counter[' '])
]
sorted(Result,key=Counter)
print sorted(Result,key=Counter)

