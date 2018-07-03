#!/usr/bin/env python
# coding=utf-8

##スーパークラス
class NewStyleClassBase(object):
    def test_method(self, msg):
        print 'NewStyleClassBase: {}'.format(msg)


##サブクラス
#継承
class NewStyleClass(NewStyleClassBase):
    def test_method(self, msg):
        print 'NewStyleClass: {}'.format(msg)
        #スーパークラスの__init__メソッド呼び出す。
        #super(クラス, インスタンス自身).メソッド名()
        super(NewStyleClass, self).test_method(msg)
        # NewStyleClassBase.test_method(self, msg)


new = NewStyleClass()
new.test_method('method call')
