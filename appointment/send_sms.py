# from twilio.rest import Client


# def sendsms():
#     account_sid = "ACe96aec894ba7878875d0e65af391dff1"
#     auth_tocken = "fc0a86e4f4ae6878dd59767e6eb635d2"
#     client = Client(account_sid,auth_tocken)
#     message = client.messages  \
#                 .create(
#                     body = "Congratulations Mr/Mrs." + appointment[patient_name] +", You have taken a serial on" 
#                     +str(appointment[appointment_date])+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  "+str(appointment),
                
#                     from = '+12186703680'
#                     to = ''
#                 )