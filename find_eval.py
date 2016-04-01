import math

# horuff - 04/01/2016

#https://en.wikipedia.org/wiki/Catalan_number

##all ways to operate on two nodes
def bin_ops(l, r):
    lv, ls = l
    rv, rs = r
    if type(lv) is long or type(rv) is long:
      return
    if type(lv) is set or type(rv) is set:
      return
    if lv > 0 and lv < 10 and rv < 10:
      yield (lv**rv, '%s^%s'%(ls,rs))
      pass
    if rv != 0:
      yield (lv/rv, '(%s/%s)'%(ls,rs))
    yield (lv+rv, '(%s+%s)'%(ls,rs))
    yield (lv-rv, '(%s-%s)'%(ls,rs))
    yield (lv*rv, '(%s*%s)'%(ls,rs))

##all ways to operate on a single node
def single_ops(op):
    v, s  = op
    if type(v) is long:
      return
    if type(v) is int and v >= 0 and v < 1000:
      yield (math.factorial(v), '(%s)!'%s)
    if v > 0:
      yield (math.sqrt(v), 'sqrt(%s)'%s)
    if type(v) in (int, float):
      #yield (math.sin(v), 'sin(%s)'%s)
      pass

# recursive
# return list of all ways one could operate on n nodes of
# values v

# for all possilbe divisions in to two groups (or 1, base):
# gather list of all possible value interpretations of the left child group
# crossed with the list all possible value interpretations of the right group
# crossed with all possible values interpretable by two single values (left and right product) crossed with all possible values interpretable by a single value (our previous product)
# ^cross last again (for nesting ie (sqrt(sqrt(8+8))))
# return this list

# its a list of values in a 5(?) dimentional matrix containing a
# rendering of all possible ways of operate on n values of v
# and their interpreted value

def eval_all_for(n, v):
    res = []

    if n == 1:
      res.append((v, str(v)))
      for so in single_ops((v, str(v))):
        res.append(so)
        for so2 in single_ops((so)):
          res.append(so2)
      return res

    for i in range(1, n):
      left = eval_all_for(i, v)
      right = eval_all_for(n-i, v)
      for l in left:
        for r in right:
          for op in bin_ops(l, r):
            res.append(op)
            for so in single_ops(op):
              res.append(so)
              for so2 in single_ops(so):
                res.append(so2)
    return res

def search_for_solution(num_digs, value, needle, top_results=1):
    shortest_solution = lambda a, b: len(a[1])-len(b[1])
    correct = lambda x: x[0] == needle
    results = eval_all_for(num_digs, value)
    print 'sultions for:', value

    for res in filter(correct, sorted(results, shortest_solution)):
      v, s = res
      print '\t%s = %s' % (s, v)
    print

for x in range(10):
  search_for_solution(3, x, 6, 100000)
