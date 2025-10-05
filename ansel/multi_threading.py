import threading
import time

def walk_dog(first, last):
	time.sleep(10)
	print(f"Walk the dog {first} {last}")

def get_mail():
	time.sleep(4)
	print("go get the mail")

def finish_work():
	time.sleep(6)
	print("you can finish your work")


chore1 = threading.Thread(target = walk_dog, args = ("Bobby", "Doo"))
chore1.start()

chore2 = threading.Thread(target = get_mail)
chore2.start()

chore3 = threading.Thread(target = finish_work)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chore are complete!")