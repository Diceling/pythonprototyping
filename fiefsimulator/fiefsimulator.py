import fiefsimulator_business as business


business.initialize()


updateString = "{ \"points\":35, \"id\":1,\"newValues\": {\"farming\": 4,\"livestock\":3,\"fishing\":3,\"hunting\":4},\"currentValues\": {\"farming\": 3,\"livestock\":4,\"fishing\":1,\"hunting\":2}}"
print updateString

business.updateIndustries(updateString)
