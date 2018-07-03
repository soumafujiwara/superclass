#!/usr/bin/env python
# coding=utf-8

##スーパークラス
class Dog(object):
    def __init__(self, name):
       self.name = name

##サブクラス
#継承
class UltraDog(Dog):
    def __init__(self, name, type):
        #スーパークラスの__init__メソッド呼び出す。
        #super(クラス, インスタンス自身).メソッド名()
        super(UltraDog, self).__init__(name)
        self.type = type

ud1 = UltraDog("taro", "akita")
print(ud1.name)
print(ud1.type)
