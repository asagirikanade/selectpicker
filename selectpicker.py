# -*- coding: utf-8 -*-
import maya.cmds as mc
import pickle
from functools import partial


class SelectPicker:
    def __init__(self,*args):
        self.list = []

    def add(self,*args):
        sel = mc.ls(sl=True)
        if sel[0] in self.list:
            print 'EROOR!!!'
            return
        else:
            self.list.append(sel[0])
            

    def mainmenu(self,*args):
        mc.window()
        mc.columnLayout(adj=True)
        mc.button(l='EXP', c=self.add)
        mc.button(l='PRINT', c=self.pri)
        mc.showWindow()

    def pri(self,*args):
        print self.list
a = SelectPicker()
a.mainmenu()

