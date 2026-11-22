# Alternate-flavor recipes. Executed inside the recipes2.py namespace (rec, I, FILL, VG, ... available).
def A(code, name): return code + "|" + name

rec(A("MA","Cranberry Bog"), [
 ("CRANBERRY", [I("cran","3/4 cup","fresh cranberries"), I("crs","1/4 cup","sugar"), I("oj","2 tbsp","orange juice")]),
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1 tsp") + [I("z","1 orange","zest")]),
 ("ORANGE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("goj","1 1/2 tbsp","orange juice")]),
 ("SUGARED CRANBERRIES", [I("scr","1/4 cup","fresh cranberries"), I("ssug","2 tbsp","sugar")]),
],[
 "The night before, rinse {scr}, roll them while damp in {ssug}, and let dry on parchment.",
 "Cook {cran} with {crs} and {oj} until the berries pop and it thickens, 6-8 min. Cool.",
 "Mix the filling: {b}, {s}, {c} and {z}.",
 SHAPE("Spread the cranberry over it"), RISE, BAKE(),
 "Whisk {ps} with {goj}, drizzle over the rolls, and top with the sugared cranberries.",
])

rec(A("NJ","Highbush Blueberry"), [
 ("BLUEBERRIES", [I("bb","1/2 cup","blueberries (fresh or frozen)"), I("bs","2 tbsp","sugar"), I("bc","2 tsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("LEMON GLAZE", [I("ps","3/4 cup","powdered sugar"), I("lj","1 1/2 tbsp","lemon juice")]),
 ("TOPPING", [I("fb","2 tbsp","fresh blueberries")]),
],[
 "Cook {bb} with {bs} and {bc} until thick, 3-4 min. Cool.",
 FS, SHAPE("Spread the blueberries over it"), RISE, BAKE(),
 "Whisk {ps} with {lj}, drizzle over the rolls, and top with {fb}.",
])

rec(A("NJ","Jersey Crumb Bun"), [
 ("FILLING", [I("b","3 tbsp","butter"), I("s","1/4 cup","brown sugar"), I("c","1 tsp","cinnamon")]),
 ("CRUMB TOPPING", [I("cf","1/2 cup","flour"), I("cs","1/4 cup","brown sugar"), I("csug","2 tbsp","sugar"), I("cc","1/2 tsp","cinnamon"), I("salt","pinch","salt"), I("cb","4 tbsp","butter","melted")]),
 ("FINISH", [I("dust","1 tbsp","powdered sugar","for dusting")]),
],[
 "Brown {b} and let it cool until soft. Mix in {s} and {c}.",
 "Make the crumb: stir {cf}, {cs}, {csug}, {cc} and {salt}, then pour in {cb} and toss with a fork into big clumps.",
 SHAPE(), RISE,
 "Press the crumb thickly over the tops of the risen rolls. A Jersey crumb bun should be mostly crumb.",
 BAKE(), "Dust with {dust}.",
])

rec(A("NJ","Rainbow Cookie"), [
 ("FILLING", [I("ap","1/3 cup","almond paste","grated"), I("b","3 tbsp","butter","softened"), I("s","2 tbsp","sugar"), I("ax","1/4 tsp","almond extract"), I("jam","1/4 cup","raspberry jam")]),
 ("CHOCOLATE GLAZE", [I("choc","2 oz","semisweet chocolate","chopped"), I("cream","3 tbsp","heavy cream")]),
 ("TOPPING", [I("spr","2 tsp","red and green sprinkles")]),
],[
 "Beat {ap}, {b}, {s} and {ax} until smooth.",
 SHAPE("Spread {jam} over the almond filling"), RISE, BAKE(),
 "Heat {cream} until steaming and pour over {choc}. Let sit 2 min, stir smooth, and spread over the rolls.",
 "Sprinkle with {spr} for the tricolor look.",
], "NO CINNAMON")

rec(A("NV","Pine Nut"), [
 ("FILLING", [I("b","3 tbsp","butter"), I("s","1/3 cup","brown sugar"), I("c","1 tsp","cinnamon"), I("pn","1/3 cup","pine nuts")]),
 ("HONEY GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gh","1 tbsp","honey"), I("gm","1 tbsp","milk")]),
 ("PINE NUT BRITTLE", [I("bs","1/4 cup","sugar"), I("bpn","2 tbsp","pine nuts"), I("salt","pinch","salt")]),
],[
 "Toast {pn} in a dry pan until golden, about 3 min. Chop half.",
 "Brown {b} and let it cool until soft. Mix in {s}, {c} and the toasted pine nuts.",
 "Make the brittle: melt {bs} in a dry pan until amber, stir in {bpn} and {salt}, pour onto parchment, cool, and crack.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gh} and {gm}, drizzle over the rolls, and top with brittle shards.",
])

rec(A("NV","Strawberries & Champagne"), [
 ("ROASTED STRAWBERRIES", [I("str","1 cup","strawberries","chopped"), I("ss","1 tbsp","sugar")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1/2 tsp")),
 ("CHAMPAGNE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("champ","1 1/2 tbsp","champagne or sparkling wine")]),
 ("TOPPING", [I("spark","1 tsp","coarse sparkling sugar")]),
],[
 "Toss {str} with {ss} and roast at 400" + DEG + " for 20 min. Cool and mash.",
 FS, SHAPE("Spread the mashed strawberries over it"), RISE, BAKE(),
 "Whisk {ps} with {champ}, drizzle over the rolls, and sprinkle {spark}.",
], "LIGHT CINNAMON")

rec(A("TX","Czech Kolache"), [
 ("FILLING", [I("b","2 tbsp","butter","softened"), I("s","2 tbsp","sugar"), I("c","1/2 tsp","cinnamon"), I("pop","1/2 cup","poppy seed filling (canned)")]),
 ("SWEET CHEESE", [I("cc","3 oz","cream cheese","softened"), I("ccs","2 tbsp","sugar"), I("yolk","1","egg yolk"), I("lz","1/2 tsp","lemon zest")]),
 ("POSYPKA CRUMB", [I("pf","2 tbsp","flour"), I("pps","2 tbsp","sugar"), I("pb","1 tbsp","cold butter")]),
],[
 "Mix {b}, {s} and {c}.",
 "Beat {cc}, {ccs}, {yolk} and {lz} until smooth.",
 SHAPE("Spread {pop} over it"), RISE,
 "Spoon the sweet cheese on top of each risen roll. Rub {pf}, {pps} and {pb} into crumbs and sprinkle over the cheese.",
 BAKE(),
])

rec(A("TX","Dr Pepper"), [
 ("DR PEPPER SYRUP", [I("dp","2 cups","Dr Pepper")]),
 ("FILLING", FILL() + [I("all","1/4 tsp","ground allspice")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gv","1/4 tsp","vanilla")]),
 ("TOPPING", [I("cher","4","maraschino cherries")]),
],[
 "Boil {dp} in a wide pan until reduced to about 1/3 cup of syrup, 15-20 min. Cool.",
 "Mix the filling: {b}, {s}, {c}, {all} and 1 tbsp of the syrup.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gv} and about 2 tbsp of the syrup into a glaze and spoon over the rolls. Top each with one of the {cher}.",
])

rec(A("LA","Bananas Foster"), [
 ("BANANAS", [I("ban","1 ripe","banana","diced"), I("bb","1 tbsp","butter"), I("bs","1 tbsp","brown sugar"), I("rum","1 tbsp","dark rum")]),
 ("FILLING", FILL()),
 ("RUM GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gr","1 tbsp","dark rum"), I("gm","1 tbsp","milk")]),
],[
 "Cook {ban} with {bb} and {bs} for 2 min, add {rum}, and cook 1 min more. Cool.",
 FS, SHAPE("Spoon the bananas over it"), RISE, BAKE(),
 "Whisk {ps}, {gr} and {gm} and drizzle over the rolls.",
])

rec(A("HI","Lilikoi"), [
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1/2 tsp")),
 ("LILIKOI BUTTER ICING", [I("ib","2 tbsp","butter","softened"), I("ps","3/4 cup","powdered sugar"), I("pf","1 1/2 tbsp","passion fruit puree")]),
 ("TOPPING", [I("mac","2 tbsp","macadamia nuts","toasted and chopped")]),
],[
 FS, SHAPE(), RISE, BAKE(),
 "Beat {ib} with {ps}, then beat in {pf}. Spread over the rolls and top with {mac}.",
], "LIGHT CINNAMON")

rec(A("HI","Haupia"), [
 ("HAUPIA (make ahead)", [I("cm","1/2 cup","full-fat coconut milk"), I("hs","2 tbsp","sugar"), I("corn","1 1/2 tbsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1/2 tsp")),
 ("TOPPING", [I("coco","2 tbsp","sweetened shredded coconut","toasted")]),
],[
 "At least 2 hours ahead, whisk {cm}, {hs} and {corn} in a small pan and cook, stirring, until very thick, 3-4 min. Chill.",
 FS, SHAPE(), RISE, BAKE(),
 "Spread the chilled haupia over the cooled rolls and sprinkle {coco}.",
], "LIGHT CINNAMON")

rec(A("MD","Old Bay Caramel"), [
 ("FILLING", FILL() + [I("ob","1/2 tsp","Old Bay seasoning")]),
 ("SALTED CARAMEL", [I("cb","2 tbsp","butter"), I("cs","1/4 cup","brown sugar"), I("cr","2 tbsp","heavy cream"), I("salt","pinch","salt")]),
 ("TOPPING", [I("ob2","pinch","Old Bay seasoning")]),
],[
 "Mix the filling: {b}, {s}, {c} and {ob}.",
 SHAPE(), RISE, BAKE(),
 "Melt {cb} with {cs}, {cr} and {salt}, and simmer 2 min until smooth.",
 "Spoon the caramel over the rolls and finish with {ob2}.",
])

rec(A("WA","Seattle Espresso"), [
 ("FILLING", FILL(cin="2 tsp") + [I("esp","2 tsp","instant espresso powder")]),
 ("COFFEE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("cof","1 1/2 tbsp","strong brewed coffee")]),
 ("TOPPING", [I("nibs","1 tbsp","cacao nibs")]),
],[
 "Mix the filling: {b}, {s}, {c} and {esp}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps} with {cof}, drizzle over the rolls, and sprinkle {nibs}.",
])

rec(A("WV","Ramp"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("ramps","1/2 cup","ramps","finely chopped (or 2 green onions plus 1 garlic clove)"), I("salt","pinch","salt")]),
 ("TOPPING", [I("parm","2 tbsp","Parmesan","grated"), I("fs","","flaky salt")]),
],[
 "Mix {b}, {ramps} and {salt} into ramp butter.",
 SHAPE("Use the ramp butter as the filling"), RISE,
 "Sprinkle the risen rolls with {parm}.",
 SAVB, "Finish with {fs}.",
], "SAVORY, NO CINNAMON")

rec(A("WV","Black Walnut"), [
 ("FILLING", FILL() + [I("bw","1/2 cup","black walnuts","chopped")]),
 ("BROWN BUTTER GLAZE", [I("gb","2 tbsp","butter"), I("ps","3/4 cup","powdered sugar"), I("gm","1 tbsp","milk")]),
 ("TOPPING", [I("bw2","2 tbsp","black walnuts","toasted and chopped")]),
],[
 FS, SHAPE("Scatter {bw} over it"), RISE, BAKE(),
 "Brown {gb}, cool slightly, and whisk in {ps} and {gm}. Drizzle over the rolls and top with {bw2}.",
])

rec(A("WV","Buckwheat"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("bh","3 tbsp","buckwheat honey"), I("s","2 tbsp","brown sugar"), I("c","2 tsp","cinnamon")]),
 ("BROWN BUTTER GLAZE", [I("gb","2 tbsp","butter"), I("ps","3/4 cup","powdered sugar"), I("gm","1 tbsp","milk")]),
],[
 "Mix the filling: {b}, {bh}, {s} and {c}.",
 SHAPE(), RISE, BAKE(),
 "Brown {gb}, cool slightly, and whisk in {ps} and {gm}. Drizzle over the rolls.",
])

rec(A("PA","Shoofly"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","brown sugar"), I("mol","2 tbsp","molasses"), I("c","2 tsp","cinnamon")]),
 ("CRUMB TOPPING", [I("cf","1/3 cup","flour"), I("cs","3 tbsp","brown sugar"), I("cc","1/4 tsp","cinnamon"), I("cb","2 tbsp","cold butter")]),
],[
 "Mix the filling: {b}, {s}, {mol} and {c}.",
 SHAPE(), RISE,
 "Rub {cf}, {cs}, {cc} and {cb} into crumbs and sprinkle thickly over the risen rolls.",
 BAKE(),
], "Plain base dough: skip the pretzel wash for this version.")

rec(A("NY","Black & White Cookie"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("v","1 tsp","vanilla"), I("lz","1/2 tsp","lemon zest"), I("c","1/2 tsp","cinnamon")]),
 ("BLACK AND WHITE ICING", [I("ps","1 cup","powdered sugar"), I("cs","1 tbsp","light corn syrup"), I("gm","1-2 tbsp","milk"), I("gv","1/2 tsp","vanilla"), I("cocoa","1 tbsp","cocoa powder"), I("choc","1 oz","semisweet chocolate","melted")]),
],[
 "Mix the filling: {b}, {s}, {v}, {lz} and {c}. Like the cookie, it's a vanilla-lemon base.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {cs}, {gv} and {gm} into a thick, smooth icing. Split it in half.",
 "Stir {cocoa} and {choc} into one half, adding a few drops of milk if it gets too thick.",
 "Once the rolls are cool, ice one half of each roll with the vanilla icing and the other half with the chocolate.",
], "LIGHT CINNAMON")

rec(A("CT","Election Cake"), [
 ("FILLING", FILL(cin="1 tsp") + [I("cur","1/3 cup","dried currants"), I("br","2 tbsp","brandy"), I("nut","1/4 tsp","nutmeg"), I("mace","1/4 tsp","ground mace")]),
 ("BRANDY GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gb","1 tbsp","brandy"), I("gm","1 tbsp","milk")]),
],[
 "Soak {cur} in {br} for 30 min.",
 "Mix the filling: {b}, {s}, {c}, {nut} and {mace}.",
 SHAPE("Scatter the soaked currants over it"), RISE, BAKE(),
 "Whisk {ps}, {gb} and {gm} and drizzle over the rolls.",
], "Sweet roll: bake at the sweet-roll temperature, not the savory one.")

