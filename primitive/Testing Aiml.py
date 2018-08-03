import aiml

k = aiml.Kernel()

k.learn("std-startup.xml")

#k.respond("load aiml b")

mess = "hello"
print(k.respond(mess))