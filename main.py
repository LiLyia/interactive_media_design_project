#from project import path as p
#from flask import Flask, render_template, request
import path as p



import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(abspath(__file__))))


def path():
  start = "South gate"
  end = 507
  if start == "South gate":
      start = 100
  else:
      start = int(start)
  if end == "South gate":
      end = 100
  else:
      end = int(end)
  p.main(start, end)
  text = p.textpath(p.minpath, start, end)
  return text
path()
