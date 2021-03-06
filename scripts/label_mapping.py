#!/usr/bin/python
# coding: utf8

LABEL_MAPPING_PREFIX={
  "I": "",
  "II": "",
  "III": "",
  "F1": "", # TODO: what do these codes mean?
  "F2": "",
  "G1": "",
  "G2": "",
  "Cactus": "",
  "Div": "",
  "Ebelin": "",
  "ebelin": "",
  "Ebel": "",
  "Fascino": "",
  "gefülltes": "",
  "Modul": "",
  "Natur": "",
  "Standard": "",
  "standard": "",
  "Sonstige": "",
  "sonstige": "",
  "sonstiges": "",
  "sonst": "",
  'Sonst': '',
  "4er": "",
  "dicke": "",
  "dünne": "",
  "ultra": "",
  'Univ': '',
  'Mini': '',
  "Zw": "", # means "in between" I guess?
  'Deko': 'Dekorative',
  'D': 'Damen',
  'F': 'Damen',
  'H': 'Herren',
  'M': 'Herren',
  'B': 'Baby',
  'K': 'child',
  'KW': 'child',
  'Elektr': 'elektrische',
  'Künstl': 'künstliche',
  'Chem': 'chemische',
  'Med': 'medizinische',
  'Kosm': 'kosmetische',
  'Flüss': 'flüssige',
}

LABEL_MAPPING_SUFFIX={
  '1': '',
  '2': '',
  '4er': '',
  'Standard': '',
  'allgemein': '',
  'S': '',
  'ST': '',
  'Set': '',
  'selbstklebend': '',
  'spezial': '',
  'feucht': '',
  'trocke': '',
  "fest": "",
  "flüssig": "",
  "ultra": "",
  'kbA': '',
  'Mode': '',
  'Natur': '',
  'vorportioniert': '',
  'Prof': '',
  ### TODO below unknown meaning
  'OT': '',
  'UT': '',
  'GP': '',
  'Bhf': '',
  'Mod': '',
}