rec(A("NE","Kool-Aid"), [
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1/2 tsp")),
 ("TANGY CREAM CHEESE BASE", CCI),
 ("KOOL-AID GLAZE", [I("kps","3/4 cup","powdered sugar"), I("ka","1 tsp","unsweetened tropical punch Kool-Aid mix"), I("km","1-2 tbsp","milk")]),
],[
 FS, SHAPE(), RISE, BAKE(), CCIS.replace("spread over the rolls", "spread a thin layer over the rolls"),
 "Whisk {kps}, {ka} and {km} into a bright red glaze and drizzle over the cream cheese.",
], "LIGHT CINNAMON")

rec(A("AL","Blackberry Bramble"), [
 ("FILLING", FILL(cin="1 tsp") + [I("jam","1/3 cup","blackberry jam")]),
 ("STREUSEL", [I("sf","3 tbsp","flour"), I("ss","2 tbsp","brown sugar"), I("sb","1 tbsp","cold butter")]),
 ("BUTTERMILK GLAZE", [I("ps","3/4 cup","powdered sugar"), I("bm","1 1/2 tbsp","buttermilk"), I("gv","1/4 tsp","vanilla")]),
],[
 FS, SHAPE("Spread {jam} over it"), RISE,
 "Rub {sf}, {ss} and {sb} into crumbs and sprinkle over the risen rolls.",
 BAKE(),
 "Whisk {ps}, {bm} and {gv} and drizzle over the rolls.",
])

