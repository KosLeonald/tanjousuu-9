import json 
import random
import time , datetime 


 
    today = datetime.datetime.fromtimestamp(time.time())
    time  = today.strftime('%H')  
 
        if int(time) > 20 :
            line_bot_api.push_message(USER_ID,messages=messages)
        else :
            line_bot_api.push_message(USER_ID,messages=messages2)  


    
if __name__ == "__main__" :
    main()
