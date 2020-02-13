import requests
import orodja as oro
import  re
import csv
import json




#for i in range (1,1468):
#    oro.shrani_spletno_stran(f'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&appid=730#p{i}_price_desc', f'zajeti_podatki/{i}_stran.html')

for i in range (1, 1469):
    with open(f'zajeti_podatki/{i}_stran.html', encoding='utf8') as f:
        vsebina = f.read()


    vzorec1 = (
    r'class="market_listing_item_name" style="color: (.*?);">(\w+)?\s?\|?\s?(\w+\s?\w*?)?(\((.*?)\))?</span>'
    )
    vzorec2 = (
    r'span class="market_listing_num_listings_qty" data-qty="(\d+)">'
    )
    zadetki1 = re.findall(vzorec1, vsebina)
    zadetki2 = re.findall(vzorec2, vsebina)
    print(zadetki1, zadetki2)








