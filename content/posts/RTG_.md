---
Title: RTG
---  
  
  
  
  
Estimate the **heat and electrical energy output** of a radioisotope thermoelectric generator (RTG) using 5 kg of Pu-238 over 50 years at 5% efficiency:
  
---
  
### 🔬 Step 1: Key Properties of Pu-238
  
- **Half-life**: 87.7 years
- **Specific power**: ~0.57 watts/gram (thermal)
- **Decay mode**: Alpha decay (no significant gamma or neutron radiation)
- **Energy per decay**: ~5.593 MeV
  
---
  
### ⚙️ Step 2: Initial Thermal Power
  
Pu-238 has a specific thermal power of:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?0.57%20\,%20\text{W/g}%20\times%205000%20\,%20\text{g}%20=%202850%20\,%20\text{W}"/></p>  
  
  
This is the **initial thermal power** at time <img src="https://latex.codecogs.com/gif.latex?t%20=%200"/>.
  
---
  
### 📉 Step 3: Decay Over Time
  
The power decreases exponentially due to radioactive decay:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?P(t)%20=%20P_0%20\cdot%20e^{-\lambda%20t}"/></p>  
  
Where:
- <img src="https://latex.codecogs.com/gif.latex?\lambda%20=%20\frac{\ln(2)}{T_{1/2}}%20=%20\frac{\ln(2)}{87.7}%20\approx%200.0079%20\,%20\text{yr}^{-1}"/>
- <img src="https://latex.codecogs.com/gif.latex?t%20=%2050"/> years
  
So:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?P(50)%20=%202850%20\cdot%20e^{-0.0079%20\cdot%2050}%20\approx%202850%20\cdot%200.673%20\approx%201917%20\,%20\text{W}"/></p>  
  
  
---
  
### 🔥 Step 4: Total Thermal Energy Over 50 Years
  
Integrate the power over time:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?E_{\text{thermal}}%20=%20\int_0^{50}%20P_0%20\cdot%20e^{-\lambda%20t}%20\,%20dt%20=%20\frac{P_0}{\lambda}%20\left(1%20-%20e^{-\lambda%20\cdot%2050}%20\right)"/></p>  
  
  
Plug in values:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?E_{\text{thermal}}%20=%20\frac{2850}{0.0079}%20\cdot%20(1%20-%200.673)%20\approx%20360,759%20\cdot%200.327%20\approx%20118,000%20\,%20\text{kWh}"/></p>  
  
  
---
  
### ⚡ Step 5: Electrical Energy at 5% Efficiency
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?E_{\text{electric}}%20=%200.05%20\cdot%20E_{\text{thermal}}%20\approx%200.05%20\cdot%20118,000%20\approx%205900%20\,%20\text{kWh}"/></p>  
  
  
---
  
### ✅ Summary
  
| Quantity                  | Value                  |
|--------------------------|------------------------|
| Initial thermal power     | 2850 W                 |
| Thermal power after 50 yrs| ~1917 W                |
| Total thermal energy      | ~118,000 kWh           |
| Total electrical energy   | ~5900 kWh              |
  
---
  