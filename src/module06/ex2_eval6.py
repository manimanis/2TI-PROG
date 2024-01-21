from numpy import array


ch1 = "sagittarius"
ch2 = "Pegasus"

t1 = array([str]*5)
t2 = array([int()]*5)

t1[0] = ch1[0]
t1[1] = ch1[len(ch1) // 2]
t1[2] = ch1[ch1.find(t1[0])+1:ch1.find(t1[1])+1]
t1[3] = ch2[:2] + ch2[5:]
t1[4] = t1[3][:2] + t1[2][:2] + ch2[1]

t2[0] = len(t1[0]+t1[4])
t2[1] = (t2[0] % 2 == 0) * abs(1-t2[0])
t2[4] = int(str(t2[1]) + "0" + str(t2[0]))
t2[2] = (t2[4]>t2[0])*t2[0]+(t2[4]<=t2[0])*t2[4]
t2[3] =  ord(str(t2[0]))+ord(str(t2[2]))*2

print(t1)
print(t2)