rec(A("UT","Raspberry Jell-O"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("v","1/2 tsp","vanilla")]),
 ("JELL-O GLAZE", [I("jello","1 tbsp","raspberry Jell-O powder"), I("hw","2 tbsp","hot water"), I("ps","3/4 cup","powdered sugar")]),
 ("WHIPPED CREAM ICING", [I("hc","1/3 cup","heavy cream"), I("wps","1 tbsp","powdered sugar")]),
 ("TOPPING", [I("fd","1 tbsp","freeze-dried raspberries","crushed")]),
],[
 "Mix the filling: {b}, {s} and {v}.",
 SHAPE(), RISE, BAKE(),
 "Dissolve {jello} in {hw}, whisk in {ps}, and spoon over the cooled rolls.",
 "Whip {hc} with {wps} to soft peaks, dollop on top, and sprinkle {fd}.",
], "NO CINNAMON")

rec(A("UT","Bear Lake Raspberry"), [
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp") + [I("jam","1/3 cup","raspberry jam")]),
 ("RASPBERRY CREAM GLAZE", [I("cc","2 oz","cream cheese","softened"), I("ps","3/4 cup","powdered sugar"), I("gj","1 tbsp","raspberry jam"), I("gm","1 tsp","milk")]),
 ("TOPPING", [I("rasp","1/4 cup","fresh raspberries")]),
],[
 FS, SHAPE("Spread {jam} over it"), RISE, BAKE(),
 "Beat {cc} with {ps}, {gj} and {gm} until smooth. Spread over the rolls and top with {rasp}.",
])

