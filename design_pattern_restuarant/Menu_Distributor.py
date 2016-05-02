class Menu_Distributor(object):
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            print('Staff notified to bring menu...')
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        print('Notifying additional staff...')
        [o.notify(self) for o in self.observers]