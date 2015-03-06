def for_version(items):
   result = []
   for i in range(len(items) - 1, -1, -1):
      result.append(items[i])
   return result

def while_version(items):
    array = []
    i = (len(items)-1)
    print ("okay")
    print (i)
    while i>=0:
        array.append(items[i])
        i = i - 1
    return array
pass
