price_list = [100, 90, 70, 110, 120, 60, 200, 95, 135]
gst = 0.17
newPriceList = []

for price in price_list:
    newPriceList.append(price + price * gst)
    
else:
    newPriceList.append(price)
print(newPriceList)        