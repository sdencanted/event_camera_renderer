import numpy as np
fx=635.0
fy=630.0
cx=600.0
cy=350.0
k=np.array([[fx,0,cx],[0,fy,cy],[0,0,1]])
k_inv=np.linalg.inv(k)
theta=0.14
r=np.array([[1,0,theta],[0,1,0],[-theta,0,1]])

u=np.random.randint(0,1000)
v=np.random.randint(0,700)

pixel_coords=np.array([[u],[v],[1]])

world_coords=np.matmul(k_inv,pixel_coords)
rotated_world_coords=np.matmul(r,world_coords)
rotated_pixel_coords=np.matmul(k,rotated_world_coords)

s=rotated_pixel_coords[2][0]
new_u=rotated_pixel_coords[0][0]/s
new_v=rotated_pixel_coords[1][0]/s

math_s=-theta*((u-cx-(fx/theta))/fx)
math_u=(u+(cx*theta/fx)*((fx*fx/cx) +cx-u))/math_s
math_v=(v-cy*theta*(u-cx)/fx)/math_s

math_s=fx-theta*(u-cx)
math_u=(u*(fx-cx*theta)+theta*(fx*fx+cx*cx))/math_s
math_v=(v*fx-cy*theta*u+cx*cy*theta)/math_s

print(s,math_s,new_u,math_u,new_v,math_v)