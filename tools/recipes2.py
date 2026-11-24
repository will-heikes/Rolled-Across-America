import os
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "planner.html")
import json, re
p = PAGE
s = open(p, encoding="utf-8").read()
DEG = "°F"

def line(amt, name, note):
    if name == "zest": return f"Zest of {amt}"
    if amt == "pinch": return f"Pinch of {name}"
    if not amt: return name[0].upper() + name[1:] + (f", {note}" if note else "")
    return f"{amt} {name}" + (f", {note}" if note else "")
def inl(amt, name, note):
    if name == "zest": return f"zest of {amt}"
    if amt == "pinch": return f"a pinch of {name}"
    if not amt: return name + (f" ({note})" if note else "")
    return f"{name} ({amt}" + (f", {note}" if note else "") + ")"

def SHAPE(extra=""):
    return ("Roll the dough (1/3 of the batch, about 1 lb) into a 12 x 8 in rectangle. Spread the filling over it, leaving a 1/2-in bare strip along one long edge"
            + (f". {extra}" if extra else "") +
            ". Roll up tightly toward the bare edge, cut into 4 rolls (3 in wide), and set them in a parchment-lined 8-inch pan.")
RISE = "Cover loosely and let rise until noticeably puffy and nearly doubled, about 45-60 min. Rises run faster at altitude, so go by look."
def BAKE(t=350, mins="20-28"):
    return f"Bake at {t}{DEG} ({t-25}{DEG} if convection) for {mins} min, until lightly golden and cooked through (190{DEG} in the center). Cool until warm."

R = {}
def rec(code, groups, steps, note=None, head="Makes 4 large rolls (one 8-inch pan, 1/3 of a dough batch)."):
    items = {}
    out = head + "\n"
    if note: out += note + "\n"
    out += "\nINGREDIENTS"
    for title, lst in groups:
        out += f"\n\n{title}"
        for k, amt, name, nt in lst:
            assert k not in items, (code, k)
            items[k] = inl(amt, name, nt)
            out += "\n" + line(amt, name, nt)
    out += "\n\nSTEPS"
    for i, st in enumerate(steps, 1):
        txt = st.format(**items)
        out += f"\n{i}. {txt}"
    R[code] = out

def I(k, amt, name, note=""): return (k, amt, name, note)
def FILL(b="3 tbsp", sug=("1/3 cup", "brown sugar"), cin="1 tbsp"):
    l = [I("b", b, "butter", "softened"), I("s", sug[0], sug[1])]
    if cin: l.append(I("c", cin, "cinnamon"))
    return l
FS = "Mix the filling: {b}, {s} and {c}."
VG = [I("ps", "3/4 cup", "powdered sugar"), I("gm", "1-2 tbsp", "milk"), I("gv", "1/4 tsp", "vanilla")]
VGS = "Whisk {ps}, {gm} and {gv} into a glaze and drizzle over the rolls."
CCI = [I("cc", "2 oz", "cream cheese", "softened"), I("cb", "1 tbsp", "butter", "softened"), I("cps", "3/4 cup", "powdered sugar"), I("cv", "1/2 tsp", "vanilla"), I("csalt", "pinch", "salt"), I("cm", "1-2 tsp", "milk")]
CCIS = "Beat {cc} and {cb} until smooth, then beat in {cps}, {cv} and {csalt}. Add {cm} to loosen, and spread over the rolls."

rec("MA", [
 ("PASTRY CREAM (make ahead)", [I("milk","1/2 cup","whole milk"), I("yolk","1","egg yolk"), I("pcs","2 tbsp","sugar"), I("corn","1 tbsp","cornstarch"), I("pcb","1 tsp","butter"), I("pcv","1/2 tsp","vanilla")]),
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1 tsp")),
 ("CHOCOLATE GANACHE", [I("choc","2 oz","semisweet chocolate","chopped"), I("cream","3 tbsp","heavy cream")]),
],[
 "At least 2 hours ahead, make the pastry cream: whisk {yolk}, {pcs} and {corn} in a bowl. Heat {milk} until steaming, then slowly whisk it into the yolk mixture. Return it to the pan and cook over medium heat, whisking, until thick, 1-2 min. Off the heat, stir in {pcb} and {pcv}. Press plastic wrap onto the surface and chill.",
 FS, SHAPE(), RISE, BAKE(),
 "Once the rolls are cool, poke a hole in the top of each and pipe in the chilled pastry cream.",
 "Heat {cream} until steaming and pour it over {choc}. Let it sit 2 min, stir until smooth, and spoon over the rolls.",
])

rec("TX", [
 ("GRAPEFRUIT CURD", [I("gj","1/4 cup","grapefruit juice"), I("egg","1","egg"), I("gs","3 tbsp","sugar"), I("gb","1 tbsp","butter")]),
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1/2 tsp") + [I("z","1 grapefruit","zest")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gj2","1 1/2 tbsp","grapefruit juice")]),
 ("TOPPING", [I("curl","","grapefruit zest curls","from the zested grapefruit, made with a zester or vegetable peeler")]),
],[
 "Make the curd: whisk {gj}, {egg}, {gs} and {gb} in a small pan over low heat until thick, about 5 min. Cool.",
 "Mix the filling: {b}, {s}, {c} and {z}.",
 SHAPE("Spread the cooled curd over the filling"), RISE, BAKE(),
 "Whisk {ps} with {gj2} and drizzle over the rolls. Top with {curl}.",
], "LIGHT CINNAMON")

rec("LA", [
 ("FILLING", FILL() + [I("cc","2 oz","cream cheese","softened"), I("ccs","1 tbsp","sugar")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gm","1 1/2 tbsp","milk"), I("gv","1/4 tsp","vanilla or almond extract")]),
 ("TOPPING", [I("sug","1 tbsp each","purple, green and gold sanding sugar")]),
],[
 FS, "Stir {cc} with {ccs}.",
 SHAPE("Dot the cream cheese mixture over the filling"), RISE, BAKE(),
 "Whisk {ps}, {gm} and {gv} and spoon over the rolls. Right away, sprinkle {sug} in stripes. Optional: tuck a small plastic baby into the bottom of one roll.",
])

COCOA = "Uses cocoa dough (chocolate bake)."
rec("OH", [
 ("FILLING", [I("pb","1/3 cup","creamy peanut butter"), I("b","2 tbsp","butter","softened"), I("s","1/4 cup","brown sugar"), I("c","1 tsp","cinnamon")]),
 ("GANACHE", [I("choc","2 oz","semisweet chocolate","chopped"), I("cream","3 tbsp","heavy cream")]),
 ("PEANUT BUTTER DRIZZLE", [I("pb2","2 tbsp","creamy peanut butter"), I("dps","2 tbsp","powdered sugar"), I("dm","1-2 tsp","milk")]),
],[
 "Mix the filling: {pb}, {b}, {s} and {c}.",
 SHAPE(), RISE, BAKE(),
 "Heat {cream} until steaming and pour over {choc}. Let sit 2 min, stir smooth, and spread over the rolls.",
 "Warm {pb2} with {dps} and {dm} until pourable, and drizzle over the ganache.",
], COCOA)

rec("TN", [
 ("FILLING", FILL(sug=("1/4 cup","brown sugar"), cin="1 tsp") + [I("gr","1/3 cup","graham crackers","crushed")]),
 ("TOPPING", [I("mm","1 cup","mini marshmallows"), I("ch","1 1/2 oz","chocolate","melted")]),
],[
 "Mix the filling: {b}, {s}, {c} and {gr}.",
 SHAPE(), RISE, BAKE(),
 "For the last 5 min of baking, scatter {mm} over the rolls (or add them after and torch).",
 "Drizzle {ch} over the top.",
], COCOA)

rec("MS", [
 ("FILLING", FILL(cin="1 tsp") + [I("cocoa","2 tbsp","cocoa powder"), I("chips","1/3 cup","semisweet chocolate","chopped")]),
 ("CHOCOLATE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gc","2 tbsp","cocoa powder"), I("gm","2 tbsp","milk")]),
 ("TOPPING", [I("mm","1/2 cup","mini marshmallows"), I("pec","2 tbsp","pecans","toasted and chopped")]),
],[
 "Mix the filling: {b}, {s}, {cocoa} and {c}. Spread it out, then scatter {chips} over it before rolling.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gc} and {gm} and spread over the rolls.",
 "Top with {mm}, torch until toasted, and sprinkle {pec}.",
], COCOA)

