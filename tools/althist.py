import os
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "planner.html")
import json, re
p = PAGE
s = open(p, encoding="utf-8").read()

H = {
"MA|Cranberry Bog": ("Massachusetts is one of the country's top cranberry growers, and cranberry juice is the official state beverage.",
 "Cranberries are one of the few fruits native to North America, and the Wampanoag ate them long before colonists arrived. Commercial growing started around 1816, when Captain Henry Hall of Dennis on Cape Cod noticed his wild vines grew better when sand blew over them. The Ocean Spray cooperative later grew up around Massachusetts bogs, and cranberry juice became the official state beverage in 1970."),
"NJ|Highbush Blueberry": ("Highbush blueberry is New Jersey's state fruit, and the cultivated blueberry was born there.",
 "In the early 1900s, Elizabeth White, whose family ran a cranberry farm at Whitesbog in the Pine Barrens, teamed up with USDA botanist Frederick Coville to tame the wild blueberry. White paid local pickers to find the best wild bushes, and Coville bred from them. In 1916 they harvested and sold the first commercial crop of cultivated blueberries. Most blueberries sold in American stores descend from that work, and New Jersey later named the highbush blueberry its state fruit."),
"NJ|Jersey Crumb Bun": ("Crumb buns are a staple of New Jersey bakeries.",
 "German immigrants brought streuselkuchen, a yeast cake topped with buttery crumbs, to the New York and New Jersey area in the 1800s. Local bakeries turned it into the crumb bun: soft yeast dough under a crumb layer often as thick as the cake itself, finished with powdered sugar. It's a classic order at Jersey bakeries and diners, and locals will tell you the crumb-to-cake ratio is the whole point."),
"NJ|Rainbow Cookie": ("Rainbow cookies are an Italian-American bakery classic across New Jersey.",
 "Rainbow cookies, also called tricolor or seven-layer cookies, were created by Italian-American bakers in the New York and New Jersey area in the early 1900s. Three layers of almond sponge, tinted green, white and red like the Italian flag, are stacked with raspberry or apricot jam and coated in chocolate. They're a fixture of Italian bakery trays at Christmas, weddings and holidays across North Jersey."),
"NV|Pine Nut": ("The single-leaf piñon is Nevada's state tree, and its nuts are an ancient Great Basin food.",
 "The single-leaf piñon pine grows across Nevada's mountain ranges and is one of its two state trees. For thousands of years, the Washoe, Paiute and Western Shoshone peoples have gathered its nuts each fall. The harvest was a major seasonal event, with families traveling to the groves together, and it's still celebrated today with gatherings and pine nut festivals."),
"NV|Strawberries & Champagne": ("A nod to Las Vegas glamour and celebration.",
 "Las Vegas started as a railroad stop in 1905. Nevada legalized gambling in 1931, and by the 1950s the Strip's casinos and showrooms had made Vegas shorthand for glamour and celebration, which is the spirit of a champagne roll."),
"TX|Czech Kolache": ("Czech bakeries along I-35 made the kolache a Texas staple.",
 "Czech immigrants began settling in Central Texas in the 1850s, building farming towns like West, Ennis and Caldwell. They brought kolaches, soft yeast buns filled with fruit, poppy seed or sweet cheese. Today kolaches are a Texas breakfast staple, the town of West is famous for its Czech bakeries along I-35, and Caldwell calls itself the Kolache Capital of Texas."),
"TX|Dr Pepper": ("Dr Pepper was invented in Waco.",
 "Dr Pepper was created in 1885 by pharmacist Charles Alderton at Morrison's Old Corner Drug Store in Waco, which makes it one of the oldest major soft drinks in the US. The Dr Pepper Museum in Waco now stands in an old bottling plant. Its blend of 23 flavors has always been a secret, which is why this roll leans on cherry, vanilla and allspice to get close."),
"LA|Bananas Foster": ("Bananas Foster was invented at Brennan's in New Orleans.",
 "Bananas Foster was created at Brennan's in New Orleans in 1951. New Orleans was the country's main banana import port, and owner Owen Brennan asked his chef to make a dessert with them. It was named for Richard Foster, a friend of Brennan's and a city crime commissioner, and is traditionally flambéed at the table."),
"HI|Lilikoi": ("Lilikoi butter is a classic island spread.",
 "Passion fruit was introduced to Hawaii from Australia in the 1880s. A common story says the Hawaiian name, lilikoi, comes from an area on Maui where the first vines were planted. Lilikoi butter, a sweet-tart spread like lemon curd, became a beloved island staple."),
"HI|Haupia": ("Haupia is the coconut pudding served at Hawaiian luaus.",
 "Haupia is a traditional Hawaiian coconut pudding, originally made from coconut milk thickened with arrowroot, called pia. Today it's usually made with cornstarch and served in firm squares at luaus and family gatherings. It also shows up in haupia pie, chocolate haupia pie and haupia-filled malasadas."),
"MD|Old Bay Caramel": ("Old Bay seasoning was created in Baltimore.",
 "Old Bay seasoning was created in Baltimore in 1939 by Gustav Brunn, a German-Jewish spice merchant who had fled Nazi Germany. He named it after the Old Bay Line, a steamship company that carried passengers on the Chesapeake Bay. It was made for steamed crabs, but Marylanders now put it on almost everything, which makes Old Bay caramel a crab-free way to taste Maryland."),
"WA|Seattle Espresso": ("Seattle coffee culture.",
 "The first Starbucks opened at Seattle's Pike Place Market in 1971, selling coffee beans rather than drinks. Over the 1980s, espresso carts and cafés spread across the city, and Seattle became the center of America's espresso boom."),
"WV|Ramp": ("Spring ramp feeds are an Appalachian tradition.",
 "Ramps are wild leeks that are among the first green plants to appear in Appalachian forests each spring. For mountain families after a long winter they were a prized 'spring tonic.' Community ramp feeds became a West Virginia tradition, including the Feast of the Ramson in Richwood, which calls itself the Ramp Capital of the World."),
"WV|Black Walnut": ("Spencer has held a Black Walnut Festival since the 1950s.",
 "Black walnut trees grow wild across West Virginia, and gathering and cracking the hard-shelled nuts each fall was a rural Appalachian tradition. Their flavor is much stronger and earthier than store-bought English walnuts. The town of Spencer has celebrated the harvest with its West Virginia Black Walnut Festival since the 1950s."),
"WV|Buckwheat": ("Preston County's Buckwheat Festival dates to the 1930s.",
 "Buckwheat grows well in the cool, high country of Preston County, and buckwheat cakes with sausage became a regional staple. The Preston County Buckwheat Festival in Kingwood began in the late 1930s and still serves buckwheat cakes by the thousands each fall."),
"PA|Shoofly": ("Pennsylvania Dutch shoofly pie.",
 "Shoofly pie comes from the Pennsylvania Dutch, German-speaking settlers who arrived in the 1700s and 1800s. Molasses was a cheap pantry staple, and the pie is basically molasses under a crumb topping. The most repeated explanation for the name is that the sweet, sticky pies attracted flies that bakers had to shoo away."),
"NY|Black & White Cookie": ("The black-and-white is a New York bakery classic.",
 "The black-and-white cookie is a soft, cakey cookie iced half in vanilla and half in chocolate. It's often traced to Glaser's Bake Shop, a German bakery that opened in Manhattan's Yorkville neighborhood in 1902, though its exact origin is debated. It became a staple of New York bakeries and delis, and a 1994 episode of Seinfeld made it famous nationwide."),
"CT|Election Cake": ("Hartford's historic Election Day cake.",
 "Election cake is a spiced, fruit-studded yeast cake that New Englanders baked for Election Day, when people traveled to town to vote and celebrate. Hartford became especially associated with it, and American Cookery, the first American cookbook, published in Hartford in 1796, includes a recipe. Some modern bakers have revived it as an Election Day tradition."),
"NE|Kool-Aid": ("Kool-Aid was invented in Hastings and is Nebraska's official state soft drink.",
 "Edwin Perkins invented Kool-Aid in Hastings, Nebraska, in 1927. He turned a liquid drink concentrate into a powder, which was cheaper to ship. It was a hit during the Great Depression, when a packet sold for a nickel. Nebraska named Kool-Aid its official state soft drink in 1998, and Hastings celebrates with Kool-Aid Days every August."),
"AL|Blackberry Bramble": ("Blackberry is Alabama's state fruit.",
 "Wild blackberries grow along fences and roadsides all over Alabama, and picking them was a summer tradition in rural families. Alabama named the blackberry its official state fruit."),
"UT|Raspberry Jell-O": ("Jell-O is Utah's official state snack.",
 "Utah has long ranked among the biggest Jell-O eaters in the country, and Jell-O salads are a fixture at church potlucks and family dinners. When Utah slipped in per-capita sales in the late 1990s, a campaign helped make Jell-O the official state snack in 2001. Green Jell-O pins were a hit souvenir at the 2002 Salt Lake City Winter Olympics. The raspberry flavor is a nod to Bear Lake's famous raspberries."),
"UT|Bear Lake Raspberry": ("Bear Lake raspberry shakes.",
 "Farmers in Utah's Bear Lake Valley found that the cool mountain climate suited raspberries. Roadside shake stands near Garden City made the Bear Lake raspberry shake famous, and the town celebrates with a yearly Raspberry Days festival in early August."),
"WY|Chokecherry": ("Chokecherry jelly is a Wyoming ranch-kitchen classic.",
 "Chokecherries grow wild across the Plains and Rockies. Plains tribes pounded the dried berries into pemmican, and homesteaders later turned the very tart fruit into jelly and syrup. Chokecherry jelly is still a classic ranch-kitchen staple in Wyoming."),
"NM|Biscochito": ("The biscochito is New Mexico's official state cookie.",
 "Biscochitos are crisp, anise-flavored shortbread cookies dusted with cinnamon sugar, brought to New Mexico by Spanish colonists. They're baked for Christmas, weddings and other celebrations, traditionally with lard. In 1989 New Mexico made the biscochito its official state cookie, the first official state cookie in the country."),
"KS|Sunflower": ("The Sunflower State.",
 "Wild sunflowers grow across the Kansas prairie, and Plains tribes ate the seeds and made oil and dye from them. Kansas adopted the sunflower as its state flower in 1903, which gave it the nickname the Sunflower State."),
"KS|Wheat Harvest": ("Kansas is the Wheat State.",
 "In the 1870s, Mennonite immigrants from Russia settled in Kansas and brought Turkey Red, a hardy winter wheat that could survive the plains' harsh winters and dry summers. It helped turn Kansas into one of the country's top wheat producers, earning it the nicknames the Wheat State and the Breadbasket of the World."),
"AR|Tontitown Grape": ("Tontitown has held a grape festival for over a century.",
 "In 1898 Father Pietro Bandini led Italian immigrants to the Ozarks and founded Tontitown, Arkansas. They planted vineyards, and the town held its first grape festival soon after. It has continued for more than 120 years, making it one of the oldest festivals in the state."),
"AR|Pink Tomato Jam": ("The South Arkansas vine-ripe pink tomato is both the state fruit and the state vegetable.",
 "Bradley County in southern Arkansas became known for its pink tomatoes in the early 1900s, and the town of Warren has held the Bradley County Pink Tomato Festival since 1956. In 1987 the legislature named the South Arkansas vine-ripe pink tomato both the official state fruit and the official state vegetable, since a tomato is botanically a fruit but cooked like a vegetable."),
"AR|Rice Pudding": ("Arkansas grows about half of America's rice.",
 "Rice farming took off on the Grand Prairie of eastern Arkansas in the early 1900s, after farmers found the flat land and clay soil held floodwater well. Arkansas is now by far the country's largest rice producer, growing roughly half of all US rice, and Stuttgart calls itself the Rice and Duck Capital of the World."),
"ND|Juneberry": ("Juneberry pie is a Northern Plains tradition.",
 "Juneberries, also called saskatoons or serviceberries, grow wild in coulees and along rivers across North Dakota. Plains tribes dried them and mixed them into pemmican, and homesteaders baked them into pies. They ripen in early summer, which is where the name comes from."),
"ND|Honey": ("North Dakota produces more honey than any other state.",
 "North Dakota produces more honey than any other state. Many beekeepers bring their hives to North Dakota for summer, when clover, canola and sunflower fields are in bloom."),
"NH|Cider Donut": ("Cider donuts at New England orchards.",
 "Apple orchards and cider have been part of New England life since colonial times, when hard cider was a common everyday drink. Fall orchard visits with cider and fresh cider donuts became a New Hampshire tradition, and boiled cider, made by cooking cider down into a syrup, is an old New England baking ingredient."),
"VA|Virginia Peanut Pie": ("Virginia peanuts are famous, and peanut pie is a Virginia classic.",
 "Peanuts became a major crop in southeastern Virginia after the Civil War, and the large-kernel Virginia peanut became the prized variety for roasting. The town of Suffolk became known as the Peanut Capital of the World, and Planters, the company behind Mr. Peanut, opened a plant there in 1913. Peanut pie, made like pecan pie, is a classic in Virginia's peanut country."),
"AK|Sourdough Lowbush Cranberry": ("Alaskans call themselves sourdoughs, and lowbush cranberries are a staple wild berry.",
 "Alaskans who have lived through enough winters are called 'sourdoughs,' a nickname from Gold Rush prospectors who carried sourdough starter with them, sometimes keeping it warm inside their coats. Lowbush cranberries, also known as lingonberries, grow across Alaska's forests and tundra. Alaska Native families have long picked them for foods like akutaq, a whipped mix of berries and fat, and late-summer berry picking is still a statewide tradition."),
"AK|Sourdough Salmonberry": ("Salmonberries are one of Alaska's most distinctive wild berries.",
 "Alaskans who have lived through enough winters are called 'sourdoughs,' a nickname from Gold Rush prospectors who carried sourdough starter with them. Salmonberries grow along Alaska's coasts and rivers and look like large orange or red raspberries. Alaska Native families have long picked them, and they're a classic ingredient in akutaq. They're very hard to find outside the state, so raspberries are the usual stand-in."),
"AK|Fireweed": ("Fireweed is Alaska's signature summer wildflower.",
 "Fireweed is one of the first plants to return after a wildfire, and its tall magenta spikes cover Alaska in summer. Alaskans say that when fireweed goes to seed, summer is almost over. The flowers are made into jelly, syrup and honey. Gold Rush prospectors carried sourdough starters, and longtime Alaskans are still nicknamed 'sourdoughs.'"),
"AK|Birch Syrup": ("Alaska is one of the few places that makes birch syrup commercially.",
 "Birch syrup is made by boiling down the sap of birch trees, like maple syrup, but it takes far more sap: roughly 100 gallons for one gallon of syrup. Alaska's vast birch forests made it one of the few places to produce it commercially, with small producers in the Interior and the Mat-Su Valley. It tastes darker than maple, with notes of molasses and caramel."),
"IL|Morton Pumpkin": ("Morton calls itself the pumpkin capital of the world.",
 "Illinois grows more pumpkins than any other state, especially the kind processed into canned pumpkin. Libby's has run a pumpkin canning plant in Morton since 1929, and much of America's canned pumpkin comes from there. Morton calls itself the Pumpkin Capital of the World and has held a pumpkin festival since 1967."),
"IL|Palmer House Brownie": ("The brownie was invented at Chicago's Palmer House hotel.",
 "Bertha Palmer, wife of hotel owner Potter Palmer, asked the Palmer House pastry chef to create a dessert that could be packed into ladies' boxed lunches at the 1893 World's Columbian Exposition in Chicago. The result was a dense chocolate square with walnuts and an apricot glaze, widely considered the first brownie. The Palmer House still serves it from the original recipe."),
"VI|Tamarind": ("Tamarind is a Caribbean staple.",
 "Tamarind trees were brought to the Caribbean from Africa and Asia centuries ago and became part of everyday life in the Virgin Islands. The sweet-sour pulp is used in tamarind balls, drinks and stews, and old shade-giving tamarind trees are local landmarks."),
"GU|Calamansi": ("Calamansi is a favorite citrus on Guam.",
 "Calamansi, a small, very tart citrus, came to Guam from the nearby Philippines and is widely grown there. Guam's large Filipino community helped make it a kitchen staple, used for juice, marinades and desserts."),
"CO|Rocky Ford Cantaloupe": ("Rocky Ford cantaloupes.",
 "In the 1870s, settler George Washington Swink began growing melons in the Arkansas Valley around Rocky Ford. In 1878 he started handing out free watermelons at harvest time, and that event grew into Watermelon Day, one of the oldest celebrations in Colorado. Rocky Ford's sweet, heavily netted cantaloupes became famous across the country, and their short August season is something Coloradans wait for every year."),
"RI|Del's Lemonade": ("Del's frozen lemonade is a Rhode Island summer staple.",
 "Del's Lemonade started in 1948, when Angelo DeLucia began selling frozen lemonade from a stand in Cranston. The recipe came from his family in Italy, who made it with snow, lemons and sugar. The bright yellow trucks and stands are now a Rhode Island summer ritual."),
"CO|Palisade Lavender": ("Palisade on Colorado's Western Slope is lavender country.",
 "The orchard town of Palisade on Colorado's Western Slope, better known for its peaches, has also become a lavender-growing center. Its sunny, dry climate and high elevation suit the plant. Lavender farms there draw visitors every summer, and the area holds a lavender festival in early summer."),
}

