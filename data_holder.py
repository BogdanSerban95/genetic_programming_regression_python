class DataHolder(object):
    def __init__(self):
        self.x = []
        self.y = []

    def load_data(self, file):
        with open(file, 'r') as open_file:
            for line in open_file.readlines():
                self.x.append([float(i) for i in line.split('\t')])
                self.y.append(self.x[-1][-1])
                self.x[-1] = self.x[-1][: len(self.x[-1]) - 1]
