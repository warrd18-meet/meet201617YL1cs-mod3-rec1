from branch import Branch
import turtle

max_depth=7 #The maximum number of branches the tree can have
length=256 #The length of the first branch
startx=0
starty=-250
branch1=Branch((startx,starty),(startx,starty+length))
turtle.hideturtle()

def draw_tree( this_branch, branch_num ):
    '''
    Draw a branch in the tree; then, split the branch and
    recursively call draw_tree again.

    :param this_branch: the branch that will be drawn in turtle
    :param branch_num: the number corresponding to how deep in the tree this branch exists
    '''
    #Complete this method

    turtle.pendown()
    turtle.goto(0,-256)
    '''
    def split(self):
        rel_branch_size=0.5
        new_stop1=self.stop[0]+1j*self.stop[1]+rel_branch_size*self.length*cmath.exp(1j*(self.angle-cmath.pi/6.0))
        new_stop2=self.stop[0]+1j*self.stop[1]+rel_branch_size*self.length*cmath.exp(1j*(self.angle+cmath.pi/6.0))

        branch1=Branch(self.stop, (new_stop1.real,new_stop1.imag))
        branch2=Branch(self.stop, (new_stop2.real,new_stop2.imag))
        '''
draw_tree(branch1,1)

turtle.mainloop()
