def commonCharacterCount(s1, s2):
   ans = 0
   for i in set(list(s1)).intersection(set(list(s2))):
      ans += min(list(s1).count(i), list(s2).count(i))
      print i , ans
   return ans