rec(A("WY","Chokecherry"), [
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp") + [I("jel","1/3 cup","chokecherry jelly")]),
 ("GLAZE", VG),
],[
 FS, SHAPE("Spread {jel} over it"), RISE, BAKE(), VGS,
], "Sweet roll: bake at the sweet-roll temperature, not the savory one.")

rec(A("NM","Biscochito"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("c","1 tbsp","cinnamon"), I("anise","1 tsp","anise seed","lightly crushed")]),
 ("CINNAMON SUGAR CRUST", [I("mb","1 tbsp","butter","melted"), I("ts","2 tbsp","sugar"), I("tc","1 tsp","cinnamon")]),
],[
 "Mix the filling: {b}, {s}, {c} and {anise}.",
 SHAPE(), RISE, BAKE(),
 "While the rolls are warm, brush with {mb} and sprinkle with {ts} mixed with {tc}, like a biscochito. No glaze.",
])

rec(A("KS","Sunflower"), [
 ("FILLING", [I("sb","1/4 cup","sunflower seed butter"), I("b","2 tbsp","butter","softened"), I("s","1/4 cup","brown sugar"), I("c","1 tsp","cinnamon")]),
 ("GLAZE", VG),
 ("CANDIED SUNFLOWER SEEDS", [I("seeds","2 tbsp","sunflower seeds"), I("ss","1 tbsp","sugar")]),
],[
 "Toast {seeds} with {ss} in a dry pan until glossy. Cool.",
 "Mix {sb}, {b}, {s} and {c}. Keep baking soda out of the filling, or the sunflower butter can turn green.",
 SHAPE(), RISE, BAKE(), VGS, "Top with the candied seeds.",
])