rec("FL", [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("z","3 key limes (or 1 regular lime)","zest"), I("curd","1/4 cup","lime curd")]),
 ("ICING", [I("cc","2 oz","cream cheese","softened"), I("cb","1 tbsp","butter","softened"), I("cps","3/4 cup","powdered sugar"), I("lj","1 tsp","key lime juice")]),
 ("TOPPING", [I("gr","2 tbsp","graham cracker crumbs"), I("z2","","lime zest","to finish")]),
],[
 "Mix {b}, {s} and {z}.",
 SHAPE("Spread {curd} over it"), RISE, BAKE(),
 "Beat {cc} and {cb} smooth, then beat in {cps} and {lj}. Spread over the rolls.",
 "Sprinkle with {gr} and {z2}.",
], "NO CINNAMON")

rec("MO", [
 ("FILLING", FILL()),
 ("GOOEY BUTTER TOPPING", [I("cc","2 oz","cream cheese","softened"), I("gb","2 tbsp","butter","softened"), I("yolk","1","egg yolk"), I("gps","3/4 cup","powdered sugar"), I("gv","1/2 tsp","vanilla")]),
 ("FINISH", [I("dust","1 tbsp","powdered sugar","for dusting")]),
],[
 FS, SHAPE(), RISE,
 "Beat {cc}, {gb}, {yolk}, {gps} and {gv} until smooth, and spoon over the risen rolls.",
 BAKE(), "Dust with {dust}.",
])

rec("VT", [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/4 cup","maple sugar (or brown sugar)"), I("ms","1 tbsp","maple syrup"), I("c","2 tsp","cinnamon")]),
 ("MAPLE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gms","2 tbsp","pure maple syrup"), I("salt","pinch","salt")]),
 ("TOPPING", [I("fs","","flaky salt")]),
],[
 "Mix the filling: {b}, {s}, {ms} and {c}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gms} and {salt}, drizzle over the rolls, and finish with {fs}.",
])

rec("IN", [
 ("FILLING", FILL(cin="1 tsp") + [I("nut","1/4 tsp","nutmeg")]),
 ("SUGAR CREAM", [I("hc","1/3 cup","heavy cream"), I("hs","2 tbsp","sugar")]),
 ("ICING", [I("ps","3/4 cup","powdered sugar"), I("ic","1 1/2 tbsp","heavy cream"), I("iv","1/2 tsp","vanilla")]),
 ("TOPPING", [I("fn","","freshly grated nutmeg")]),
],[
 "Mix the filling: {b}, {s}, {c} and {nut}.",
 SHAPE(), RISE,
 "Stir {hc} with {hs} and pour it into the pan around the risen rolls.",
 BAKE(),
 "Whisk {ps}, {ic} and {iv}, spread over the rolls, and finish with {fn}.",
])

rec("HI", [
 ("PINEAPPLE", [I("pine","1/2 cup","fresh pineapple","finely diced"), I("pb","1 tbsp","butter"), I("pbs","1 tbsp","brown sugar")]),
 ("FILLING", FILL(cin="1/2 tsp")),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("pj","1 1/2 tbsp","pineapple juice")]),
 ("TOPPING", [I("mac","2 tbsp","macadamia nuts","toasted and chopped")]),
],[
 "Cook {pine} with {pb} and {pbs} over medium-high heat until caramelized, 5-6 min. Drain and cool.",
 FS, SHAPE("Scatter the pineapple over it"), RISE, BAKE(),
 "Whisk {ps} with {pj}, drizzle over the rolls, and top with {mac}.",
], "LIGHT CINNAMON")

rec("CA", [
 ("FILLING", FILL(sug=("1/4 cup","brown sugar")) + [I("dates","1/2 cup","Medjool dates (about 5)","pitted and chopped"), I("hw","1 tbsp","hot water")]),
 ("MALTED ICING", [I("ps","3/4 cup","powdered sugar"), I("malt","2 tbsp","malted milk powder"), I("im","2 tbsp","milk"), I("iv","1/2 tsp","vanilla")]),
],[
 "Mash {dates} with {hw} into a rough paste.",
 "Mix the filling: {b}, {s}, {c}, then stir in the date paste.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {malt}, {im} and {iv} and spread over the rolls.",
])

rec("SC", [
 ("FILLING", FILL() + [I("ses","2 tbsp","sesame seeds","toasted")]),
 ("GLAZE", VG),
 ("SESAME BRITTLE", [I("bs","1/4 cup","sugar"), I("bses","2 tbsp","sesame seeds","toasted"), I("salt","pinch","salt")]),
],[
 "Make the brittle: melt {bs} in a dry pan over medium heat until amber, stir in {bses} and {salt}, pour onto parchment, cool, and crack into shards.",
 "Mix the filling: {b}, {s}, {c} and {ses}.",
 SHAPE(), RISE, BAKE(), VGS, "Top with the brittle shards.",
])

SAVB = "Bake at 375" + DEG + " for 22-28 min, until deep golden and 188" + DEG + " in the center. Cool 5 min."
rec("WV", [
 ("FILLING", [I("gb","2 tbsp","butter","melted"), I("garlic","1 small","garlic clove","minced"), I("pep","2 oz","sliced pepperoni (about 30 slices)"), I("mozz","3/4 cup","low-moisture mozzarella","shredded"), I("it","1/4 tsp","Italian seasoning")]),
 ("TOPPING", [I("parm","2 tbsp","Parmesan","grated")]),
],[
 "Stir {garlic} into {gb}.",
 SHAPE("Brush most of the garlic butter over the dough instead of a sweet filling, then layer {pep}, {mozz} and {it}"), RISE,
 "Brush the tops with the rest of the garlic butter and sprinkle {parm}.",
 SAVB,
], "SAVORY, NO CINNAMON")

