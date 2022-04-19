##This code calculates the amount of time to download an archive through the size and the link speed

fileSize = float(input("Qual o tamanho do arquivo a ser baixado em MB?\n"))
linkSpeed = float(input("Qual velocidade do seu link em Mbps?\n"))
downloadTime = fileSize / (linkSpeed / 8)
print("O tempo de download desse arquivo em minutos é: " + str(downloadTime / 60))