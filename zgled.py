import requests
import orodja
import  re

zgreseni = 0
zgreseni2 = 0
slovar = []
slovar2 = []
#for i in range(0,167):
#    orodja.pripravi_imenik(f'zajeti_podatki/{i+1}. stran')
#    orodja.shrani_spletno_stran(f'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=detailed&sort=desc&page={i}', f'zajeti_podatki/{i+1}. stran.html')
for i in range (0,167):
    with open(f'zajeti_podatki/{i + 1}. stran.html', encoding='utf8') as f:
        vsebina = f.read()

        vzorec = (
        r'<span class="title numbered">\n' #začetek
        r'\s*(?P<stevilka>\d+.)\n' #zaporedna številka igre
        r'\s*</span>\n' #filc
        r'\s*\n'
        r'\s*<a href="(?P<url_do_igre>/game/(?P<konzola>.*)/.*)" class="title">\n' # url za kasneje, ga bo treba kombinitati z www.metascore.com
        r'\s*.*\n'
        r'\s*(?P<naslov>\w.*)\n' # naslov
        r'\s*.*\n' # filc h3
        r'\s*.*\n' #filc a
        r'\s*' # filc blank
        r'.*\n' #filc clamp
        r'\s*\n' # filc blank
        r'\s*<span>(?P<Datum_izdaje>.+)<.*\n' #datum izdaje
        r'\s*\n'
        r'\s*\n'
        r'\s*.*\n'
        r'\s*\n'
        r'\s*<div class="summary">\s*\n'
        r'\s*(?P<povzetek>.*)\n'
        )

        vzorec2 = (
            r'<div class="metascore_w large.*?>(?P<Metascore>.*)<(.*\n){8}<div class="metascore_w user.*>(?P<ocena_uporabnikov>.*)<'
            
        )

    
    stevec = 0
    
    stevec2 = 0
    for zadetek in re.finditer(vzorec, vsebina):
        #print(zadetek.groupdict())
        stevec += 1
        slovar.append(zadetek.groupdict())
    
    print(stevec)

    for zadetek in re.finditer(vzorec2,vsebina):
        
        slovar2.append(zadetek.groupdict())
        stevec2 += 1 

    zgreseni += 100 - stevec
    
    print(stevec2)
    zgreseni2 += 100 - stevec2
    
orodja.zapisi_json(slovar, 'jsoni\podatki.json')
orodja.zapisi_csv(slovar, slovar[1].keys(), f'csvji\podatki.csv')
orodja.zapisi_json(slovar2, 'jsoni\ocene.json')
orodja.zapisi_csv(slovar2, slovar2[1].keys(), f'csvji\ocene.csv')
print(zgreseni)
print(zgreseni2)
