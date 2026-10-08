# Gridiron Duel

A turn-based football coordinator game. Each coach picks their personnel and calls a play on offense or defense, then the snap is simulated.

## How to play

**Online:** tap **Create a game**, set up your team, and send your friend the invite link (or the 4-letter code). They pick their team and join, then you kick off. Each of you plays on your own phone.

**One phone:** set up both teams on the start screen and pass the phone between calls. Either team can be coached by the computer.

## What's in the game

- Offensive and defensive playbooks with matchup edges
- Personnel packages (10, 11, 12, 21, 13, Jumbo vs. Base, Nickel, Dime, Goal Line)
- Audibles at the line, with defenses that sometimes disguise their look
- Punts, field goals, fakes, PATs and two-point tries, onside kicks
- Game clock with timeouts, spikes, kneel-downs and the two-minute warning
- Penalties, play log and box score

## How online play works

The game state lives in a Firebase Realtime Database under `games/<CODE>`. Whoever makes a decision runs the play on their own phone and saves the new state; the other phone picks it up and redraws. A save only goes through if nobody else saved first, so the two phones always agree.

- `firebase-config.js` holds the Firebase project settings (not secret).
- `database.rules.json` holds the database security rules to paste into the Firebase console.
