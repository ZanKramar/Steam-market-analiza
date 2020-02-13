import requests
import orodja as oro
import  re
import csv
import json
seznam = []
vzorec = (r'\s*<span class="label">Developer:</span>\n'
         r'\s*<span class="data">\s*\n'
         r' \s*(?P<Zaloznik>\w+)\s*.*\n'
         )

vzorec1 =(r' \s+<li class="summary_detail product_genre"><span.* class="label".*<span class="data" >(?P<zanr1>\w+\s?-?\w*)</span>.*<span class="data" >(?P<zanr2>\w+\s?-?\w*)</span>.*\s*\n'
         )

vzorec2 =(r'\s*<span class="label"># of players:</span>\n \s*<span class="data">(.+?)</span>')

vzorec3 = (r'<span class="label">Rating:</span>\n \s*<span class="data" >(?P<esbr>\w*)</span>'
)

slovar =[]
for i in range(16688):
    with open(f'{i+1}_igra.html', encoding='utf8') as f:
            vsebina = f.read()
    umesni = {}
    for zadetek1 in re.finditer(vzorec, vsebina):
            umesni.update(zadetek1.groupdict())

    for zadetek2 in re.finditer(vzorec1,vsebina):
        umesni.update(zadetek2.groupdict())

    for zadetek3 in re.finditer(vzorec2, vsebina):
        umesni.update(zadetek3.groupdict())

    for zadetek4 in re.finditer(vzorec3, vsebina):
        umesni.update(zadetek4.groupdict())    
    print(umesni)
    print(i)
    slovar.append(umesni)
oro.zapisi_json(slovar, 'jsoni\igre.json')
oro.zapisi_csv(slovar, slovar[1].keys(), f'csvji\igre.csv')




#my_file = open('csvji/podatki.csv', mode='r', errors = 'ignore')
#parsed_data = csv.reader(my_file)
#for row in parsed_data:
#    if row != []:
#
#        seznam.append(row)
#print(seznam)
#seznam_url = []
#for i in seznam:
#    seznam_url.append(i[1])



#stevec = 16700
#u = 1
#for i in seznam_url:
#    oro.shrani_spletno_stran(f'https://www.metacritic.com{i}', f'{u}_igra.html', vsili_prenos=False)
#    print(u)
#    u = u+1
#print('opravljeno')

