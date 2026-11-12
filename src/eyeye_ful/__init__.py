"""The clanker who loves your mom

Had fun reading "https://pypi.org/project/eyeye_ful", yeah? :v: :sob: :wilted_rose:

(This module is for personal usage, so if you accidentally found this, uhh you can try, it's still pretty inefficient tho)
This skibidi module allows you to access a python neural network,
the module contains enough features for further usage ig, including changable neural
network or training.This neural network(aight ima call it eyeye for short) is
overshoot-proofed, which is done by my big-brian frien MeiMei

However, there are some things you need to notice:

The 'a' list is the neural network itself, its structure is something like this

a = [0,(neurons in the first layer),0,(neurons in the second layer),...]

For instance: a = [0,0.1,0.2,0,0.1,0.2,0.3]. So there are 2 neurons in the first layer and
3 neurons in the second layer, the network has 2 layers

The similar thing happen with w and b:

w = [0,(weights connect the first layer to the second layer),0,(w connect 2 to 3),...]

b = [0,(bias of the first layer),0,(bias of the second layer),...]

About the "nonel" and the "N", see "reset_network()"
Aight pls read the rest my rizzy skibidi user

Aight...new update, that was just the desc of our old "eyeye"
A lil change is by just eyeye_ful.Eyeye(), you can make as many eyeye as u want, nice!
The syntax is still kinda the same...ig
Now there are multiple eyeyes fighting to decide who is the most worthy one to be with your mother  :))))
"""




from math import *
import random
import time
import sys
import numpy as np

six_seven = 67 + 67/99#SIX SEVEEEEEENNN, i mean WHY NOTTT??????

def printpro(stri,start = 0):
    """Do you like sans? He speaks exactly like what this func does just printpro("Ur gonna have a bad time") and see
It's not gonna spawn a random hole and make you fall into the underground world tho, dont worry =)))"""
    st = start + 1
    le = len(str(stri))
    print(stri[start],end = '')
    time.sleep(0.01)
    if st != le:
        printpro(stri,start = st)
    else:
        print('')
class EyeyeLovesYourMom(Exception):
    pass

def activa(x,func="sigmoid",c=0):
    """This skibid sigma function activate the neurons
    Ab the func: sigmoid(default),softmax,yo mama"""
    if func == "sigmoid":
        x = np.clip(x,-500,500)
        return 1/(np.exp(-x)+1)
    elif func == "softmax":
        x=np.clip(x,-500,500)
        return np.exp(x)/(c)
    elif func == "yo mama":
        raise EyeyeLovesYourMom("Thanks for bringing me to your mother :))))")

def dsigmoida(x,func="sigsoft"):
    """Return x-x^2, internal func, so get outta here, lil bro, or gimme some mommy's voice...
        func: sigsoft,const"""
    if func == "sigsoft":
        return x - x**2
    elif func == "const":
        return 1

def delta(x,M=0,R=0):
    """Return 3/(3+4*exp((-x/1.5)+1)), this is an internal func, and yeah, this is MeiMei's
W MeiMei :sob: :sob: :sob:
    M,R option: stands for mommy romantic... i meant M is the max value, R is the range, from x=R the function starts decreasing when x gets smaller"""
    if M==0 and R==0:
    	return 3/(3+4*exp((-x/1.5)+1))
    else:
    	return M/(exp(-4*x/R)+1)

