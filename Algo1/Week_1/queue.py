from vector import Vector


class Queue:

	def __init__(self):
		self.__queue = Vector()

	def push(self, value):
		self.__queue.add(value)