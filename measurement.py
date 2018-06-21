#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random
import sys

class Mes:
  def ali_measurement(self,dm):
    # print('測定するよ',dm)
    theta_list = {
      '0': 0,
      '45': 45, 
      '22.5': 22.5, 
    }
    ran_theta_list = [
      '0',
      '45',
      '22.5',
    ]
    theta = np.deg2rad(theta_list[ran_theta_list[random.randint(0,2)]])
    print(theta_list[ran_theta_list[random.randint(0,2)]])

    # Z rotation operator
    R = np.matrix([
      [-1j*theta/2, 0],
      [0, 1j*theta/2]
    ])
    # print('R:')
    # print(R)

    # musurement operator
    mes_Z = np.matrix([
      [1, 0],
      [0, -1]
    ])
    print('mes_Z:')
    print(mes_Z)

    mes =  np.dot(mes_Z, R)
    print(mes)
    # ここが違う…？
    mes = np.outer(mes, np.eye(2))
    print('できねぇ', mes)
    q_quality = np.dot(mes, dm)
    print(q_quality)

  def bob_measurement(self):
    print("I'm bob")
    theta_list = {
      '0': 0,
      '45': 45, 
      '-22.5': -22.5, 
    }
    ran_theta_list = [
      '0',
      '45',
      '-22.5',
    ]

  def eve_measurement(self):
    print("I'm eve")