def pascal_triangle(n):
        """
            Generate Pascal's triangle up to n rows.

                Args:
                    - n: The number of rows in the Pascal's triangle.

                        Returns:
                            - A list of lists of integers representing Pascal's triangle.
                                """
                                    if n <= 0:
                                            return []

                                                triangle = [[1]]
                                                    
                                                        for i in range(1, n):
                                                                row = [1]
                                                                        for j in range(1, i):
                                                                                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
                                                                                            row.append(1)
                                                                                                    triangle.append(row)

                                                                                                        return triangle


                                                                                                        if __name__ == "__main__":
                                                                                                            # Example usage
                                                                                                                triangle = pascal_triangle(5)
                                                                                                                    print_triangle(triangle)