# every alternate must have a history
rows = re.findall(r'^(\["([A-Z]+)",\s*"[A-Z][^"]*",\s*\d+,.*\]),?$', s, flags=re.M)
keys = set()
for line, code in rows:
    arr = json.loads(line)
    for a in arr[11]: keys.add(code + "|" + a[0])
missing = keys - set(H); extra = set(H) - keys
assert not missing and not extra, (missing, extra)

def rep(a, b):
    global s
    if b in s: return
    assert a in s, ("MISSING", a[:90]); s = s.replace(a, b, 1)

blob = "const ALT_HIST=" + json.dumps(H, ensure_ascii=False) + ";\n"
s, n = re.subn(r'const ALT_HIST=\{.*?\};\n', lambda m: blob, s, count=1, flags=re.S)
if n == 0:
    JS = blob + r'''const HDRAFTS=new Set([...Object.values(HISTORY),...Object.values(ALT_HIST).map(x=>x[1])]);
function isHDraft(t){return !t||HDRAFTS.has(t)}
function histFor(code,roll){if(roll===BY[code].roll)return HISTORY[code]||"";const a=ALT_HIST[code+"|"+roll];return a?a[1]:""}
function whyFor(code,roll){if(roll===BY[code].roll)return BY[code].why;const a=ALT_HIST[code+"|"+roll];return a?a[0]:""}
'''
    rep("const CONF_LABEL={", JS + "const CONF_LABEL={")

