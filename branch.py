import turtle
import cmath
import math

class Branch:
    """
    This class is used to model one graphic segment in the 
    """

    def __init__( self, start, stop ):
        '''
        Initialize the branch.
        
        :param start: tuple, (x,y), at which the branch (line segment) starts
        :param stop: tuple, (x,y), at which the branch (line segment) ends.
        '''
        self.start=start
        self.stop=stop
        self.length=math.hypot((stop[0]-start[0]),(stop[1]-start[1]))
        self.angle = cmath.phase(stop[0]+1j*stop[1]-(start[0]+1j*start[1]))

    def split(self):
        '''
        Split this branch into two child branches.

        :return: Two new branch instances which start where this branch ends, point
                at +-30 degrees from the vector defined by this branch, and are half
                as long.
        '''
        new_stop1=self.stop[0]+1j*self.stop[1]+0.5*self.length*cmath.exp(1j*(self.angle-cmath.pi/6.0))
        new_stop2=self.stop[0]+1j*self.stop[1]+0.5*self.length*cmath.exp(1j*(self.angle+cmath.pi/6.0))

        branch1=Branch(self.stop, (new_stop1.real,new_stop1.imag))
        branch2=Branch(self.stop, (new_stop2.real,new_stop2.imag))

        return [branch1, branch2]
