listaCord = [(1, 2), (3, 4), (5, 6)]

print(listaCord[1][2])

somax = listaCord[0][0] + listaCord[1][0] + listaCord[2][0]
somay = listaCord[0][1] + listaCord[1][1] + listaCord[2][1]

mediax = somax / 3
mediay = somay / 3

tuplaMedia = (mediax, mediay)

print(tuplaMedia)