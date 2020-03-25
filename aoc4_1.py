def run():


  def validate(numstr):
    valid = False
    for d in [numstr[i:i+2] for i in range(0,len(numstr)-1)]:
      if d[0]>d[1]:
        return False
      valid |= d[0] == d[1]
    return valid
    

  valids = [ i for i in range(168630,718098+1) if validate(str(i))]

  print(valids)
  print(len(valids))