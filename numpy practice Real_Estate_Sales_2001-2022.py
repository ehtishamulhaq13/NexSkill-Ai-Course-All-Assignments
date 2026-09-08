import numpy as np
SerialNumber,ListYear,DateRecorded,Town=np.genfromtxt('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', usecols=(0,1,2,3), unpack=True, dtype=None, skip_header=1 ) 
print('SerialNumber:', SerialNumber)
print('List Year:', ListYear)
print('datarecorded:', DateRecorded)
print('Town:', Town)
print()

print(np.min(ListYear))
print('reat estate by 2001:', np.mean(ListYear))
print('real estate by 2001:', np.average(ListYear))
print('real estate by 2001:', np.median(ListYear))
print('real to real estate by 2001:', np.max(ListYear))
print('real estate by 2001:', np.percentile(ListYear,75))
print('real estate by 2001:', np.std(ListYear))
print('real estate by 2001:', np.abs(ListYear))
print('real estate by 2001:', np.power(ListYear,ListYear))

addition=ListYear+SerialNumber
subtraction=ListYear-SerialNumber
multiplication=ListYear*SerialNumber
division=ListYear/SerialNumber

print('real estate by 2001:',addition)
print('real estate by 2001:', subtraction)
print('real estate by 2001:', multiplication)
print('real estate by 2001:', addition)

ListYearpie=(ListYear/np.pi)+1

sin_value=np.sin(ListYearpie)
cos_value=np.cos(ListYearpie)
tan_value=np.tan(ListYearpie)
print('rean estate 2001 sin value:', sin_value)
print('real estate by cos value:', cos_value)
print('real estate by 2001 tan value:', tan_value)

cosh_value=np.cosh(ListYearpie)
print("real estate by 2001:", cosh_value)

sinh_value=np.sinh(ListYearpie)
print("real estate by 2001:", sinh_value)

asin_value=np.asin(ListYearpie)
print('realestate by 2001:', asin_value)

acos_value=np.acos(ListYearpie)
print('realestae by 2001:', acos_value)

asinh_value=np.asinh(ListYearpie)
print('real estate by 2001:', asinh_value)

acosh_value=np.acosh(ListYearpie)
print('real estate by 2001:', acosh_value)

logarray=np.log(ListYearpie)
print('real estate by 2001:', logarray)

logarray10=np.log10(ListYearpie)
print('real estate by 2001:', logarray10)
D2ListYear=np.array([ListYear,SerialNumber])

print("RealEstate.com price plus id-2Dimention-array-Dimention:", D2ListYear.ndim)
print("RealEstate.com price plus id-2Dimention-array-toyal number of element:", D2ListYear.size)
print("RealEstate.com price plus id-2Dimention-give size of array in each dimention:", D2ListYear.shape)
print("RealEstate.com price plus id-2Dimention-data type:", D2ListYear.dtype)

for elem in np.nditer(D2ListYear):
    print(elem)
for index,elem in np.ndenumerate(D2ListYear):
    print(index,elem)

rows=np.shape(D2ListYear)[0]
cols=np.shape(D2ListYear)[1]
for i in range(0,rows):
    for j in range(0,cols):
        print(D2ListYear[i,j])