import numpy as np

class Table():
        
    def __init__(self):
        self.table = np.zeros((6,7), dtype=int)
    
    def winning_check(self)-> bool:
        '''
        Checks if there is four equal numbers in every
        slice, row, column and diagonal of the matrix
        -------
        To Do: 
        Optimize the checking process by checking 
        just the slices that intersect the last 
        droped number.
        '''
        
        def _winning_rule(arr):
            '''
            BROKEN
            '''
            unique = np.unique(arr, return_counts=True)
            winning_player = unique[0][unique[1] > 3]
            return winning_player
        
        def _get_diagonals(a):
            # hacky getting all the diagonals
            diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
            diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
            return diags

        def _get_axes(_table):
            axes = []
            for i in range(_table.shape[0]):
                axes.append(_table[i,:])
            for j in range(_table.shape[1]):
                axes.append(_table[:,j])
            return axes
        
        all_axes = []
        all_axes.extend(_get_axes(self.table))
        all_axes.extend(_get_diagonals(self.table))
        
        for ax in all_axes:
            winner = _winning_rule(ax)
            if not  winner:
                # no winner yet
                pass
            else:
                # winner!
                return True
        
    def drop(self, player, column):
        '''
        Drops a number (same as player) in the column specified
        '''
        colummn_vec = self.table[:,column]
        non_zero = np.where(colummn_vec != 0)[0]
        
        if non_zero.size == 0:                        
            # sets the stone to the last element 
            self.table[self.table.shape[0]-1,column] = player
        else:                                          
            # sets the stone on the last 0
            self.table[non_zero[0]-1,column] = player
        # checking if winning for every drop!
        if self.winning_check():
            print(f'Player {player} wins!')
        else:
            return self.table 
    
    def reset(self):
        return self.__init__()