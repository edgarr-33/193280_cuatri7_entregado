import time
from threading import Thread, Lock
import threading
mutex = Lock()

tenedores = [1,1,1]

def filosofo():
    tenedor = []
    hiloActual = threading.current_thread().getName()
    while True:
        print(f'Filosofo {hiloActual} -------esperando-------')
        time.sleep(2)
        mutex.acquire()
        if len(tenedores) != 0:
            print(f'Filosofo {hiloActual} toma 2 tenedores')
            time.sleep(2)
            tenedor.append(tenedores.pop())
            tenedor.append(tenedores.pop())
            
        try:
            if len(tenedor)==2:
                print(f'Filosofo {hiloActual} esta comiendo')   
                time.sleep(3) 
                tenedores.append(tenedor.pop())
                tenedores.append(tenedor.pop())
        finally:
            print(f'Filosofo {hiloActual} termino de comer')         
            time.sleep(2)
            mutex.release()
            break




def main ():
    filosofo1 = Thread(name='1',target=filosofo, args=())
    filosofo2 = Thread(name='2',target=filosofo, args=())
    filosofo3 = Thread(name='3',target=filosofo, args=())
 
    

    filosofo1.start()
    filosofo2.start()
    filosofo3.start()
   

main()