result = {
	"tesoura": ["papel", "lagarto"], 
	"papel": ["pedra", "spock"], 
	"lagarto": ["spock", "papel"],  
	"spock":["tesoura", "pedra"], 
	"pedra": ["lagarto", "tesoura"]
	}

def lizard():
	sheldon, raj = input().split()
	if sheldon == raj:
		return 'De novo!'
	else:
		if raj.lower() in result[sheldon.lower()]:
			return 'Bazinga!'
		elif sheldon.lower() in result[raj.lower()]:
			return 'Raj trapaceou!'
		
teste = int(input())
for i in range(1, teste+1):
	print("Caso #{}:".format(i), lizard())
	