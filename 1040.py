a,b,c,d=map(float,input().split())
m=float((a*2+b*3+c*4+d)/10)
print("Media: %.1f" % m)
if m>=7.0:print("Aluno aprovado.")
elif m>=5.0:
    print("Aluno em exame.")
    e=float(input())
    print("Nota do exame: %.1f" % e)
    if (e+m)/2.0>5.0:print("Aluno aprovado.")
    else:print("Aluno reprovado.")
    print("Media final: %.1f" % ((e+m)/2.0))
else:print("Aluno reprovado.")
