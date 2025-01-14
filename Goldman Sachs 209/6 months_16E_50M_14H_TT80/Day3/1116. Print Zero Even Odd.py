### 完全没遇到过多线程相关的题

import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n  # 要打印的数字范围 1 到 n
        self.current = 1  # 当前要打印的数字，从 1 开始
        self.lock = threading.Condition()  # 条件变量，控制线程同步
        self.zero_turn = True  # 标记是否轮到 zero 打印 0
        self.even_turn = False  # 标记是否轮到 even 打印偶数

    # 打印 0 的线程调用
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.lock:  # 获取锁，保证线程安全
                while not self.zero_turn:  # 轮不到 zero 时等待
                    self.lock.wait()
                printNumber(0)  # 打印 0
                self.zero_turn = False  # 下一个不是 zero 打印
                # 判断下一个是奇数还是偶数
                if self.current % 2 == 0:
                    self.even_turn = True  # 如果 current 是偶数，轮到 even
                else:
                    self.even_turn = False  # 如果 current 是奇数，轮到 odd
                self.lock.notify_all()  # 唤醒其他线程

    # 打印偶数的线程调用
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):  # 偶数最多有 n // 2 个
            with self.lock:
                while not self.even_turn:  # 轮不到 even 时等待
                    self.lock.wait()
                printNumber(self.current)  # 打印当前偶数
                self.current += 1  # 更新 current
                self.zero_turn = True  # 下一个轮到 zero 打印
                self.even_turn = False  # 停止 even 打印
                self.lock.notify_all()  # 唤醒其他线程

    # 打印奇数的线程调用
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):  # 奇数最多有 (n + 1) // 2 个
            with self.lock:
                while self.even_turn or self.zero_turn:  # 轮不到 odd 时等待
                    self.lock.wait()
                printNumber(self.current)  # 打印当前奇数
                self.current += 1  # 更新 current
                self.zero_turn = True  # 下一个轮到 zero 打印
                self.lock.notify_all()  # 唤醒其他线程
