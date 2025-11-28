#!/usr/bin/env python3
"""
Simple Daily Timer App
- Click button to start countdown
- Window stays on top
- Click again to restart
"""

import tkinter as tk

# ============================================
# CHANGE THIS VALUE TO SET YOUR TIMER (seconds)
COUNTDOWN_SECONDS = 60
# ============================================


class TimerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Daily Timer")
        
        # Keep window always on top
        self.root.attributes("-topmost", True)
        
        # Window size and position
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        
        # Dark background
        self.root.configure(bg="#2d2d2d")
        
        # Time remaining
        self.time_left = COUNTDOWN_SECONDS
        self.running = False
        self.timer_id = None
        
        # Timer display
        self.time_label = tk.Label(
            self.root,
            text=self.format_time(self.time_left),
            font=("Helvetica", 72, "bold"),
            fg="#00ff00",
            bg="#2d2d2d"
        )
        self.time_label.pack(pady=20)
        
        # Start/Restart button - simple label that acts as button
        self.start_button = tk.Label(
            self.root,
            text="[ Start ]",
            font=("Helvetica", 28),
            fg="white",
            bg="#2d2d2d",
            cursor="hand2"
        )
        self.start_button.pack(pady=20)
        self.start_button.bind("<Button-1>", lambda e: self.start_timer())
        
    def format_time(self, seconds):
        """Format seconds as MM:SS"""
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins}:{secs:02d}"
    
    def start_timer(self):
        """Start or restart the timer"""
        # Cancel any existing timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        # Reset time
        self.time_left = COUNTDOWN_SECONDS
        self.running = True
        self.start_button.config(text="[ Restart ]")
        self.time_label.config(fg="#00ff00")
        
        # Start countdown
        self.countdown()
    
    def countdown(self):
        """Countdown logic"""
        if self.time_left > 0 and self.running:
            self.time_label.config(text=self.format_time(self.time_left))
            
            # Change color when low on time
            if self.time_left <= 10:
                self.time_label.config(fg="#ff4444")
            elif self.time_left <= 30:
                self.time_label.config(fg="#ffaa00")
            
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            # Timer finished
            self.time_label.config(text="0:00", fg="#ff4444")
            self.running = False
    
    def run(self):
        """Start the app"""
        self.root.mainloop()


if __name__ == "__main__":
    app = TimerApp()
    app.run()
