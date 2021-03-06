from numpy import *
import matplotlib.pyplot as plt

# h(x) = y = mx + b
# m is slope, b is y-intercept or m is theta 1, b is theta 0
#========================================================================================================================================================
#Squared error function

def compute_error_for_line_given_points(b, m, points):
    sum =0
    for i in range(len(points)):
        sum += ((m * points[i][0] + b) - points[i][1])**2

    return sum/(2*len(points))

# ========================================================================================================================================================
#theta0 = theta0 - eta * (1/n)*sum(h(xi)-y(xi))
#theta1 = theta1 - eta * (1/n)*sum(xi* h(xi)-y(xi))

def step_gradient(b_current, m_current, points, learningRate):
    number_of_points = float(len(points))
    b_gradient = 0
    m_gradient = 0

    # computing the summation part of the derivative

    for i in range(len(points)):

        b_gradient += ((b_current + m_current * points[i][0] ) - points[i][1])
        m_gradient += (points[i][0] * ((b_current + m_current * points[i][0] ) - points[i][1]))

    b_gradient /= number_of_points
    m_gradient /= number_of_points

    new_b = b_current - learningRate * b_gradient
    new_m = m_current - learningRate * m_gradient

    return [new_b,new_m]

# ========================================================================================================================================================

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations = 3):
    counter = 0 # counter used for the drawing
    b = starting_b
    m = starting_m
    for i in range(num_iterations+1):

# ========================================================================================================================================================
        #   The drawing staff, we will update it once after each 10 iterations
        if counter%500 is 0:
            plt.plot(points[:, 0], points[:, 1], 'ro') # Draw the dataset
            plt.plot([0, 80], [b, 80*m+b], 'b')
            plt.show()
# ========================================================================================================================================================
        b, m = step_gradient(b, m, points, learning_rate)
        counter+=1
        print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(counter, b, m, compute_error_for_line_given_points(b, m, points)))
    return [b, m]

#========================================================================================================================================================

def Train():
    points = genfromtxt("data.csv", delimiter=",") # Function in Numby that reads the data from a file and organize it.
    print(points)
    learning_rate = 0.000001 # Eta
    initial_b = 0 # initial y-intercept guess (theta 2)
    initial_m = 0 # initial slope guess (theta 1)
    num_iterations = 2000

    print ("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print ("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))

#========================================================================================================================================================
#The Main:
Train();

# ========================================================================================================================================================
'''
Some useful resources:
 * Linear regression:
   - http://www.ozzieliu.com/tutorials/Linear-Regression-Gradient-Descent.html
 * Gradient Descent:
   - http://blog.hackerearth.com/gradient-descent-algorithm-linear-regression
 * numpy:
   - https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
 * Existing projects:
   - https://github.com/mattnedrich/GradientDescentExample
   - https://github.com/sq0032/ML/blob/master/LinearRegression/main.py
 * Other blogs:
   - http://www.ozzieliu.com/tutorials/Linear-Regression-Gradient-Descent.html
 * Simple rich tutorial:
   - http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-1/
   - http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-2/
   - http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-3/
'''