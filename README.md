# Global_model_Te

a zero-dimensional (global) model based on the particle balance equation of charged species. In this model, charged species are produced by electron-impact ionization on ground state Ar atoms and lost by diffusion towards the reactor walls. This model yield the electron temperature as a function of the pressure for low pressure Ar plasma of known size. It can be change for any other plasma by changing the mass of the ion and the electron impact cross section for direct ionization.

This model come from M. A. Lieberman and A. J. Lichtenberg, Principles of Plasma Discharges and Materials Processing: Second Edition. 2005. (P.131) and it solve the following equation:

<img width="207" alt="screen shot 2018-08-12 at 12 54 58 pm" src="https://user-images.githubusercontent.com/33142211/44004360-89f5a032-9e2f-11e8-80f3-75971cd08663.png">


 It is worth highlighting that this model takes into account the collisionless, the variable mobility, and diffusion regimes in the calculations of the effective plasma size d_eff which is defined as :

<img width="197" alt="screen shot 2018-08-12 at 1 01 51 pm" src="https://user-images.githubusercontent.com/33142211/44004385-fb3f50a8-9e2f-11e8-952e-09bfa5ef220b.png">
<img width="251" alt="screen shot 2018-08-12 at 1 01 54 pm" src="https://user-images.githubusercontent.com/33142211/44004386-fcde5d00-9e2f-11e8-8356-ea43b7d99464.png">

# Result exemple
For an argon plasma of radius R = 8 cm and a length L = 20 cm (reactor dimensions)
<img width="608" alt="screen shot 2018-08-12 at 1 07 13 pm" src="https://user-images.githubusercontent.com/33142211/44004438-bf594444-9e30-11e8-8115-92c5c484cd99.png">
