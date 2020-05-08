import asyncio
import threading



def target():
    print(threading.current_thread())
    loop = asyncio.get_event_loop()
    print(loop)


if __name__ == '__main__':
    print(threading.current_thread())
    threading.Thread(target=target, name='thd-1', args=()).start()
    import time
    time.sleep(0.5)
    print(asyncio.get_event_loop())