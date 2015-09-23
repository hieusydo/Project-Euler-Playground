##num = ['','one','two','three','four','five','six','seven','eigth','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
##for d in ('twenty','thirty','forty','fifty', 'sixty', 'seventy', 'eighty','ninety'):
##    for n in num[:10]:
##        num.append(d+n)
##for c in num[1:10]:
##    num.append(c+'hundred')
##    for n in num[1:100]:
##        num.append(c+'hundredand'+n)
##num.append('onethousand')
##print(sum([len(w) for w in num]))

from num2word import to_card
