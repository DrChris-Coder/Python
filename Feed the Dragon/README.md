Feed the Dragon 🐉🎮

A quick, arcade-style game built with Python and Pygame. Eat coins to rack up points, avoid misses, and see how long you can last as the speed steadily increases.

✨ Features

Smooth player movement (W/↑ and S/↓)

Progressive difficulty: coins accelerate with every catch

Collision detection for scoring

HUD with score, lives, and title banner

Game Over screen with “press any key to continue”

Audio & music for feedback and atmosphere

Custom pixel font for a retro feel

🕹 Controls

Move Up: W or ↑

Move Down: S or ↓

Quit: close the window

▶️ How to Run

Clone the repository:

git clone https://github.com/<YOUR_USERNAME>/feed-the-dragon.git
cd feed-the-dragon


(Optional) Create & activate a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


If you don’t have a requirements.txt yet, you can create one with:

echo pygame>=2.5.0 > requirements.txt


Run the game:

python feed_the_dragon.py

📁 Project Structure
feed-the-dragon/
├─ feed_the_dragon.py
├─ requirements.txt
├─ Feed the Dragon/
│  └─ feed_the_dragon_assets/
│     ├─ dragon_right.png
│     ├─ coin.png
│     ├─ AttackGraffiti.ttf
│     ├─ coin_sound.wav
│     ├─ miss_sound.wav
│     └─ ftd_background_music.wav
└─ README.md


The code expects the assets in:
Feed the Dragon\feed_the_dragon_assets\...
Keep this structure or update the paths in feed_the_dragon.py.

⚙️ Notes on Paths (Cross-Platform Tip)

Paths in the script currently use Windows backslashes. If you plan to support macOS/Linux, consider switching to Python’s os.path.join or pathlib:

from pathlib import Path
ASSETS = Path("Feed the Dragon") / "feed_the_dragon_assets"
font = pygame.font.Font(ASSETS / "AttackGraffiti.ttf", 32)
coin_sound = pygame.mixer.Sound(ASSETS / "coin_sound.wav")

🧪 How Scoring & Difficulty Work

Catch a coin → +1 score and a coin sound plays

Each coin caught → coin speed increases by COIN_ACCELERATION (default 0.5)

Miss a coin (off left edge) → -1 life and a “miss” sound plays

Lose all lives → Game Over screen; press any key to reset

Key game constants in feed_the_dragon.py:

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100
FPS = 60

🛠 Troubleshooting

No audio / mixer errors: Some systems need the mixer pre-init before pygame.init():

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()


Font not found: Ensure AttackGraffiti.ttf is in the assets folder and the path matches.

Black screen: Check that the main loop calls pygame.display.update() and that assets loaded successfully (watch your console for load errors).

🗺 Roadmap (Nice-to-Have Upgrades)

Add background art & parallax scrolling

Animate the dragon & coin sprites

Difficulty modes (Easy/Normal/Hard)

High score persistence (simple JSON file)

Start menu & pause menu

Controller support

Unit tests for core logic

🤝 Contributing

Issues and pull requests are welcome! If you spot bugs or want to add features, feel free to open an issue first to discuss the change.

📜 License

MIT License (recommended for learning projects).
