class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return  '\n'.join([' '.join(map(str, el))for el in self.list])

    def __add__(self, other):
        answer = ''
        if len(self.list) == len(other.list):
            for mat_1,  mat_2 in zip(self.list, other.list):
                if len(mat_1) != len(mat_2):
                    return 'Матрицы нельзя сложить!'

                sum = [x + y for x, y in zip(mat_1, mat_2)]
                answer += ' '.join([str(line) for line in sum]) + '\n'

        else:
            return 'Матрицы нельзя сложить!'
        return answer

matrix_1 = Matrix([[10,2], [5,2], [2,5]])
matrix_2 = Matrix([[3,2], [6,1], [9,2]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)