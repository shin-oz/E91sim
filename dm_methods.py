#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random
import sys

class Dm:
  def __init__(self):
    self.Phi_plus = (1/np.sqrt(2)) * np.array([1, 0, 0, 1])
    self.Phi_minus = (1/np.sqrt(2)) * np.array([1, 0, 0, -1])
    self.Psi_plus = (1/np.sqrt(2)) * np.array([0, 1, 1, 0])
    self.Psi_minus = (1/np.sqrt(2)) * np.array([0, 1, -1,0])
    self.bellpairs = {
      'Phi_plus' : (1/np.sqrt(2)) * np.array([1, 0, 0, 1]),
      'Phi_minus' : (1/np.sqrt(2)) * np.array([1, 0, 0, -1]),
      'Psi_plus' : (1/np.sqrt(2)) * np.array([0, 1, 1, 0]),
      'Psi_minus' : (1/np.sqrt(2)) * np.array([0, 1, -1,0])
    }
  
  def set_n_of_bell(self):
      # !!!for_debug!!!
      n_of_bell = 1
      # n_of_bell = random.randint(1, 4)
      print('number of bellpair: ', n_of_bell, '\n')
      return n_of_bell

  # !!!task:redundant!!!
  def set_bellpair(self, n_of_bell):
    index_bellpairs = [
      'Phi_plus',
      'Phi_minus',
      'Psi_plus',
      'Psi_minus'
    ]
    index = random.sample(range(n_of_bell), n_of_bell)
    q_states = []
    for i in index:
      print('selected ballpair: ', index_bellpairs[i])
      print('selected ballpair: ', self.bellpairs[index_bellpairs[i]],'\n')
      q_states.append([
        index_bellpairs[i],
        self.bellpairs[index_bellpairs[i]]
      ])
    return(q_states)
    # if n_of_bell == 1:
    #   selected_bellpair1_index = random.randint(0, 3)
    #   print('selected ballpair_1: ', index_bellpairs[selected_bellpair1_index])
    #   print('selected ballpair_1: ', self.bellpairs[index_bellpairs[selected_bellpair1_index]])
    #   return [
    #     index_bellpairs[selected_bellpair1_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair1_index]]
    #   ]
    # elif n_of_bell == 2:
    #   index = random.sample(range(n_of_bell), n_of_bell)#抽出する添字を取得
    #   q_states = []
    #   for i in index:
    #     print('selected ballpair: ', index_bellpairs[i])
    #     print('selected ballpair: ', self.bellpairs[index_bellpairs[i]])
    #     q_states.append([
    #       index_bellpairs[i],
    #       self.bellpairs[index_bellpairs[i]]
    #     ])
    #   print(q_states)
    #   return [
    #     index_bellpairs[selected_bellpair1_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair1_index]],
    #     index_bellpairs[selected_bellpair2_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair2_index]]
    #   ]
    # elif n_of_bell == 3:
    #   selected_bellpair1_index = random.randint(0, 3)
    #   selected_bellpair2_index = random.randint(0, 3)
    #   selected_bellpair3_index = random.randint(0, 3)
    #   print('selected ballpair_1: ', self.bellpairs[index_bellpairs[selected_bellpair1_index]])
    #   print('selected ballpair_2: ', index_bellpairs[selected_bellpair2_index])
    #   print('selected ballpair_2: ', self.bellpairs[index_bellpairs[selected_bellpair2_index]])
    #   print('selected ballpair_3: ', index_bellpairs[selected_bellpair3_index])
    #   print('selected ballpair_3: ', self.bellpairs[index_bellpairs[selected_bellpair3_index]])
    #   return [
    #     index_bellpairs[selected_bellpair1_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair1_index]],
    #     ndex_bellpairs[selected_bellpair2_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair2_index]],
    #     index_bellpairs[selected_bellpair3_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair3_index]]
    #   ]
    # elif n_of_bell == 4:
    #   selected_bellpair1_index = random.randint(0, 3)
    #   selected_bellpair2_index = random.randint(0, 3)
    #   selected_bellpair3_index = random.randint(0, 3)
    #   selected_bellpair4_index = random.randint(0, 3)
    #   print('selected ballpair_1: ', index_bellpairs[selected_bellpair1_index])
    #   print('selected ballpair_1: ', self.bellpairs[index_bellpairs[selected_bellpair1_index]])
    #   print('selected ballpair_2: ', index_bellpairs[selected_bellpair2_index])
    #   print('selected ballpair_2: ', self.bellpairs[index_bellpairs[selected_bellpair2_index]])
    #   print('selected ballpair_3: ', index_bellpairs[selected_bellpair3_index])
    #   print('selected ballpair_3: ', self.bellpairs[index_bellpairs[selected_bellpair3_index]])
    #   print('selected ballpair_4: ', index_bellpairs[selected_bellpair4_index])
    #   print('selected ballpair_4: ', self.bellpairs[index_bellpairs[selected_bellpair4_index]])
    #   return [
    #     index_bellpairs[selected_bellpair1_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair1_index]],
    #     index_bellpairs[selected_bellpair2_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair2_index]],
    #     index_bellpairs[selected_bellpair3_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair3_index]],
    #     index_bellpairs[selected_bellpair4_index],
    #     self.bellpairs[index_bellpairs[selected_bellpair4_index]]
    #   ]
    # else:
    #   print('error <random number generation>: ', n_of_bell, '\n')
    #   sys.exit()



    
  # !!!task:redundant!!!
  def set_ensemble(self, n_of_bell, f_once, q_states):
    if f_once:
      if n_of_bell == 1:
        ensemble = [1, q_states[0][1]]
        return ensemble
      elif n_of_bell == 2:
        while True:
          print('1st bell pair ratio?: ', end="")
          bell_ratio_1 = int(input())/100
          print('2nd bell pair ratio?: ', end="")
          bell_ratio_2 = int(input())/100
          bell_ratio_total = bell_ratio_1 + bell_ratio_2
          if bell_ratio_total == 1:
            break
          print('error <ratio of bell pair>: ', bell_ratio_total, '\n')

        ensemble = [
          [bell_ratio_1, q_states[0][1]],
          [bell_ratio_2, q_states[1][1]]
          ]
        return ensemble
      elif n_of_bell == 3:
        while True:
          print('1st bell pair ratio?: ', end="")
          bell_ratio_1 = int(input())/100
          print('2nd bell pair ratio?: ', end="")
          bell_ratio_2 = int(input())/100
          print('3rd bell pair ratio?: ', end="")
          bell_ratio_3 = int(input())/100
          bell_ratio_total = bell_ratio_1 + bell_ratio_2 + bell_ratio_3
          if bell_ratio_total == 1:
            break
          print('error <ratio of bell pair>: ', bell_ratio_total, '\n')

        ensemble = [
          [bell_ratio_1, q_states[0][1]],
          [bell_ratio_2, q_states[1][1]],
          [bell_ratio_3, q_states[2][1]]
          ]
        return ensemble
      elif n_of_bell == 4:
        while True:
          print('1st bell pair ratio?: ', end="")
          bell_ratio_1 = int(input())/100
          print('2nd bell pair ratio?: ', end="")
          bell_ratio_2 = int(input())/100
          print('3rd bell pair ratio?: ', end="")
          bell_ratio_3 = int(input())/100
          print('4th bell pair ratio?: ', end="")
          bell_ratio_4 = int(input())/100
          bell_ratio_total = bell_ratio_1 + bell_ratio_2 + bell_ratio_3 + bell_ratio_4
          if bell_ratio_total == 1:
            break
          print('error <ratio of bell pair>: ', bell_ratio_total, '\n')

        ensemble = [
          [bell_ratio_1, q_states[0][1]],
          [bell_ratio_2, q_states[1][1]],
          [bell_ratio_3, q_states[2][1]],
          [bell_ratio_4, q_states[3][1]]
          ]
        return ensemble
      else:
        print('error <random number generation>: ', n_of_bell, '\n')
        sys.exit()
    else:
      if n_of_bell == 1:
        ensemble = [1, self.Phi_plus]
        return ensemble
      elif n_of_bell == 2:
        ensemble = [
          [0.5, self.Phi_plus],
          [0.5, self.Psi_plus]
          ]
        return ensemble
      elif n_of_bell == 3:
        ensemble = [
          [0.23, self.Phi_plus], 
          [0.33, self.Psi_plus], 
          [0.54, self.Psi_plus]
          ]
        return ensemble
      elif n_of_bell == 4:
        ensemble = [
          [10, self.Phi_plus], 
          [20, self.Psi_plus], 
          [30, self.Psi_plus], 
          [40, self.Psi_plus]
          ]
        return ensemble
      else:
        print('error <random number generation>: ', n_of_bell, '\n')
        sys.exit()

  # !!!task:redundant!!!
  def convert_to_dm(self, ensemble, n_of_bell):
    if n_of_bell == 1:
      op_A = ensemble[0]
      q_state_A = np.matrix(ensemble[1])
      
      dm = op_A * np.dot(q_state_A.T, q_state_A)
      return dm
    elif n_of_bell == 2:
      op_A = ensemble[0][0]
      q_state_A = np.matrix(ensemble[0][1])
      op_B = ensemble[1][0]
      q_state_B = np.matrix(ensemble[1][1])
      
      dm = op_A * np.dot(q_state_A.T, q_state_A) + op_B * np.dot(q_state_B.T, q_state_B)
      return dm     
    elif n_of_bell == 3:
      op_A = ensemble[0][0]
      q_state_A = np.matrix(ensemble[0][1])
      op_B = ensemble[1][0]
      q_state_B = np.matrix(ensemble[1][1])
      op_C = ensemble[2][0]
      q_state_C = np.matrix(ensemble[2][1])
      
      dm = op_A * np.dot(q_state_A.T, q_state_A) + op_B * np.dot(q_state_B.T, q_state_B) + op_C * np.dot(q_state_C.T, q_state_C)
      return dm
    elif n_of_bell == 4:
      op_A = ensemble[0][0]
      q_state_A = np.matrix(ensemble[0][1])
      op_B = ensemble[1][0]
      q_state_B = np.matrix(ensemble[1][1])
      op_C = ensemble[2][0]
      q_state_C = np.matrix(ensemble[2][1])
      op_D = ensemble[3][0]
      q_state_D = np.matrix(ensemble[3][1])
      
      dm = op_A * np.dot(q_state_A.T, q_state_A) + op_B * np.dot(q_state_B.T, q_state_B) + op_C * np.dot(q_state_C.T, q_state_C) + op_D * np.dot(q_state_D.T, q_state_D)
      return dm
    else:
      print('error <random number generation>: ', n_of_bell, '\n')
      sys.exit()

if __name__ == '__main__':
  print("I'm dm_methds.py, and the code itself was called")
