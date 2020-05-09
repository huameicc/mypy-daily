import inspect


def a(a, b=0, *c, d, e=1, **f):
    print(a, b, c, d, e, f, sep='\n')


a(1,2,3,4, d = 'ddd')


aa = inspect.signature(a)
print("inspect.signature(fn)是{0}".format(aa))
print("inspect.signature(fn)的类型是{0}".format(type(aa)))
bb = aa.parameters
print("signature.parameters属性是{0}".format(bb))
print("signature.parameters属性的类型是{0}".format(type(bb)))
for cc, dd in bb.items():
    print("mappingproxy.items()返回的值分别是{0}，{1}, {2}".format(cc, dd, dd.kind.name))
    print("mappingproxy.items()返回的值类型分别是{0}，{1}".format(type(cc), type(dd)))
ee = dd.kind
print("parameter.kind属性是{0}".format(ee))
print("parameter.kind属性类型是{0}".format(type(ee)))
gg = dd.default
print("parameter.default属性是{0}".format(gg))
print("parameter.default属性类型是{0}".format(type(gg)))
ff = inspect.Parameter.KEYWORD_ONLY
print("inspect.Parameter.KEYWORD_ONLY属性是{0}".format(ff))
print("inspect.Parameter.KEYWORD_ONLY属性类型是{0}".format(type(ff)))
