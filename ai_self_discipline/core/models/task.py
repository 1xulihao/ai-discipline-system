# models/task.py
from PyQt5.QtCore import QTime


class Task:
    def __init__(self, title, start_time_str, duration_minutes,
                 start_mode="fixed_start",
                 complete_mode="duration_based",
                 repeat_mode="one_time",
                 track_mode="user_mark"):
        self.title = title
        self.start_time_str = start_time_str  # e.g., "10:30"
        self.duration_minutes = duration_minutes
        self.start_mode = start_mode
        self.complete_mode = complete_mode
        self.repeat_mode = repeat_mode
        self.track_mode = track_mode
        # 以下是新加的属性
        self.is_completed = False
        self.has_been_notified = False
        self.start_time = QTime.fromString(start_time_str, "HH:mm")

    def to_dict(self):
        return {
            "title": self.title,
            "start_time": self.start_time_str,
            "duration_minutes": self.duration_minutes,
            "start_mode": self.start_mode,
            "complete_mode": self.complete_mode,
            "repeat_mode": self.repeat_mode,
            "track_mode": self.track_mode
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            start_time_str=data["start_time"],
            duration_minutes=data["duration_minutes"],
            start_mode=data.get("start_mode", "fixed_start"),
            complete_mode=data.get("complete_mode", "duration_based"),
            repeat_mode=data.get("repeat_mode", "one_time"),
            track_mode=data.get("track_mode", "user_mark")
        )
    
    def should_start(self, current_qtime):
        return (
            self.start_mode == "fixed_start" and
            not self.is_completed and
            not self.has_been_notified and
            current_qtime.hour() == self.start_time.hour() and
            current_qtime.minute() == self.start_time.minute()
        )

    def mark_as_complete(self):
        self.is_completed = True

    def postpone(self, minutes):
        self.start_time = self.start_time.addSecs(minutes * 60)
        self.start_time_str = self.start_time.toString("HH:mm")
        self.has_been_notified = False