rec("ID", [
 ("FILLING", [I("b","2 tbsp","butter","softened"), I("garlic","1","garlic clove","minced"), I("chv","1 tsp","chives","chopped"), I("mash","1/2 cup","mashed potato","seasoned"), I("ched","1/2 cup","cheddar","shredded")]),
 ("SOUR CREAM AND CHIVE DRIZZLE", [I("sc","3 tbsp","sour cream"), I("dm","1 tbsp","milk"), I("dch","1 tbsp","chives","chopped"), I("salt","pinch","salt")]),
 ("TOPPING", [I("shal","2 tbsp","crispy fried shallots")]),
],[
 "Mix {b}, {garlic} and {chv}.",
 SHAPE("Use the garlic-herb butter as the base, then spread {mash} and sprinkle {ched}"), RISE, SAVB,
 "Whisk {sc}, {dm}, {dch} and {salt}, drizzle over the rolls, and top with {shal}.",
], "SAVORY, NO CINNAMON")

rec("KY", [
 ("FILLING", FILL() + [I("bour","1 tbsp","bourbon")]),
 ("BOURBON GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gb","1 tbsp","bourbon"), I("gm","1 tbsp","milk")]),
 ("CANDIED WALNUTS", [I("wal","1/4 cup","walnuts"), I("ws","1 tbsp","sugar")]),
],[
 "Toast {wal} with {ws} in a dry pan, stirring, until glossy. Cool and chop.",
 "Mix the filling: {b}, {s}, {c} and {bour}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gb} and {gm}, drizzle over the rolls, and top with the walnuts.",
])

rec("SD", [
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1 tsp") + [I("rhu","1/2 cup","rhubarb","finely chopped"), I("rs","1 tbsp","sugar"), I("rc","1 tsp","cornstarch")]),
 ("KUCHEN CUSTARD", [I("sc","1/4 cup","sour cream"), I("yolk","1","egg yolk"), I("ks","2 tbsp","sugar"), I("kv","1/4 tsp","vanilla")]),
 ("FINISH", [I("dust","1 tbsp","powdered sugar","for dusting")]),
],[
 "Toss {rhu} with {rs} and {rc}.",
 FS, SHAPE("Scatter the rhubarb over it"), RISE,
 "Whisk {sc}, {yolk}, {ks} and {kv} and spoon over the risen rolls.",
 BAKE(), "Dust with {dust}.",
])

rec("PA", [
 ("FILLING", FILL()),
 ("PRETZEL WASH", [I("soda","1 tsp","baking soda"), I("hw","1/2 cup","hot water")]),
 ("SALTED BROWN BUTTER CARAMEL", [I("cb","2 tbsp","butter"), I("cs","1/4 cup","brown sugar"), I("cr","2 tbsp","heavy cream"), I("salt","pinch","salt")]),
 ("TOPPING", [I("ps","1-2 tsp","coarse pretzel salt")]),
],[
 FS, SHAPE(), RISE,
 "Dissolve {soda} in {hw} and brush it generously over the risen rolls for a pretzel-colored crust.",
 BAKE(),
 "Brown {cb} in a small pan, then add {cs}, {cr} and {salt}. Simmer 2 min until smooth.",
 "Spoon the caramel over the rolls and sprinkle {ps}.",
])

rec("DE", [
 ("ROASTED STRAWBERRIES", [I("str","1 cup","strawberries","chopped"), I("ss","1 tbsp","sugar")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1/2 tsp")),
 ("ICING", CCI),
 ("TOPPING", [I("fd","2 tbsp","freeze-dried strawberries","crushed to a powder")]),
],[
 f"Toss {{str}} with {{ss}} and roast at 400{DEG} for 20 min. Cool and mash; you'll use about 1/3 cup.",
 FS, SHAPE("Spread the mashed strawberries over it"), RISE, BAKE(), CCIS, "Dust with {fd}.",
], "LIGHT CINNAMON")

rec("NY", [
 ("FILLING", FILL(cin="2 tsp")),
 ("CHEESECAKE SWIRL", [I("cc","3 oz","cream cheese","softened"), I("cs","2 tbsp","sugar"), I("yolk","1","egg yolk"), I("cv","1/2 tsp","vanilla"), I("lz","1/2 tsp","lemon zest")]),
 ("SOUR CREAM ICING", [I("sc","2 tbsp","sour cream"), I("ps","3/4 cup","powdered sugar"), I("iv","1/2 tsp","vanilla")]),
 ("TOPPING", [I("cr","2","shortbread cookies or graham crackers","crushed")]),
],[
 FS, "Beat {cc}, {cs}, {yolk}, {cv} and {lz} until smooth.",
 SHAPE("Dollop the cheesecake mixture over the filling"), RISE, BAKE(),
 "Whisk {sc}, {ps} and {iv}, spread over the rolls, and sprinkle {cr}.",
])

rec("CT", [
 ("FILLING", [I("tom","1/3 cup","crushed tomatoes"), I("garlic","1","garlic clove","minced"), I("ore","1/2 tsp","dried oregano"), I("pec","1/3 cup","pecorino romano","grated"), I("mozz","1/2 cup","low-moisture mozzarella","optional: classic New Haven tomato pie skips it")]),
 ("TOPPING", [I("oil","1 tbsp","olive oil"), I("pec2","2 tbsp","pecorino romano","grated")]),
],[
 "Simmer {tom} with {garlic} and {ore} until very thick, about 8 min. Cool.",
 SHAPE("Use the tomato as the filling and sprinkle {pec} and {mozz} over it"), RISE,
 "Brush with {oil} and sprinkle {pec2}.",
 f"Bake at 400{DEG} for 20-25 min, until the edges are charred in spots and the center reaches 188{DEG}.",
], "SAVORY, NO CINNAMON")

rec("GA", [
 ("PEACHES", [I("pch","3/4 cup","peaches (fresh or frozen)","diced"), I("ps1","1 tbsp","sugar"), I("pc","1 tsp","cornstarch"), I("nut","pinch","nutmeg")]),
 ("FILLING", FILL()),
 ("OAT CRUMBLE", [I("cf","3 tbsp","flour"), I("co","2 tbsp","oats"), I("cs","2 tbsp","brown sugar"), I("cbut","2 tbsp","cold butter")]),
 ("GLAZE", VG),
],[
 "Cook {pch} with {ps1}, {pc} and {nut} until thick, 4-5 min. Cool.",
 FS, SHAPE("Spoon the peaches over it"), RISE,
 "Rub {cf}, {co}, {cs} and {cbut} together into crumbs and sprinkle over the risen rolls.",
 BAKE(), VGS,
])

rec("WY", [
 ("CHILI BUTTER", [I("b","3 tbsp","butter"), I("chili","2-3 tsp","Chugwater Chili seasoning"), I("bs","1 tsp","brown sugar")]),
 ("FILLING", [I("pj","3/4 cup","pepper jack","shredded"), I("sc","2","scallions","sliced")]),
 ("TOPPING", [I("pj2","1/4 cup","pepper jack","shredded")]),
 ("SOUR CREAM DRIZZLE", [I("sr","3 tbsp","sour cream"), I("dm","1 tbsp","milk"), I("salt","pinch","salt"), I("sc2","1","scallion","sliced")]),
],[
 "Melt {b}, stir in {chili} and cook 1 min to bloom the spices. Stir in {bs} and let cool until spreadable.",
 SHAPE("Use the chili butter as the base, then sprinkle {pj} and {sc}"), RISE,
 SAVB.replace("Cool 5 min.", "For the last 5 min, add {pj2} on top. Cool 5 min."),
 "Whisk {sr}, {dm} and {salt}, drizzle over the rolls, and top with {sc2}.",
], "SAVORY, NO CINNAMON")

rec("NJ", [
 ("FILLING", FILL(cin="1/2 tsp") + [I("taffy","8 pieces","saltwater taffy","chopped (vanilla, molasses or chocolate work best)")]),
 ("GLAZE", VG + [I("fs","","flaky sea salt")]),
 ("TOPPING", [I("taffy2","4 pieces","saltwater taffy","whole")]),
],[
 FS, SHAPE("Scatter {taffy} over it"), RISE, BAKE(),
 "Right out of the oven, press {taffy2} onto the tops so they soften.",
 "Whisk {ps}, {gm} and {gv}, drizzle over the rolls, and finish with {fs}.",
], "LIGHT CINNAMON")

rec("MI", [
 ("COMPOTE", [I("ch","3/4 cup","tart cherries (frozen is fine)"), I("cs","2 tbsp","sugar"), I("cc","2 tsp","cornstarch"), I("lj","1 tsp","lemon juice")]),
 ("FILLING", FILL()),
 ("ALMOND GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gm","1 1/2 tbsp","milk"), I("alm","1/4 tsp","almond extract")]),
 ("TOPPING", [I("sa","2 tbsp","sliced almonds","toasted")]),
],[
 "Cook {ch}, {cs}, {cc} and {lj} until thick, 4-5 min. Cool.",
 FS, SHAPE("Spread about 1/3 cup of the compote over it"), RISE, BAKE(),
 "Whisk {ps}, {gm} and {alm}, drizzle over the rolls, and top with {sa}.",
])

