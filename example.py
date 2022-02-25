from ecmath.core import Point
from ecmath.core import Curve


curve = Curve()
curve.A = 1
curve.B = 226
curve.P = 227

p = Point()
p.x = 1
p.y = 1

q = Point()
q.x = 7
q.y = 203

r = curve.Add(p, q)

print("Add:")
print(r.x)
print(r.y)

r = curve.Multiply(p, 5)

print("Multiply:")
print(r.x)
print(r.y)

print("Press any key to continue")
input()




