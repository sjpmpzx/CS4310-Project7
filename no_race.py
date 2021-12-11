import random
import threading
import time

n = 64
k = 16
t = 3
f = 0
e = 64
buffer = [0 for _ in range(n)]

def producer_thread():
    global e
    global f
    next_in = 0

    while True:
        k1 = random.randint(0, k)
        for i in range(0, k1):

            # P(e)
            while True:
                if e != 0:
                    e -= 1
                    print("Producer P(e) executed", f" f:{f} e:{e}")
                    break

            buffer[(next_in + i) % n] += 1

            # V(f)
            f += 1
            print("Producer V(f) executed", f" f:{f} e:{e}")

        next_in = (next_in + k1) % n
        t1 = random.randint(0, t)
        print(f"Producer: {buffer}")
        time.sleep(t1)


def consumer_thread():
    global e
    global f
    next_out = 0

    while True:
        t2 = random.randint(0, t)
        time.sleep(t2)
        k2 = random.randint(0, k)
        for i in range(0, k2):

            # P(f)
            while True:
                if f != 0:
                    f -= 1
                    print("Consumer P(f) executed", f" f:{f} e:{e}")
                    break

            data = buffer[(next_out + i) % n]
            if data > 1:
                print("Race condition occurs! Consumer is too slow!")
                return
            elif data == 0:
                print("Race condition occurs! Producer is too slow!")
                return

            buffer[(next_out + i) % n] = 0

            # V(e)
            e += 1
            print("Consumer V(e) executed", f" f:{f} e:{e}")

        print(f"Consumer: {buffer}")
        next_out = (next_out + k2) % n


if __name__ == "__main__":
    producer = threading.Thread(target=producer_thread, daemon=True)
    consumer = threading.Thread(target=consumer_thread)
    producer.start()
    consumer.start()
