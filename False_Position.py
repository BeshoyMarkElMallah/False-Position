import math as m

error = 100
xr_old = 0

xl = float(input("Enter the lower limit: "))
xu = float(input("Enter the upper limit: "))



while error > 0.001:
    
    fxl = m.pow((m.pow(xl, 2)+1), 2)-25
    fxu = m.pow((m.pow(xu, 2)+1), 2)-25
    xr_new = ((xu*fxl)-(xl*fxu))/(fxl-fxu)

    
    fxr = m.pow((m.pow(xr_new, 2)+1), 2)-25


    mul_fxl_fxr = fxl*fxr
    
    if mul_fxl_fxr < 0:
        xu = xr_new
    elif mul_fxl_fxr > 0:
        xl = xr_new

    if xr_old != 0:
        error = ((xr_new - xr_old)/xr_new) * 100
        
        if(error < 0):
            error = error * -1
        else:
            error = error
        
    xr_old = xr_new


print("The root is: ", xr_new)
print("The error is: ", error)
