# Gridiron Duel: saves the app icon (1024 x 1024), the launch image (2732 x 2732) and the web icons
# from tools/icon.html. Run from the repo folder: python3 tools/icon.py
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = (ROOT / "tools" / "icon.html").as_uri()
APPICON = ROOT / "ios/App/App/Assets.xcassets/AppIcon.appiconset/AppIcon-512@2x.png"
SPLASH = ROOT / "ios/App/App/Assets.xcassets/Splash.imageset"
TMP = pathlib.Path("/tmp/gd-splash.png")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", args=["--no-sandbox"])
        for path, q, n in ((APPICON, "", 1024), (TMP, "?splash", 2732)):
            pg = await b.new_page(viewport={"width": n, "height": n})
            await pg.goto(PAGE + q)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(path), clip={"x": 0, "y": 0, "width": n, "height": n})
            await pg.close()
        await b.close()
    Image.open(APPICON).convert("RGB").save(APPICON)  # the App Store refuses an icon with transparency
    sp = Image.open(TMP).convert("RGB")
    for name in ("splash-2732x2732.png", "splash-2732x2732-1.png", "splash-2732x2732-2.png"):
        sp.save(SPLASH / name)
    ic = Image.open(APPICON)
    for size, name in ((512, "icon-512.png"), (180, "apple-touch-icon.png"), (32, "favicon-32.png")):
        ic.resize((size, size), Image.LANCZOS).save(ROOT / "icons" / name)

asyncio.run(main())
