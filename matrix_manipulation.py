from urllib3.connectionpool import xrange


class GetMatrix:
    def __init__(self, matrix_str):
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
        return [l[i:i + n] for i in xrange(0, len(l), n)]

    async def counterClockspiralPrint(self, m, n, arr):
        ''' GET SPIRAL ARRAY FROM MATRIX AGAINST CLOCKWISE FROM TOP LEFT'''
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

        while (k < m and l < n):
            if (cnt == total):
                break

            # Print the first column
            # from the remaining columns
            for i in range(k, m):
                final_array.append(arr[i][l])
                cnt += 1

            l += 1

            if (cnt == total):
                break

            # Print the last row from
            # the remaining rows
            for i in range(l, n):
                final_array.append(arr[m - 1][i])
                cnt += 1

            m -= 1

            if (cnt == total):
                break

            # Print the last column
            # from the remaining columns
            if (k < m):
                for i in range(m - 1, k - 1, -1):
                    final_array.append(arr[i][n - 1])
                    cnt += 1
                n -= 1

            if (cnt == total):
                break

            # Print the first row
            # from the remaining rows
            if (l < n):
                for i in range(n - 1, l - 1, -1):
                    final_array.append(arr[k][i])
                    cnt += 1

                k += 1

        return final_array

    async def get_final_matrix(self):
        matrix_as_list = await self.get_matrix_as_list()
        matrix_dim_part = await self.get_matrix_dim()
        matrix = await self.to_matrix(matrix_as_list, matrix_dim_part)
        final_array = await self.counterClockspiralPrint(len(matrix), len(matrix[0]), matrix)
        return final_array
