#Author Imrose singh arora
import unittest
def classify_triangle(a_si, b_si, c_si):
    if a_si == 0 or b_si == 0 or c_si == 0:
        return "Error:Side=0 not a Triangle"
    elif a_si + b_si < c_si or b_si + c_si < a_si or a_si + c_si < b_si:
        return"Error"
    elif a_si**2+b_si**2 == c_si**2 or a_si**2+c_si**2 == b_si**2 or\
            b_si**2+c_si**2 == a_si**2:
        return "Right"
    elif a_si == b_si and b_si == c_si:
        return "Equilateral"
    elif  a_si == b_si or a_si == c_si or b_si == c_si:
        return "Isoceles"
    else:
        return "Scalene"
def runclassify_triangle(a_si, b_si, c_si):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classify_triangle(', a_si, ',', b_si, ',', c_si, ')=',
          classify_triangle(a_si, b_si, c_si), sep="")
class TestTriangles(unittest.TestCase):
#define multiple sets of tests as functions with names that begin
# with 'test'.  Each function may include multiple tests
    def test_set1(self): # test invalid inputs
# your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5, 12, 13 is a Right triangle')
        self.assertEqual(classify_triangle(5, 5, 5),
                         'Equilateral', '5, 5, 5 is a Equilateral triangle')
    def testmy_testset2(self):
# define multiple test sets to test different aspects of the code
#notice that tests can have bugs too!
        self.assertEqual(classify_triangle(2, 2, 17), 'Error', 'Error')
        self.assertNotEqual(classify_triangle(5, 0, 17), 'Isoceles', 'Error:Side=0 not a Triangle')
        self.assertEqual(classify_triangle(8, 15, 17), 'Right', '8, 15, 17is a  Right triangle')
if __name__ == '__main__':
    # examples of running the code
    runclassify_triangle(2, 2, 2)
    runclassify_triangle(3, 8, 25)
    runclassify_triangle(3, 4, 5)
    runclassify_triangle(18, 18, 25)
    runclassify_triangle(9, 2, 15)
    runclassify_triangle(9, 0, 18)
    runclassify_triangle(0, 0, 0)
    runclassify_triangle(9, 9, 9)
    runclassify_triangle(8, 6, 9)

    