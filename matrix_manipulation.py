from urllib3.connectionpool import xrange
from exceptions import InvalidDimensionException, EmptyArrayException

class GetMatrix:
    def __init__(self, matrix_str):
        if not isinstance(matrix_str, str):
            raise ValueError(f'Matrix should be string, but you matrix type is {type(matrix_str)}')
        self.matrix_str = matrix_str

    async def get_matrix_as_list(self):
        ''' FLATTEN MATRIX FROM STRING TO 1D LIST  '''
        return [int(s.strip()) for s in self.matrix_str.split('|') if s.strip().isdigit()]

    async def get_matrix_dim(self):
        ''' GET COLUMN SHAPE OF THE MATRIX '''
        rows = self.matrix_str.split('\n')
        parts = [x.strip() for x in rows[1].split('|')]
        cols = [int(s) for s in parts if s.isdigit()]
        return len(cols)

    async def to_matrix(self, l, n):
        ''' CONVERT TO 2D MATRIX '''
        if n <= 0:
            raise InvalidDimensionException('Dimension of matrix is negative or 0, should be positive instead')
        return [l[i:i + n] for i in xrange(0, len(l), n)]

    async def get_spiral_matrix(self, m, n, arr):
        ''' GET SPIRAL ARRAY FROM MATRIX AGAINST CLOCKWISE FROM TOP LEFT'''

        # check if array is empty
        if not arr:
            raise EmptyArrayException('Input matrix you passed is empty, should')
        if m <= 0 or n <= 0:
            raise InvalidDimensionException('Dimensions of matrix are negative or 0, should be positive instead')
        # check if input array has valid dimensions

        k = 0

        l = 0

        # k - starting row index
        # m - ending row index
        # l - starting column index
        # n - ending column index
        # i - iterator

        # initialize the count
        cnt = 0

        # total number of
        # elements in matrix
        total = m * n
        final_array = []

        while k < m and l < n:
            if cnt == total:
                break

            # Get the first column
            # from the remaining columns
            for i in range(k, m):
                final_array.append(arr[i][l])
                cnt += 1

            l += 1

            if cnt == total:
                break

            # Get the last row from
            # the remaining rows
            for i in range(l, n):
                final_array.append(arr[m - 1][i])
                cnt += 1

            m -= 1

            if cnt == total:
                break

            # Get the last column
            # from the remaining columns
            if k < m:
                for i in range(m - 1, k - 1, -1):
                    final_array.append(arr[i][n - 1])
                    cnt += 1
                n -= 1

            if cnt == total:
                break

            # Get the first row
            # from the remaining rows
            if l < n:
                for i in range(n - 1, l - 1, -1):
                    final_array.append(arr[k][i])
                    cnt += 1

                k += 1

        return final_array

    async def get_final_matrix(self):
        matrix_as_list = await self.get_matrix_as_list()
        matrix_dim_part = await self.get_matrix_dim()
        matrix = await self.to_matrix(matrix_as_list, matrix_dim_part)
        final_array = await self.get_spiral_matrix(len(matrix), len(matrix[0]), matrix)
        return final_array
