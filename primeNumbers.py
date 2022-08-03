import time

def Count():
    start = time.time() 
    n = 1
    i = 1
    
    while i < 100001:  
        test = 1
        num_factors = 0
        test_sq = test * test
        while  test_sq <= n:
            test += 1
            test_sq = test * test
            
            num = n / test
            def is_whole(num):
                return num % 1 == 0
            
            if is_whole(num) == 1:
            
                num_factors += 1
                  
        if num_factors == 0:
            print(n)
        i += 2
        n += 2

    end = time.time()
    timeElaps = end - start
    timeElaps = round(timeElaps, 3)
    
    print("Time Taken:", timeElaps, "Seconds")


Count()