LABEL_MAPPING_WORD={
  #### acronyms
  'KLKD': 'child clothing',
  'WPR': 'Haushalt item',
  'LM': 'Nahrung',
  'ZC': 'Zahncreme',
  'ZB': 'Zahnbürste',
  'HS': 'Haarschmuck',
  'MS': 'Modeschmuck',
  'HGSM': 'Spühlmittel',
  'MGSM': 'Spühlmittel',
  'HHN': 'Pflegeprodukt', # haut-haare-nase
  'WC': 'Toilette',
  'UWM': 'Waschmittel',
  'SpezialWM': 'Waschmittel',
  'HHfol': 'Haushaltsfolie',
  'FSH': 'Feinstrick Hose',
  #### abbreviations
  'Access': 'Accessoire',
  'Acc': 'Accessoire',
  'artik': 'Artikel',
  'Allzweckr': 'Allzweckreiniger',
  'Allzwe': 'Allzweck',
  'Badean': 'Badeanzug',
  'Beaut': 'Beauty',
  'Belohn': 'Belohnung',
  'Bodenreinige': 'Bodenreiniger',
  'Brotaufstric': 'Brotaufstrich',
  'Brotauf': 'Brotaufstrich',
  'Butterbrotpa': 'Butterbrotpapier',
  'Deotüch': 'Deotücher',
  'Diagn': 'Diagnostik',
  'Einwegrasier': 'Einwegrasierer',
  'Entf': 'Entferner',
  'Faschingsart': 'Faschingsartikel',
  'Fensterdeko': 'Fensterdekoration',
  'flie': 'Stubenfliegen',
  'Fertiggeric': 'Fertiggericht',
  'Fußcre': 'Fußcreme',
  'Frischhaltef': 'Frischhaltefolie',
  'Gebißhaftmit': 'Gebißhaftmittel',
  'Gebißreinige': 'Gebißreiniger',
  'Gesundhe': 'Gesundheit',
  'Getr': 'Getreide',
  'Ges': 'Gesicht',
  'Gefrierbeute': 'Gefrierbeutel',
  'Grußk': 'Grußkarte',
  'Haarent': 'Haarentferner',
  'Haush': 'Haushalt',
  'Haushaltshel': 'Haushaltshelfer',
  'Haushaltsfol': 'Haushaltsfolie',
  'Hunden': 'Hundefutter',
  'Hundenah': 'Hundefutter',
  'Ins': 'Insekten',
  'Insekt': 'Insekten',
  'Kalkrei': 'Kalkreiniger',
  'Katzenna': 'Katzenfutter',
  'Ker': 'Kerze',
  'Kerz': 'Kerze',
  'Kniestr': 'Kniestrümpfe',
  'Kreisla': 'Kreislauf',
  'Kerzengl': 'Kerzenglas',
  'Johanniskrau': 'Johanniskraut',
  'Lufterfrisch': 'Lufterfrischer',
  'Lebensm': 'Lebensmittel',
  'Magn': 'Magnesium',
  'Magnesiu': 'Magnesium',
  'Maschinenpfl': 'Maschinenpflege',
  'Manikü': 'Maniküre',
  'Miner': 'Mineralien',
  'Minera': 'Mineralien',
  'Mott': 'Motten',
  'Nagelackentf': 'Nagelackentferner',
  'Nerv': 'Nerven',
  'Pap': 'Papier',
  'Pflan': 'Pflanzen',
  'Pfl': 'Pflege',
  'Problemlö': 'Problemlöser',
  'Rasie': 'Rasierapparat',
  'Rasiervorber': 'Rasiervorbereitung',
  'Rasierzubeh': 'Rasierzubehör',
  'Rein': 'Reinigung',
  'Saiso': 'Saison',
  'So': 'Sommer',
  'Spezialreini': 'Spezialreiniger',
  'Spülm': 'Spülmittel',
  'Stärk': 'Stärkung',
  'Taschentüche': 'Taschentücher',
  'Tatü': 'Taschentücher',
  'Teelichte': 'Teelichter',
  'Teppichreini': 'Teppichreiniger',
  'Toilettenpap': 'Toilettenpapier',
  'Toipa': 'Toilettenpapier',
  'Traubenzucke': 'Traubenzucker',
  'tro': 'trocken',
  'u': 'und',
  'Vitami': 'Vitamine',
  'Verdau': 'Verdauung',
  'Verba': 'Verbandszeug',
  'Verp': 'Verpackung',
  'Wasserenthär': 'Wasserenthärter',
  'Wi': 'Winter',
  'Zahnfl': 'Zahnfleisch',
  'Zubehö': 'Zubehör',
  'Zubeh': 'Zubehör',
  'Zube': 'Zubehör',
  'Zub': 'Zubehör',
  'Zungenreinig': 'Zungenreiniger',
  'Abwehr': 'Abwehrstärkung',
  'Abwehrstärku': 'Abwehrstärkung',
  'AntiAge': 'Anti Age',
  #### replacements
  'Bonbon': 'Süßigkeiten',
  'Bonbons': 'Süßigkeiten',
  'Coctailservietten': 'Cocktailservietten',
  'Deo': 'Parfüm',
  'Duschbäder': 'Duschgel',
  'Dusche2in1': 'Dusche',
  'Düfte': 'Parfüm',
  'Duft': 'Parfüm',
  'Schorle': 'Spritzer',
  'Feinstrick': 'clothing',
  'Geschenkpaier': 'Geschenkpapier',
  'Grobstrick': 'clothing',
  'Haushaltspap': 'Papier',
  'Hygienepapie': 'Papier',
  'Naturkosmetik': 'Kosmetik',
  'Pull': 'clothing', # TODO: what's the difference between push/pull?
  'Push': 'clothing',
  'SoBri': 'Sonnenbrille',
  'Zwischenverz': 'Nahrung',
  'verz': 'Nahrung',
  'NaWä': 'clothing',
  'TagWä': 'clothing',
  'Konfek': 'clothing',
  'Konf': 'clothing',
  'TKK': 'Produkt',
  #### delete words
  'Jumbopacks': '',
  'Spezialprod': '',
  'div': '',
  'XL': '',
  'Ja': '', # means "some season of the year"
  'klein': '',
  'maxi': '',
  'Maxi': '',
  'midi': '',
  'Prem': '',
  'Spez': '',
  '1tg': '',
  '2tg': '',
  'Zielg': '', # TODO: what does it mean
}

