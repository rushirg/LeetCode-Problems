class Solution:
    
    # our dfs function here
    def dfs(self, board, i, j, word):
        
        # lets check if the word is not empty or not
        if len(word) == 0:
            # this does indicate that we don't have a word to search for anymore, we have processed all the letters 
            return True
    
        # check for corner cases when are going outof our matrix or the starting letter of our word isn't matching with the given matrix letter
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        
        # store the current value of board[i][j]
        # as if we reach here our i, j value is in the reach or we found our first matching letter
        temp = board[i][j]
        
        # store some special letter at board[i][j] position so that to mark as visited
        board[i][j] = "#"
        
        # recursively check for all 4 directions/neighbors for next letter of the word
        result = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        
        # resotre the original value of borad[i][j] as we are done searching
        board[i][j] = temp
        
        # return our result
        return result
    
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
         # We will need to use dfs approach here
        
        # check the basic conditions
        # if board not present return False
        if not board:
            return False
        
        # let us go through each index in matrix to check for starting word
        for i in range(len(board)):
            for j in range(len(board[0])):
                # here we will call our dfs function
                # it will recursively check for starting letter of the word and all its neighbors
                # if we get true from the dfs function we will return found i.e. True
                # else we will go through rest of the matrix index to check if we could find the starting letter and eventually all the word by recursively going through
                if self.dfs(board, i, j, word):
                    return True
        
        # if after going through all the matrix we didn't get the word, return False
        return False
    
