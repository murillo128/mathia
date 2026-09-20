# MI-059 — Local and Markov-jump boundary nullity collapse to the Mangoldt ray

**Evidence level:** supported RH-independent synthesis from [WP-386](../../findings/WP-386-pointwise-local-positive-boundary-selectors-collapse-to-the-mangoldt-ray.md) and [WP-387](../../findings/WP-387-beurling-deny-jump-selectors-collapse-to-unit-cell-invisibility.md), extending the boundary classifications of WP-384--WP-385. Arbitrary non-Markov off-diagonal forms and strongly local/interface terms remain outside the classification.

WP-386 classifies arbitrary positive pointwise reweighting in the native boundary coordinate. Exact nullity of every mixed-prime shell forces the measure into `(0,1)`, where every profile is the constant `Lambda(m)/sqrt(m)`. The complete shell Gram and every local-anchor incidence therefore collapse to one Mangoldt ray.

WP-387 tests the first canonical genuinely nonlocal positive continuation: the pure-jump sector of a Beurling--Deny Dirichlet form. The arithmetic boundary profiles satisfy an exact discretization: every `h_m` is constant on each unit cell `I_n=[n,n+1)` (with `I_0=(0,1)`), while fresh mixed-prime shells separate any two distinct cells.

For a positive symmetric jump measure `J`, exact mixed-shell nullity is therefore equivalent to `J` being supported only on same-cell pairs. But on that support every arithmetic difference `h_m(x)-h_m(y)` is zero, so the jump form annihilates **all** shell pairs, not only the mixed ones. Adding a positive killing measure recovers exactly the WP-386 contribution on `(0,1)`, hence

`E_(J,nu)(h_m,h_n)=nu((0,1)) Lambda(m)Lambda(n)/sqrt(mn)`.

Thus replacing pointwise locality by a positive Markov jump conductance does not create a second arithmetic channel. Mixed-shell nullity forces the jump geometry into directions that the entire boundary family cannot see, and the jump-plus-killing sector has the same rank-one arithmetic response as the pointwise-local class.

The surviving routes must therefore change operator category or stage. A strongly local/interface component whose domain genuinely contains the shell steps, a non-Markov positive off-diagonal form with an independent source reason for its kernel, a finite-`q` prelimit term lost in the continuum boundary, or a finite--archimedean coupling whose final positivity appears only after assembly are not classified by WP-386--WP-387.

**Boundary.** WP-387 does not say that every nonlocal positive kernel is arithmetic-blind. Its exact classification uses the difference structure and independent nonnegativity of the Beurling--Deny jump/killing sectors on the WP-384 profiles. Strongly local diffusion/interface energy, arbitrary positive-definite kernels and delayed indefinite couplings require separate audits.