#classes and objects
class Person:
  pass
print(Person)

p = Person()
print(p)
from collection import Counter
import math

class Statistics:
  def __init__(self, data):
    self.data = data

  def count(self):
    return len(self.data)

  def sum(self):
    return sum(self.data)

  def min(self):
    return min(self.data)

  def max(self):
    return max(self.data)

  def range(self):
    return self.max() - self.min()

  def mean(self):
    return self.sum() / self.count()

  def median(self):
    sorted_data = sorted(self.data)
    n = self.count()
    mid = n // 2
    if n % 2 == 1:
      return sorted_data[mid]
    else:
      return (sorted_data[mid - 1] + sorted_data[mid]) / 2
  def mode(self):
    counter = Counter(self.data)
    mode_val, count = counter.most_common(1)[0]
    return {'mode': mode_val, 'count': count}

  def var(self):
    m = sum(self.data) / len(self.data)
    return round(sum((x- m)**2 for x in self.data) / self.count(), 1)

  def std(self):
    return round(math.sqrt(self.var()), 1)

  def freq_dist(self):
    counter = Counter(self.data)
    total = self.count()
    dist = [(round((count / total) * 100, 1), val) for val, count in counter.items()]
    return sorted(dist, reverse=True)

  def percentile(self, p):
    sorted_data = sorted(self.data)
    k = (p/100) * (len(sorted_data) - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
      return sorted_data[int(k)]
    d0 = sorted_data[int(f)] * (c - k)
    d1 = sorted_data[int(c)] * (k - f)
    return d0 + d1
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) 