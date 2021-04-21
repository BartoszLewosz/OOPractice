class OpenFile():
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with OpenFile('sample.txt', 'w') as f:
    f.write("testing")

print(f.closed)