vertices = int(input("Digite o número de vértices: "))

with open ("grafoCompleto"+str(vertices)+".txt", "w") as arquivo:
    arquivo.write(str(vertices)+"\n")
    
    for i in range(vertices):
        for j in range(i+1, vertices):
            arquivo.write(str(i)+" "+str(j)+"\n")