def board_to_string(board):
    result = []
    for row in board:
        temp_result = " | ".join(row)
        result.append("| " + temp_result + " |")
    return "\n".join(result)

board = [["X", "O", "#"],
         ["X", "X", "X"],
         ["#", "#", "#"]]

result = board_to_string(board)

print(result)
