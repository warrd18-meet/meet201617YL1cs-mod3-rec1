import turtle
import cmath

class Branch:
    length=50

    def __init__( self, start, stop ):
        self.start=start
        self.stop=stop
        self.angle = cmath.phase(stop[0]+1j*stop[1]-(start[0]+1j*start[1]))

    def split(self):
        new_stop1=stop[0]+1j*stop[1]+length*cmath.exp(self.angle-cmath.pi/6.0)
        new_stop1=stop[0]+1j*stop[1]+length*cmath.exp(self.angle+cmath.pi/6.0)

        branch1=Branch(self.stop, [cmath.real(new_stop1),cmath.imag(new_stop1)])
        branch2=Branch(self.stop, [cmath.real(new_stop2),cmath.imag(new_stop2)])

        return [branch1, branch2]
