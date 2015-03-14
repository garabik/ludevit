#!/usr/bin/python
# -*- coding: UTF-8 -*-



table_voc = {
u'^zámen'        : u'^všemen',
u'^zámena$'      : u'^zámena$',
u'^náreč'        : u'^rozličnoreč',
u'^prípon'       : u'^prívesk',
u'^prípon$'      : u'^prívesák$',
u'^skloňovan'    : u'^sklonen',
u'^slabik'       : u'^silab',
u'^slabík'       : u'^siláb',

u'^kokot'        : u'^paloš',
u'^penis'        : u'^paloš',
u'^hovno$'       : u'^výkal$',
u'predseda$'     : u'predsedatel$',
u'predsed'       : u'predsedatel',
u'predsedu$'     : u'predsedatela$',
u'prezident'     : u'mocnár',
u'^kurv'         : u'^pobehlic',
u'^kurvy$'       : u'^pobehlice$',
u'^kurve$'       : u'^pobehlici$',
u'^kuriev$'      : u'^pobehlíc$',


u'grék'          : u'rék',
u'gréc'          : u'réc',
u'gréč'          : u'réč',
u'maďar$'        : u'uher$',
u'maďar'         : u'uhr',
u'maďarsk'       : u'uhersk',
u'maďara'        : u'uhra',
u'talian'        : u'talyan',

u'^ľudovít'      : u'^ludëvít',
u'slávneho'      : u'slávnjëho',

# pieseň -> peseň
u'^pies'         : u'^pes',

u'vidieť$'       : u'videť$',
u'vedieť$'       : u'vedeť$',
u'vedie'         : u'vede',
u'erie$'         : u'ere$',
u'erieš$'        : u'ereš$',
u'^zmenši'       : u'^umenši',
u'^zmenší'       : u'^umenší',
u'^použ'         : u'^už',
u'^zača'         : u'^započa',
u'^začn'         : u'^započn',

u'^prv$'         : u'^prú$',
u'^najprv$'      : u'^najprú$',
u'^najsamprv$'   : u'^najsamíprú$',
u'^veď$'         : u'^veť$',
u'^nech$'        : u'^nach$',
u'^necha'        : u'^nacha',
u'^nechá'        : u'^nachá',
u'^takmer$'      : u'^tëmer$',
u'^ten$'         : u'^tën$',
u'^tento$'       : u'^tënto$',
u'^lásk$'        : u'^lask$',
u'^kto$'         : u'^kdo$',
u'^dakto$'       : u'^dakdo$',
u'^daktor'       : u'^dakdor',
u'^niekto$'      : u'^volakdo$',
u'^ktosi$'       : u'^kdosi$',
u'^nikto$'       : u'^nikdo$',
u'^avšak$'       : u'^ašak$',
u'^aspoň$'       : u'^aspon$',
u'^vzájom'       : u'^vzájem',
u'možné$'        : u'možnuo$',

u'jeden'         : u'jedën',
u'^teda$'        : u'^tëda$',
u'^tejto'        : u'^tëjto',
u'^tej$'         : u'^tëj$',
u'teror'         : u'tëror',
u'telef'         : u'tëlef',
u'telev'         : u'tëlev',
u'ex'            : u'ëx',
u'ix'            : u'yx',
u'politi'        : u'polity',
u'^inciden'      : u'^incidën',
u'^veľvyslanc'   : u'^posl',
u'^veľvyslanec$' : u'^posol$',
u'^veľvyslanect' : u'^posolst',
u'disk'          : u'dysk',
u'feder'         : u'fedër',
u'mini'          : u'miny',
u'diana'         : u'dyana',
u'partner'       : u'partnër',
u'strateg'       : u'stratëg',
u'detail'        : u'dëtail',
u'^tím'          : u'^tým',
u'lingvistic'    : u'lingvistyc',
u'lingvistik'    : u'lingvistyk',
u'^opozi'        : u'^oppozi',
u'^opozí'        : u'^oppozí',
u'identi'        : u'ydënty',
u'univerz'       : u'unyvers',
u'internet'      : u'intërnët',
u'diplom'        : u'dyplom',
u'automati'      : u'automaty',
u'tex'           : u'tëx',
u'foneti'        : u'fonëty',
u'geneti'        : u'genëty',
u'moder'         : u'modër',
u'defin'         : u'dëfin',
u'teoreti'       : u'tëorety',
u'mónie$'        : u'monyy$',
u'mónia$'        : u'monya$',
u'móniou$'       : u'monyou$',
u'mónii$'        : u'monyy$',
u'atentát'       : u'atëntát',
u'katedr'        : u'katëdr',
u'online'        : u'onlajn',
u'^tel$'         : u'^tël$',
u'alter'         : u'altër',
u'systém'        : u'system',
u'digi'          : u'dygi',
u'reuters'       : u'reutërs',
u'matemati'      : u'matëmaty',
u'informati'     : u'informaty',



# europske unie a podobne
u'^úni'          : u'^uny',
u'milión'        : u'milion',
u'miliar'        : u'milyar',


u'^vonkajš'      : u'^vňešn',
u'^vonkajšia'    : u'^vňešná',
u'^pripom'       : u'^prípom',

u'^budapeš'      : u'^peš',
u'^angli'        : u'^engli',
u'^chorvá'       : u'^horvá',
u'^bratislavsk'  : u'^prešporsk',

# ak sa zmeni rod, budu zle pripadne adjektiva
# ale toto je prilis casty pripad tak ho dame ako vynimka
# s tym, ze nejake adjektiva sa tu nepouzivaju az tak casto
u'^bratislava$'  : u'^prešporok$',
u'^bratislavy$'  : u'^prešporku$',
u'^bratislave$'  : u'^prešporku$',
u'^bratislavu$'  : u'^prešporok$',

}

