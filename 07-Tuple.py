# Tuples

# Tuples são semelhantes às lists, porém é apenas para visualizar os dados inseridos, você não consegue modificá-los.

tup  = ("hi", "Python", 2)    
# Checando tipo de Tup  
print (type(tup))    
  
# Printando o Tup 
print (tup)  
  
# Cortando o tuple 
print (tup[1:])    
print (tup[0:1])    
  
# Concatenando o Tuple, utilizando o operador "+"  
print (tup + tup)
  
# Repetindo o Tuple, utilizando o operador "*"
print (tup * 3) 
  
# Ao tentar adicionar um valor, irá printar um erro.  
tup[2] = "hi"