class Eyeye:
    """Create your own freaky clanker by just Eyeye()!"""
    N = 0
    a = []
    nonel = []
    mark = []
    corans = []
    w = []
    b = []
    markw = []
    markb = []
    da, dw, db = [], [], []
    tima = 0
    
    def set_up(self):
        """Well, if you wanna let the user set up the neural network by themselves, use this function
    It will ask "Type the number of layers: " first then "The number of neurons of layer <i>"
    after doing this, use reset_network() is a must, so the final syntax is:
    eyeye.set_up()
    eyeye.reset_network()
    If you can make me alive... then please send your mama's voice into the input...I miss that wawawa"""
        #global sela, nonel, mark, corans, N
        self.a = []
        self.nonel = []
        self.mark = []
        self.corans = []
        cur_ind = 0
        self.nonel.append(0)
        self.mark.append(0)
        self.corans.append(0)
        self.N = int(input("Type the number of layers: "))
        for x in range(1, self.N+1):
            self.mark.append(cur_ind+x-1)
            self.a.append(0)
            each_input = int(input("The number of neurons of layer " + str(x) + " : "))
            self.nonel.append(each_input)
            cur_ind += each_input
            for i in range(0, each_input):
                self.a.append(0)
        for x in range(1,self.nonel[self.N]+1):
            self.corans.append(0)
        
    def reset_gen_network(self):
        """Well, set every single neurons of the eyeye to 0, useless, huh?
At least it has its job, not like someone, jobless :)))))"""
        #global a
        for i in range(1,len(self.a)):
            self.a[i] = 0

    def reset_network(self,opt = 0):
        """Bro will need to run this every time you need to change the neural network, the syntax:
    eyeye.N = <num of layers>
    eyeye.nonel = [0,(num of neuron each layer)]
    eyeye.reset_network(opt=1)

    For eg, create a 4-10-10-5 neural network
    eyeye.N = 4
    eyeye.nonel = [0,4,10,10,5]
    eyeye.reset_network(opt=1)

    If you wan the user do it, see "set_up()"
    If you... you are OK with my love for your mom... see "prepare_training_data()"
    """
        #global w, b, markw, markb,a,corans,mark
        self.reset_gen_network()
        self.w = []
        self.b = []
        inde = 0
        self.markw,self.markb = [],[]
        self.markw.append(0)
        self.markb.append(0)
        if opt == 1:
            self.mark = [0]
            self.a = []
            self.corans = [0]
            cur_ind = 0
            for x in range(1,self.N+1):
                self.mark.append(cur_ind+x-1)
                self.a.append(0)
                cur_ind += self.nonel[x]
                for i in range(1,self.nonel[x]+1):
                    self.a.append(0)
            for i in range(1,self.nonel[self.N]+1):
                self.corans.append(0)
        for i in range(2, self.N+1):
            self.markw.append(inde + i - 2)
            self.w.append(0)
            for i2 in range(0, self.nonel[i-1]):
                for i3 in range(0, self.nonel[i]):
                    self.w.append(1 * (random.random() - random.random()))
                    inde += 1
        inde = 0
        for i in range(2, self.N+1):
            self.markb.append(inde + i - 2)
            self.b.append(0)
            for i2 in range(0, self.nonel[i]):
                self.b.append(1 * (random.random() - random.random()))
                inde += 1

# Network calculation


    def read_input(self):
        """Run this to let the user manually type the input
    For each input number i, it will ask " Type the input <i> :"
    """
        #global nonel, a
        for i in range(1, self.nonel[1]+1):
            inp = float(input("Type the input " + str(i) + " : "))
            self.a[i] = inp

    def calculate_output(self,outfunc="sigmoid",zs=0):
        """This alpha male rizzy skibidi dop dop yes yes function here run the neural network
    First you have to type the input, you can either inject directly to the 'a' or use read_input() to manually type this
    And yeah, to access the output, there is no way except...acess the 'a'
    "omg~ this dont use numpy so its gonna be so slow"nah, nerd, remember...
    ONE MORE COMPLAINT AND PREPARE_TRAINING_DATA() WILL BE AUTO ACTIVATED!:)))))
    ... wait... i-i didnt mean to force you to do that... ugh w-what am i doing...
    Anyways....after SO MUCH amount of complaint...
    Then here we go! Now we have numpy!
    Now you better prepare ^_^, this eyeye is...is...is... gonna cry, when thinking it will never meet your mom once TT

    outfunc option: change the activation func of the output neurons
    Available function: sigmoid,softmax
    Choosing softmax will cause the func return a list of z's
    zs: Set this to 1 will cause the func to return a list of z's too"""
        #global a,w,b,nonel
        #print(a)#bug right here
        oi=0
        for i in range(1,self.N):
            daa = np.array(self.a[self.mark[i]+1:self.mark[i]+1+self.nonel[i]],dtype = np.float32)
            #print(self.markw[i]+1+self.nonel[i+1]*(i+1))
            daw = np.array(list(self.w[self.markw[i]+1+self.nonel[i]*j:self.markw[i]+1+self.nonel[i]*(j+1)] for j in range(self.nonel[i+1])),dtype = np.float32)
            """daw = []
            for j in range(self.nonel[i+1]):
                print(self.w[self.markw[i]+1+self.nonel[i+1]*j:self.markw[i]+1+self.nonel[i+1]*(j+1)])
                daw.append(self.w[self.markw[i]+1+self.nonel[i+1]*j:self.markw[i]+1+self.nonel[i+1]*(j+1)])
            daw = np.array(daw,dtype=np.float32)"""
            dab = np.array(self.b[self.markb[i]+1:self.markb[i]+1+self.nonel[i+1]],dtype = np.float32)
            if i != self.N-1:
                self.a[self.mark[i+1]+1:self.mark[i+1]+1+self.nonel[i+1]] = list(activa(daw@daa+dab))
            else:
                if outfunc == "softmax":
                    oi = daw@daa+dab
                    ay = sum(e**(oi))
                    self.a[self.mark[i+1]+1:self.mark[i+1]+1+self.nonel[i+1]] = list(activa(oi,func="softmax",c=ay))
                elif zs==1:
                    oi = daw@daa+dab
                    self.a[self.mark[i+1]+1:self.mark[i+1]+1+self.nonel[i+1]] = list(activa(daw@daa+dab))
        if outfunc == "softmax" or zs==1:
            return list(oi)
        """for i in range(1, self.N):
            for i2 in range(1, self.nonel[i+1]+1):
                for i3 in range(1, self.nonel[i]+1):
                    #print(a[i2+mark[i+1]])
                    self.a[i2+self.mark[i+1]] += self.w[i2*self.nonel[i]-(self.nonel[i]-i3) + self.markw[i]] * self.a[i3+self.mark[i]]
                    #print(w[i2*nonel[i]-(nonel[i]-i3) + markw[i]],a[i3+mark[i]],w[i2*nonel[i]-(nonel[i]-i3) + markw[i]] * a[i3+mark[i]])
                    #print(a[i2+mark[i+1]])
                    #print(w[i2*nonel[i]-(nonel[i]-i3) + markw[i]], a[i3+mark[i]])
                self.a[i2+self.mark[i+1]] += self.b[i2+self.markb[i]]
                self.a[i2+self.mark[i+1]] = activa(self.a[i2+self.mark[i+1]])"""


