import Les

l = Les.Les()
print(l.getQuant(), '\n')
print(l.estaCheia(), '\n')
print(l.estaVazia(), '\n')
if not l.estaCheia():
    l.inserirFim('A')
    
l.inserirFim('B')
l.inserirFim('C')
l.show()
print()

l.removerFim()
l.show()
print()

l.inserirFim('D')
l.show()
print()

l.inserirInicio('X')
l.show()
print()

l.removerInicio()
l.show()
print()

l.inserirAposDeterminado('D','B')
l.show()
print()
