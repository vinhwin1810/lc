def solution(numbers):
    

    res = []
    window = []
    for num in numbers:
        window.append(num)
        
        if len(window) == 3:
            if (window[0] < window[1] and window[1] > window[2]) or (window[0] > window[1] and window[1] < window[2]):
                res.append(1)
            else:
                res.append(0)
            
            window = window[1:]
    
    return res