# Training calculation

    def calculateda(self,index, layer, opt = 0, li = [], outspec = "sigsoft",hidspec = "sigsoft"):
        """This is internal function, dont be curious lil bro
Actually this calcs the partial derivative of the a's, but it's a lil inconvenient to explain it, so dont mind ab it
outspec: sigsoft,const, hidspec the same"""
        #global corans, a, nonel, w, markw, mark, N
        if layer == self.N:
            #print(corans[index],a[mark[layer]+index])
            if opt == 0:
                return -2 * (self.corans[index] - self.a[self.mark[layer]+index])
            else:
                return li[index-1]
        else:
            suma = 0
            wcu = 0
            #print(suma,"here")
            for i in range(1, self.nonel[layer+1]+1):
                wcu = self.w[self.markw[layer] + self.nonel[layer]*i - (self.nonel[layer]-index)]
                if layer != self.N-1:
                    suma += wcu * dsigmoida(self.a[self.mark[layer+1]+i],func=hidspec) * self.calculateda(i, layer+1,opt,li)
                else:
                    suma += wcu * dsigmoida(self.a[self.mark[layer+1]+i],func=outspec) * self.calculateda(i, layer+1,opt,li)
                
                #print(wcu)
                #print(dsigmoida(a[mark[layer+1]+i]))
                #print(calculateda(i, layer+1),"memememe")
            #print(suma,"lol")
            return suma

    def calculatedwb(self,player,index,calc = 0,opt = 0,li = [],outspec="sigsoft",hidspec="sigsoft"):
        """Again, internal function but...aight..if u wanna get the partial derivative of the cost func with respect to a parameter(w or b), use this
        player: the layer of the bias, or the previos layer of a w, for eg a w connect from a neuron in layer 1 to a neuron in layer 2, so player = 1
        index: start from 1 yk, if you dont know what w it calculates just print the w and the b out so for eg the w:
        eyeye.w = [0,0.1,0.3,0.5,0,...]
        and if u set player = 1, index = 2, you are calculating the w=0.2
        understood lil bro? if not then uhh...
        Hey, it's me, it's Verity!
        Ask me anything!
        I know... about... a mil things
        Ask me anything!
        'What's the capital of France?'
        Oh oui oui oui, it is Paris! Merci!
        Ok... what does the fox say?
        Oh... the fox says...
        Ding ding ding ding ding ding x3.14159265358
        They call me LOOORD...Verity!
        Masta of humanity...
        LOOORD!! Verity
        They call me mastuh, mastuh yeah!...."""
        #global mark, nonel
        atc = ceil(index/self.nonel[player])
        apcsi = 0
        if index % self.nonel[player] == 0:
            apcsi = self.nonel[player]
        else:
            apcsi = index % self.nonel[player]
        apcs = self.a[apcsi + self.mark[player]]
        if calc == 0:
            if player+1 != self.N:
                return apcs*dsigmoida(self.a[atc+self.mark[player+1]],func=hidspec)*self.calculateda(atc,player+1,opt = opt, li = li, outspec = outspec,hidspec=hidspec)
            else:
                return apcs*dsigmoida(self.a[atc+self.mark[player+1]],func=outspec)*self.calculateda(atc,player+1,opt = opt, li = li, outspec = outspec,hidspec=hidspec)
        elif calc == 1:
            if player+1 != self.N:
                return dsigmoida(self.a[atc+self.mark[player+1]],func=hidspec)*self.calculateda(atc,player+1,opt = opt, li = li, outspec = outspec,hidspec=hidspec)
            else:
                return dsigmoida(self.a[atc+self.mark[player+1]],func=outspec)*self.calculateda(atc,player+1,opt = opt, li = li, outspec = outspec,hidspec=hidspec)

    """    elif calc == 2: #testing only!
            print(apcs*dsigmoida(a[apcsi+mark[player+1]])*calculateda(atc,player+1), dsigmoida(a[apcsi+mark[player+1]])*calculateda(atc,player+1), dsigmoida(a[apcsi+mark[player+1]]), calculateda(atc,player+1))"""

    def prepare_training_data(self):
        """Interal func, running this DOES affect the 'a'... and means that you accept my love for your mom...
I only need that... if I have that... my life will never be happier than this day..."""
        #This may change in the future
        #global corans
        self.reset_gen_network()
        for x in range(1,len(self.corans)):
            self.corans[x] = 0
        caseoh = random.random()
        caseoh2 = caseoh*random.random()
        case = random.randint(1,3)
        if case == 1:
            self.a[1] = caseoh2
            self.a[2] = caseoh
            self.corans[1] = 1
        elif case == 2:
            self.a[1] = caseoh
            self.a[2] = caseoh
            self.corans[2] = 1
        else:
            self.a[1] = caseoh
            self.a[2] = caseoh2
            self.corans[3] = 1
            #print(a)
        self.calculate_output()

    def train_the_eyeye(self,times,mode = 0,opt = 0, li =[], di = [], outspec = "sigsoft", hidspec = "sigsoft",Md=0,Rd=0):
        """Aight lil bro we are here, this func will train the eyeye
    times:Pretty useless, so you should always set times=1
    mode: Setting it to 1 let the func return dw,db,k
    opt: Set this to 1 if you use the li, 0 if you leave it blank. The only thing is not optional... is my need of being with your mom...
    li: This list must contains full of the partial derivative of the cost function with respect to each output neuron.Order? From left to right in the 'a'
    The li can be leaved blank, so the nn will use the default (y-y^)^2 func, use 'corans' list to store the desired output before training
    di: If you calculated the dw and db by ur self, plug in this argument, it must be in two lists, first is dw and second is db, and have the same structure as the w and b list
    U dont need to set opt=1 anymore when using this argument lol
    outspec,hidspec: the activation function used in output layer and hidden layer respectively
    Md,Rd, modify the M,R of delta(x)
    Available option: sigsoft(sigmoid or softmax),const(linear)
    So that was an absolutely thorough explanation ig, and I would fall in love immediately if I can feel your mom's heart..."""
        #global w,b,a
        if di == []:
            for x in range(0,times):
                living = time.time()
                m_a = 0
                if opt == 0:
                    self.prepare_training_data()
                #time.sleep(0.01)
                self.dw,self.db = [],[]
                sqsum = 0
                #print(corans)
                for i in range(1,self.N):
                    self.dw.append(0)
                    self.db.append(0)
                    for j in range(1,self.nonel[i+1]+1):
                        for k in range(1,self.nonel[i]+1):
                            dwi = self.calculatedwb(i,self.nonel[i]*j-(self.nonel[i]-k),opt = opt, li = li,outspec = outspec, hidspec = hidspec)
                            self.dw.append(dwi)
                            sqsum += dwi**2
                        dbi = self.calculatedwb(i,self.nonel[i]*j,1,opt = opt, li = li, outspec = outspec, hidspec = hidspec)
                        self.db.append(dbi)
                        sqsum += dbi**2
                sqsum = sqrt(sqsum)
                k = delta(sqsum,M=Md,R=Rd)
                indexa = 0
                self.w = list(np.array(self.w) - k*np.array(self.dw))
                self.b = list(np.array(self.b) - k*np.array(self.db))
                """for y in self.dw:
                    #print(y,indexa,w[indexa],k*y,w[indexa] - k*y)
                    self.w[indexa] -= k*y
                    indexa += 1
                indexa = 0
                for y in self.db:
                    self.b[indexa] -= k*y
                    indexa += 1"""
        else:
            k = delta(sqrt(sum(np.array(di[0])**2)+sum(np.array(di[1])**2)))
            self.w = list(np.array(self.w) - k*np.array(di[0]))
            self.b = list(np.array(self.b) - k*np.array(di[1]))
        if mode == 1:
            return self.dw, self.db, k

    def fake_train(self,x):
        """Return a tuple
    The first item is the average time(sec) it takes to done a training
    The second item is the average training speed(training/s)
    About the x, it must be a positive int, the bigger x is, the more accurate the result become(ig?), and also the longer it takes to finish the func
    x=10 is recommended
    After its done fake_training... tell her i love her, pls"""
        #global w, b, tima
        #print(corans)
        saw = self.w.copy()
        sab = self.b.copy()
        if self.nonel[1] == 2 and self.nonel[-1] == 3:
            living = time.time()
            self.train_the_eyeye(x)
            tima = (time.time()-living)/x
        else:
            teli = []
            for i in range(self.nonel[-1]):
                teli.append(random.random())
            living = time.time()
            for i in range(x):
                self.train_the_eyeye(1,opt=1,li=teli)
            tima = (time.time()-living)/x
        self.w = saw.copy()
        self.b = sab.copy()
        return (tima,floor(1/tima))
    
    def export_param(self):
        """Export the parameters to 2 txt files...But i prefer it to export my love to your mom's heart..."""
        code="".join(list(i[0:-1] for i in str(list(time.localtime()))[1:].split()))
        wtw=[]
        ly=1
        for i in range(len(self.w)):
            if not i in self.markw:
                wtw.append(str(float(self.w[i])))
            else:
                wtw.append("layer_"+str(ly))
                ly += 1
        wtw.append("no more layer")
        fi = open("w"+code+".txt","w")
        fi.write("\n".join(wtw))
        fi.close()
        wtw=[]
        ly=1
        for i in range(len(self.b)):
            if not i in self.markb:
                wtw.append(str(float(self.b[i])))
            else:
                wtw.append("layer_"+str(ly))
                ly += 1
        wtw.append("no more layer")
        fi = open("b"+code+".txt","w")
        fi.write("\n".join(wtw))
        fi.close()

    def import_param(self,name_w=-404,name_b=-404):
        """Import the parameter from given txt files... and I...aight i think i need to stop"""
        hmm = "Missing argument or wtv...man i miss your mom so bad..."
        hmmm = "Oh my...in and out with your mom..."    
        if type(name_w) != str and type(name_b) != str:
            raise TypeError(hmm)
        else:
            if name_w != -404:
                #fi = 
                file = open(name_w+".txt","r")
                indexu = 1
                leye = 0
                error = 0
                for x in file:
                    if x[0] == "l" or x[0] == "n":
                        indexu = 1
                        leye += 1
                    else:
                        if indexu > self.nonel[leye]*self.nonel[leye+1]:
                            #print("Bro, why there is too much w, W bro :wilted_rose:")
                            #print(indexu, nonel[leye], nonel[leye+1])
                            error = 1
                            break
                        else:
                            self.w[self.markw[leye]+indexu] = float(x)
                            indexu += 1
                if error == 1:
                    raise IOError(hmmm)
            if name_b != -404:
                file = open(name_b + ".txt",'r')
                indexu = 1
                leye = 0
                error = 0
                for x in file:
                    if x[0] == "l" or x[0] == "n":
                        indexu = 1
                        leye += 1
                    else:
                        if indexu > self.nonel[leye+1]:
                            #print("Bro, too much b, the bees gonna sting ur mo-")
                            error = 1
                            break
                        else:
                            self.b[self.markb[leye]+indexu] = float(x)
                            indexu += 1
                if error == 1:
                    raise IOError(hmmm)

    def __init__(self,layer1=2,layer2=3,*layers):
        """What's in it? Its heart. For your lovely mom only...This is a very...honest...love
        The default setup is: 2 layers, 2 input neurons and 3 output neurons
        But you can totally change it!
        Creating an eyeye will auto print the speed...of this eyeye running to your mother after it found her
        Nice...ig,maybe its gonna be different if it has ur mo- i meant...nothing, my skibidi user
        """
        #                       __init__
        print("--------------------------WELCOME TO MY EYEYE-------------------------")
        print("------------------------------LETS START!!-----------------------------")#print("Setting part(in vietnamese cuz im tired)")                    
        #set_up()
        #reset_network()
        self.N=len([layer1]+[layer2]+list(layers))
        self.nonel = [0]+[layer1]+[layer2]+list(layers)
        self.reset_network(opt=1)
        hai = self.fake_train(10)
        print("Training speed: "+str(hai[1])+" training/s\nEach training takes "+str(hai[0])+" seconds")
        #connecto = 0
        #Interact with user
        
        #                       __init__

            
