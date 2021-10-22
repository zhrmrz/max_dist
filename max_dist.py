class Sol:
    def max_dist(self,seats):
        l = [i for i, x in enumerate(seats) if x == 1]
        maxi,idx=0,0
        for i in range(1,len(l)):
            if maxi<l[i]-l[i-1]:
                maxi=l[i]-l[i-1]
                idx=l[i-1]
        mid=(maxi//2)+idx
        dist_to_first_one=l[0]
        dist_to_last_one=len(seats)-1-l[-1]
        if maxi>dist_to_first_one and maxi>dist_to_last_one:
            return mid
        elif dist_to_first_one>maxi and dist_to_first_one>dist_to_last_one:
            return 0
        else:
            return len(seats)-1

if __name__ == '__main__':
    p = Sol()
    print(p.max_dist(seats=[1,0]))
