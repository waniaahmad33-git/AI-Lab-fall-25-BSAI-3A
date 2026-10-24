import math
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global count
    if depth == target:
        count += 1
        visited.append(scores[index])
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth+1, index*2+i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth+1, index*2+i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

# Reordered tree: root's right branch moved to the left
scores = [2, 5, 9, 8, 6, 4, 7, 3]
depth = int(math.log2(len(scores)))
count = 0
visited = []
print(alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))
print("Leaves evaluated:", count)
print("Visit order:", visited)