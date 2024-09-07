import time
import subprocess
import os

def start_up(tflist):
  for infra in tflist:
    print("Starting up {infra}!".format(infra = infra))
    work_dir = "/aws/{infra}".format(infra = infra)
    os.chdir(work_dir)
    subprocess.run(["terraform", "init"])
    subprocess.run(["terraform", "apply", "--auto-approve"])
    print("Your {infra} is ready! Go check it out!".format(infra = infra))
    os.chdir("")

def end_game(tflist):
  time.sleep(15)
  keep_alive = input("Are you there?\nAnything but 'yes' will teardown the infra: ")
  if keep_alive == 'yes':
    end_game(tflist)
  else:
    for infra in tflist:
      print("Destorying {infra}!".format(infra = infra))
      work_dir = "/aws/{infra}".format(infra = infra)
      os.chdir(work_dir)
      subprocess.run(["terraform", "destroy", "--auto-approve"])
      print("Destoryed {infra}!".format(infra = infra))
    
print("Welcome!")
usertf = input("Type directories to startup: ")
tflist = usertf.replace(" ", "").split(",")
# start_up(tflist)
end_game(tflist)
