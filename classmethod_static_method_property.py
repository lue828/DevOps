#coding=utf-8

class MyClass(object):
    def __init__(self):
        print 'init'
        self._name = 'the5fire'

    @staticmethod
    def static_method():
        print 'This is a static method!'

    @classmethod
    def class_method(cls):
        print 'This is a class method',cls
        print 'visit the property of the class:',cls.name
        print 'visit the static method of the class:',cls.static_method()
        instance = cls()
        print 'visit the normal method  of the class:',instance.test()


    def test(self):
        print 'call test'

    @property
    def name(self):
        return self._name

if __name__ == '__main__':
    MyClass.static_method()
    MyClass.class_method()
    mc = MyClass()
    print mc.name
    #mc.name = 'huyang'
