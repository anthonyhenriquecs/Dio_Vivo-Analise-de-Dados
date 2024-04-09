def calculadora(operação):
    def soma(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mult(a,b):
        return a*b
    
    def div(a,b):
        return a/b
    
    match operação:
        case "+":
            return soma
        
        case "-":
            return sub
        
        case "*":
            return mult
        
        case "/":
            return div
        
print(calculadora('*')(2,2))

variavel = calculadora('-')(2,2)
print(variavel)