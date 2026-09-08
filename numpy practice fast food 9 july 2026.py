#import numpy as np

#address, city, country, keys, latitude, longitude, name, postalCode, province, websites = np.genfromtxt('FastFoodRestaurants.csv', delimiter=",", usecols=(0,2,3,4,5,6), unpack=True, dtype=None, skip_header=1)

#print("addrees", address)
#print("city", city)
#print("country", country)
#print("krys", keys)
#print("latitude", latitude)
#print("longitude", longitude)
#print("name", name)
#print("postalCode", postalCode)
#print("province",province)
#print("websites", websites)



#print(np.min(name))









import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

address, latitude , longitude , name, = np.genfromtxt("FastFoodRestaurants.csv",
                                                                delimiter=',',
                                                                usecols=(0, 4, 5, 6),
                                                                unpack=True,
                                                                dtype=('U100', 'f8', 'f8', 'U100'),   # force correct types
                                                                encoding='utf-8',
                                                                skip_header=1,
                                                                invalid_raise=False)

print(address)
print(latitude)
print(longitude)
print(name)

cleaned_longitude = longitude[~np.isnan(longitude)]


# FastFood Restaurant addrees - statistics operations

print("FastFood Restaurant.com address mean: " , np.mean(address))
print("FastFood Restaurant.com address average: " , np.average(address))
print("FastFood Restaurant.com address std: " , np.std(address))
print("FastFood Restaurant.com address mod: " , np.median(address))
print("FastFood Restaurant.com address percentile - 25: " , np.percentile(address,25))
print("FastFood Restaurant.com address percentile  - 75: " , np.percentile(address,75))
print("FastFood Restaurant.com address percentile  - 3: " , np.percentile(address,3))
print("FastFood Restaurant.com address min : " , np.min(address))
print("FastFood Restaurant.com address max : " , np.max(address))