rec("RI", [
 ("FILLING", FILL(cin="2 tsp") + [I("syr","1 tbsp","coffee syrup (Autocrat)")]),
 ("COFFEE MILK GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gsyr","1 1/2 tbsp","coffee syrup (Autocrat)"), I("gm","1 tbsp","milk")]),
 ("TOPPING", [I("esp","pinch","instant espresso powder")]),
],[
 "Mix the filling: {b}, {s}, {c} and {syr}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gsyr} and {gm} into a pale coffee-milk glaze and drizzle over the rolls. Finish with {esp}.",
 "(No coffee syrup? Simmer 1 cup strong brewed coffee with 1/2 cup sugar until reduced to about 1/3 cup, and cool.)",
])

rec("NE", [
 ("APRICOT FILLING", [I("apr","1/2 cup","dried apricots"), I("aw","1/3 cup","water"), I("as","2 tbsp","sugar")]),
 ("FILLING", FILL(sug=("1/4 cup","brown sugar"), cin="1 tsp")),
 ("STREUSEL", [I("sf","3 tbsp","flour"), I("ss","2 tbsp","sugar"), I("sb","1 tbsp","cold butter")]),
 ("ICING", CCI),
],[
 "Simmer {apr} with {aw} and {as} until soft, about 10 min, then blend smooth. Cool.",
 FS, SHAPE("Spread about 1/3 cup of the apricot over it"), RISE,
 "Rub {sf}, {ss} and {sb} into crumbs and sprinkle over the risen rolls.",
 BAKE(), CCIS,
])

rec("ME", [
 ("BLUEBERRIES", [I("bb","1/2 cup","wild blueberries (frozen)"), I("bs","2 tbsp","sugar"), I("bc","2 tsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("OAT CRUMBLE", [I("cf","2 tbsp","flour"), I("co","2 tbsp","oats"), I("cs","1 tbsp","brown sugar"), I("cb","1 tbsp","cold butter")]),
 ("BROWN BUTTER GLAZE", [I("gb","2 tbsp","butter"), I("ps","3/4 cup","powdered sugar"), I("gm","1 tbsp","milk"), I("gv","1/4 tsp","vanilla")]),
],[
 "Cook {bb} with {bs} and {bc} until thick, 3-4 min. Cool.",
 FS, SHAPE("Spread the blueberries over it"), RISE,
 "Rub {cf}, {co}, {cs} and {cb} into crumbs and sprinkle over the risen rolls.",
 BAKE(),
 "Brown {gb}, let it cool slightly, then whisk in {ps}, {gm} and {gv}. Drizzle over the rolls.",
])

rec("MT", [
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp") + [I("jam","1/3 cup","huckleberry jam","or 1/2 cup frozen huckleberries cooked with 2 tbsp sugar and 1 tsp cornstarch")]),
 ("LEMON GLAZE", [I("ps","3/4 cup","powdered sugar"), I("lj","1 1/2 tbsp","lemon juice")]),
 ("TOPPING", [I("hb","","a few whole huckleberries")]),
],[
 FS, SHAPE("Spread {jam} over it"), RISE, BAKE(),
 "Whisk {ps} with {lj}, drizzle over the rolls, and top with {hb}.",
])

rec("UT", [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("h","3 tbsp","honey"), I("s","2 tbsp","brown sugar"), I("c","1 tbsp","cinnamon")]),
 ("HONEY GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gh","1 tbsp","honey"), I("gm","1 tbsp","milk")]),
 ("TOPPING", [I("comb","2 tbsp","honeycomb","in small shards"), I("dh","1 tbsp","honey","for drizzling"), I("fs","","flaky salt")]),
],[
 "Mix the filling: {b}, {h}, {s} and {c}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gh} and {gm} and drizzle over the rolls. Top with {comb}, drizzle {dh}, and finish with {fs}.",
])

rec("IA", [
 ("CORN", [I("corn","1/2 cup","sweet corn kernels"), I("ch","1 tbsp","honey"), I("salt","pinch","salt")]),
 ("FILLING", [I("bb","3 tbsp","butter"), I("s","1/4 cup","brown sugar")]),
 ("BROWN BUTTER STREUSEL", [I("sbb","2 tbsp","butter"), I("sf","3 tbsp","flour"), I("cm","1 tbsp","cornmeal"), I("ss","2 tbsp","brown sugar")]),
 ("CORN-MILK GLAZE", [I("ps","3/4 cup","powdered sugar"), I("milk","1 1/2 tbsp","corn milk (scraped from the cob) or whole milk"), I("gsalt","pinch","salt")]),
],[
 "Blend {corn} into a coarse puree and cook it with {ch} and {salt} for 3 min. Cool.",
 "Brown {bb} and {sbb} in separate small pans. Chill the 2 tbsp for the streusel until firm, and let the 3 tbsp cool until soft.",
 "Mix the softened brown butter with {s}, then stir in the corn.",
 SHAPE(), RISE,
 "Rub {sf}, {cm}, {ss} and the chilled brown butter into crumbs and sprinkle over the risen rolls.",
 BAKE(),
 "Whisk {ps}, {milk} and {gsalt} and drizzle over the rolls.",
], "NO CINNAMON")

