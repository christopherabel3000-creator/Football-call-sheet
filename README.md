# Gridiron Duel

A turn-based football coordinator game. Each coach picks their personnel and calls a play on offense or defense, then the snap is simulated.

## Status

**Live on itch.io** (launched October 31, 2026) at [playbyear.itch.io/gridiron-duel](https://playbyear.itch.io/gridiron-duel). `itchUrl` in `site-config.js` points there, so online invites from the itch version open that page with the game code.

**iPhone app:** being prepared for the App Store (November 2026), the same way as Friday to Sunday, Shardkin, Hidden Ranks and Salvo Command. The store text, reviewer notes and privacy answers are in [appstore/listing.md](appstore/listing.md). The website, itch.io and the app all share one database, so a player on any of them can join a game from the others.

## How to play

**Online:** tap **Create a game**, set up your team, and send your friend the invite link (or the 4-letter code). They pick their team and join, then you kick off. Each of you plays on your own phone.

**One phone:** set up both teams on the start screen and pass the phone between calls. Either team can be coached by the computer.

The **How to play** button at the top of every screen explains the rules without leaving the game.

## What's in the game

- Offensive and defensive playbooks with matchup edges
- Personnel packages (10, 11, 12, 21, 13, Jumbo vs. Base, Nickel, Dime, Goal Line)
- Audibles at the line, and defenses that choose whether to show their real look or disguise it as another (a good fake baits a bad audible, but rotating late costs a step at the snap)
- Three ways to punt: a regular punt, Pin it deep (a high, short kick aimed to drop inside the 10; overkick it and it's a touchback) or Boom it (about 6 yards longer and it rolls, but it outkicks the coverage, so big returns and return touchdowns are likelier). The computer pins you from around midfield and booms it when it's backed up deep
- Punts, field goals, fakes, PATs and two-point tries, and onside kicks at any point in the game (the 2026 pro rule)
- Game clock with timeouts, kneel-downs and the two-minute warning. Spikes and sideline routes open up in the last two minutes of each half and of the 2nd, 4th and 6th overtime periods
- Run the clock: in the 4th quarter, the team with the lead can use 36 to 39 seconds between plays. It can't be combined with no huddle or a spike, and computer coordinators always do it with a 4th-quarter lead
- Overtime works like pro playoff overtime: both teams are guaranteed the ball (the clock running out doesn't take it away), then sudden death, and periods keep going until there's a winner. Once the other team has had its possession and a field goal would win it, the field goal unit can come out on any down
- Penalties, play log and box score
- Computer difficulty: Rookie (loose play calls, no scouting, audibles or disguises, a step slow), Pro (reads the situation and charts your tendencies) and All-Pro (learns your habits fast, counters hard, executes a little better)
- Halftime scouting report: each team's first-half calls by down and distance, what worked and what didn't, audible and disguise rates, and the habits worth attacking
- Team identities: each team picks an offensive style (Balanced, Air Raid, Ground & Pound, West Coast) and a defensive style (Balanced, Blitz-Happy, No-Fly Zone, Run Stuffers). Styles tilt the matchups, and the computer coaches to its own style. In Play vs. Computer the computer gets a surprise identity unless you pick one.
- Screen reader support: each new screen moves VoiceOver to its heading or play result, the scoreboard and field are read as plain sentences, and timeouts and other in-place changes are announced

## How online play works

The game state lives in a Firebase Realtime Database under `games/<CODE>`. Whoever makes a decision runs the play on their own phone and saves the new state; the other phone picks it up and redraws. A save only goes through if nobody else saved first, so the two phones always agree.

- `firebase-config.js` holds the Firebase project settings (not secret).
- `database.rules.json` holds the database security rules to paste into the Firebase console (Realtime Database → Rules → Publish). This Firebase project, `call-sheet-football`, is Gridiron Duel's own. [Forty-Two Fronts](https://github.com/christopherabel3000-creator/Forty-Two-Fronts) (`fortyTwoFronts/<CODE>`) and [Sovereign Fire](https://github.com/christopherabel3000-creator/Sovereign-Fire) (`sovereignFire/<CODE>`) also keep their online games here for now, so the file has a section for each. Hidden Ranks, Shardkin and Friday to Sunday have moved to Firebase projects of their own; their old sections (`hiddenRanks`, `shardkinDuels`, `shardkinSaves`, `fridayToSundaySaves`) stay so saves made before the move can still be found. Always paste the whole file, or the other games will stop working online. The rules only accept well-formed saves, require each save to be exactly one version newer than the last (so nobody can rewind or wipe a game), and only allow deleting games nobody has touched in 7 days. Cloud saves can't be deleted.
- Each time someone creates a game, their phone also deletes up to 20 games that have sat untouched for over a week, so old games don't pile up.
- If a phone loses its connection mid-game, a banner says so, and the game picks up again when it reconnects.
- Every save carries the game's version number (`BUILD` near the top of the script in `index.html`). A phone that opens a game saved by a newer version stops and asks its player to reload, so two phones never play one game under different rules.
- A coach's seat is tied to an ID saved in the browser. If a phone loses it (a different phone, cleared browser data, or iPhone Safari wiping storage for games inside itch.io's frame), the coach types the game code and taps "I'm the ... coach" (or "I created this game" before the friend joins). Whichever phone had the seat switches to watching.

## Play counts

The game keeps anonymous play counts in the shared database under `gridironStats/<day>/<site>`. Each day (Eastern time) and site (`itch`, `github`, `app` for the iPhone app, or `other`) has a count of games started and finished for each mode (`online`, `local` for one phone, `watch` for computer against computer, and `cpu_rookie`, `cpu_pro` and `cpu_allpro`), plus `dev/<id>` for each random device ID seen that day, for a rough count of players. An online game counts once, on the phone that kicks it off and the phone that plays the final snap. Nothing about the players or the game itself is stored. The counts can be read by anyone, and the rules only let a count go up by one and a device ID be added once.

## Publishing on itch.io

1. Zip `index.html`, `firebase-config.js`, `site-config.js`, `privacy.html`, `support.html` and the `fonts`, `icons` and `vendor` folders, with no folder around them (the zip opens straight to `index.html`).
2. On itch.io, create a new project, set **Kind of project** to **HTML**, upload the zip and tick **This file will be played in the browser**.
3. Set the embed size to about 420 × 860 and turn on **Mobile friendly**, **Fullscreen button** and **Enable scrollbars** (most screens are taller than 860).
4. Once the page has its address, put it in `site-config.js` as `itchUrl` and upload a fresh zip. Online invites from the itch version then point to that page and include the game code (on itch, friends join by typing the code). The update screen also uses it to reload the whole itch page. The address is chosen on itch.io's new-project form, so if you put it in `site-config.js` before zipping, one upload is enough.
5. Before announcing it, play a quick online game on the itch page from two phones. On an iPhone, close and reopen the page mid-game and check that you can take your seat back with the game code.

## Releasing an update

1. Raise `BUILD` near the top of the script in `index.html` by 1. The How to play screen shows it as the version number.
2. Merge to `main`. GitHub Pages updates on its own.
3. Zip the same files and folders and upload the zip to itch.io in place of the old one, right away. Both copies share one database, so a player on either one can join a game from the other.
4. Open How to play on both copies and check that they show the new version.
5. If the change affects how a game plays (anything that raised `BUILD`), send the iPhone app an update too, the same day if you can: Actions tab, **iPhone app**, **Run workflow**, then submit the new TestFlight build in App Store Connect. Until Apple approves it, a player in the app who joins a game saved by the newer website is asked to update from the App Store.

## The iPhone app

The App Store app wraps the same game with Capacitor. Nothing in the game needs a build step; the app's packages are only for the wrapper.

- `capacitor.config.json`, `ios/` and `package.json`: the Capacitor project (bundle ID `com.playbyear.gridironduel`).
- `scripts/build-www.js` copies the game's own files into `www/`, the folder the app is built from.
- `.github/workflows/ios.yml` builds the app on GitHub's Macs. Every push checks it still builds; **Run workflow** in the Actions tab builds a signed copy and sends it to TestFlight. It needs the four App Store Connect secrets (`APPLE_TEAM_ID`, `ASC_KEY_ID`, `ASC_ISSUER_ID`, `ASC_KEY_P8`) in the repo's Settings, Secrets and variables, Actions, the same as the other apps.
- Fonts (`fonts/`) and the Firebase library (`vendor/firebase/`) are kept with the game, so nothing loads from outside.
- In the app, invite links point to the GitHub Pages site, and the app remembers the online game it's in so it rejoins when it's opened again.
- `privacy.html` and `support.html` are linked from the bottom of the game and used as the App Store's privacy policy and support URLs.
- `tools/icon.py` draws the app icon, launch image and web icons from `tools/icon.html`. `tools/screenshots.py` plays a quick game against the computer and saves the App Store screenshots in `appstore/screenshots/`.
