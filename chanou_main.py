#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dm_methods import Dm 
from measurement import Mes
import numpy as np
import random
# import math

def only_once():
  f_once = True
  # ベルペアの数を指定
  n_of_bell = dm_ms.set_n_of_bell()
  # ベルペアを選択
  q_states = dm_ms.set_bellpair(n_of_bell)
  print('\n===> SELECTED BELLPAIR')
  print(q_states,'\n')
  # ensembleを作成
  ensemble = dm_ms.set_ensemble(n_of_bell, f_once, q_states)
  print('\n===> ENSEMBLE')
  print(ensemble,'\n')
  # ensembleをdmに変換
  dm = dm_ms.convert_to_dm(ensemble, n_of_bell)
  print('===> DENSITY MATRIX')
  print(dm)
  print()
  return dm

def repeat():
  f_once = False
  r_time = 10
  for i in range(10):
    print('-----------exp',i,'----------')
    # ベルペアの数を指定
    n_of_bell = dm_ms.set_n_of_bell()
    # ensembleを作成
    ensemble = dm_ms.set_ensemble(n_of_bell, f_once)
    print('\n===> ENSEMBLE')
    print(ensemble)
    # ensembleをdmに変換
    dm = dm_ms.convert_to_dm(ensemble, n_of_bell)
    print('===> DENSITY MATRIX')
    print(dm)
    print()

if __name__ == "__main__":
  print('\n#####This is E91 sim by chanou#####')
  dm_ms = Dm()
  mes = Mes()

  dm = only_once()
  mes.ali_measurement(dm)
  # repeat()
  
  # # ベルペアの数を指定
  # n_of_bell = dm_ms.set_n_of_bell()
  # # ensembleを作成
  # ensemble = dm_ms.set_ensemble(n_of_bell)
  # print('\n===> ENSEMBLE')
  # print(ensemble)
  # # ensembleをdmに変換
  # dm = dm_ms.convert_to_dm(ensemble, n_of_bell)
  # print('===> DENSITY MATRIX')
  # print(dm)
  # print()


# メモ
# クラスインスタンスを作る
# gc = GodChannel(None)
# GodChannelが持つベル状態の数を指定
# gc.nstates = 1
# Bell状態は2qubitsなので、2を指定
# gc.nqubits = 2
# ensambleを指定
# ensemble = [ [0.8, gc.Phi_plus], [0.2, gc.Psi_plus] ]
# print ensemble
# dm = gc.convert_to_dm(ensemble)
# print '#### return dm',dm
# 測定するqubitのindexを指定
# measuring_qubits = [1, 2]

# 測定規定を指定。順番をmeasureing_qubitsと対応するようにする
# basis = ["Z", "M"]

# 実際に測定するのが下の関数呼び出し。dm_after_measurementには測定後の密度行列が、
# resulutには測定結果が文字列で入っている。
# (dm_after_measurement, result,) =  gc.get_measured_values_dm(dm, measuring_qubits, basis)
# print "The density matrix after measurement in {0} & {1} axes is {2}, with the outcome {3}.".format(basis[0],basis[1],dm_after_measurement, result)

# 参考
# http://idken.net/posts/2017-02-28-math_github/
# https://note.nkmk.me/python-random-randrange-randint/
# https://pythondatascience.plavox.info/numpy/%E6%95%B0%E5%AD%A6%E7%B3%BB%E3%81%AE%E9%96%A2%E6%95%B0
# https://deepage.net/features/numpy-dot.html
# http://sucrose.hatenablog.com/entry/2013/03/16/162019
# http://uxmilk.jp/12929