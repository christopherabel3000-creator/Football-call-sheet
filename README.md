# Gridiron Duel

A turn-based football coordinator game. Each coach picks their personnel and calls a play on offense or defense, then the snap is simulated.

## How to play

**Online:** tap **Create a game**, set up your team, and send your friend the invite link (or the 4-letter code). They pick their team and join, then you kick off. Each of you plays on your own phone.

**One phone:** set up both teams on the start screen and pass the phone between calls. Either team can be coached by the computer.

The **How to play** button at the top of every screen explains the rules without leaving the game.

## What's in the game

- Offensive and defensive playbooks with matchup edges
- Personnel packages (10, 11, 12, 21, 13, Jumbo vs. Base, Nickel, Dime, Goal Line)
- Audibles at the line, and defenses that choose whether to show their real look or disguise it as another (a good fake baits a bad audible, but rotating late costs a step at the snap)
- Punts, field goals, fakes, PATs and two-point tries, onside kicks
- Game clock with timeouts, kneel-downs and the two-minute warning. Spikes and sideline routes open up in the last two minutes of each half, and in the last two minutes of any overtime period for a team that's behind
- Overtime: both teams get the ball, then sudden death. Once the other team has had its possession and a field goal would win it, the field goal unit can come out on any down
- Penalties, play log and box score
- Computer difficulty: Rookie (loose play calls, no scouting, audibles or disguises, a step slow), Pro (reads the situation and charts your tendencies) and All-Pro (learns your habits fast, counters hard, executes a little better)
- Halftime scouting report: each team's first-half calls by down and distance, what worked and what didn't, audible and disguise rates, and the habits worth attacking
- Team identities: each team picks an offensive style (Balanced, Air Raid, Ground & Pound, West Coast) and a defensive style (Balanced, Blitz-Happy, No-Fly Zone, Run Stuffers). Styles tilt the matchups, and the computer coaches to its own style. In Play vs. Computer the computer gets a surprise identity unless you pick one.
- Screen reader support: each new screen moves VoiceOver to its heading or play result, the scoreboard and field are read as plain sentences, and timeouts and other in-place changes are announced

## How online play works

The game state lives in a Firebase Realtime Database under `games/<CODE>`. Whoever makes a decision runs the play on their own phone and saves the new state; the other phone picks it up and redraws. A save only goes through if nobody else saved first, so the two phones always agree.

- `firebase-config.js` holds the Firebase project settings (not secret).
- `database.rules.json` holds the database security rules to paste into the Firebase console (Realtime Database → Rules → Publish). This Firebase project is shared with [Hidden Ranks](https://github.com/christopherabel3000-creator/Hidden-Ranks), whose games live under `hiddenRanks/<CODE>`, and [Shardkin: Eight Realms](https://github.com/christopherabel3000-creator/Shardkin-Eight-Realms), whose live duels live under `shardkinDuels/<CODE>` and cloud saves under `shardkinSaves/<KEY>`, so the file has a section for each. Always paste the whole file, and keep it the same as the copies in the Hidden Ranks and Shardkin repos, or the other games will stop working online. They only accept well-formed saves, require each save to be exactly one version newer than the last (so nobody can rewind or wipe a game), and only allow deleting games nobody has touched in 7 days. Shardkin's cloud saves can't be deleted.
- Each time someone creates a game, their phone also deletes up to 20 games that have sat untouched for over a week, so old games don't pile up.
- If a phone loses its connection mid-game, a banner says so, and the game picks up again when it reconnects.
- Every save carries the game's version number (`BUILD` near the top of the script in `index.html`). A phone that opens a game saved by a newer version stops and asks its player to reload, so two phones never play one game under different rules.
- A coach's seat is tied to an ID saved in the browser. If a phone loses it (a different phone, cleared browser data, or iPhone Safari wiping storage for games inside itch.io's frame), the coach types the game code and taps "I'm the ... coach" (or "I created this game" before the friend joins). Whichever phone had the seat switches to watching.

## Publishing on itch.io

1. Zip `index.html`, `firebase-config.js` and `site-config.js` (no folder inside the zip).
2. On itch.io, create a new project, set **Kind of project** to **HTML**, upload the zip and tick **This file will be played in the browser**.
3. Set the embed size to about 420 × 860 and turn on **Mobile friendly** and **Fullscreen button**.
4. Once the page has its address, put it in `site-config.js` as `itchUrl` and upload a fresh zip. Online invites from the itch version then point to that page and include the game code (on itch, friends join by typing the code). The update screen also uses it to reload the whole itch page.

## Releasing an update

1. Raise `BUILD` near the top of the script in `index.html` by 1. The How to play screen shows it as the version number.
2. Merge to `main`. GitHub Pages updates on its own.
3. Zip the same three files and upload the zip to itch.io in place of the old one, right away. Both copies share one database, so a player on either one can join a game from the other.
4. Open How to play on both copies and check that they show the new version.
