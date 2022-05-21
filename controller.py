import ui
import log

def run():
    temp = ui.initial()
    #result = log.log_to_file(temp[0], temp[1], temp[2], temp[3])
    # print(result)
    print(temp)
    #log.log_to_file(temp, result)
    #return(result)
    log.log_to_file(temp[0], temp[1], temp[2], temp[3], temp[4])
    #return result