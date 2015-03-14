ludevít
-------

ludevít číta štandardní vstup v UTF-8 kódovaní a kovertuje spisovnú slovenčinu
na štúrovskú.

Požjadavki
----------
* python versia aspon 2.3

Inštalacia
----------
Inštalacia užíva distutils, stačí napísať
python setup.py install

Užívaňje
--------
Bez ďalších parametrou ludevít číta štandardní vstup a vístup
zapisuje na štandardní vístup.
Ak je ako parameter meno súboru, program číta tento súbor namjesto
štandardnjeho vstupu.

Vístup je možno modifikovať ďalšimí argumentamí k programu:

-o súbor alebo --output-file súbor - vístup zapíše do súboru mjesto na štadardní vístup
-D alebo --nfkd - vístup buďe v NFKD normalizácii
-d alebo --nfkd-hack - písmeni ď a ť budú v NFKD normalizácii, ostatnje v NFKC
-e ENCODING alebo --encoding ENCODING - mjesto štandardnjeho koduvaňja utf-8,
   predpokladaj vstup a vístup v koduvaňí ENCODING, ktoruo muože biť hocijaké
   koduvaňje podporovanuo pythonom, ale pravďepodobňe víznam má len jedno
   z utf-8, iso8859_2, cp1250, cp852 alebo mac_latin2. 
   Koduvaňja inuo ňež utf-8 ňje je kompatibilnuo s volbamí -D a -d.

Víznam parametra -d
-------------------
Kďe sa zvuki mekko vislovujú takjeto sa zmekčujúcou čjarkou viznačujú, ale
písmeni „d“ a „t“ ju v dobe modernej inakšje označujú, značka táto skoro ako
dlhá čjarka má podobu. 

Abi sme historickú vernosť zachovali, normalizujeme tjeto dve písmeni na
unicodovskí „NFKD“ spuosob, to značí že zmekčujúce čjarki sú ako samostatnje
kombinujúce písmeni (combining characters, kombinierende diakritische Zeichen)
reprezentovanje, keď sa s predchádzajúcou písmenou vjažu, zrjedka bíva
implementovaná úplná podpora kombinujúcich písmen, a tak sa často písmena nad
predchádzajúcou ňezmeňená zobrazí, čo vizerá temer ako puovodní historickí
spuosob písaňja. Žjal, ňjektorje renderovacie sistemi alebo tjeto čjarki zle
zobrazujú, alebo naopak tak ako má čjarku s písmenou skombinujú dobre a ináč
zobrazja, a teda tento spuosob ňje vždi dobrje vísledki dáva.
