## Gaussian Blur / noise reduction
___
formula for gaussian distribution over 2 dimensional space
 - waited average of the pixels 
<!-- $$
G(x,y) = {1 \over 2\pi \sigma^2} e ^{ -(x^2+y^2) \over 2 \sigma^2}
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=G(x%2Cy)%20%3D%20%7B1%20%5Cover%202%5Cpi%20%5Csigma%5E2%7D%20e%20%5E%7B%20-(x%5E2%2By%5E2)%20%5Cover%202%20%5Csigma%5E2%7D%0D"></div>

## Bilateral Blur 
___
formula 
 - waited avaerage of neighboring pixels of similar intensity 
 - preserves edges 

<!-- $$ 
 BF[I_p] = { 1 \over W_p} \sum_ { q \in S } G_\sigma{_s} (||p-q||)G_\sigma{  _r (I_p - I_q)}I_q
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%20BF%5BI_p%5D%20%3D%20%7B%201%20%5Cover%20W_p%7D%20%5Csum_%20%7B%20q%20%5Cin%20S%20%7D%20G_%5Csigma%7B_s%7D%20(%7C%7Cp-q%7C%7C)G_%5Csigma%7B%20%20_r%20(I_p%20-%20I_q)%7DI_q%0D"></div>

 <!-- $$ W_p = \sum_{ q \in S } G_\sigma{_s} (||p-q||)G_\sigma{  _r (I_p - I_q)} $$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>