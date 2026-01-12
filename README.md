# Daily Timer ⏱️

A simple countdown timer for daily standups. Stays on top of other windows so it's visible during screen sharing.

## Features

- **Always on top** - Window stays visible during screen sharing
- **Overtime tracking** - Timer continues counting into negative time after reaching zero
- **Color indicators**:
  - 🟢 Green: Normal countdown
  - 🟠 Orange: Warning (15 seconds or less remaining)
  - 🔴 Red: Overtime (time has run out)
- **Dark theme** - Easy on the eyes

## Usage

1. Open `DailyTimer.app`
2. Click **[ Start ]** to begin countdown
3. Click **[ Restart ]** anytime to reset
4. When time runs out, the timer turns red and continues counting negative time

## Configuration

Edit `timer.py` line 12 to change the countdown duration:

```python
COUNTDOWN_SECONDS = 60  # seconds
```

## Building

Requires Python 3 with tkinter.

```bash
# Install tkinter (if needed)
brew install python-tk

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pyinstaller

# Build the app
pyinstaller --onefile --windowed --name "DailyTimer" timer.py
```

App will be in `dist/DailyTimer.app`

## Running without building

```bash
python3 timer.py
```

## macOS Gatekeeper Workaround

If macOS shows "Apple could not verify" warning when opening the app, run:

```bash
xattr -cr /Applications/DailyTimer.app
```

Then open the app again.

