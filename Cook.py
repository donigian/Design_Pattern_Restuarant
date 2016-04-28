import time

class Cook:
    def __init__(self):
        pass

    def time_to_prepare(func):

        def decorated(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print('Total time to prepare: ', time.time() - start )
            return result
        return decorated

    @time_to_prepare
    def cook(self):
        print("Cook: Cooking...")
        pass