rec(A("KS","Wheat Harvest"), [
 ("FILLING", [I("b","3 tbsp","butter"), I("s","1/3 cup","brown sugar"), I("c","1 tsp","cinnamon")]),
 ("TOASTED WHEAT CRUMBLE", [I("wf","3 tbsp","whole wheat flour"), I("ws","2 tbsp","brown sugar"), I("wb","2 tbsp","cold butter")]),
 ("HONEY GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gh","1 tbsp","honey"), I("gm","1 tbsp","milk")]),
],[
 "Brown {b} and let it cool until soft. Mix in {s} and {c}.",
 "Toast {wf} in a dry pan until nutty, 2-3 min. Cool, then rub in {ws} and {wb} to make crumbs.",
 SHAPE(), RISE, "Sprinkle the crumble over the risen rolls.", BAKE(),
 "Whisk {ps}, {gh} and {gm} and drizzle over the rolls.",
])

rec(A("AR","Tontitown Grape"), [
 ("FILLING", FILL(cin="1/2 tsp") + [I("jam","1/3 cup","Concord grape jam")]),
 ("CRUMBLE", [I("sf","3 tbsp","flour"), I("ss","2 tbsp","sugar"), I("sb","1 tbsp","cold butter")]),
 ("GRAPE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gj","1 1/2 tbsp","Concord grape juice")]),
],[
 FS, SHAPE("Spread {jam} over it"), RISE,
 "Rub {sf}, {ss} and {sb} into crumbs and sprinkle over the risen rolls.",
 BAKE(), "Whisk {ps} with {gj} and drizzle over the rolls.",
], "LIGHT CINNAMON")

