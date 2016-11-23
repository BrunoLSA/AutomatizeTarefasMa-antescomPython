import PyPDF2
import re

pdfFileObj = open('161116 ESCAVOO1GAVCA.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
list_text = text.splitlines()


# exclui informações extras da escala. Deixa a lista apenas com os voos.
for n in list_text:
    if re.match(r'..:..Z', n):
        list_text = list_text[list_text.index(n):]
        break

for n in list_text:
    if re.match(r'PLC - .*', n):
        list_text = list_text[:list_text.index(n)]
        break


total_missoes = []
list_aux = []

print('voos = ', total_missoes)


for n in list_text:
    if re.match(r'..:..Z', n):
        list_aux = []
        list_aux.append(n)
        total_missoes.append(list_aux)
    else:
        list_aux.append(n)

print(total_missoes)

total_anvs = []

for i in total_missoes:
    if len(i) < 11:
        # define o voo de apenas 1 aeronave
        if re.match(r'[A-Z]{3}', i[-2]) and len(i[-2]) == 3: # checa se a aeronave tem 2 pilotos
            total_anvs.append(i)
        else:
            i.append('') # insere campo em branco para nacele traseira
            total_anvs.append(i)

    elif len(i) < 15:
        # define o voo de 2 aeronaves
        if re.match(r'[A-Z]{3}', i[7]) and len(i[7]) == 3: # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            anv2 = i[8:]

        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            anv2 = i[7:]

        anv2.insert(0, anv1[1])
        anv2.insert(0, anv1[0])
        anv2.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv2[-2]) and len(anv2[-2]) == 3: # checa se a segunda aeronave tem 2 pilotos
            total_anvs.append(anv2)
        else:
            anv2.append('')
            total_anvs.append(anv2)

    elif len(i) < 19:
        # define o voo de 3 aeronaves
        if re.match(r'[A-Z]{3}', i[7]) and len(i[7]) == 3: # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3: # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            anv3 = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            anv3 = resto[7:]

        anv3.insert(0, anv1[1])
        anv3.insert(0, anv1[0])
        anv3.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv3[-2]) and len(anv3[-2]) == 3:  # checa se a terceira aeronave tem 2 pilotos
            total_anvs.append(anv3)
        else:
            anv3.append('')
            total_anvs.append(anv3)

    elif len(i) < 23:
        # define o voo de 4 aeronaves
        if re.match(r'[A-Z]{3}', i[7]) and len(i[7]) == 3: # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3: # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            resto = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3: # checa se a terceira aeronave tem 2 pilotos
            anv3 = resto[:8]
            total_anvs.append(anv3)
            anv4 = resto[8:]
        else:
            anv3 = resto[:7]
            anv3.append('')
            total_anvs.append(anv3)
            anv4 = resto[7:]

        anv4.insert(0, anv1[1])
        anv4.insert(0, anv1[0])
        anv4.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv4[-2]) and len(anv4[-2]) == 3:  # checa se a quarta aeronave tem 2 pilotos
            total_anvs.append(anv4)
        else:
            anv4.append('')
            total_anvs.append(anv4)

    elif len(i) < 27:
        # define o voo de 5 aeronaves
        if re.match(r'[A-Z]{3}', i[7]) and len(i[7]) == 3:  # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            resto = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a terceira aeronave tem 2 pilotos
            anv3 = resto[:8]
            total_anvs.append(anv3)
            resto = resto[8:]
        else:
            anv3 = resto[:7]
            anv3.append('')
            total_anvs.append(anv3)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a quarta aeronave tem 2 pilotos
            anv4 = resto[:8]
            total_anvs.append(anv4)
            anv5 = resto[8:]
        else:
            anv4 = resto[:7]
            anv4.append('')
            total_anvs.append(anv4)
            anv5 = resto[7:]

        anv5.insert(0, anv1[1])
        anv5.insert(0, anv1[0])
        anv5.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv5[-2]) and len(anv5[-2]) == 3:  # checa se a quinta aeronave tem 2 pilotos
            total_anvs.append(anv5)
        else:
            anv5.append('')
            total_anvs.append(anv5)

    elif len(i) < 31:
        # define o voo de 6 aeronaves
        if re.match(r'[A-Z]{3}', i[7]) and len(i[7]) == 3:  # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            resto = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a terceira aeronave tem 2 pilotos
            anv3 = resto[:8]
            total_anvs.append(anv3)
            resto = resto[8:]
        else:
            anv3 = resto[:7]
            anv3.append('')
            total_anvs.append(anv3)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a quarta aeronave tem 2 pilotos
            anv4 = resto[:8]
            total_anvs.append(anv4)
            resto = resto[8:]
        else:
            anv4 = resto[:7]
            anv4.append('')
            total_anvs.append(anv4)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]) and len(resto[7]) == 3:  # checa se a quinta aeronave tem 2 pilotos
            anv5 = resto[:8]
            total_anvs.append(anv5)
            anv6 = resto[8:]
        else:
            anv5 = resto[:7]
            anv5.append('')
            total_anvs.append(anv5)
            anv6 = resto[7:]

        anv6.insert(0, anv1[1])
        anv6.insert(0, anv1[0])
        anv6.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv6[-2]) and len(anv6[-2]) == 3:  # checa se a sexta aeronave tem 2 pilotos
            total_anvs.append(anv6)
        else:
            anv6.append('')
            total_anvs.append(anv6)



print(total_anvs)

for i in total_anvs:
    print(len(i))

print(len(total_anvs))