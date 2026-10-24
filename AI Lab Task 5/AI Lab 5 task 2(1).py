import math

leaf_count = 0

# Maximizing player can get
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaf_count
    # Base case: targetDepth reached
    if curDepth == targetDepth:
        leaf_count += 1
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )

    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )


# Driver code
scores = [6, 4, 7, 3, 2, 5, 9, 8]

treeDepth = math.ceil(math.log2(len(scores)))

# Pad scores to make a complete binary tree
scores += [0] * (2**treeDepth - len(scores))

print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))
print("Leaves evaluated:", leaf_count)