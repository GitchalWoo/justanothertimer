# Daily Timer ⏱️

A simple countdown timer for daily standups. Stays on top of other windows so it's visible during screen sharing.

## Usage

1. Open `DailyTimer.app`
2. Click **[ Start ]** to begin countdown
3. Click **[ Restart ]** anytime to reset

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