rec(A("AR","Pink Tomato Jam"), [
 ("TOMATO JAM", [I("tom","1 cup","ripe tomatoes","chopped"), I("ts","1/3 cup","sugar"), I("lj","1 tbsp","lemon juice"), I("gin","1/4 tsp","ground ginger"), I("tc","1/4 tsp","cinnamon")]),
 ("FILLING", FILL(sug=("1/4 cup","brown sugar"), cin="1/2 tsp")),
 ("ICING", CCI),
],[
 "Simmer {tom}, {ts}, {lj}, {gin} and {tc}, stirring now and then, until thick and jammy, 25-30 min. Cool.",
 FS, SHAPE("Spread about 1/3 cup of the tomato jam over it"), RISE, BAKE(), CCIS,
], "LIGHT CINNAMON")

rec(A("AR","Rice Pudding"), [
 ("RICE PUDDING", [I("rice","1/2 cup","cooked white rice"), I("milk","1/2 cup","milk"), I("rs","2 tbsp","sugar"), I("rv","1/2 tsp","vanilla")]),
 ("FILLING", FILL(cin="2 tsp")),
 ("GLAZE", VG),
],[
 "Simmer {rice}, {milk} and {rs}, stirring, until thick and creamy, about 10 min. Stir in {rv} and cool.",
 FS, SHAPE("Spread the rice pudding over it"), RISE, BAKE(), VGS,
])

rec(A("ND","Juneberry"), [
 ("JUNEBERRIES", [I("jb","1/2 cup","juneberries (saskatoons), frozen"), I("js","2 tbsp","sugar"), I("jc","2 tsp","cornstarch"), I("alm","1/8 tsp","almond extract")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("GLAZE", VG),
],[
 "Cook {jb} with {js} and {jc} until thick, 3-4 min. Stir in {alm} and cool.",
 FS, SHAPE("Spread the juneberries over it"), RISE, BAKE(), VGS,
])

rec(A("ND","Honey"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("h","3 tbsp","honey"), I("s","2 tbsp","brown sugar"), I("c","1 tbsp","cinnamon")]),
 ("HONEY GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gh","1 tbsp","honey"), I("gm","1 tbsp","milk")]),
],[
 "Mix the filling: {b}, {h}, {s} and {c}.",
 SHAPE(), RISE, BAKE(), "Whisk {ps}, {gh} and {gm} and drizzle over the rolls.",
])

rec(A("NH","Cider Donut"), [
 ("CIDER REDUCTION", [I("cid","1 cup","apple cider")]),
 ("FILLING", FILL()),
 ("CIDER GLAZE", [I("ps","3/4 cup","powdered sugar")]),
 ("CINNAMON SUGAR CRUST", [I("mb","1 tbsp","butter","melted"), I("ts","2 tbsp","sugar"), I("tc","1 tsp","cinnamon")]),
],[
 "Boil {cid} until reduced to about 3 tbsp. Cool.",
 "Mix the filling: {b}, {s}, {c} and 2 tbsp of the cider reduction.",
 SHAPE(), SRISE, BAKE(),
 "Brush the warm rolls with {mb} and sprinkle with {ts} mixed with {tc}.",
 "Whisk {ps} with the rest of the cider reduction and drizzle lightly over the top.",
], SOUR)

