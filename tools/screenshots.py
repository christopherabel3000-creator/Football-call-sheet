# Gridiron Duel: takes the App Store screenshots, six for iPhone 6.3" (1206 x 2622) and six for
# iPad 13" (2064 x 2752). Build the app's files first (node scripts/build-www.js), then run
# python3 tools/screenshots.py appstore/screenshots
# It plays a quick game against the computer, picking calls at random, and saves screens on the way.
import asyncio, pathlib, random, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "www" / "index.html").as_uri()
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "appstore" / "screenshots")
NAV = {"help", "mute", "end", "color", "ostyle", "dstyle", "ctrl", "pkg", "diff", "qlen", "aud", "netcreate", "netcode", "nohuddle", "to", "spike", "side", "disg", "dlook", "burn", "onside", "audible", "audpick", "netback", "netleave", "newsetup", "rematch"}

STEP = """() => {
  const bs = [...document.querySelectorAll('#app [data-a]')].filter(e => !e.disabled);
  const by = a => bs.filter(e => e.dataset.a === a);
  const lock = document.querySelector('#app [data-a=lock]');
  const pick = (l) => l[Math.floor(Math.random() * l.length)];
  let el = by('snap')[0] || by('cont')[0];
  if (!el && lock && !lock.disabled) el = lock;
  if (!el && lock && lock.disabled) el = pick(by('pick'));
  if (!el) el = bs.find(e => !%s.includes(e.dataset.a) && !['audpick'].includes(e.dataset.a));
  if (el) { el.click(); return el.dataset.a; }
  return null;
}""" % sorted(NAV).__repr__()

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    random.seed(4)
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", args=["--no-sandbox"])
        for dev, w, h, scale in (("iphone", 402, 874, 3), ("ipad", 1032, 1376, 2)):
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=scale, has_touch=True, is_mobile=True)
            pg = await ctx.new_page(); errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.add_init_script("window.Capacitor = { isNativePlatform: () => true }; Math.random = (() => { let s = 7; return () => (s = (s * 16807) % 2147483647) / 2147483647; })();")
            await pg.goto(URL); await pg.wait_for_timeout(800)
            heading = lambda: pg.evaluate("(document.querySelector('#app h1, #app h2')?.innerText || '').replace(/\\s+/g, ' ')")
            async def shot(name, sel=None, pad=12):
                if sel: await pg.evaluate("([s,p]) => { const e = document.querySelector(s); if (e) window.scrollTo(0, e.getBoundingClientRect().top + window.scrollY - p); }", [sel, pad])
                else: await pg.evaluate("window.scrollTo(0,0)")
                await pg.evaluate("document.activeElement && document.activeElement.blur()")
                await pg.wait_for_timeout(300)
                await pg.screenshot(path=str(OUT / f"{dev}-{name}.png"))
            # Setup: name the home team and face the computer
            await pg.fill("input[data-t='0']", "Ridgeview")
            await pg.fill("input[data-t='1']", "Harbor City")
            await pg.click("[data-a=ctrl][data-v='1'][data-t='1']")
            await pg.wait_for_timeout(200)
            await shot("05-setup")
            await pg.click("[data-a=kickoff]"); await pg.wait_for_timeout(500)
            got = set()
            for i in range(900):
                hd = (await heading()).upper()
                if "CALL YOUR PLAY" in hd and "01-call" not in got and i > 12:
                    # pick a play so the call sheet shows a selection
                    await pg.evaluate("document.querySelector('#app [data-a=pick][data-v=pa]')?.click()"); await pg.wait_for_timeout(250)
                    await shot("01-call"); got.add("01-call")
                if "READ THE" in hd and "02-read" not in got and i > 12:
                    await shot("02-read"); got.add("02-read")
                if "03-result" not in got and await pg.evaluate("!!document.querySelector('#app .headline')") and i > 20:
                    await shot("03-result"); got.add("03-result")
                if "04-halftime" not in got and await pg.evaluate("!!document.querySelector('#app [data-a=half]')"):
                    await shot("04-halftime"); got.add("04-halftime")
                if len(got) >= 4: break
                a = await pg.evaluate(STEP)
                if not a: print("stuck at", hd); break
                await pg.wait_for_timeout(120)
            # The play-by-play and box score at the bottom of any screen
            await pg.evaluate("document.querySelectorAll('#app details').forEach(d => d.open = true)")
            await shot("06-log", "#app details", 12)
            print(dev, "last:", await heading())
            print(dev, "screens:", sorted(got), "| errors:", errs)
            await ctx.close()
        await b.close()

asyncio.run(main())
