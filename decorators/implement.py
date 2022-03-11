from decorators import dec_timer, dec_debugger

class TimeWaster:
    @dec_debugger
    def __init__(self, max_n):
        self.max_n = max_n

    @dec_timer
    def sum_squares(self, num_of_times_to_run):
        for _ in range(num_of_times_to_run):
            sm = sum([i**2 for i in range(self.max_n)])
            print(sm)


tw = TimeWaster(1341237)
tw.sum_squares(10)
