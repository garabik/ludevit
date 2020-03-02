#!/usr/bin/python
# -*- coding: UTF-8 -*-


table_voc = {
'^zámen'        : '^všemen',
'^zámena$'      : '^zámena$',
'^náreč'        : '^rozličnoreč',
'^prípon'       : '^prívesk',
'^prípon$'      : '^prívesák$',
'^skloňovan'    : '^sklonen',
'^slabik'       : '^silab',
'^slabík'       : '^siláb',

'^kokot'        : '^paloš',
'^penis'        : '^paloš',
'^hovno$'       : '^výkal$',
'predseda$'     : 'predsedatel$',
'predsed'       : 'predsedatel',
'predsedu$'     : 'predsedatela$',
'prezident'     : 'mocnár',
'^kurv'         : '^pobehlic',
'^kurvy$'       : '^pobehlice$',
'^kurve$'       : '^pobehlici$',
'^kuriev$'      : '^pobehlíc$',


'grék'          : 'rék',
'gréc'          : 'réc',
'gréč'          : 'réč',
'maďar$'        : 'uher$',
'maďar'         : 'uhr',
'maďarsk'       : 'uhersk',
'maďara'        : 'uhra',
'talian'        : 'talyan',

'^ľudovít'      : '^ludëvít',
'slávneho'      : 'slávnjëho',

# pieseň -> peseň
'^pies'         : '^pes',

'vidieť$'       : 'videť$',
'vedieť$'       : 'vedeť$',
'vedie'         : 'vede',
'erie$'         : 'ere$',
'erieš$'        : 'ereš$',
'^zmenši'       : '^umenši',
'^zmenší'       : '^umenší',
'^použ'         : '^už',
'^zača'         : '^započa',
'^začn'         : '^započn',

'^prv$'         : '^prú$',
'^najprv$'      : '^najprú$',
'^najsamprv$'   : '^najsamíprú$',
'^veď$'         : '^veť$',
'^nech$'        : '^nach$',
'^necha'        : '^nacha',
'^nechá'        : '^nachá',
'^takmer$'      : '^tëmer$',
'^ten$'         : '^tën$',
'^tento$'       : '^tënto$',
'^lásk$'        : '^lask$',
'^kto$'         : '^kdo$',
'^dakto$'       : '^dakdo$',
'^daktor'       : '^dakdor',
'^niekto$'      : '^volakdo$',
'^ktosi$'       : '^kdosi$',
'^nikto$'       : '^nikdo$',
'^avšak$'       : '^ašak$',
'^aspoň$'       : '^aspon$',
'^vzájom'       : '^vzájem',
'možné$'        : 'možnuo$',

'jeden'         : 'jedën',
'^teda$'        : '^tëda$',
'^tejto'        : '^tëjto',
'^tej$'         : '^tëj$',
'teror'         : 'tëror',
'telef'         : 'tëlef',
'telev'         : 'tëlev',
'ex'            : 'ëx',
'ix'            : 'yx',
'politi'        : 'polity',
'^inciden'      : '^incidën',
'^veľvyslanc'   : '^posl',
'^veľvyslanec$' : '^posol$',
'^veľvyslanect' : '^posolst',
'disk'          : 'dysk',
'feder'         : 'fedër',
'mini'          : 'miny',
'diana'         : 'dyana',
'partner'       : 'partnër',
'strateg'       : 'stratëg',
'detail'        : 'dëtail',
'^tím'          : '^tým',
'lingvistic'    : 'lingvistyc',
'lingvistik'    : 'lingvistyk',
'^opozi'        : '^oppozi',
'^opozí'        : '^oppozí',
'identi'        : 'ydënty',
'univerz'       : 'unyvers',
'internet'      : 'intërnët',
'diplom'        : 'dyplom',
'automati'      : 'automaty',
'tex'           : 'tëx',
'foneti'        : 'fonëty',
'geneti'        : 'genëty',
'moder'         : 'modër',
'defin'         : 'dëfin',
'teoreti'       : 'tëorety',
'mónie$'        : 'monyy$',
'mónia$'        : 'monya$',
'móniou$'       : 'monyou$',
'mónii$'        : 'monyy$',
'atentát'       : 'atëntát',
'katedr'        : 'katëdr',
'online'        : 'onlajn',
'^tel$'         : '^tël$',
'alter'         : 'altër',
'systém'        : 'system',
'digi'          : 'dygi',
'reuters'       : 'reutërs',
'matemati'      : 'matëmaty',
'informati'     : 'informaty',

# europske unie a podobne
'^úni'          : '^uny',
'milión'        : 'milion',
'miliar'        : 'milyar',

'^vonkajš'      : '^vňešn',
'^vonkajšia'    : '^vňešná',
'^pripom'       : '^prípom',

'^budapeš'      : '^peš',
'^angli'        : '^engli',
'^chorvá'       : '^horvá',
'^bratislavsk'  : '^prešporsk',

# ak sa zmeni rod, budu zle pripadne adjektiva
# ale toto je prils casty pripad tak ho dame ako vynimka
# s tym, ze nejake adjektiva sa tu nepouzivaju az tak casto
'^bratislava$'  : '^prešporok$',
'^bratislavy$'  : '^prešporku$',
'^bratislave$'  : '^prešporku$',
'^bratislavu$'  : '^prešporok$',

}

