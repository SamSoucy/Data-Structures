class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() -1)
   

  def delete(self):
    self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
    value_to_return = self.storage.pop()
    self._sift_down(0)
    return value_to_return

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            index = parent
      else:
        break

  def _sift_down(self, index):
    if (self.get_size() - 1) >= ((2 * index) + 1):
          if self.storage[(2 * index) + 1] > self.storage[index]:
                if (self.get_size() - 1) >= ((2 * index) + 2):
                      if self.storage[(2 * index) + 2] > self.storage[(2 * index) + 1]:
                            self.storage[(2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2 * index) + 2]
                            self._sift_down((2 * index) + 2)
                      else:
                            self.storage[(2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2 * index) + 1]
                            self._sift_down((2 * index) + 1)
                else:
                  self.storage[(2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2 * index) + 1]
                  self._sift_down((2 * index) + 1)
          else:
            if (self.get_size() - 1) >= ((2 * index) + 2):
              if self.storage[(2 * index) + 2] > self.storage[index]:
                self.storage[(2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2 * index) + 2]
                self._sift_down((2 * index) + 2)
              else:
                return
            else:
              return
          