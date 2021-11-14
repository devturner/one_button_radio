import RPi.GPIO as GPIO
import os
import signal
import sys
import time

os.environ['DISPLAY'] = ':0'

import pyautogui

BUTTON_PIN = 18
LED_PIN = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)

	def exit_gracefully(self, *args):
		GPIO.output(LED_PIN, False)
		GPIO.cleanup()
		# sys.exit(0)
		self.kill_now = True


def main():
	while True:
		GPIO.output(LED_PIN, True)
		GPIO.output(LED_PIN, GPIO.LOW)
		input_state = GPIO.input(18)
        
		if input_state == False:
			print('Button Pressed')
			GPIO.output(LED_PIN, GPIO.HIGH)
			pyautogui.press('space')
			time.sleep(.3)
			GPIO.output(LED_PIN, GPIO.LOW)
			time.sleep(.7)


if __name__ == '__main__':
	GPIO.output(LED_PIN, False)
	time.sleep(45)
	killer = GracefulKiller()
	while not killer.kill_now:
		main()
	