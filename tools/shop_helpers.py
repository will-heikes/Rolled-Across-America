# Unit parsing and store-section helpers used by swapfix.py.
import re, math
from fractions import Fraction

VOL = {"tsp": 1, "tbsp": 3, "cup": 48, "cups": 48}
def num(t):
    t = t.strip()
    if " " in t:
        a, b = t.split(" ", 1); return Fraction(a) + Fraction(b)
    return Fraction(t)
def parse(amt):
    a = amt.split(" (")[0].strip()
    m = re.match(r'^([\d/ ]+?)(?:-([\d/ ]+?))?\s+(tsp|tbsp|cups?|oz)\b', a)
    if m:
        q = num(m.group(2) or m.group(1)); u = m.group(3)
        if u == "oz": return ("oz", q)
        return ("vol", q * VOL[u])
    m = re.match(r'^(\d+)(?:\s+(small|medium|large|pieces))?$', a)
    if m: return ("count", Fraction(int(m.group(1))))
    return None

def fmt_vol(tsp, name):
    if name == "butter":
        tb = math.ceil(tsp / 3)
        q = math.ceil(tb / 2) / 4; w = int(q); fr = Fraction(q - w).limit_denominator(4)
        st = (str(w) if w else "") + (" " if w and fr else "") + (str(fr) if fr else "")
        return f"{tb} tbsp (about {st} stick{'s' if q > 1 else ''})"
    if tsp >= 12:
        q = math.ceil(tsp / 12) / 4
        whole = int(q); frac = Fraction(q - whole).limit_denominator(4)
        t = (str(whole) if whole else "") + (" " if whole and frac else "") + (str(frac) if frac else "")
        return f"{t} cup{'s' if q > 1 else ''}"
    if tsp >= 3:
        q = math.ceil(tsp / 1.5) / 2
        t = str(int(q)) if q == int(q) else (f"{int(q)} 1/2" if int(q) else "1/2")
        return f"{t} tbsp"
    q = math.ceil(tsp * 4) / 4
    whole = int(q); frac = Fraction(q - whole).limit_denominator(4)
    t = (str(whole) if whole else "") + (" " if whole and frac else "") + (str(frac) if frac else "")
    return f"{t} tsp"

CAT_PRODUCE = ["apple","lemon","lime","orange","grapefruit","peach","pineapple","strawberr","rhubarb","cranberr","scallion","garlic","onion","corn kernels","mango","mint","chives","sweet potato","potato","raspberr","blueberr","cantaloupe","cherries","huckleberr","key lime"]
CAT_DAIRY = ["butter","milk","cream","sour cream","cheddar","mozzarella","parmesan","pecorino","pepper jack","egg","evaporated"]
CAT_PANTRY = ["sugar","flour","cornstarch","cocoa powder","cinnamon","nutmeg","vanilla","salt","honey","maple","oats","corn syrup","cardamom","ginger","baking soda","cream of tartar","pumpkin pie spice","oregano","italian seasoning","mustard","sesame","pecan","walnut","hazelnut","almond","macadamia","chocolate","graham","raisins","coconut","marshmallow","peanut butter","cornmeal","crushed tomatoes","olive oil","pepitas","sunflower seeds"]
SPECIALTY_FIRST = ["peanut butter","coconut milk","chocolate pudding","malted","freeze-dried","sakura","sanding","pearl","pretzel","taffy","guava","prickly","chokecherry","sand plum","huckleberry jam","curd","apple butter","caramel corn","caramel sauce","grenadine","amaro","brandy","bourbon","beer","pepperoni","chile","chili","shallots","dates","candied","pumpkin puree","sunflower seed butter","calamansi","guavaberry","dried apricots","honeycomb","cherry blossom","tart cherries","wild blueberries","lemon curd","lime curd","shortbread","pine","cranberry sauce","piñon","Chugwater"]
def category(name):
    n = name.lower()
    if any(k.lower() in n for k in ["coconut milk","chocolate pudding","malted","freeze-dried","sakura","sanding sugar","pearl sugar","pretzel salt","taffy","guava","prickly","chokecherry","sand plum","huckleberry jam","lemon curd","lime curd","apple butter","caramel corn","caramel sauce","grenadine","amaro","brandy","bourbon","beer","pepperoni","chile","chili","shallots","dates","candied","pumpkin puree","sunflower seed butter","calamansi","guavaberry","dried apricots","honeycomb","cherry blossom","tart cherries","wild blueberries","salted cherry","pink coloring"]):
        return "Specialty (order or shop ahead)"
    if n in ("egg", "egg yolk", "egg white"): return "Dairy and eggs"
    if any(k in n for k in CAT_PRODUCE) and "juice" not in n: return "Produce and frozen fruit"
    if "juice" in n: return "Produce and frozen fruit"
    if any(k in n for k in CAT_DAIRY) and "peanut" not in n and "cream of tartar" not in n: return "Dairy and eggs"
    return "Pantry and baking"

