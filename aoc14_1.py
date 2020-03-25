tr1 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""
tr2 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
tr3 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

tr = """3 JQFM, 5 QMQB, 20 WQCT => 8 PHBMP
2 XJFQR => 1 WQCT
133 ORE => 3 KFKWH
1 QGVJV, 9 TNRGW, 9 NSWDH => 5 HJPD
4 QMQB, 2 QZMZ, 3 DQPX, 1 HJFV, 5 SLQN, 4 XHKG, 23 DBKL => 5 CVZLJ
6 GFDP, 1 MXQF => 7 TDPN
19 BWHKF, 2 KXHQW, 8 GHNG, 8 CSNS, 8 JVRQ, 1 PHBMP, 20 LZWR, 7 JKRZH => 5 PZRSQ
1 JQFM => 1 QGVJV
8 KFKWH => 7 ZJKB
3 VMDSG, 2 BMSNV => 9 XJFQR
7 ZKZHV => 6 DVRS
1 WKFTZ, 5 SVTK, 1 QDJD => 7 JQFM
19 FRTK => 2 QMTMN
23 DVRS, 3 XNGTQ => 9 MCWF
188 ORE => 3 HDRMK
3 MCWF => 5 LHXN
12 KFKWH, 2 DWBL => 8 ZKZHV
2 GHNG => 8 SVTK
4 MLJN, 9 CSNS => 6 DQPX
2 NDNP, 1 LWGNJ, 6 DBKL, 3 RLKDF, 9 DQPX, 1 BWHKF => 3 JVGRC
4 TNRGW => 2 CFBP
2 KXHQW => 1 BWHKF
7 HJFV => 4 PDKZ
2 QZMZ => 5 BMSNV
1 SVTK, 1 LZWR, 1 WQCT => 3 SLQN
1 TDPN, 1 VMDSG => 7 NHVQD
1 SVTK => 2 LZWR
149 ORE => 9 DWBL
1 XMHN, 1 PDKZ => 5 LWGNJ
6 WCMV => 6 XNGTQ
7 MCWF, 2 VCMPS => 1 HJFV
11 BRTX, 37 CFBP, 2 HJPD, 72 HDRMK, 5 LWGNJ, 7 JVGRC, 3 CVZLJ, 8 PZRSQ, 3 LQBJP => 1 FUEL
9 QMTMN, 14 FRTK, 14 HJFV => 9 NDNP
1 KFKWH, 3 ZJKB => 9 MXQF
1 HJFV, 1 XJFQR => 9 TNRGW
1 DVRS => 2 BRTX
4 QZMZ, 3 BMSNV, 3 GFDP => 6 VMDSG
3 NHVQD => 6 WKFTZ
1 BWHKF => 6 DBKL
8 DWBL => 8 QZMZ
4 MLJN, 16 NSWDH, 4 XHKG => 8 JVRQ
2 DVRS, 32 XNGTQ, 9 MXQF => 7 GHNG
1 DWBL => 8 WCMV
8 SLQN, 1 CFBP => 9 MLJN
1 QDJD => 4 XMHN
3 BWHKF, 2 TNRGW => 9 XHKG
1 WGLN => 8 GFDP
1 MCWF, 1 XJFQR => 2 CSNS
3 XNGTQ => 1 QDJD
15 KXHQW, 3 WQCT, 2 QMTMN => 8 NSWDH
9 XCMJ, 1 QMTMN => 2 JKRZH
4 HDRMK => 4 WGLN
9 NSWDH, 12 LHXN, 16 NDNP => 1 QMQB
16 NHVQD, 3 DWBL, 1 WKFTZ => 4 FRTK
1 GFDP => 2 VCMPS
2 JQFM, 2 XMHN => 6 XCMJ
1 DVRS, 19 QZMZ, 1 DWBL => 5 KXHQW
1 QGVJV, 8 NDNP, 5 PDKZ => 1 RLKDF
29 HJFV, 2 WKFTZ, 4 GFDP => 2 LQBJP"""

text_recipe = tr


def parse_recipes(tr):
    def parse_item(item):
        amount, name = item.split()
        return (int(amount), name)

    recipes = {}

    for line in tr.split('\n'):
        ingredients_text, result_text = line.split('=>')
        ingredients = [parse_item(item) for item in ingredients_text.split(',')]
        amount, result = parse_item(result_text)
        recipes[result] = (ingredients, amount)
    return recipes


def calc_needded_ORE(amount, item, recipes, remainder):
    # print('For {} {}'.format(amount, item))

    if item == 'ORE':
        return (amount, amount)

    ingredients, will_produce = recipes[item]
    set_num = (amount - 1) // will_produce + 1

    ore_needed = 0
    for for_one_set, ingredient in ingredients:
        needed = for_one_set * set_num
        in_stock = remainder.get(ingredient, 0)

        remains = max(in_stock - needed, 0)

        remainder[ingredient] = remains
        needed = max(needed - in_stock, 0)

        ore, actual = calc_needded_ORE(needed, ingredient, recipes, remainder)
        ore_needed += ore
        r = remainder.get(ingredient, 0)
        remainder[ingredient] = r + actual - needed

    return (ore_needed, set_num * will_produce)


if __name__ == '__main__':
    recipes = parse_recipes(text_recipe)

    remainder = {}
    ore, _ = calc_needded_ORE(1, 'FUEL', recipes, remainder)

    print(ore)
