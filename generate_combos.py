def generate_combos(wheels):
  current_positions = [ 0 for x in range(0,len(wheels))]
  current_wheel = 0
  combos = []

  def add_combo():
      #an array with the values reference by each position in the current_possitions array
      combo = []
      for i in range(len(current_positions)):
        wheel = wheels[i]
        symbol = wheel[current_positions[i]]
        combo.append(symbol)
      combos.append(combo)
  
  add_combo()

  while current_wheel < len(wheels):
    if ( current_positions[current_wheel] + 1 ) != len(wheels[current_wheel]):
      current_positions[current_wheel] = current_positions[current_wheel] + 1
      add_combo()
    else:
        def wheels_left(): return (current_wheel + 1) < len(wheels)
        def next_wheel_overloaded():
            if wheels_left():
                 return (current_positions[current_wheel + 1 ] + 1) \
                                == len(wheels[current_wheel + 1])
            else: 
                return True
        while(wheels_left() and next_wheel_overloaded()) :
            current_wheel = current_wheel + 1

        #finally ran out of combos
        last_wheel = current_wheel == len(wheels) -1 
        current_overloaded = current_positions[current_wheel] == len(wheels[current_wheel]) - 1
        if last_wheel and current_overloaded:
            return combos
        else: #otherwise not exhausted
             #increment current wheel by 1 and reset all between it and 0 to for 
            current_positions[current_wheel+1] = current_positions[current_wheel+1] + 1
            for i in range(current_wheel,-1,-1):
                current_positions[i] = 0
            current_wheel = 0
            add_combo()

combos = generate_combos([["a","b"],["c","d"],["d","a"]])

print(combos)
print(len(combos))
