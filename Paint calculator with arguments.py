#!/usr/bin/env python
# coding: utf-8

# In[4]:


def paint_calculator_with_arguments(L,W,H,D,wi):
    L = eval(input("What is the length of the room you would like to paint in feet?"))
    W = eval(input("What is the width of the room you would like to paint in feet?"))
    H = eval(input("What is the height of the room you would like to paint in feet?"))
    D = eval(input("How many doors are in the room you would like to paint?"))
    wi = eval(input("How many windows are in the room you would like to paint?"))
    A = L * W + L * H + H * W
    a = 2 * A
    T = a - D * 20 - wi * 15
    G = T / 350
    V = "You will need to cover {} square feet."
    v = "You will need {} gallons of paint to paint this room."
    print(V.format(T))
    print(v.format(G))
    print("You're welcome :).")
paint_calculator_with_arguments(L,W,H,D,wi)

