import os
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "planner.html")
import json, re, math
from fractions import Fraction
SP = HERE + "/"
src = open(SP + "recipes2.py", encoding="utf-8").read()
src = src.replace("R = {}", "R = {}\nITEMS = {}", 1)
src = src.replace("    R[code] = out", "    R[code] = out\n    ITEMS[code] = [x for _, l in groups for x in l]", 1)
src = re.sub(r'\nprint\(R\["MA"\]\).*$', "\n", src, flags=re.S)
ns = {"__file__": os.path.join(HERE, "recipes2.py")}
exec(compile(src, "recipes2", "exec"), ns)
exec(compile(open(SP + "alts.py", encoding="utf-8").read(), "alts", "exec"), ns)
R, ITEMS = ns["R"], ns["ITEMS"]
ALT = {k: v for k, v in R.items() if "|" in k}
print("alts", len(ALT))

# reuse parse/category from shop.py
helpers = open(SP + "shop_helpers.py", encoding="utf-8").read()
hns = {"re": re, "math": math, "Fraction": Fraction}
exec(helpers, hns)
parse, category = hns["parse"], hns["category"]
EXTRA_SPECIALTY = ["coffee syrup","poppy","dr pepper","maraschino","passion fruit","old bay","espresso","cacao","ramps","black walnut","buckwheat","currants","kool-aid","jell-o","anise","concord","juneberr","lingonberr","lowbush","salmonberr","fireweed","birch","tamarind","lavender","almond paste","champagne","sparkling sugar","dark rum","sprinkles","mace"]
def cat(name):
    n = name.lower()
    if any(k in n for k in EXTRA_SPECIALTY): return "Specialty (order or shop ahead)"
    if n == "buttermilk": return "Dairy and eggs"
    if "banana" in n or n == "ripe tomatoes": return "Produce and frozen fruit"
    return category(name)

ALIAS = {"cold butter":"butter","whole milk":"milk","pure maple syrup":"maple syrup","flaky sea salt":"flaky salt","scallion":"scallions","graham cracker crumbs":"graham crackers","pecan halves":"pecans","roasted green chile":"roasted Hatch green chile","a few whole huckleberries":"huckleberries","freshly grated nutmeg":"nutmeg","garlic clove":"garlic cloves","cheddar":"sharp cheddar","chocolate":"semisweet chocolate","fresh blueberries":"blueberries","fresh raspberries":"raspberries","light corn syrup":"corn syrup"}
def normalize(key):
    agg = {}
    for k, amt, name, note in ITEMS[key]:
        if name != "zest":
            name = re.sub(r'\s*\(.*?\)', '', name).strip()
            name = re.sub(r',\s*frozen$', '', name)
            if name.startswith("a tiny drop of "): name = "pink food coloring"
            name = ALIAS.get(name, name)
            if name in ("hot water", "water"): continue
            if name in ("lemon zest", "lime zest", "orange zest"):
                if amt and re.match(r'^[\d/ ]+\s*tsp', amt): pass
                else: amt = "1 " + name.split()[0]; name = "zest"
        k2 = name.lower()
        if name == "zest":
            fruit = re.sub(r'\s*\(.*?\)', '', amt).strip()
            fruit = re.sub(r'^\d+(/\d+)?\s*', '', fruit)
            fruit = fruit.rstrip("s") if fruit.endswith("limes") else fruit
            k2 = fruit + " (for zest)"; name = k2
        if k2 in ("egg", "egg yolk", "egg white"): k2 = "eggs"; name = "eggs"
        e = agg.setdefault(k2, {"name": name, "v": Fraction(0), "o": Fraction(0), "q": Fraction(0), "u": None, "x": []})
        pr = parse(amt) if amt and amt != "pinch" and name != "zest" else None
        if name.endswith("(for zest)"):
            m = re.match(r'^(\d+(?:/\d+)?)', amt)
            if not e.get("seen") or not amt.startswith("1 ") or e["q"] == 0:
                e["q"] += Fraction(m.group(1)) if m else 1
            e["seen"] = True
        elif k2 == "eggs": e["q"] += 1
        elif pr is None:
            if amt and amt != "pinch": e["x"].append(amt)
        elif pr[0] == "vol": e["v"] += pr[1]
        elif pr[0] == "oz": e["o"] += pr[1]
        else:
            e["q"] += pr[1]
            if any(w in amt for w in ("small", "medium", "pieces")): e["u"] = amt.split()[-1]
    return [[k2, e["name"], cat(e["name"]), round(float(e["v"]), 6), round(float(e["o"]), 6), round(float(e["q"]), 6), e["u"], e["x"]] for k2, e in agg.items()]

SHOPDATA = {k: normalize(k) for k in R}

p = PAGE
s = open(p, encoding="utf-8").read()
def rep(a, b):
    global s
    if b in s or b[:120] in s: return
    assert a in s, ("MISSING", a[:90]); s = s.replace(a, b, 1)

# data blobs: replace old SHOP with ALT_RECIPE + SHOPDATA
blob = ("const ALT_RECIPE=" + json.dumps(ALT, ensure_ascii=False) + ";\n"
        "const SHOPDATA=" + json.dumps(SHOPDATA, ensure_ascii=False, separators=(",", ":")) + ";\n")
