import signal
import sys
import time

class Main:
    exit = False
    running = False

    def signal_handler(self, signal, frame):
        print("OK, exiting.")
        if self.running:
            self.exit = True
        else:
            sys.exit(0)

    def run(self):
        self.running = True
        print("->")
        time.sleep(1)
        print("-<")
        self.running = False
        if self.exit:
            sys.exit(0)
        time.sleep(10)

m = Main()

signal.signal(signal.SIGINT, m.signal_handler)

while True:
    m.run()
