import sys
import time
import random
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/lerod/Downloads"


class  fileMovementHandler(FileSystemEventHandler):
   
    def on_created(self,event):
        print(f"Olá, {event.src_path} foi criado!")
    def on_deleted(self,event):
        print(f"Opa, alguem excluiu {event.src_path}!")
    def on_modified(self,event):
        print(f"Olá, {event.src_path} foi modificado!")
    def on_moved(self,event):
        print(f"Olá, alguém moveu{event.src_path} para {event.dest_path}")
        

event_handler = fileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir,  recursive=True)
observer.start()
try:
  while True:
    time.sleep(2)
    print("executando...")
except KeyboardInterrupt:
  print("interrompido!")
  observer.stop()

