def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book) - 1): #0 ~ 1
        #for j in range(i+1, len(phone_book)): #i ~ 2
        if phone_book[i] in phone_book[i+1][:len(phone_book)]:
            return False
            
    
    return answer