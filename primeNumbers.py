def Count():
    n = 1
    i = 1
    
    while i < 1001:  
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
        i += 1
        n += 1


Count()