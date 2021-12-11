import random
import threading
import time

n = 64
k = 16
t = 3
buffer = [0 for _ in range(n)]

def producer_thread():
    next_in = 0

    while True:
        k1 = random.randint(0, k)
        for i in range(0, k1):
            buffer[(next_in + i) % n] += 1
        next_in = (next_in + k1) % n
        t1 = random.randint(0, t)
        print(f"Producer: {buffer}")
        # print(f"Producer index: {next_in}")
        time.sleep(t1)


def consumer_thread():
    next_out = 0

    while True:
        t2 = random.randint(0, t)
        time.sleep(t2)
        k2 = random.randint(0, k)
        for i in range(0, k2):
            data = buffer[(next_out + i) % n]
            if data > 1:
                print("Race condition occurs! Consumer is too slow!")
                return
            # elif data == 0:
            #     print("Race condition occurs! Producer is too slow!")
            #     return
            buffer[(next_out + i) % n] = 0
        print(f"Consumer: {buffer}")
        next_out = (next_out + k2) % n
        # print(f"Consumer index: {next_out}")


if __name__ == "__main__":
    producer = threading.Thread(target=producer_thread, daemon=True)
    consumer = threading.Thread(target=consumer_thread)
    producer.start()
    consumer.start()
