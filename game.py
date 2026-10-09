#!/usr/bin/env python3
"""Fullscreen local two-player tic tac toe."""
import curses
from ui import put,run
LINES=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
def winner(board):return next((board[a] for a,b,c in LINES if board[a]!='.' and board[a]==board[b]==board[c]),None)
def move(board,index,turn):
 if index not in range(9) or board[index]!='.':raise ValueError('Choose an empty cell.')
 board[index]=turn;return winner(board)
def loop(s):
 board=['.']*9;turn='X';selected=0;message='';done=False
 while True:
  h,w=s.getmaxyx();s.erase();put(s,0,1,'TIC TAC TOE - two local players',curses.A_BOLD);put(s,h-1,1,'1-9 or arrows+Enter | R restart | Esc/q exit')
  if h>=15 and w>=30:
   cw=max(5,(w-4)//3);ch=max(2,(h-6)//3)
   for i,v in enumerate(board):
    y=3+(i//3)*ch;x=2+(i%3)*cw
    for n in range(ch):put(s,y+n,x,'│')
    put(s,y+ch//2,x+cw//2,str(i+1) if v=='.' else v,curses.A_REVERSE if selected==i else curses.A_BOLD)
   for row in (1,2):put(s,3+row*ch-1,2,'─'*(cw*3))
   put(s,h-3,1,message or turn+' turn')
  else:put(s,2,1,'Resize to30x15.')
  s.refresh();key=s.getch()
  if key in (27,ord('q')):return
  if key==ord('r'):board=['.']*9;turn='X';done=False;message='';continue
  if key==curses.KEY_LEFT:selected=max(0,selected-1)
  elif key==curses.KEY_RIGHT:selected=min(8,selected+1)
  elif key==curses.KEY_UP:selected=max(0,selected-3)
  elif key==curses.KEY_DOWN:selected=min(8,selected+3)
  elif not done and (key in (10,13) or ord('1')<=key<=ord('9')) and h>=15 and w>=30:
   index=key-ord('1') if ord('1')<=key<=ord('9') else selected
   try:won=move(board,index,turn)
   except ValueError as exc:message=str(exc);continue
   done=bool(won or '.' not in board);message=won+' wins!' if won else 'Draw.' if done else '';turn='O' if turn=='X' else 'X'
if __name__=='__main__':
 import sys
 if '--version' in sys.argv:print('1.0.0')
 else:raise SystemExit(run(loop))
