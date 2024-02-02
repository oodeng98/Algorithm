def solution(board, moves):
    N = len(board)
    basket = []
    answer = 0
    for move in moves:
        for i in range(N):
            if board[i][move-1]:
                if basket:
                    if basket[-1] == board[i][move-1]:
                        basket.pop()
                        answer += 2
                        while True:
                            if len(basket) <= 2:
                                break
                            last = basket.pop()
                            if last == basket[-1]:
                                basket.pop()
                                answer += 2
                            else:
                                basket.append(last)
                                break
                    else:
                        basket.append(board[i][move-1])
                else:
                    basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
    return answer