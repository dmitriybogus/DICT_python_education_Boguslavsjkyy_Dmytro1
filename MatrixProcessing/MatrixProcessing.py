class MatrixProcessing:

    def init(self):
        ...

    def menu(self):
        choice = self.correctly_input_command("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > """, ("1", "2", "3", "0"))


        if choice == "1":
            self.add_matrices()
        elif choice == "2":
            self.multiplication_by_constant()
        elif choice == "3":
            ...
        elif choice == "0":
            return

        choice = self.correctly_input_command("Continue? [yes] / [no] > ", ("yes", "no"))
        if choice == "yes":
            self.menu()
        else:
            return

    def multiplication_by_constant(self):
        constant = self.correct_integer_input("Enter constant: > ")
        matrix, *_ = self.create_matrix()
        result = []
        for rows in matrix:
            columns = []
            for column in rows:
                columns.append(column * constant)
            result.append(columns)
        self.show_result(result)

    def add_matrices(self):
        matrix1, *shape1 = self.create_matrix(" first ")
        matrix2, *shape2 = self.create_matrix(" second ")
        while shape1 != shape2:
            print(f"Perform addition possible only for a matrix,"
                  f" unique numbers of rows and columns.")
            matrix2, *shape2 = self.create_matrix(" second ")

        result = []
        for m1, m2 in zip(matrix1, matrix2):
            column = []
            for a, b in zip(m1, m2):
                value = a + b
                column.append(value)
            result.append(column)
        self.show_result(result)

    def create_matrix(self, turn=" "):
        rows, columns = self.correct_input_size(f"Enter size of{turn}matrix: > ")
        matrix = self.correct_input_matrix(rows, columns)
        return matrix, rows, columns

    def correct_input_matrix(self, rows, columns):
        matrix = []
        for i in range(1, rows + 1):
            row = self.correct_input_columns(f"Row number {i}: > ", columns)
            matrix.append(row)
        return matrix

    @staticmethod
    def correct_integer_input(string):
        user_input = input(string)
        while True:
            try:
                int(user_input)
            except ValueError:
                print("Incorrect format")
                user_input = input(string)
                continue
            else:
                break
        return int(user_input)

    @staticmethod
    def show_result(matrix):
        print("The result is:")
        for rows in matrix:
            print(*rows, sep="  ")

    @staticmethod
    def correct_input_columns(string, number_rows):
        user_input = input(string)
        while True:
            user_input = user_input.split(" ")
            if len(user_input) != number_rows:
                print("Incorrect row filling")
                user_input = input(string)
            try:
                list(map(lambda x: int(x), user_input))
            except ValueError:
                print("Incorrect row filling")
                user_input = input(string)
                continue
            else:
                user_input = list(map(lambda x: int(x), user_input))
                break
        return user_input

    @staticmethod
    def valid_shape(matrix):
        shape = set()
        rows = len(matrix)
        for column in matrix:
            shape.add(len(column))
        if len(shape) == 1:
            return rows, *shape
        else:
            print("ERROR")

    @staticmethod
    def correctly_input_command(string, command):
        input_value = input(string)
        while input_value not in command:
            print("please input correctly command")
            input_value = input(string)
        return input_value

    @staticmethod
    def correct_input_size(string):
        user_input = input(string)

        while True:
            user_input = user_input.split(" ")
            if len(user_input) != 2:
                print("Please input correctly size")
                user_input = input(string)
            try:
                list(map(lambda x: int(x), user_input))
            except ValueError:
                print("Please input correctly size")
                user_input = input(string)
                continue
            else:
                user_input = list(map(lambda x: int(x), user_input))
                break

        return user_input


mxp = MatrixProcessing()
mxp.menu()