rec(A("VA","Virginia Peanut Pie"), [
 ("FILLING", FILL(cin="1 tsp") + [I("pn","1/2 cup","salted roasted peanuts","chopped")]),
 ("PEANUT CARAMEL", [I("cb","2 tbsp","butter"), I("cs","1/4 cup","brown sugar"), I("cr","2 tbsp","heavy cream"), I("salt","pinch","salt")]),
 ("TOPPING", [I("pn2","2 tbsp","salted roasted peanuts","chopped")]),
],[
 FS, SHAPE("Scatter {pn} over it"), SRISE, BAKE(),
 "Melt {cb} with {cs}, {cr} and {salt}, and simmer 2 min until smooth.",
 "Spoon the caramel over the rolls and top with {pn2}.",
], SOUR)

rec(A("AK","Sourdough Lowbush Cranberry"), [
 ("BERRIES", [I("lb","1/2 cup","lowbush cranberries or lingonberries, frozen"), I("ls","2 tbsp","sugar"), I("lc","1 tsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("ORANGE GLAZE", [I("ps","3/4 cup","powdered sugar"), I("oj","1 1/2 tbsp","orange juice"), I("z","1 orange","zest")]),
],[
 "Cook {lb} with {ls} and {lc} until thick, 4-5 min. Cool.",
 FS, SHAPE("Spread the berries over it"), SRISE, BAKE(),
 "Whisk {ps} with {oj}, drizzle over the rolls, and finish with {z}.",
], SOUR)

rec(A("AK","Sourdough Salmonberry"), [
 ("BERRIES", [I("sb","1/2 cup","salmonberries (or raspberries)"), I("bs","1 tbsp","sugar"), I("bc","1 tsp","cornstarch")]),
 ("FILLING", FILL(sug=("1/4 cup","sugar"), cin="1 tsp")),
 ("LEMON GLAZE", [I("ps","3/4 cup","powdered sugar"), I("lj","1 1/2 tbsp","lemon juice")]),
],[
 "Cook {sb} with {bs} and {bc} until thick, 3-4 min. Cool.",
 FS, SHAPE("Spread the berries over it"), SRISE, BAKE(),
 "Whisk {ps} with {lj} and drizzle over the rolls.",
], SOUR)

rec(A("AK","Fireweed"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/4 cup","sugar"), I("v","1/2 tsp","vanilla"), I("jel","1/3 cup","fireweed jelly")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gj","1 tbsp","fireweed jelly"), I("gm","1-2 tsp","milk")]),
 ("TOPPING", [I("pink","1 tsp","pink sanding sugar")]),
],[
 "Mix {b}, {s} and {v}.",
 SHAPE("Spread {jel} over it"), SRISE, BAKE(),
 "Warm {gj} until runny, whisk it with {ps} and {gm}, drizzle over the rolls, and sprinkle {pink}.",
], SOUR + "\nNO CINNAMON")

rec(A("AK","Birch Syrup"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/4 cup","brown sugar"), I("bsy","2 tbsp","birch syrup"), I("c","2 tsp","cinnamon")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gbs","1 1/2 tbsp","birch syrup")]),
 ("TOPPING", [I("fs","","flaky salt")]),
],[
 "Mix the filling: {b}, {s}, {bsy} and {c}.",
 SHAPE(), SRISE, BAKE(),
 "Whisk {ps} with {gbs}, drizzle over the rolls, and finish with {fs}.",
], SOUR)

rec(A("IL","Morton Pumpkin"), [
 ("FILLING", FILL(cin="1 tsp") + [I("pump","1/3 cup","pumpkin puree"), I("pps","1 tsp","pumpkin pie spice")]),
 ("BROWN BUTTER ICING", [I("bb","2 tbsp","butter"), I("cc","2 oz","cream cheese","softened"), I("ps","3/4 cup","powdered sugar"), I("cv","1/2 tsp","vanilla")]),
 ("TOPPING", [I("pep","2 tbsp","pepitas","toasted")]),
],[
 "Mix the filling: {b}, {s}, {c}, {pump} and {pps}.",
 SHAPE(), RISE, BAKE(),
 "Brown {bb} and cool until soft. Beat it with {cc}, then beat in {ps} and {cv}. Spread over the rolls and top with {pep}.",
])