rec("AZ", [
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1/2 tsp")),
 ("PRICKLY PEAR ICING", [I("cc","2 oz","cream cheese","softened"), I("cb","1 tbsp","butter","softened"), I("ps","3/4 cup","powdered sugar"), I("pp","1-2 tbsp","prickly pear syrup")]),
 ("TOPPING", [I("fs","","flaky salt")]),
],[
 FS, SHAPE(), RISE, BAKE(),
 "Beat {cc} and {cb} smooth, then beat in {ps} and {pp} until hot pink. Spread over the rolls and finish with {fs}.",
], "LIGHT CINNAMON")

rec("NM", [
 ("FILLING", FILL() + [I("chile","3 tbsp","roasted Hatch green chile (mild or medium)","chopped and patted dry")]),
 ("GREEN CHILE HOT HONEY", [I("h","3 tbsp","honey"), I("hc","1 tbsp","roasted green chile","minced"), I("salt","pinch","salt")]),
 ("TOPPING", [I("pn","2 tbsp","piñon (pine) nuts","toasted")]),
],[
 "Warm {h} with {hc} and {salt}, then let steep 10 min.",
 FS, SHAPE("Scatter {chile} over it"), RISE, BAKE(),
 "Drizzle the hot honey over the rolls and top with {pn}.",
])

rec("KS", [
 ("FILLING", [I("sb","1/4 cup","sunflower seed butter"), I("b","2 tbsp","butter","softened"), I("s","1/4 cup","brown sugar"), I("c","1 tsp","cinnamon"), I("jel","3 tbsp","sand plum jelly (or plum jam)")]),
 ("GLAZE", VG),
 ("CANDIED SUNFLOWER SEEDS", [I("seeds","2 tbsp","sunflower seeds"), I("ss","1 tbsp","sugar")]),
],[
 "Toast {seeds} with {ss} in a dry pan until glossy. Cool.",
 "Mix {sb}, {b}, {s} and {c}. Keep baking soda out of the filling, or the sunflower butter can turn green.",
 SHAPE("Swirl {jel} over it"), RISE, BAKE(), VGS, "Top with the candied seeds.",
])

rec("WA", [
 ("APPLE", [I("apple","1 medium","apple","peeled and finely diced"), I("ab","1 tbsp","butter"), I("as","1 tbsp","brown sugar")]),
 ("FILLING", FILL()),
 ("BROWN BUTTER GLAZE", [I("gb","2 tbsp","butter"), I("ps","3/4 cup","powdered sugar"), I("gm","1 tbsp","milk")]),
 ("TOPPING", [I("cs","1 tsp","cinnamon sugar")]),
],[
 "Cook {apple} with {ab} and {as} until just tender, about 5 min. Cool.",
 FS, SHAPE("Scatter the apple over it"), RISE, BAKE(),
 "Brown {gb}, cool slightly, and whisk in {ps} and {gm}. Drizzle over the rolls and sprinkle {cs}.",
])

rec("NV", [
 ("FILLING", FILL(cin="1 tsp") + [I("z","1 orange","zest"), I("br","1 tbsp","brandy")]),
 ("PICON GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gren","1 tbsp","grenadine"), I("am","1 tbsp","orange amaro (stand-in for Amer Picon) or orange juice")]),
 ("TOPPING", [I("lz","","lemon zest","to finish")]),
],[
 "Mix the filling: {b}, {s}, {c}, {z} and {br}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gren} and {am}, drizzle over the rolls, and finish with {lz}.",
 "(Pine nut version: swap the orange and brandy for 1/3 cup toasted pine nuts, use a honey glaze of 3/4 cup powdered sugar, 1 tbsp honey and 1 tbsp milk, and top with pine nut brittle.)",
])

rec("OR", [
 ("FILLING", FILL(sug=("1/4 cup","brown sugar"), cin="1 tsp") + [I("hz","1/2 cup","hazelnuts","toasted"), I("hs","1 tbsp","sugar")]),
 ("HAZELNUT ICING", [I("cc","2 oz","cream cheese","softened"), I("cb","1 tbsp","butter","softened"), I("ps","3/4 cup","powdered sugar"), I("hx","1/4 tsp","hazelnut extract (or 1 tsp hazelnut liqueur)")]),
 ("TOPPING", [I("hz2","2 tbsp","hazelnuts","toasted and chopped")]),
],[
 "Grind {hz} with {hs} until fine.",
 "Mix the filling: {b}, {s}, {c} and the ground hazelnuts.",
 SHAPE(), RISE, BAKE(),
 "Beat {cc} and {cb} smooth, then beat in {ps} and {hx}. Spread over the rolls and top with {hz2}.",
])

rec("IL", [
 ("FILLING", FILL(cin="1 tsp") + [I("cc","3/4 cup","caramel corn","crushed")]),
 ("SALTED CARAMEL GLAZE", [I("car","3 tbsp","caramel sauce"), I("ps","1/2 cup","powdered sugar"), I("salt","pinch","salt")]),
 ("TOPPING", [I("cc2","1/2 cup","caramel corn","whole pieces"), I("ched","1 tbsp","sharp cheddar","finely grated")]),
],[
 FS, SHAPE("Scatter {cc} over it"), RISE, BAKE(),
 "Whisk {car}, {ps} and {salt} and drizzle over the rolls. Top with {cc2} and {ched} for the Chicago mix.",
])

rec("ND", [
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp") + [I("jel","1/3 cup","chokecherry jelly")]),
 ("GLAZE", VG),
],[
 FS, SHAPE("Spread {jel} over it"), RISE, BAKE(), VGS,
])

SOUR = "Uses sourdough (sourdough bake). Rises take longer: see the dough recipe."
SRISE = "Cover and let rise until about doubled, usually 1 1/2-2 hours for sourdough."
rec("NH", [
 ("FILLING", FILL(cin="1 tsp") + [I("pump","1/3 cup","pumpkin puree"), I("pps","1 1/2 tsp","pumpkin pie spice")]),
 ("ICING", CCI),
 ("CANDIED PEPITAS", [I("pep","2 tbsp","pepitas"), I("ps2","1 tsp","sugar"), I("salt","pinch","salt")]),
],[
 "Toast {pep} with {ps2} and {salt} in a dry pan until they pop. Cool.",
 "Mix the filling: {b}, {s}, {c}, {pump} and {pps}.",
 SHAPE(), SRISE, BAKE(), CCIS, "Top with the pepitas.",
], SOUR)

