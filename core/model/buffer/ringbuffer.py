# 将GEM中的memory_data和memory_labs抽象出来, 作为一个RingBuffer类
class RingBuffer:
    def __init__(self, buffer_size, strategy, batch_size):
        self.buffer_size = buffer_size
        self.strategy = strategy
        self.batch_size = batch_size
        self.total_classes = 0
        self.images, self.labels = [], []

    def is_empty(self):
        return len(self.labels) == 0