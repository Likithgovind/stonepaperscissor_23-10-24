from getpass import getpass as input
print("select your move R for rock,S for scissor and p for papper ")
player1=input("player1>")
player2=input("player2>")
if player1=="R" and player2=="S":
  print("player1 WON")
elif player1=="R" and player2=="P":
  print("player2 won")
elif player1=="R" and player2=="R":
  print("ITS TIE")
elif player1=="P" and player2=="R":
  print("player1 won")
elif player1=="P" and player2=="S":
  print("player2 won")
elif player1=="P" and player2=="P":
  print("ITS TIE")
elif player1=="S" and player2=="R":
  print("player2 won")
elif player1=="S" and player2=="P":
  print("player1 won")
elif player1=="S" and player2=="S":
  print("ITS TIE")