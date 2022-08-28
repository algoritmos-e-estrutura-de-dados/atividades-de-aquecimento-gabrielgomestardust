linha = input().split(' ')

a, b, c = linha;

pi = 3.14159

trinagulo = (float(a)*float(c)/2)
trapezio = (((float(a)+float(b))*float(c))/2)
circulo = (pi*(float(c)*float(c)))
quadrado = (float(b) * float(b))
retangulo = (float(a) * float(b))

print('TRIANGULO: %.3f' %trinagulo)
print('CIRCULO: %.3f' %circulo)
print('TRAPEZIO: %.3f' %trapezio)
print('QUADRADO: %.3f' %quadrado)
print('RETANGULO: %.3f' %retangulo)