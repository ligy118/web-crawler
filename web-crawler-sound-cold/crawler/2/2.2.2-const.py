class _const(object):
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
#py3 change2
#       if self.__dict__.has_key(name):
        if name in self.__dict__:
#py3 change1
#           raise self.ConstError， "Can't revind const(%s)"%name
            raise self.ConstError("Can't rebind const(%s)"%name)
        self.__dict__[name] = value
    def __delattr__(self,name):
        if name in self.__dict__:
#py3 change1
#           raise self.ConstError, "Can't unbind const(%s)"%name
            raise self.ConstError("Can't unbind const(%s)"%name)
        raise NameRrror(name)
import sys
sys.modules[__name__] = _const()