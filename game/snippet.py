    def row_starts(self, threads, num_of_rows):
        size = num_of_rows // threads
        remainder = num_of_rows - threads*size
        starts = [size] * threads
        for i in range(remainder):
            starts[i] += 1
        return starts