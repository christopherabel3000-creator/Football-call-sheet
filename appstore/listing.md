# App Store listing: Gridiron Duel

Everything to paste into App Store Connect for version 1.0. Each section shows Apple's character limit.

## Name (30 characters at most)

Gridiron Duel: Play Caller

"Gridiron Duel" alone was already taken on the App Store (Nov 25 2026). The name under the icon on the home screen is still "Gridiron Duel" (CFBundleDisplayName in Info.plist).

## Subtitle (30)

Football play-calling duel

## Promotional text (170, can be changed any time without a review)

Call the plays, read the defense, outcoach your friend. Play the computer, pass one phone, or play online. Built to be played with VoiceOver.

## Description (4,000)

Gridiron Duel puts you in the coordinator's chair. Each snap, both coaches pick their personnel and call a play without seeing the other's call. Then the ball is snapped and the play runs. Win the matchups, manage the clock, and outcoach the other side.

CALL THE PLAY
Pick your personnel, from four-wide 10 personnel to a Jumbo goal-line package, then call an inside run, outside zone, draw, screen, quick game, mesh, deep shot or play-action. On defense, answer with a base 4-3, a run blitz, man coverage, Cover 2 or Cover 3 zone, a zone blitz, an all-out blitz or prevent. Every call beats some calls and loses to others.

READ THE DEFENSE
At the line you see the defense's look and can audible to a better play. But defenses can disguise their look, and a good fake baits a bad audible.

EVERY SITUATION COVERED
Punts, including Pin it deep and Boom it. Field goals, fakes, extra points, two-point tries and onside kicks. Timeouts, kneel-downs, spikes, sideline routes, the two-minute warning and running out the clock with a lead. Penalties, and overtime where both teams are guaranteed the ball.

A COMPUTER THAT SCOUTS YOU
Pick Rookie, Pro or All-Pro. The tougher computer coordinators chart your tendencies by down and distance and start calling the counter, so stay unpredictable. A halftime scouting report shows both sides' habits and what beats them.

PLAY A FRIEND
Create an online game and send your friend a four-letter code or an invite link. Each of you calls plays on your own phone, from anywhere. Or set up both teams and pass one phone back and forth.

MADE FOR VOICEOVER
Gridiron Duel was designed from the start to be fully playable with VoiceOver. Every screen starts at its heading or the play result, every call is a plain button that reads in full, and results are announced as they happen. The play-by-play and box score keep the whole game in order.

SIMPLE AND PRIVATE
Games against the computer and on one phone work offline. No ads. Nothing to buy. No accounts.

## Keywords (100, commas with no spaces)

football,play calling,coach,coordinator,playbook,two player,online,turn based,voiceover,blind

Never add the name of any real league, team or player.

## Other fields

- Primary category: Games. Subcategories: Sports, Strategy.
- Secondary category: (none needed)
- Support URL: https://christopherabel3000-creator.github.io/Football-call-sheet/support.html
- Marketing URL: (optional, leave blank)
- Privacy policy URL: https://christopherabel3000-creator.github.io/Football-call-sheet/privacy.html
- Copyright: 2026 Christopher Abel
- Version: 1.0
- Bundle ID: com.playbyear.gridironduel
- SKU: gridironduel
- Apple ID: 6839418589 (created Nov 25 2026)

## Screenshots

`appstore/screenshots/`: six for iPhone 6.3" (1206 x 2622) and six for iPad 13" (2064 x 2752), in this order:

1. Calling a play on offense
2. Reading the defense at the line, with an audible
3. A play result
4. The halftime scouting report
5. The start screen: play the computer or a friend online
6. The box score and play-by-play

They're taken by `tools/screenshots.py` (see the README).

## Content rights

No, the app does not contain, show, or access third-party content. The name, artwork, text and code are original. Teams are named by the players; the game uses no real league, team or player names. The three fonts are used under the SIL Open Font License.

## Age rating

