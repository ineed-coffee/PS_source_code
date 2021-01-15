def solution(phone_book):

    prefix_set=set()
    phone_book.sort(key=lambda x:len(x))
    
    for number in phone_book:
        for element in prefix_set:
            if number[:len(element)]==element:
                return False
        prefix_set.add(number)
    
    return True
