import queue

MyQueue = queue.Queue(3)

print("Очередь пуста: ", MyQueue.empty())

MyQueue.put(1)
MyQueue.put(2)
MyQueue.put(3)

print("Очередь заполнена: ", MyQueue.full())

print("Извлечение из очереди: ", MyQueue.get())

print("Очередь заплнена: ", MyQueue.full())
print("Извлечение из очереди: ", MyQueue.get())
print("Извлечение из очереди: ", MyQueue.get())
print("Очредь пуста: ", MyQueue.empty())
