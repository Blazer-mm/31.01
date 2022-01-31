teksts=input("Ievadi tekstu: ")
def reverseWords(teksts):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar1.reverse()
    teksts=""
    for elements in sar1:
      teksts+=elements
      teksts+=" "
  else:
    teksts = "Pārāk īss teikums!"
  return teksts
print(reverseWords(teksts))