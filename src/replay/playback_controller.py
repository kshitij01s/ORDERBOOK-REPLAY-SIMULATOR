import time
import threading

class PlaybackController:
    def __init__(self, ticks):
        self.ticks = ticks  # list of ticks sorted by timestamp
        self.speed = 1.0    # 1x real-time speed
        self.index = 0
        self.paused = True
        self.lock = threading.Lock()
        self._play_thread = None

    def set_speed(self, speed: float):
        with self.lock:
            self.speed = speed

    def pause(self):
        with self.lock:
            self.paused = True

    def resume(self):
        with self.lock:
            if not self.paused:
                return
            self.paused = False
        self._start_playback_thread()

    def _start_playback_thread(self):
        if self._play_thread and self._play_thread.is_alive():
            return
        self._play_thread = threading.Thread(target=self._playback_loop, daemon=True)
        self._play_thread.start()

    def _playback_loop(self):
        while self.index < len(self.ticks):
            with self.lock:
                if self.paused:
                    break
                current_tick = self.ticks[self.index]
                next_tick = self.ticks[self.index + 1] if self.index + 1 < len(self.ticks) else None
                self.index += 1

            # Deliver current_tick here via callback or queue (not implemented here)

            if next_tick:
                sleep_time = (next_tick['timestamp'] - current_tick['timestamp']) / 1000 / self.speed
                if sleep_time > 0:
                    time.sleep(sleep_time)
            else:
                break

    def get_current_tick(self):
        with self.lock:
            if self.index < len(self.ticks):
                return self.ticks[self.index]
            return None

    def seek(self, timestamp):
        # Move index to the first tick >= timestamp
        with self.lock:
            for i, tick in enumerate(self.ticks):
                if tick['timestamp'] >= timestamp:
                    self.index = i
                    break
