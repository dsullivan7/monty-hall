import montyhall
import sys

m = montyhall.MontyHall()
ng = int(sys.argv[1])
nd = int(sys.argv[2])
if ng >= 1 and nd >= 3:
	m.play_games(ng, nd)
else:
	print "The number of games needs to be at least 1 and the number of doors has to be at least 3"
