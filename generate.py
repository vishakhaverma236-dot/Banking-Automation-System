import random
def generate_captcha():
    li=[]
    for i in range(2):
        digit=random.randint(0,9)
        li.append(str(digit))
    for i in range(2):
        ltter=random.randint(97,122)
        ch=chr(ltter)
        li.append(ch)

    random.shuffle(li)
    captcha='  '.join(li)
    return captcha


if __name__=='__main__':
    print(generate_captcha())