s, n = re.subn(r'const ALT_RECIPE=\{.*?\};\nconst SHOPDATA=\{.*?\};\n', lambda m: blob, s, count=1, flags=re.S)
if n == 0:
    s, n = re.subn(r'const SHOP=\{.*?\};\n', lambda m: blob, s, count=1, flags=re.S)
    assert n == 1

    JS = r'''const DRAFTS=new Set([...Object.values(RECIPE),...Object.values(ALT_RECIPE)]);
function recipeKey(code,roll){return roll===BY[code].roll?code:(ALT_RECIPE[code+"|"+roll]!==undefined?code+"|"+roll:null)}
function draftFor(code,roll){const k=recipeKey(code,roll);return k?(RECIPE[k]||ALT_RECIPE[k]||""):""}
function isDraft(t){return !t||DRAFTS.has(t)}
function frac4(q){q=Math.round(q*4)/4;const w=Math.floor(q),f=Math.round((q-w)*4);const fs=["","1/4","1/2","3/4"][f];return ((w?String(w):"")+(w&&fs?" ":"")+fs)||"0"}
function fmtVol(t,key){t=Math.round(t*1e6)/1e6;
  if(key==="butter"){const tb=Math.ceil(t/3),q=Math.ceil(tb/2)/4;return `${tb} tbsp (about ${frac4(q)} stick${q>1?"s":""})`}
  if(t>=12){const q=Math.ceil(t/12)/4;return `${frac4(q)} cup${q>1?"s":""}`}
  if(t>=3){const q=Math.ceil(t/1.5)/2;return `${frac4(q)} tbsp`}
  return `${frac4(Math.ceil(t*4)/4)} tsp`}
const CATS=["Produce and frozen fruit","Dairy and eggs","Pantry and baking","Specialty (order or shop ahead)"];
function shopList(codes){const agg={},missing=[];
  codes.forEach(c=>{const r=cur(c);const k=recipeKey(c,r.roll);if(!k){missing.push(r.roll);return}
    (SHOPDATA[k]||[]).forEach(([key,name,cat,v,o,q,u,x])=>{const e=agg[key]||(agg[key]={name,cat,v:0,o:0,q:0,u:null,x:[]});e.v+=v;e.o+=o;e.q+=q;if(u)e.u=u;e.x.push(...x)})});
  const byCat={};Object.entries(agg).forEach(([key,e])=>{const parts=[];
    if(e.v)parts.push(fmtVol(e.v,key));if(e.o)parts.push(`${Math.ceil(e.o-1e-9)} oz`);
    if(e.q){const c=Math.max(1,Math.ceil(e.q-1e-9));parts.push(e.u?`${c} ${e.u}`:String(c))}
    parts.push(...e.x);if(!parts.length)parts.push("a little");
    (byCat[e.cat]=byCat[e.cat]||[]).push(`${e.name[0].toUpperCase()+e.name.slice(1)}: ${parts.join(", ")}`)});
  let out=CATS.filter(c=>byCat[c]).map(c=>c.toUpperCase()+"\n"+byCat[c].sort((a,b)=>a.toLowerCase().localeCompare(b.toLowerCase())).map(x=>"- "+x).join("\n")).join("\n\n");
  if(missing.length)out+=`\n\nNot included (no draft recipe for your custom flavor): ${missing.join(", ")}`;
  return out}
'''
    rep("const CONF_LABEL={", JS + "const CONF_LABEL={")

# cur(): treat untouched drafts as not custom, follow the current flavor
rep('recipe:o.recipe||RECIPE[d.code]||"",', 'recipe:(o.recipe&&!isDraft(o.recipe))?o.recipe:draftFor(d.code,o.roll||d.roll),')

# "Use this": swap the recipe too unless it's been customized
rep('const a=t.dataset.alt==="orig"?[d.roll,d.build]:d.alts[+t.dataset.alt];',
    'const a=t.dataset.alt==="orig"?[d.roll,d.build]:d.alts[+t.dataset.alt];const rb=document.getElementById("d-recipe");const kept=!isDraft(rb.value);if(!kept)rb.value=draftFor(openCode,a[0]);setTimeout(()=>{const m=document.getElementById("d-msg");if(m)m.textContent=kept?"Swapped in. Your own recipe was kept. Save to keep the swap.":"Swapped in with its starting recipe. Save to keep it."},0);')

# save: don't store an untouched draft, so it keeps following the flavor
rep('recipe:document.getElementById("d-recipe").value,', 'recipe:(v=>isDraft(v)?"":v)(document.getElementById("d-recipe").value),')

# shopping lists from the current flavors
rep('<pre>${esc(SHOP[b.join(",")]||"")}</pre><p class="shopnote">Everything except the dough. Totals for all ${items.length} rolls, rounded up.</p>',
    '<pre>${esc(shopList(b))}</pre><p class="shopnote">Everything except the dough, for the flavors currently chosen. Totals for all ${items.length} rolls, rounded up. Based on the starting recipes, so adjust if you\'ve changed yours.</p>')
rep('<pre>${esc(SHOP[d.code]||"")}</pre><p class="shopnote">Everything except the dough, rounded up.</p>',
    '<pre>${esc(shopList([d.code]))}</pre><p class="shopnote">Everything except the dough, rounded up. Based on the starting recipe.</p>')
open(p, "w", encoding="utf-8").write(s)
print("patched")