LABEL_MAPPING_REPLACE={
    ## 'assortment':
    'Dekorative Kosmetik': 'Beauty Product',
    'Körperpflege':        'Care Product',
    'Körperreinigung':     'Cleaning Product',
    'Schönheitspa':        'Care Product',
    'Lebensmittel':        'Food',
    'Accessoires':         'Accessory Item',
    'Ostern':              'Easter Accessory',
    'Weihnachten':         'Christmas Accessory',
    'Tier':                'Animal Accessory',
    'Baby':                'Baby Item',
    'Haar':                'Hair Care Product',
    'Haushalt':            'Household Item',
    'Gesundheit':          'Health Care Product',
    'Foto':                'Foto Accessory',
    'Kindertextil':        'Child Clothing',
    'Sonstiges':           'Other Product',
    ## 'area':
    'Posten':                               'Other Product',
    'Alltagshilfen':                        'Accessory Item',
    'Baby glas nahrung':                    'Baby Food',
    'Babypflege':                           'Baby Care Product',
    'Flaschen oder Schnuller':              'Baby Item',
    'Bad':                                  'Bathroom Item',
    'Badaccessoires':                       'Bathroom Item',
    'Beauty oder Maniküre':                 'Beauty Product',
    'GeschenksetSchönheit':                 'Beauty Product',
    'Schönheit':                            'Beauty Product',
    'Vogel':                                'Bird Accessory',
    'Kosmetik Modul':                       'Care Product',
    'Kinderwelt':                           'Child Item',
    'Lekkerland M':                         'Confectionery',
    'Süßigkeiten':                          'Confectionery',
    'Hund':                                 'Dog Accessory',
    'Dekorative Displays':                  'Decoration',
    'dekorative':                           'Decoration',
    'Gesicht':                              'Facial Care Product',
    'Fuß':                                  'Foot Care Product',
    'Hair':                                 'Hair Care Product',
    'Haarpflege':                           'Hair Care Product',
    'Haarstyling':                          'Hairstyling Product',
    'Hand':                                 'Hand Care Product',
    'Pharma':                               'Health Care Product',
    'Reform':                               'Healthy Food',
    'Filter oder Folien':                   'Household Item',
    'Insekten oder Pflanzen':               'Insecticide',
    'Katze':                                'Cat Accessory',
    'Mund oder Zahn':                       'Mouth Care Product',
    'medizinische Pflege':                  'Medicale Care Product',
    'Nagelkosmetik':                        'Nail Cosmetics',
    'Biolebensmittel':                      'Organic Food',
    'Sonstiges oder Te':                    'Other Product',
    'Parfüm':                               'Perfume',
    'Nager':                                'Rodent Control Agent',
    'Dienstleistung':                       'Service Product', # FIXME: not a physical thing
    'Posten oder Saison':                   'Seasonal Item',
    'Nassrasur':                            'Shaving Accessory',
    'Sodastream':                           'Spare Part',
    'Sonne':                                'Sun Protection Item',
    'Lesebrillen und Modul Kontaktlinsen':  'Visual Aid Product',
    ## 'subArea':
    'Aktionen':                   '',
    'frei von':                   '',
    'nicht verwendet':            '',
    'Danke':                      '',
    'Gute Wünsche':               '',
    'Werbeartikel':               '',
    'Megapacks':                  '',
    'Feeling':                    '',
    'Trinksauger':                'Baby Bottle',
    'Milchnahrung':               'Baby Food',
    'Babymenü':                   'Baby Food',
    'Weisse Linie Glas':          'Baby Food',
    'Baby Wäsche':                'Baby Clothing',
    'Einmalbäder':                'Bath Additive',
    'kosmetische Bäder':          'Bath Additive',
    'medizinische Bäder':         'Bath Additive',
    'Bäder':                      'Bathroom Item',
    'Beauty':                     'Beauty Product',
    'No Name Schöheit':           'Beauty Product',
    'Kosmetik':                   'Beauty Product',
    'GeschenksetSchönheit':       'Beauty Product',
    'Schlank Getränke':           'Beverage',
    'Geburt oder Taufe':          'Birthday Accessory',
    'Geburtstag':                 'Birthday Accessory',
    'Kindergeburtstag':           'Birthday Accessory',
    'Ratgeber oder Kinderbuch':   'Book',
    'Haut oder Haare oder N':     'Care Product',
    'Haut oder Insekten':         'Care Product',
    'Pflege':                     'Care Product',
    'Pflegen':                    'Care Product',
    'Kosmetik Pflege':            'Care Product',
    'Apres Pflege':               'Care Product',
    'Katze':                      'Cat Accessory',
    'Kinder Wäsche':              'Child Clothing',
    'Kinder Kleidung':            'Child Clothing',
    'Juniormenü':                 'Child Food',
    'Kindermenü':                 'Child Food',
    'Kinderteller':               'Child Food',
    'Kids oder Junior':           'Child Item',
    'Kosmetik Reinigung':         'Cleaning Product',
    'Reinigen':                   'Cleaning Product',
    'medizinische Reinigung':     'Cleaning Product',
    'Besen oder Bürste':          'Cleaning Product',
    'Kreislauf Chol':             'Circulatory Health Care Product',
    'Verhütung':                  'Contraceptive',
    'Süßwaren':                   'Confectionery',
    'Erkältung':                  'Cold Medicine',
    'Kleber und Basteln':         'Tinker Item',
    'Windelzubehör':              'Diapers Accessory',
    'Windelslips':                'Diapers',
    'Höschenwinde':               'Diapers',
    'Diagnostik':                 'Diagnostic Product',
    'Hund':                       'Dog Accessory',
    'Augenpflege':                'Eye Care Product',
    'Augen m Entferner':          'Eye Make Up Remover',
    'Convenience':                'Food',
    'Zubereitung':                'Food',
    'Lebensmittel':               'Food',
    'Fußpflege':                  'Foot Care Product',
    'Foto':                       'Foto Accessory',
    'Fotogeschenke':              'Foto Accessory',
    'Getreide oder Saat oder Hü': 'Grain',
    'Minikarte':                  'Greeting Card',
    'Maxikarte':                  'Greeting Card',
    'Handpflege':                 'Hand Care Product',
    'Haarschmuck Saison':         'Hair Accessory',
    'Hair':                       'Hair Care Product',
    'Blase oder Niere':           'Health Care Product',
    'Rheuma oder Musk':           'Health Care Product',
    'Beruhig oder Nerven':        'Health Care Product',
    'Aufbau oder Stärkung':       'Health Care Product',
    'Gesundheit':                 'Health Care Product',
    'Reform Kost':                'Healthy Food',
    'Reinigen Haushaltprodukt':   'Household Item',
    'Haushaltshelfer':            'Household Item',
    'Waschen Haushaltprodukt':    'Household Detergent',
    'Inkontinenz':                'Incontinence Health Care Product',
    'Abendbreie':                 'Mash',
    'Breie':                      'Mash',
    'Herren':                     'Men Item',
    'Herrendüfte':                'Men Perfume',
    'Zahnseide oder H':           'Mouth Care Product',
    'Trauer':                     'Mourning Accessory',
    'Nagelkosmetik':              'Nail Cosmetics',
    'Spezialdeos':                'Perfume',
    'Creme Parfüm':               'Perfume',
    'Parfüm':                     'Perfume',
    'Prepaid':                    'Prepaid Card',
    'Pflegeöl':                   'Body Oil',
    'Problemlöser':               'Problem Solver',
    'Nager':                      'Rodent Accessory',
    'Rooibostee':                 'Rooibos Tea',
    'Schuh oder Imprägnierer':    'Shoe Care Product',
    'Sohlen':                     'ShoeSole',
    'Feste Seifen':               'Soap',
    'Saison':                     'Seasonal Item',
    'Selbstbräuner':              'Self Tanning Cream',
    'Media':                      'Storage Media',
    'Süßen oder Ref':             'Sweetener',
    'Magen oder Verdauung':       'Stomach Health Care Product',
    'Würzen':                     'Spices',
    'Sonne Sensitiv':             'Sun Protection Item',
    'Kindersonne':                'Sun Protection Item',
    'Tischdecken':                'Table Cloth',
    'Loser Tee':                  'Tea',
    'Taschentücher':              'Tissue',
    'Damen':                      'Women Item',
    'Damendüfte':                 'Women Perfume',
    'Damenhygiene':               'Women Care Product',
    'Wundheilung':                'Wound Healing Product',
    'Hochzeit':                   'Wedding Accessory',
    'Tücher':                     'Wipe',
    'Tücher oder Schwä':          'Wipe',
    ## 'generalType':
    'Aktionen':                      'Other Product',
    'Danke':                         'Other Product',
    'Sommer Problemlöser':           'Accessory Item',
    'Zubehör':                       'Accessory Item',
    'Pflegen Anti Age':              'Anti Age Care Product',
    'Fußpilz':                       'Athletes Foot Control Agent',
    'Baby Gr clothing':              'Baby Clothing',
    'Baby Na Wä K':                  'Baby Clothing',
    'Baby Tagwä K':                  'Baby Clothing',
    'Babytee':                       'Baby Tea',
    'Mama':                          'Baby Item',
    'Bad oder Kalkreiniger':         'Bathroom Detergent',
    'Badserien':                     'Bathroom Item',
    'Backen':                        'Baking Accessory',
    'Bart':                          'Beard Care Produkt',
    'Bänder':                        'Riboon',
    'Geburtstag Humor':              'Birthday Greeting Card',
    'Geburtstag in Zahlen':          'Birthday Greeting Card',
    'Mitteldecken':                  'Blanket',
    'Blasen':                        'Blisters Control Agent',
    'Figurenkerzen':                 'Candles',
    'Stumpensets':                   'Candles',
    'Eikerzen':                      'Candles',
    'Zubehör Kerzen':                'Candles Accessory',
    'Kerzenglas':                    'Candles Container',
    'French':                        'Care Product',
    'Pflegen Basis':                 'Care Product',
    'Interdental':                   'Care Product',
    'Katzen nass':                   'Wet Cat Food',
    'child Tagwä K':                 'Child Clothing',
    'chemische Haarentferner':       'Chemical Hair Removal',
    'Vor oder Zusatzb':              'Cleaning Product',
    'Reinigen Basis':                'Cleaning Product',
    'Spezialreiniger':               'Cleaning Product',
    'Schuh oder Kleid':              'Clothing',
    'Modullinsen':                   'Contact Lenses',
    'Hornhaut':                      'Cornea Control Agent',
    'Hühneraugen':                   'Corns Control Agent',
    'Watte':                         'Cotton Wool',
    'Cocktailservietten':            'Cocktail Napkins',
    'Schrunden':                     'Cracks Control Agent',
    'Streudeko':                     'Decoration',
    'Desinfektion':                  'Disinfectant',
    'Einweg Dam':                    'Disposable Razor',
    'Einwegrasierer':                'Disposable Razor',
    'Hundefutter trocken':           'Dry Dog Food',
    'Auge':                          'Eye Care Product',
    'Eyeshadow':                     'Eye Make Up',
    'Augen m Entferner':             'Eye Make Up Remover',
    'Kajal oder Liner':              'Eye Pencil',
    'elektrische Rasierapparat':     'Electric Razor',
    'Wimpern':                       'Eyelashes Product',
    'Erotik':                        'Erotic Product',
    'künstliche Nägel Zubehör':      'Fake Nail Accessory',
    'Fußcreme oder gel':             'Foot Care Product',
    'Superfood oder Protein':        'Food',
    'Schlankkost':                   'Food',
    'Foto':                          'Foto Accessory',
    'Figuren':                       'Figurine',
    'Fitneß':                        'Fitness Product',
    'Feeling':                       'Other Product',
    'Schleifen':                     'Gift Wrap Loops',
    'Geschenkverpacung':             'Gift Wrapping',
    'Ge Verpackung':                 'Gift Wrapping',
    'No Name Geschenksets':          'Gift Set',
    'Friesiermittel':                'Hair Care Product',
    'Haarfestiger':                  'Hair Mousse',
    'Gel oder Wachs oder Cr':        'Hairstyling Product',
    'Nahrung Refo':                  'Healthy Food',
    'Sommer Rheu oder Vene':         'Health Care Product',
    'Leber oder Galle':              'Health Care Product',
    'HHReiniger':                    'Household Detergent',
    'Haushalt item Helfer':          'Household Item',
    'Folien':                        'Household Foil',
    'Zubehör Haushaltsfolie':        'Household Foil Accessory',
    'Intimpflege':                   'Intimate Care Product',
    'Insekten flieg':                'Insecticide',
    'Insekten krie':                 'Insecticide',
    'Über oder Unterlacke':          'Jacket',
    'Lippenkosm Pflege':             'Lip Care Product',
    'Lippenkosmetik Zubehör':        'Lip Care Product',
    'Lippe':                         'Lip Care Product',
    'Leggins oder Capri':            'Leggins',
    'Instant Breie':                 'Mash',
    'Pflegen Männer':                'Men Care Product',
    'Herrenpflege':                  'Men Care Product',
    'Herrenduft':                    'Men Perfume',
    'Reinigen Männer':               'Men Cleaning Product',
    'Milben':                        'Mites Control Agent',
    'Motten':                        'Moths Control Agent',
    'Lebensmittel mott':             'Moths Baits',
    'Nagelpflege':                   'Nail Care Product',
    'Nailstripes':                   'Nail Stripes',
    'Sonstiges':                     'Other Product',
    'Dauerwellen':                   'Perms Produkt',
    'Parfüm Sprays':                 'Perfume Spray',
    'Parfüm Stifte':                 'Perfume Pen',
    'Druckstellen':                  'Pressure Marks Control Agent',
    'Premiumkling':                  'Razor Blade',
    'Damenkl':                       'Razor Blade',
    'Chenille':                      'Room Decoration',
    'Raumschmuck':                   'Room Decoration',
    'Nagernahrung':                  'Rodent Food',
    'Nass Rasiera':                  'Safety Razor',
    'Binden':                        'Sanitary Napkin',
    'Rasiergel':                     'Shaving Gel',
    'Rasiervorbereitung':            'Shaving Accessory',
    'Rasierzubehör':                 'Shaving Accessory',
    'Gästeseife oder Badeperle':     'Soap',
    'Pflegen Junge Haut':            'Skin Care Product',
    'Reinigen Junge Haut':           'Skin Cleaning Product',
    'Zubehör Sonnenbrille':          'Sunglasses Accessory',
    'Teefilter':                     'Tea Filter',
    'Teint':                         'Teint Product',
    'Basteln':                       'Tinker Accessory',
    'Kleber und Basteln':            'Tinker Accessory',
    'Zubehör Toilettenpapier':       'Toilet Paper Accessory',
    'Toilette Reinigung oder Pflege':'Toilette Cleaning Product',
    'Konsum Zahncreme':              'Toothpaste',
    'Erwachsen Zahnbürste':          'Toothbrush',
    'Behang Sterne':                 'Tree Decoration',
    'Faltshopper':                   'Umbrella',
    'Erf oder Deotücher':            'Wet Wipes',
    'Damenappa':                     'Women Razor',
    'el Damenapp':                   'Women Razor',
    'Damenduft':                     'Women Perfume',
    'Damenpflege':                   'Women Care Product',
    'Windlichte':                    'Wind Light',
    'Hochzeit Humor':                'Wedding Greeting Card',
    'Hochzeitstag oder Verlobung':   'Wedding Accessory',
    ## generalType:
    'Süßen': 'Sweetener',
    'Lippenpflege': 'Lip Care Product',
    'Abendbreie Gläschen': 'Mash',
}