table_ort = {
'ov$'          : 'ou$',
'né$'          : 'ňje$',
'é$'           : 'je$',
'ého$'         : 'jeho$',
'ému$'         : 'jemu$',
'é'            : 'e',
'ý'            : 'í',
'y'            : 'i',
'ô'            : 'uo',
'ľ'            : 'l',
'ä'            : 'e',
'ë'            : 'e',

'ia'           : 'ja',
'dia'          : 'ďja',
'diakon'       : 'diakon',
'tia'          : 'ťja',
'nia'          : 'ňja',
'lia'          : 'lá',

'ľali'         : 'lali',
'júli'         : 'júli',

'ie'           : 'je',
'die'          : 'ďje',
'tie'          : 'ťje',
'nie'          : 'ňje',
'nie$'         : 'ňja$',
'^nie'         : '^ňje',

'iu'           : 'ju',
'diu'          : 'ďju',
'tiu'          : 'ťju',
'niu'          : 'ňju',

'al$'          : 'au$',
'il$'          : 'iu$',
'ol$'          : 'ou$',
'el$'          : 'eu$',
'ul$'          : 'uv$',
'iel$'         : 'jeu$',
'til$'         : 'ťiu$',
'dil$'         : 'ďiu$',
'nil$'         : 'ňiu$',
'tel$'         : 'ťeu$',
'del$'         : 'ďeu$',
'nel$'         : 'ňeu$',

'de'           : 'ďe',
'te'           : 'ťe',
'ne'           : 'ňe',
'del$'         : 'ďeu$',
'nel$'         : 'ňeu$',

'di'           : 'ďi',
'ti'           : 'ťi',
'ni'           : 'ňi',

'dí'           : 'ďí',
'tí'           : 'ťí',
'ní'           : 'ňí',

'iá'           : 'ijá',

# pravdepodobne pridavne mena
'dí$'           : 'dí$',
'tí$'           : 'tí$',
'ní$'           : 'ní$',

# vynimka - dlhe e v slove Rek, Recki
'^rék'          : '^rék',
'^réc'          : '^réc',
'^réč'          : '^réč',

# genitiv pluralu zenskych podstatnych mien
'iek$'          : 'ák$',

'ami$'          : 'amí$',
'imi$'          : 'imí$',
'ími$'          : 'imí$',
'ými$'          : 'imí$',

'acov'          : 'acuv',
'ažov'          : 'ažuv',
'slov'          : 'slov',

'^strán$'       : '^stran$',
'^tieto$'       : '^tjeto$',
'^títo$'        : '^títo$',
'^tích$'        : '^tích$',
'^tíchto$'      : '^tíchto$',
'^tí$'          : '^tí$',

'nej$'          : 'nej$',

'^posol$'       : '^posol$',
'^idol$'        : '^idol$',
'^popol$'       : '^popol$',
'zmysel$'       : 'zmisel$',
'^výkal$'       : '^víkal$',
'^poézi'        : '^poesi',
'^verzi'        : '^versi',
'^inštaláci'    : '^inštalaci',

}

def postprocess(t):
    if t.startswith('sloven') or t.startswith('vláda'):
        t = t.capitalize()
    return t

