import pandas as pd
import random 
import math
import matplotlib.pyplot as plt
import numpy as np
 
numbers = [[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1], 
          [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1], 
          [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1], 
          [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
          [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1], 
          [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1], 
          [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1], 
          [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1], 
          [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1], 
          [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1]] 
           
n3s = [[1,1,0,0,0,1,1,1,1,0,0,1,1,1,1],
       [0,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
       [1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
       [1,1,1,0,0,1,1,1,1,0,0,1,0,1,1]]
b = 1
w = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def predict(x, b, iter):
  z = 0
  s = 0
  for i in range(15):    
    s += x[iter][i] * w[i]
  
  z = b + s
  return 1 if z >= b else 0
 
for i in range(1000):
  for j in range(10):
    if j == 3: 
      if predict(numbers, b, 3) == 0:
        for k in range(len(w)):
          if numbers[3][k] == 1:
            w[k] += 1
    else:   
      if predict(numbers, b, j) == 1:
        for k in range(len(w)):
          if numbers[j][k] == 1:
            w[k] -= 1
    
for i in range(10):
    print ("Digit: " + str(i) + " prediction: " + str(predict(numbers, b, i)))
  
for i in range(4):
  print ("Distorted image of number 3: prediction: " + str(predict(n3s, b, i)))
