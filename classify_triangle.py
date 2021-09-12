# HOME WORK 01
# imrose Singh Arora
# SSW 567

import unittest

def classifyTriangle(a,b,c):
    if a ==0 or b ==0 or c ==0:
        return "Error:Side=0 not a Triangle"
    elif a + b <c or b + c <a or a+c<b:
        return"Error"
    elif a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
        return "Right"
    elif a == b and b == c:
        return "Equilateral"
    elif  a == b or a == c or b == c:
        return "Isoceles"
    else:
        return "Scalene"

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 is a Equilateral triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(2,2,17),'Error','Error')
        self.assertNotEqual(classifyTriangle(5,0,17),'Isoceles','Error:Side=0 not a Triangle')
        self.assertEqual(classifyTriangle(8,15,17),'Right','8,15,17is a  Right triangle')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(2,2,2)
    runClassifyTriangle(3,8,25)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(18,18,25)
    runClassifyTriangle(9,2,15)
    runClassifyTriangle(9,0,18)

    

