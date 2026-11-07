#Slide 1.9
log   = 'OK FAILED OK OK FAILED FAILED OK FAILED'
alert = 'FAILED'
count = 0

for word in log.spli(" "):
    if word == alert:
        count += 1

# and some print thingies