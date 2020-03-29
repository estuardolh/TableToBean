class FieldFormat:
  @staticmethod
  def getCamelCase(text, first_char_uppered = False):
    res = ''
    
    STATE_PASS = 0
    STATE_UPPER = 2
    
    state = STATE_PASS
    
    first_char_uppered_done = False
    
    for char in text:    
      if(state == STATE_PASS):
        if(char == '_' or
            char == '-' or
            char == ' '):
          # ignore
          state = STATE_UPPER
        else:
          if(first_char_uppered == True and first_char_uppered_done == False):
            res += char.upper()
            first_char_uppered_done = True
          else:
            res += char.lower()
      
      elif(state == STATE_UPPER):
        res += char.upper()
        state = STATE_PASS
      
    return res
