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
- Game clock with timeouts, spikes, kneel-downs and the two-minute warning
- Penalties, play log and box score
- Computer difficulty: Rookie (loose play calls, no scouting, audibles or disguises, a step slow), Pro (reads the situation and charts your tendencies) and All-Pro (learns your habits fast, counters hard, executes a little better)
- Halftime scouting report: each team's first-half calls by down and distance, what worked and what didn't, audible and disguise rates, and the habits worth attacking
- Team identities: each team picks an offensive style (Balanced, Air Raid, Ground & Pound, West Coast) and a defensive style (Balanced, Blitz-Happy, No-Fly Zone, Run Stuffers). Styles tilt the matchups, and the computer coaches to its own style. In Play vs. Computer the computer gets a surprise identity unless you pick one.
- Screen reader support: each new screen moves VoiceOver to its heading or play result, the scoreboard and field are read as plain sentences, and timeouts and other in-place changes are announced

## How online play works

The game state lives in a Firebase Realtime Database under `games/<CODE>`. Whoever makes a decision runs the play on their own phone and saves the new state; the other phone picks it up and redraws. A save only goes through if nobody else saved first, so the two phones always agree.

- `firebase-config.js` holds the Firebase project settings (not secret).
- `database.rules.json` holds the database security rules to paste into the Firebase console (Realtime Database → Rules → Publish). This Firebase project is shared with [Hidden Ranks](https://github.com/christopherabel3000-creator/Hidden-Ranks), whose games live under `hiddenRanks/<CODE>`, so the file has a section for each game. Always paste the whole file, and keep it the same as the copy in the Hidden Ranks repo, or the other game will stop working online. They only accept well-formed game saves, require each save to be exactly one version newer than the last (so nobody can rewind or wipe a game), and only allow deleting games nobody has touched in 7 days.
- Each time someone creates a game, their phone also deletes up to 20 games that have sat untouched for over a week, so old games don't pile up.
- If a phone loses its connection mid-game, a banner says so, and the game picks up again when it reconnects.

## Publishing on itch.io

1. Zip `index.html`, `firebase-config.js` and `site-config.js` (no folder inside the zip).
2. On itch.io, create a new project, set **Kind of project** to **HTML**, upload the zip and tick **This file will be played in the browser**.
3. Set the embed size to about 420 × 860 and turn on **Mobile friendly** and **Fullscreen button**.
4. Once the page has its address, put it in `site-config.js` as `itchUrl` and upload a fresh zip. Online invites from the itch version then point to that page and include the game code (on itch, friends join by typing the code).
