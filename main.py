#
# main.py
#
# PicoShell for CircuitPython
#
# 2024.5.26  0.01  first version by espilab

import os

version = '0.01'

# ------ const.------
file_type_normal = 0x8000
file_type_dir    = 0x4000


def invoke_cmd(cmd, cmd_line_str):
    with open(cmd) as f:
        exec(f.read())

def list_dir(path):
    try:
        dir_entry = os.listdir(path)
    except OSError as exc:
        print('listdir failed, error no=',exc.errno)
        return
    for item in dir_entry:
        #print('path=',path,' item=',item, sep="") #DEBUG
        item_path = (path + '/'+ item).replace('//','/') #os.path.join(path, item)
        ar = os.stat(item_path)
        ftype = ar[0]
        fsize = ar[6]
        if (ftype == file_type_dir):
            print('{:<20}  <dir>'.format(item))
        else:
            print('{:<20}  {:>8d} bytes'.format(item, fsize))
    fs_stat = os.statvfs(path)
    print('  ', fs_stat[0] * fs_stat[4], 'bytes free')


def process_cmd_line(cmd_line):
  args = cmd_line.split(' ')
  cmd = args[0]
  if cmd == 'ls':
    if len(args) <= 1:
      list_dir('.')
    else:
      list_dir(args[1])
  elif cmd == '?':
     show_help()
  else:
     invoke_cmd(cmd, cmd_line)

def start_message():
  print('PicoShell -- command shell started.  enter "?" for help.')

def show_help():
    print('PicoShell for CircuitPython  version', version)
    print('ls  : list directory files')
    print('<filename.py>  : invoke the program')
    print('?   : show help')


#--------main--------
prompt_str = os.getcwd() + '>'
start_message()

while True:
  cmd_line_str= input(prompt_str)
  process_cmd_line(cmd_line_str)
