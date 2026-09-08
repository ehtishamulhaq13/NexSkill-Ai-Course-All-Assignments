import numpy as np
StartupName,Industry,FundingRounds,InvestmentAmount=np.genfromtxt('startup_growth_investment_data.csv', delimiter=',', usecols=(0,1,2,3), unpack=True)
print('startup name:',StartupName)
print('StartupName:',Industry)
print('Year_Founded:', FundingRounds)
print('Industry:', InvestmentAmount)

print()
print(np.min(InvestmentAmount))

print('Startup growth rate Year_Founded.mean:', np.mean(InvestmentAmount))
print('startup growth rate Year_founded.average:',np.average(InvestmentAmount))
print('startup growth rate Year_Founded.std:', np.std(InvestmentAmount))
print('startup growth rate Year_Foinded.mod:', np.median(InvestmentAmount))
print('startup growth rate year_Founded.percentile-25:', np.percentile(InvestmentAmount,25))
print('startup growth rate Year_Founded-percentile-75:', np.percentile(InvestmentAmount,75))
print('srartup growth rate Year_Founded-percentile-3:', np.percentile(InvestmentAmount,3))
print('startup growth rate Year_Founded.min:', np.min(InvestmentAmount))
print('startup growth rate Year_Founded.max:', np.max(InvestmentAmount))
print('startup growth rate Year_Founded.square:', np.square(InvestmentAmount))
print('starup growth rate Year_Founded.abs:', np.abs(InvestmentAmount))
print('startup growth rate Year_Founded.pow:', np.power(InvestmentAmount,InvestmentAmount))
print('startup growth rate Year_Founded.sqrt:', np.sqrt(InvestmentAmount))

addition=FundingRounds+InvestmentAmount
mutiplication=FundingRounds*InvestmentAmount
dividion=FundingRounds/InvestmentAmount
subtraction=FundingRounds-InvestmentAmount

print('start up growth addition:', addition)
print('start up growth multiplication:', mutiplication)
print('start up growth division:', dividion)
print('start up growth subtraction:', subtraction)

FundingRoundspie=(FundingRounds/np.pi)+1

sin_value=np.sin(FundingRoundspie)
cosine_value=np.cos(FundingRoundspie)
tangent_value=np.tan(FundingRoundspie)

print('startup growth sin_value:', sin_value)
print("startup growth cosine_value:", cosine_value)
print('startup growth tangent_value:', tangent_value)

logarray=np.log(FundingRoundspie)
log10array=np.log10(FundingRoundspie)

print('startup growth logarray:', logarray)
print('startup growth log10array:', log10array)

sinh_value=np.sinh(FundingRoundspie)
print('startup growth sinh value:', sinh_value)

cosh_value=np.cosh(FundingRoundspie)
print('startup growth cosh value:', cosh_value)

tanh_value=np.tanh(FundingRoundspie)
print('startup growth tan value:',tanh_value)

asin=np.asin(FundingRoundspie)
print('startup growth:', asin)

acos=np.acos(FundingRoundspie)
print('startup growth inverse:', acos)

D2FoundingRoundspie=np.array([FundingRounds,InvestmentAmount])
print('startup growth d2:', D2FoundingRoundspie.ndim)
print('startup growth d2:', D2FoundingRoundspie.shape)
print('startup growth d2:', D2FoundingRoundspie.size)
print('starup growth d2:', D2FoundingRoundspie.dtype)

D2FoundingRoundspieslice=D2FoundingRoundspie[:1:4, ::3]
print('slice the startup growth:', D2FoundingRoundspieslice)

for elem in np.nditer(D2FoundingRoundspie):
    print(elem)
for index,elem in np.ndenumerate(D2FoundingRoundspie):
    print(index,elem)

rows=np.shape(D2FoundingRoundspie)[0]
cols=np.shape(D2FoundingRoundspie)[1]
for i in range(0,rows):
    for j in range(0,cols):
        print(D2FoundingRoundspie[i,j])

print(D2FoundingRoundspie.shape)    

D2PriceidT00298=np.reshape(D2FoundingRoundspie, (2,5001))
print("RealEstate.com price plus id-2-dimentional-array-(D2Priceid, (0,298)):", D2PriceidT00298)
print("RealEstate.com price plus id-2-dimentional-array-(D2priceid,(1,400)):", D2PriceidT00298.shape)
print("RealEstate.com price plus id-2-dimentional-array-(D2priceid,(1,400)):", D2PriceidT00298.size)
print("RealEstate.com price plus id-2-dementional-array-(D2priceid, (1,300)):", D2PriceidT00298.ndim)