rec("VA", [
 ("FILLING", [I("b","2 tbsp","butter","softened"), I("ab","1/3 cup","apple butter"), I("s","2 tbsp","brown sugar"), I("c","1 tsp","cinnamon")]),
 ("CIDER GLAZE", [I("cid","1/2 cup","apple cider"), I("ps","3/4 cup","powdered sugar")]),
],[
 "Boil {cid} until reduced to about 2 tbsp. Cool.",
 "Mix the filling: {b}, {ab}, {s} and {c}.",
 SHAPE(), SRISE, BAKE(),
 "Whisk {ps} with the reduced cider and drizzle over the rolls.",
], SOUR)

rec("AK", [
 ("BLUEBERRIES", [I("bb","1/2 cup","wild blueberries (frozen)"), I("bs","1 tbsp","sugar"), I("bc","1 tsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("LEMON GLAZE", [I("ps","3/4 cup","powdered sugar"), I("lj","1 1/2 tbsp","lemon juice"), I("lz","","lemon zest","to finish")]),
],[
 "Cook {bb} with {bs} and {bc} until thick, 3-4 min. Cool.",
 FS, SHAPE("Spread the blueberries over it"), SRISE, BAKE(),
 "Whisk {ps} with {lj}, drizzle over the rolls, and finish with {lz}.",
], SOUR)

rec("NC", [
 ("FILLING", FILL(cin="1 tsp") + [I("sp","1/3 cup","roasted sweet potato","mashed"), I("nut","1/4 tsp","nutmeg"), I("gin","pinch","ground ginger")]),
 ("GLAZED-DOUGHNUT GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gm","2 tbsp","milk"), I("gv","1/2 tsp","vanilla")]),
],[
 "Mix the filling: {b}, {s}, {c}, {sp}, {nut} and {gin}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gm} and {gv} into a thin glaze and pour over the warm rolls.",
])

rec("MD", [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("v","1 tsp","vanilla"), I("c","1/4 tsp","cinnamon")]),
 ("SMITH ISLAND FUDGE ICING", [I("fb","2 tbsp","butter"), I("em","2 tbsp","evaporated milk or heavy cream"), I("fs","2 tbsp","sugar"), I("choc","2 oz","semisweet chocolate","chopped"), I("fv","1/2 tsp","vanilla"), I("salt","pinch","salt")]),
],[
 "Mix the filling: {b}, {s}, {v} and {c}.",
 "Roll the dough (1/3 of the batch) thinner than usual, about 14 x 8 in, so the cut rolls show lots of thin layers like the cake. Spread the filling, roll up very tightly from a long side, cut into 4, and set in a parchment-lined 8-inch pan.",
 RISE, BAKE(),
 "Simmer {fb}, {em} and {fs} for 2 min. Off the heat, stir in {choc}, {fv} and {salt} until glossy. Pour warm over the rolls so it sets shiny.",
], "LIGHT CINNAMON")

rec("OK", [
 ("PECAN PIE GOO", [I("gb","3 tbsp","butter"), I("gs","1/4 cup","brown sugar"), I("cs","2 tbsp","corn syrup or maple syrup"), I("ph","1/3 cup","pecan halves")]),
 ("FILLING", FILL() + [I("pec","1/2 cup","pecans","toasted and chopped")]),
],[
 "Melt {gb} with {gs} and {cs}, pour into the 8-inch pan, and scatter {ph} over it.",
 FS,
 "Roll the dough (1/3 of the batch) into a 12 x 9 in rectangle, spread the filling, and sprinkle {pec} over it. Roll up tightly, cut into 4, and set the rolls on top of the pecan goo.",
 RISE, BAKE(),
 "Right away, run a knife around the edge and turn the pan out onto a plate so the pecan goo ends up on top.",
])

rec("AL", [
 ("LANE FILLING", [I("rai","1/4 cup","raisins"), I("bour","2 tbsp","bourbon"), I("coco","1/4 cup","sweetened shredded coconut"), I("pec","1/4 cup","pecans","chopped")]),
 ("FILLING", FILL(sug=("1/4 cup","brown sugar"), cin="1 tsp")),
 ("SEVEN-MINUTE ICING", [I("ew","1","egg white"), I("is","1/3 cup","sugar"), I("iw","1 tbsp","water"), I("ct","pinch","cream of tartar")]),
],[
 "Soak {rai} in {bour} for 30 min.",
 FS, SHAPE("Scatter the soaked raisins (with any bourbon left), {coco} and {pec} over it"), RISE, BAKE(),
 "In a heatproof bowl over simmering water, whisk {ew}, {is}, {iw} and {ct} for 4-5 min, until thick and glossy with stiff peaks.",
 "Swoop the icing over the cooled rolls. Torch lightly if you like.",
])

rec("MN", [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("card","1 1/2 tsp","ground cardamom (freshly ground is best)"), I("c","1 tsp","cinnamon"), I("z","1/2 orange","zest")]),
 ("TOPPING", [I("egg","1","egg","beaten"), I("pearl","1 tbsp","pearl sugar")]),
 ("LIGHT GLAZE", [I("ps","1/2 cup","powdered sugar"), I("gm","1 tbsp","milk")]),
],[
 "Mix the filling: {b}, {s}, {card}, {c} and {z}.",
 SHAPE(), RISE,
 "Brush the risen rolls with {egg} and sprinkle {pearl}.",
 BAKE(),
 "Whisk {ps} with {gm} and drizzle lightly so the pearl sugar still shows.",
])

rec("AR", [
 ("FILLING", FILL(sug=("1/4 cup","brown sugar"), cin="1 tsp") + [I("pec","1/3 cup","pecans","toasted and finely chopped")]),
 ("POSSUM PIE LAYERS", [I("cc","2 oz","cream cheese","softened"), I("cps","2 tbsp","powdered sugar"), I("cm","1 tbsp","milk"), I("pud","1/3 cup","chocolate pudding (instant is fine)"), I("hc","1/3 cup","heavy cream"), I("wps","1 tbsp","powdered sugar"), I("pec2","1 tbsp","pecans","chopped")]),
],[
 FS, SHAPE("Sprinkle {pec} over it"), RISE, BAKE(),
 "Once the rolls are completely cool, beat {cc} with {cps} and {cm} and spread it over the tops.",
 "Spoon {pud} over the cream cheese layer.",
 "Whip {hc} with {wps} to soft peaks, spread over the pudding, and sprinkle {pec2}. Chill 20 min before serving.",
])

rec("WI", [
 ("FILLING", [I("b","2 tbsp","butter","melted"), I("mus","1 tsp","brown mustard"), I("onion","1 small","onion","thinly sliced"), I("ob","1 tsp","butter"), I("ched","3/4 cup","sharp cheddar","shredded")]),
 ("BEER-MUSTARD GLAZE", [I("gb","1 tbsp","butter","melted"), I("beer","1 tbsp","beer"), I("gmus","1 tsp","brown mustard")]),
 ("TOPPING", [I("ched2","1/4 cup","sharp cheddar","shredded")]),
],[
 "Cook {onion} in {ob} over medium-low heat, stirring now and then, until deep golden, about 20 min. Cool.",
 "Stir {mus} into {b}.",
 SHAPE("Use the mustard butter as the base, then scatter the onion and {ched}"), RISE,
 SAVB.replace("Cool 5 min.", "For the last 5 min, add {ched2} on top."),
 "Whisk {gb}, {beer} and {gmus} and brush over the warm rolls.",
], "SAVORY, NO CINNAMON")

