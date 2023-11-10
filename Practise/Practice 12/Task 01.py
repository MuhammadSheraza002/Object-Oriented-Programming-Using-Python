def main():
    f = open('players.txt','r')
    name = [''] * 100
    country = [''] * 100
    startyear = [0]*100
    endyear = [0]*100
    no_match = [0]*100
    no_inning= [0]*100
    no_time_not_out= [0]*100
    totalruns= [0]*100
    highestruns= [0]*100
    avgruns= [0]*100
    hundreds= [0]*100
    fifties= [0]*100
    out_at_0 = [0]*100
    for i in range(100):
        name[i]+=f.readline().strip()
        country[i] += f.readline().strip()
        startyear[i] = int(f.readline().strip())
        endyear[i] = int(f.readline().strip())
        no_match[i] = int(f.readline().strip())
        no_inning[i] = int(f.readline().strip())
        no_time_not_out[i] = int(f.readline().strip())
        totalruns[i] = int(f.readline().strip())
        highestruns[i] = int(f.readline().strip())
        avgruns[i] = float(f.readline().strip())
        hundreds[i] = int(f.readline().strip())
        fifties[i] = int(f.readline().strip())
        out_at_0[i] = int(f.readline().strip())

    for i in range(100):
        print(name[i],end='\t')
        print(country[i],end='\t')
        print(startyear[i],end='\t')
        print(endyear[i],end='\t')
        print(no_match[i],end='\t')
        print(no_inning[i],end='\t')
        print(no_time_not_out[i],end='\t')
        print(totalruns[i],end='\t')
        print(highestruns[i],end='\t')
        print(avgruns[i],end='\t')
        print(hundreds[i],end='\t')
        print(fifties[i],end='\t')
        print(out_at_0[i],end='\t')
        print()
main()