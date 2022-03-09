import random,sys

def sortea():
	sorteados = [random.randint(0,2) for i in range(10)]
	return random.choice(sorteados)

def escolhe(escolhida,trocar):
	global quantGanhouTrocou,quantGanhouNaoTrocou,quantPerdeuTrocou,quantPerdeuNaoTrocou

	portas = {'p1':"",'p2':"",'p3':""}
	correta = sortea()
	ganhou = False

	if escolhida=="p1":
		naoEscolhidas = ["p2","p3"]
	elif escolhida=="p2":
		naoEscolhidas = ["p1","p3"]
	elif escolhida=="p3":
		naoEscolhidas = ["p1","p2"]
	else:
		print("que")
		return 1

	for i in range(3):
		if correta==i:
			portas['p%d'%(i+1)] = "dinheiro"
		else:
			portas['p%d'%(i+1)] = "cabra"

	if portas[naoEscolhidas[0]]=="dinheiro":
		notChoose = naoEscolhidas.pop()
	else:
		notChoose = naoEscolhidas.pop(0)

	#print("abrindo porta %s: %s!"%(notChoose,portas[notChoose].upper()))

	if trocar:
		naoEscolhidas[0],escolhida = escolhida,naoEscolhidas[0]
		#print("como vc trocou, ",end="")
	else:
		pass
		#print("como vc escolheu nao trocar, ",end="")

	if portas[escolhida]=="dinheiro":
		#print("vc ganhou!")
		ganhou = True
	else:
		pass
		#print("vc perdeu :(")

	if ganhou:
		if trocar:
			quantGanhouTrocou += 1
		else:
			quantGanhouNaoTrocou += 1
	else:
		if trocar:
			quantPerdeuTrocou += 1
		else:
			quantPerdeuNaoTrocou += 1

tentativas = 100000
trocar = False
quantGanhouTrocou = quantGanhouNaoTrocou = quantPerdeuTrocou = quantPerdeuNaoTrocou = 0

for i in range(tentativas):
	escolhe("p2",False)
	escolhe("p3",True)

if tentativas==1000000:
	print("\n[*] Executando 1 milhão de vezes")
elif tentativas==100000:
	print("\n[*] Executando 100.000 vezes")
else:
	print("\n[*] Executando %d vezes"%tentativas)


print("\nQuando vc escolheu trocar, vc: ")
print("\tganhou = %.3f%% vezes"%(quantGanhouTrocou/tentativas*100))
print("\tperdeu = %.3f%% vezes"%(quantPerdeuTrocou/tentativas*100))

if quantGanhouTrocou>quantPerdeuTrocou:
	print("\nOu seja, valeu a pena trocar :D")
else:
	print("\nOu seja, não valeu a pena trocar :(")

print("\nQuando vc escolheu NÃO trocar, vc: ")
print("\tganhou = %.3f%% vezes"%(quantGanhouNaoTrocou/tentativas*100))
print("\tperdeu = %.3f%% vezes"%(quantPerdeuNaoTrocou/tentativas*100))

if quantGanhouNaoTrocou>quantPerdeuNaoTrocou:
	print("\nOu seja, valeu a pena trocar :D")
else:
	print("\nOu seja, não valeu a pena trocar :(")