rec("CO", [
 ("FILLING", [I("b","3 tbsp","butter"), I("s","1/4 cup","sugar"), I("h","1 tbsp","honey"), I("salt","pinch","salt")]),
 ("CANTALOUPE CREAM GLAZE", [I("cc","2 oz","cream cheese","softened"), I("ps","1/2 cup","powdered sugar"), I("cant","3 tbsp","cantaloupe puree","strained (frozen in August)")]),
 ("PUEBLO CHILE HOT HONEY", [I("hh","3 tbsp","honey"), I("chile","1 tbsp","roasted Pueblo green chile","minced (frozen in August)")]),
 ("TOPPING", [I("fs","","flaky salt"), I("mint","","fresh mint","optional")]),
],[
 "Brown {b} and let it cool until soft, then mix in {s}, {h} and {salt}.",
 "Warm {hh} with {chile} and let steep 10 min.",
 SHAPE(), RISE, BAKE(),
 "Once the rolls are fully cool, beat {cc} with {ps}, then beat in {cant}. Spread over the rolls (it's a no-cook glaze, so keep it off warm rolls).",
 "Drizzle the Pueblo hot honey over the top and finish with {fs} and {mint}.",
], "NO CINNAMON")

rec("DC", [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("v","1/2 tsp","vanilla"), I("sak","1 tsp","sakura (cherry blossom) powder")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gm","1 1/2 tbsp","milk"), I("gsak","1 tsp","sakura powder (or a few drops of cherry blossom extract)"), I("pink","","a tiny drop of pink coloring","if needed")]),
 ("TOPPING", [I("ss","1 tsp","pink sanding sugar"), I("blos","","salted cherry blossoms","optional, rinsed")]),
],[
 "Mix the filling: {b}, {s}, {v} and {sak}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gm}, {gsak} and {pink} until pale pink, and drizzle over the rolls. Sprinkle {ss} and add {blos}.",
], "NO CINNAMON")

rec("PR", [
 ("FILLING", [I("b","2 tbsp","butter","softened"), I("s","2 tbsp","sugar"), I("c","1/2 tsp","cinnamon"), I("gp","3 oz","guava paste"), I("hw","1 tbsp","hot water"), I("cc","2 oz","cream cheese","softened"), I("cs","1 tbsp","sugar")]),
 ("GUAVA GLAZE", [I("gp2","1 oz","guava paste"), I("gw","1 tbsp","water"), I("ps","1/2 cup","powdered sugar")]),
],[
 "Microwave {gp} with {hw} in 15-second bursts, stirring, until spreadable. Stir {cc} with {cs}.",
 "Mix {b}, {s} and {c}.",
 SHAPE("Spread the guava over it and dot the cream cheese on top"), RISE, BAKE(),
 "Melt {gp2} with {gw}, whisk in {ps}, and drizzle over the rolls.",
])