Answer None or No to everything. It's a football strategy game shown as a scoreboard, a field diagram and text: there are no injuries, violence or realistic players shown.

Questions to read carefully when filling in the form:

- User-Generated Content: No. Players type only their own team names, which only their opponent sees; there are no messages or chat.
- Messaging and Chat: No.
- Contests: None.

## App Privacy

- Does the app collect data? Yes, because of optional online games and the anonymous play counts.
- Data type 1: User Content, then Gameplay Content. (Each online game's team names, settings and play calls.) Used for: App Functionality. Linked to the user's identity: No. Used for tracking: No.
- Data type 2: Usage Data, then Product Interaction. (Daily counts of games started and finished, by where and how they were played.) Used for: Analytics. Linked: No. Tracking: No.
- Data type 3: Identifiers, then Device ID. (The random code the game makes up for each device, used to keep a coach's seat in an online game and for a rough daily count of players. It isn't the iPhone's advertising identifier.) Used for: App Functionality and Analytics. Linked: No. Tracking: No.
- Nothing else is collected: no ads, no names, no accounts. The contact form opens in Safari, outside the app.

## Accessibility (App Store accessibility labels)

VoiceOver only, for iPhone and iPad, the same as Christopher's other apps. Don't add any other label (such as Dark Interface or Reduced Motion) unless he asks for it.

## Notes for the reviewer

Apple asks every new app for six things in this field: a screen recording made on a real iPhone, and answers 2 to 6 below. Only the recording link changes.

Gridiron Duel is a complete turn-based football strategy game for one or two players, built to be fully playable with VoiceOver by a developer who plays with a screen reader. The build was tested on a physical iPhone through TestFlight before submission.

1. SCREEN RECORDING
Recorded on a physical iPhone running the latest iOS, starting from launching the app: (paste the YouTube link here)
The voice heard in the recording is VoiceOver, since the developer plays the game with a screen reader.
The app has no account registration or login, no user-generated content (players type only their own team names, seen only by their opponent; there are no messages or chat), and no paid content or purchases. So those flows don't exist to show.

2. PURPOSE AND AUDIENCE
A turn-based football strategy game. Each snap, both coaches choose personnel and call a play without seeing the other's call, then the play is simulated and the result announced. It can be played against a computer opponent at three difficulty levels, by two people passing one device, or online between two friends who share a four-letter code. It is for football and strategy fans, and especially for blind and low-vision players: it was designed for VoiceOver from the start.

3. HOW TO USE IT
No account, login or sample files are needed. On the first screen, tap Play vs. Computer. Choose to receive or defer at the coin toss, then pick a personnel group, tap a play, and tap Lock in. At the line, tap the button with your play's name to snap the ball (or pick another play to audible). The rules are under How to play at the top of every screen.
To try online play with one device: tap Create a game, then Create game. It shows a four-letter code and an invite link. Open the link in a browser on a second device or a computer to join as the other coach (the website and the app can play each other).

4. EXTERNAL SERVICES
Only one: Google Firebase Realtime Database, used for online games between two friends who share a four-letter code, and for anonymous daily counts of games played (no names or game content). There are no authentication services, payment processors, ad networks, third-party analytics or AI services. The whole game is bundled in the app, and games against the computer run offline.

5. REGIONS
The app works the same in every region. It is in English only. There is no region-specific content or behavior.

6. REGULATED INDUSTRIES AND THIRD-PARTY MATERIAL
Not applicable. The app is not in a regulated industry. It contains no third-party or licensed material: the name, artwork, text and code are original, and it uses no real league, team or player names. The three fonts are used under the SIL Open Font License.

## Price and availability

Free. Every country and region except the 27 European Union countries (selling there needs a trader declaration) and China mainland (games there need extra filings). Released automatically once approved.

## Encryption

The app only uses standard HTTPS, so it's exempt. `ITSAppUsesNonExemptEncryption` is already set to NO in Info.plist, so App Store Connect won't ask.