rec(A("IL","Palmer House Brownie"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","brown sugar"), I("cocoa","3 tbsp","cocoa powder"), I("c","1/2 tsp","cinnamon"), I("choc","2 oz","semisweet chocolate","chopped"), I("wal","1/4 cup","walnuts","chopped")]),
 ("APRICOT GLAZE", [I("jam","3 tbsp","apricot jam"), I("aw","1 tsp","water")]),
],[
 "Mix {b}, {s}, {cocoa} and {c} into a brownie-like paste.",
 SHAPE("Scatter {choc} and {wal} over it"), RISE, BAKE(),
 "Warm {jam} with {aw} and brush over the warm rolls, like the original Palmer House brownie's apricot glaze.",
], "LIGHT CINNAMON")

rec(A("VI","Tamarind"), [
 ("FILLING", FILL(cin="1/2 tsp") + [I("tam","1 tbsp","tamarind paste")]),
 ("TAMARIND GLAZE", [I("ps","3/4 cup","powdered sugar"), I("tam2","1 tbsp","tamarind paste"), I("gw","1 tbsp","water")]),
],[
 "Mix the filling: {b}, {s}, {c} and {tam}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {tam2} and {gw} and drizzle over the rolls.",
], "LIGHT CINNAMON")

rec(A("GU","Calamansi"), [
 ("CALAMANSI CURD", [I("cj","1/4 cup","calamansi juice (frozen)"), I("egg","1","egg"), I("cs","3 tbsp","sugar"), I("cb","1 tbsp","butter")]),
 ("FILLING", FILL(sug=("1/3 cup","sugar"), cin="1/2 tsp")),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("cj2","1 1/2 tbsp","calamansi juice (frozen)")]),
],[
 "Whisk {cj}, {egg}, {cs} and {cb} in a small pan over low heat until thick, about 5 min. Cool.",
 FS, SHAPE("Spread the curd over it"), RISE, BAKE(),
 "Whisk {ps} with {cj2} and drizzle over the rolls.",
], "LIGHT CINNAMON")

rec(A("CO","Rocky Ford Cantaloupe"), [
 ("FILLING", [I("b","3 tbsp","butter"), I("s","1/4 cup","sugar"), I("h","1 tbsp","honey"), I("salt","pinch","salt")]),
 ("CANTALOUPE CREAM GLAZE", [I("cc","2 oz","cream cheese","softened"), I("ps","1/2 cup","powdered sugar"), I("cant","3 tbsp","cantaloupe puree","strained")]),
 ("TOPPING", [I("mint","","fresh mint"), I("fs","","flaky salt")]),
],[
 "Brown {b} and let it cool until soft, then mix in {s}, {h} and {salt}.",
 SHAPE(), RISE, BAKE(),
 "Once the rolls are fully cool, beat {cc} with {ps}, then beat in {cant}. Spread over the rolls and finish with {mint} and {fs}.",
], "NO CINNAMON")

rec(A("CO","Palisade Lavender"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("lav","1 tsp","culinary lavender","finely ground")]),
 ("HONEY-LAVENDER GLAZE", [I("ps","3/4 cup","powdered sugar"), I("gh","1 tbsp","honey"), I("gm","1 tbsp","milk"), I("lav2","1/4 tsp","culinary lavender","finely ground")]),
],[
 "Mix the filling: {b}, {s} and {lav}.",
 SHAPE(), RISE, BAKE(),
 "Whisk {ps}, {gh}, {gm} and {lav2} and drizzle over the rolls.",
], "NO CINNAMON")

rec(A("RI","Del's Lemonade"), [
 ("FILLING", [I("b","3 tbsp","butter","softened"), I("s","1/3 cup","sugar"), I("z","1 lemon","zest"), I("curd","1/4 cup","lemon curd")]),
 ("GLAZE", [I("ps","3/4 cup","powdered sugar"), I("lj","1 1/2 tbsp","lemon juice")]),
 ("TOPPING", [I("z2","","lemon zest","to finish")]),
],[
 "Mix {b}, {s} and {z} into lemon sugar butter.",
 SHAPE("Spread {curd} over it"), RISE, BAKE(),
 "Whisk {ps} with {lj}, drizzle over the rolls, and top with {z2}.",
], "NO CINNAMON")