table_ort = {
u'ov$'          : u'ou$',
u'né$'          : u'ňje$',
u'é$'           : u'je$',
u'ého$'         : u'jeho$',
u'ému$'         : u'jemu$',
u'é'            : u'e',
u'ý'            : u'í',
u'y'            : u'i',
u'ô'            : u'uo',
u'ľ'            : u'l',
u'ä'            : u'e',
u'ë'            : u'e',

u'ia'           : u'ja',
u'dia'          : u'ďja',
u'diakon'       : u'diakon',
u'tia'          : u'ťja',
u'nia'          : u'ňja',
u'lia'          : u'lá',

u'ľali'         : u'lali',
u'júli'         : u'júli',

u'ie'           : u'je',
u'die'          : u'ďje',
u'tie'          : u'ťje',
u'nie'          : u'ňje',
u'nie$'         : u'ňja$',
u'^nie'         : u'^ňje',

u'iu'           : u'ju',
u'diu'          : u'ďju',
u'tiu'          : u'ťju',
u'niu'          : u'ňju',

u'al$'          : u'au$',
u'il$'          : u'iu$',
u'ol$'          : u'ou$',
u'el$'          : u'eu$',
u'ul$'          : u'uv$',
u'iel$'         : u'jeu$',
u'til$'         : u'ťiu$',
u'dil$'         : u'ďiu$',
u'nil$'         : u'ňiu$',
u'tel$'         : u'ťeu$',
u'del$'         : u'ďeu$',
u'nel$'         : u'ňeu$',


u'de'           : u'ďe',
u'te'           : u'ťe',
u'ne'           : u'ňe',
u'del$'         : u'ďeu$',
u'nel$'         : u'ňeu$',



u'di'           : u'ďi',
u'ti'           : u'ťi',
u'ni'           : u'ňi',

u'dí'           : u'ďí',
u'tí'           : u'ťí',
u'ní'           : u'ňí',

u'iá'           : u'ijá',

# pravdepodobne pridavne mena
u'dí$'           : u'dí$',
u'tí$'           : u'tí$',
u'ní$'           : u'ní$',

# vynimka - dlhe e v slove Rek, Recki
u'^rék'          : u'^rék',
u'^réc'          : u'^réc',
u'^réč'          : u'^réč',

# genitiv pluralu zenskych podstatnych mien
u'iek$'          : u'ák$',

u'ami$'          : u'amí$',
u'imi$'          : u'imí$',
u'ími$'          : u'imí$',
u'ými$'          : u'imí$',


u'acov'          : u'acuv',
u'ažov'          : u'ažuv',
u'slov'          : u'slov',

u'^strán$'       : u'^stran$',
u'^tieto$'       : u'^tjeto$',
u'^títo$'        : u'^títo$',
u'^tích$'        : u'^tích$',
u'^tíchto$'      : u'^tíchto$',
u'^tí$'          : u'^tí$',

u'nej$'          : u'nej$',

u'^posol$'       : u'^posol$',
u'^idol$'        : u'^idol$',
u'^popol$'       : u'^popol$',
u'zmysel$'       : u'zmisel$',
u'^výkal$'       : u'^víkal$',
u'^poézi'        : u'^poesi',
u'^verzi'        : u'^versi',
u'^inštaláci'    : u'^inštalaci',

}

def postprocess(t):
    if t.startswith(u'sloven') or t.startswith(u'vláda'):
        t = t.capitalize()
    return t