rep('history:o.history??(HISTORY[d.code]||""),', 'history:(o.history&&!isHDraft(o.history))?o.history:histFor(d.code,o.roll||d.roll),why:whyFor(d.code,o.roll||d.roll),')
rep('<b>Why it fits:</b> ${esc(d.why)}', '${r.why?`<b>Why it fits:</b> ${esc(r.why)}<br>`:""}')
rep('<br><b>Season:</b> ${esc(d.season)}', '${r.roll===d.roll?`<b>Season:</b> ${esc(d.season)}`:""}')
rep('const kept=!isDraft(rb.value);if(!kept)rb.value=draftFor(openCode,a[0]);',
    'const kept=!isDraft(rb.value);if(!kept)rb.value=draftFor(openCode,a[0]);const hb=document.getElementById("d-hist");const hkept=!isHDraft(hb.value);if(!hkept)hb.value=histFor(openCode,a[0]);')
rep('m.textContent=kept?"Swapped in. Your own recipe was kept. Save to keep the swap.":"Swapped in with its starting recipe. Save to keep it."',
    'm.textContent=(kept||hkept)?"Swapped in. Your own "+(kept&&hkept?"recipe and history were":kept?"recipe was":"history was")+" kept. Save to keep the swap.":"Swapped in with its recipe and history. Save to keep it."')
rep('history:document.getElementById("d-hist").value,', 'history:(v=>isHDraft(v)?"":v)(document.getElementById("d-hist").value),')
open(p, "w", encoding="utf-8").write(s)
print("ok", len(H))
