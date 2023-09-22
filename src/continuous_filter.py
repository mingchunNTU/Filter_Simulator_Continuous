from data import *

# the code is based on the continuous filter model from "Unit Operations of Chemical Engineering, McCabe"

# ===========================================

setting_dir="../examples/KNO3/"

# ===========================================

file=setting_dir+"operating_condition.csv"
tmp1=parameter_read(file)

c=get_variable(tmp1,"slurry concentration").value[0]
V=get_variable(tmp1,"slurry flowrate").value[0]/3600
mu=get_variable(tmp1,"slurry viscosity").value[0]
alpha=get_variable(tmp1,"cake resistance").value[0]
epsilon=get_variable(tmp1,"cake porosity").value[0]
rho=get_variable(tmp1,"crystal density").value[0]
p=get_variable(tmp1,"pressure drop").value[0]*133.3
f=get_variable(tmp1,"filter area ratio").value[0]
n=1/(get_variable(tmp1,"rotation period").value[0]*60)
Rm=get_variable(tmp1,"filter medium resistance").value[0]

# calculate the required area 
mc=c*V

denominator=(2*c*alpha*p*f*n/mu+(n*Rm)**2)**0.5-n*Rm
A=alpha*mc/denominator

print("Required Filter Area = "+str(A)+" m^2")

# calculate the cake thickness
L=V*(f/n)*c/((A*f)*rho*(1-epsilon))*1000

print("Cake Thickness= "+str(L)+" mm")