rec("GU", [
 ("LATIYA CUSTARD (make ahead)", [I("milk","1/2 cup","milk"), I("yolk","1","egg yolk"), I("cs","2 tbsp","sugar"), I("corn","1 tbsp","cornstarch"), I("cv","1/2 tsp","vanilla"), I("cb","1 tsp","butter")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("TOPPING", [I("dust","1 tsp","cinnamon","for dusting")]),
],[
 "At least 2 hours ahead, whisk {yolk}, {cs} and {corn}. Heat {milk} until steaming and slowly whisk it in. Cook in the pan, whisking, until thick, 1-2 min. Off the heat, stir in {cv} and {cb}. Chill covered.",
 FS, SHAPE(), RISE, BAKE(),
 "Spread the chilled custard over the cooled rolls and finish with a heavy dusting of {dust}.",
])

rec("AS", [
 ("FILLING", [I("b","2 tbsp","butter","softened"), I("s","1/4 cup","sugar"), I("c","1/2 tsp","cinnamon")]),
 ("COCONUT SAUCE", [I("cm","3/4 cup","full-fat coconut milk"), I("cs","1/3 cup","sugar"), I("salt","pinch","salt")]),
],[
 FS, SHAPE(), RISE,
 "Simmer {cm}, {cs} and {salt} for 3-4 min, until the sugar dissolves. Pour it into the pan around the risen rolls.",
 f"Bake at 350{DEG} for 30-35 min, until the rolls are golden and the sauce is bubbling and caramelized at the edges. Spoon the sauce over the rolls to serve.",
])

rec("MP", [
 ("MANGO", [I("mango","1/2 cup","mango (fresh or frozen)","finely diced"), I("ms","1 tbsp","sugar"), I("mc","1 tsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1/2 tsp")),
 ("CALAMANSI GLAZE", [I("ps","3/4 cup","powdered sugar"), I("cj","1 1/2 tbsp","calamansi juice (frozen), or half lime and half orange juice")]),
],[
 "Cook {mango} with {ms} and {mc} until thick, 3-4 min. Cool.",
 FS, SHAPE("Spread the mango over it"), RISE, BAKE(),
 "Whisk {ps} with {cj} and drizzle over the rolls.",
], "LIGHT CINNAMON")

rec("VI", [
 ("FILLING", FILL(cin="1/2 tsp") + [I("nut","1/4 tsp","nutmeg")]),
 ("GUAVABERRY GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gl","1 tbsp","guavaberry liqueur (or 2 tbsp guavaberry jam, warmed)"), I("gm","1-2 tsp","milk")]),
],[
 "Mix the filling: {b}, {s}, {c} and {nut}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gl} and {gm} and drizzle over the rolls.",
 "(Backup: a tamarind glaze of 1 tbsp tamarind paste, 3/4 cup powdered sugar and 1 tbsp water.)",
], "LIGHT CINNAMON")

rec("JULY", [
 ("APPLE PIE FILLING", [I("apple","1","apple","peeled and diced"), I("ab","1 tbsp","butter"), I("as","1 tbsp","sugar"), I("ac","1/2 tsp","cinnamon"), I("nut","pinch","nutmeg"), I("lj","1 tsp","lemon juice")]),
 ("FILLING", FILL()),
 ("GLAZE", VG),
 ("TOPPING", [I("rasp","1/4 cup","raspberries"), I("blue","1/4 cup","blueberries")]),
],[
 "Cook {apple} with {ab}, {as}, {ac}, {nut} and {lj} until tender, about 5 min. Cool.",
 FS, SHAPE("Spoon the apple over it"), RISE, BAKE(),
 "Whisk {ps}, {gm} and {gv} and pipe it across the tops in a lattice. Top with {rasp} and {blue} for red, white and blue.",
])

rec("TGIV", [
 ("CRANBERRY", [I("cran","3/4 cup","fresh cranberries (or 1/2 cup whole-berry cranberry sauce)"), I("cs","1/4 cup","sugar"), I("oj","2 tbsp","orange juice")]),
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1 tsp") + [I("z","1 orange","zest")]),
 ("PECAN CRUMBLE", [I("pf","2 tbsp","flour"), I("ps2","2 tbsp","brown sugar"), I("pb","1 tbsp","cold butter"), I("pec","2 tbsp","pecans","chopped")]),
 ("ORANGE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("goj","1 1/2 tbsp","orange juice"), I("gz","","orange zest","to finish")]),
],[
 "Cook {cran} with {cs} and {oj} until the berries pop and it thickens, 6-8 min. Cool. (Skip this if using cranberry sauce.)",
 "Mix the filling: {b}, {s}, {c} and {z}.",
 SHAPE("Spread the cranberry over it"), RISE,
 "Rub {pf}, {ps2}, {pb} and {pec} into crumbs and sprinkle over the risen rolls.",
 BAKE(),
 "Whisk {ps} with {goj}, drizzle over the rolls, and finish with {gz}.",
])

rec("BOOK", [
 ("DOUGH (half batch)", [I("dm","6 tbsp","milk"), I("dw","1/2 cup + 1 tbsp","water"), I("db","5 tbsp","butter","cut into chunks"), I("dfl","3-3 1/4 cups","all-purpose flour","plus extra for dusting"), I("dsa","1/2 tsp","salt"), I("dy","2 tsp","active dry yeast"), I("dsu","6 tbsp","sugar"), I("de","1","large egg")]),
 ("DRIED APPLES", [I("da","1 1/2 cups","dried apples","chopped"), I("cid","1 cup","apple cider (or water)"), I("as","1 tbsp","brown sugar")]),
 ("FILLING", [I("s","2/3 cup","brown sugar","packed"), I("c","3 1/2 tsp","cinnamon"), I("b","4 tbsp","butter","softened")]),
 ("ICING", [I("ps","1 cup","powdered sugar"), I("isalt","pinch","salt"), I("iv","1/4 tsp","vanilla"), I("im","1-1 1/2 tbsp","milk"), I("ib","1 tsp","butter")]),
 ("TOPPING", [I("fl","","edible flowers","optional")]),
],[
 "Friday night, make the dough: heat {dm}, {dw} and {db} to 115-120\u00b0F. The butter doesn't need to melt.",
 "In the mixing bowl, combine 1 1/2 cups of the flour with {dsa}, {dy} and {dsu}.",
 "Add the milk mixture and beat well. Beat in {de}.",
 "Keep beating, adding the rest of the {dfl} as needed, until a soft dough forms. Knead on a floured surface until smooth and satiny, about 5 min.",
 "Cover and refrigerate overnight. (Or, to bake the same day, let it rise until doubled, about 1 1/2-2 hours.)",
 "Simmer {da} with {cid} and {as} until the apples are soft and the liquid is absorbed, 10-15 min. Cool. (You can do this Friday night too.)",
 "Saturday: mix the filling into a paste: {s}, {c} and {b}.",
 "Roll the dough into a 15 x 11 in rectangle, keeping the edges straight. Spread the filling paste over it, leaving a 1/2-in bare strip along one long edge, and scatter the apples over it. Roll up toward the bare edge, pinch to seal, and cut into 9 even rolls. Set them 3 x 3 in a parchment-lined 8-inch square pan.",
 "Cover and let rise until about doubled, about 1-1 1/2 hours (cold dough takes longer).",
 "Bake at 350\u00b0F (metal pan) for 25-35 min, until browned and 188\u00b0F in the center of the middle roll.",
 "While the rolls bake, beat {ps}, {isalt}, {iv}, {ib} and 1 tbsp of the {im} until spreadable, adding the rest of the milk if needed.",
 "Right out of the oven, spread on about half the icing so it melts into the rolls. Once they cool, add the rest and top with {fl} just before serving.",
], "Book club special for Saturday, November 21. Make the dough Friday night.", head="Makes 9 rolls (one 8-inch square pan). Dough included.")
assert len(R) == 59, len(R)

DOUGHR = {
"Base dough": """BASE DOUGH: makes 12 large rolls (3 pans of 4)
Cheryl's Famous Cinnamon Rolls dough, from Mel's Kitchen Cafe. A sponge method, with no set kneading time.

INGREDIENTS
Sponge
1/2 cup granulated sugar
1/2 cup neutral oil
2 cups milk (2% works), scalded and cooled until warm
4 cups all-purpose flour (unbleached)
1 tbsp instant yeast

Dough
3/4 cup all-purpose flour
1/2 tsp baking powder
1/2 tsp baking soda
1 1/2 tsp salt

STEPS
1. Make the sponge: stir the sugar (1/2 cup) and oil (1/2 cup) together in the mixer bowl. Add the scalded milk (2 cups) and mix. Let it sit about 15 min, until warm but not hot.
2. Add the flour (4 cups) and sprinkle the instant yeast (1 tbsp) over the top. Mix until no dry streaks remain. It will be loose and wet. Cover and let it rise until puffy and doubled, 45-60 min.
3. Make the dough: add the flour (3/4 cup), baking powder (1/2 tsp), baking soda (1/2 tsp) and salt (1 1/2 tsp). Mix until smooth and cohesive. There's no set kneading time. Add a little more flour only if it's too sticky to handle; the dough should stay slightly sticky.
4. Move to a lightly greased bowl, cover, and let rise until doubled, about 1 hour. At altitude, check at 40 min.
5. Divide into 3 equal pieces (about 1 lb each), one per pan, and follow each roll's recipe. (For one big batch of 12, roll the whole dough to 18 x 12 in and bake on a parchment-lined half sheet pan at 350\u00b0F for 18-25 min.)

Using active dry yeast: proof it first in a little warm water with a pinch of the sugar until bubbly, then add it to the sponge.""",
"Cocoa dough": """COCOA DOUGH (chocolate bake): the base dough with these changes
1. In the sponge, use 3 1/2 cups flour plus 1/2 cup (45 g) Dutch-process cocoa powder in place of the 4 cups flour.
2. Increase the sugar to 1/2 cup + 2 tbsp.
Everything else is the same.""",
"Sourdough": """SOURDOUGH (sourdough bake): the base dough with these changes
1. Start the day before you bake.
2. Leave out the yeast (or keep 1 tsp as insurance).
3. In the sponge, use 1 1/2 cups milk and 3 1/2 cups flour, and stir in 1 cup (240 g) active, bubbly starter with the milk.
4. Let the sponge ferment until bubbly and doubled, 3-5 hours at room temperature, or overnight in the fridge.
5. Finish the dough as usual (the baking soda tames some of the tang), then rise until doubled, 2-3 hours.
6. After shaping, let the rolls rise 1 1/2-2 hours.""",
}

s, n = re.subn(r'const RECIPE=\{.*?\};\nconst DOUGH_RECIPE=\{.*?\};\n',
               lambda m: "const RECIPE=" + json.dumps(R, ensure_ascii=False) + ";\nconst DOUGH_RECIPE=" + json.dumps(DOUGHR, ensure_ascii=False) + ";\n",
               s, count=1, flags=re.S)
assert n == 1
open(p, "w", encoding="utf-8").write(s)
print("ok")
print(R["MA"]); print("----"); print(R["WY"])
