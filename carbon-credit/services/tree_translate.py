TREE_SPECIES_TO_EN = {
    "สัก": "Teak",
    "ยูคาริปตัส": "Eucalyptus",
    "กระถินเทพา": "Acacia mangium",
    "กระถินณรงค์": "Earleaf acacia",
    "กระถินยักษ์": "giant acacia",
    "โกงกาง": "Loop-root mangrove",
    "ยางพารา": "Pará rubber tree",
    "ปาล์มน้ำมัน": "Oil palms",
    "พรรณไม้พื้นเมืองโตช้า": "Slow local growing tree",
    "พรรณไม้อเนกประสงค์": "Multipurpose plants",
    "พรรณไม้ปลูกในเมือง": "Urban plants"
}

TREE_SPECIES_TO_TH = {
    "Teak": "สัก",
    "Eucalyptus": "ยูคาริปตัส",
    "Acacia mangium": "กระถินเทพา",
    "Earleaf acacia": "กระถินณรงค์",
    "giant acacia": "กระถินยักษ์",
    "Loop-root mangrove": "โกงกาง",
    "Pará rubber tree": "ยางพารา",
    "Oil palms": "ปาล์มน้ำมัน",
    "Slow local growing tree": "พรรณไม้พื้นเมืองโตช้า",
    "Multipurpose plants": "พรรณไม้อเนกประสงค์",
    "Urban plants": "พรรณไม้ปลูกในเมือง"
}

def trans_list(tree_list: list):
    res = []
    for tree in tree_list:
        try:
            res.append(TREE_SPECIES_TO_EN[tree])
        except:
            pass
    return res

def filter_plant(tree_list: list):
    res = []
    for tree in tree_list:
        try:
            temp = (TREE_SPECIES_TO_EN[tree])
            res.append(tree)
        except:
            pass
    return res