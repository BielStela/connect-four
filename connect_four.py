import numpy as np

class Table():


    def __init__(self):
        self.table = np.zeros((6,7), dtype=int)
    
    def _winning_rule(self, arr)-> bool:
        win1rule = np.array([1,1,1,1])
        win2rule = np.array([2,2,2,2])
        # subarrays of len = 4
        sub_arrays = [arr[i:i+4] for i in range(len(arr)-3)] 

        player1wins = any([np.array_equal(win1rule,sub) for sub in sub_arrays])
        player2wins = any([np.array_equal(win2rule,sub) for sub in sub_arrays])

        if player1wins or player2wins:
            return True
        else:
            return False
    
    # def _get_diagonals(self, _table)-> list:
    #     # hackyly gets all the diagonals
    #     diags = [_table[::-1,:].diagonal(i) for i in range(-_table.shape[0]+1,_table.shape[1])]
    #     diags.extend(_table.diagonal(i) for i in range(_table.shape[1]-1,-_table.shape[0],-1))
    #     return diags

    # def _get_axes(self, _table)-> list:
    #     axes = []
    #     for i in range(_table.shape[0]):
    #         axes.append(_table[i,:])
    #     for j in range(_table.shape[1]):
    #         axes.append(_table[:,j])
    #     return axes
    
    def _get_diagonals(self, _table, i, j)-> list:
        diags = []
        diags.append(np.diagonal(_table, offset=(j - i)))
        diags.append(np.diagonal(np.rot90(_table), offset=-_table.shape[1] + (j + i) + 1))
        return diags

    def _get_axes(self, _table, i, j)-> list:
        axes = []
        axes.append(_table[i,:])
        axes.append(_table[:,j])
        return axes


    def _winning_check(self, i, j)-> bool:
        '''
        Checks if there is four equal numbers in every
        row, column and diagonal of the matrix
        -------
        To Do: 
        Optimize the checking process by checking 
        just the slices that intersect the last 
        droped number.
        '''
                
        all_arr = []
        all_arr.extend(self._get_axes(self.table, i, j))
        all_arr.extend(self._get_diagonals(self.table, i, j))
        
        for arr in all_arr:
            winner = self._winning_rule(arr)
            if winner:
                return True
            else:
                pass
                
    def drop(self, player, column):
        '''
        Drops a number (same as player) in the column specified
        '''
        colummn_vec = self.table[:,column]
        non_zero = np.where(colummn_vec != 0)[0]
        
        if non_zero.size == 0:                        
            # sets the stone to the last element
            i = self.table.shape[0]-1
            self.table[i,column] = player
        else:                                          
            # sets the stone on the last 0
            i = non_zero[0]-1
            self.table[i,column] = player
        # checking if winning for every drop!
        if self._winning_check(i, column):
            print(f'Player {player} wins!')
        else:
            return self.table 
    
    def drop_sim(self, player, column)-> bool:
        '''
        Drop mechanics but faster and bool return for simulation purposes
        '''
        colummn_vec = self.table[:,column]
        non_zero = np.where(colummn_vec != 0)[0]
        
        if non_zero.size == 0:                        
            # sets the stone to the last element
            i = self.table.shape[0]-1
            self.table[i,column] = player
        else:                                          
            # sets the stone on the last 0
            i = non_zero[0]-1
            self.table[i,column] = player
        # checking if winning for every drop!
        if self._winning_check(i, column):
            # we got a winner :)
            return True
        else:
            # no winner yet :(
            return False 
    
    def reset(self):
        return self.__init__()