def whatAge():
    whatMonth = raw_input("Type M if you want to know your age in Months and W if you want it in weeks\n")
    if whatMonth == "M":
        userMonth = raw_input("How old are you? ")
        return ("!  Thou hath lived {} months on earth".format (int(userMonth) * 12 ))
    elif whatMonth == "W":
        userMonth = raw_input("How old are you? ")
        return ("!  Thou hath lived {} weeks on earth".format (int(userMonth) * 52 ))

        
