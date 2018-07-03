#!/usr/bin/env python
# coding=utf-8

##スーパークラス
class ClassA(object):
    def test_methodA(self):
        self.numberA = 1
        return self.number

##サブクラス
#継承
class ClassB(ClassA):
    def test_methodB(self):
        super(ClassB, self).__init__()

        #print self.number#使えない
        #print ClassA.test_methodA() #使えない
        #print cA.test_methodA() #使えない



cA = ClassA()
cB = ClassB()
#print cA.test_methodA() #1
print cB.test_methodB()
