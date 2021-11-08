import time
import sys

def ft_progress(listy):
	start = time.time()
	for i in listy:
		end = time.time()
		sys.stdout.write("ETA: ")
		sys.stdout.write(str(round(end - start, 2)))
		sys.stdout.write("s [")
		sys.stdout.write(" " * len(str(len(str((i * 100) / len(listy) + 1)))))
		sys.stdout.write(str((i * 100) / len(listy) + 1))
		sys.stdout.write("%] [")
		sys.stdout.write("=" * int(((i * 40) / len(listy))))
		sys.stdout.write(">")
		sys.stdout.write(" " * (40 - (int(((i * 40) / len(listy))))))
		sys.stdout.write("]")
		sys.stdout.write(" " * int(len(str(len(listy))) - len(str(i))))
		sys.stdout.write(str(i + 1))
		sys.stdout.write("/")
		sys.stdout.write(str(len(listy)))

		sys.stdout.flush()
		sys.stdout.write("\b" * (15 + len(str(round(end - start, 2))) + 4 + 40 + len(str(len(listy))) + len(listy)))
		yield i

listy = range(100)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)