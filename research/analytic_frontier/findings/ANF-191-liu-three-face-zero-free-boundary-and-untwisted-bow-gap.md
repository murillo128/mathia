# ANF-191 — Liu's three-face zero-free boundary and the untwisted bow-scale gap

**Status:** LITERATURE-CLAIM + EXACT-ALGEBRA-CHECK + CONDITIONAL-CLASSICAL-COROLLARY + QUANTIFIED-SOURCE-GAP + NEEDS-INDEPENDENT-ANALYTIC-AUDIT.

## 1. Source statement and the kind of zero information it supplies

Baiying Liu, *Slightly improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234v1 (8 October 2026), Theorem 21.1, **claims** that every finite-order Hecke `L`-function over `Q(sqrt(-3))`, every Dirichlet `L`-function and `zeta` has no zeros in the open half-plane

[
Re(s)>B_*:=rac{1507-2sqrt{921}}{1653}
=0.874957069799ldots .
	ag{1}
]

Poles of principal functions are excluded from the zero claim. Relative to the earlier claimed `7/8` half-plane, the improvement is

[
Delta_*:=rac78-B_*=0.000042930200831ldots>0.
	ag{2}
]

If Theorem 21.1 is valid, for `N(sigma,T)` counting zeta zeros with `Re(rho)>=sigma` and `0<Im(rho)<=T`, it yields `N(sigma,T)=0` for **every** `sigma>B_*` and every `T`. It does not address zeros exactly on `sigma=B_*`, nor the entire range `1/2<sigma<=B_*`; thus it is not RH. This is an *all-heights exclusion* claim, unlike a density/proportion bound. The analytic theorem and the claimed Lean formalization have not been independently compiled or audited here.

## 2. Independent exact check of the three affine exponent constraints

The algebraic certificate is **already Proposition 25.1 of Liu**, not a new theorem of Mathia. Set

[
d=rac{49-sqrt{921}}{48},quad
L_0=rac56+rac M{12}-rac{ell}{6},quad
L_K=rac13+rac{7M}{12}+rac{ell}{3},quad
H_c=1+d-rac{1+d}{2}M+dell.
	ag{3}
]

For arbitrary real `M,ell,B`, *under the explicit assumptions* `B>=L_0`, `B>=L_K`, `B>=H_c`, choose

[
w_0=rac{4+18d}{9+18d},qquad
w_K=rac{2}{9+18d},qquad
w_H=rac{3}{9+18d}.
	ag{4}
]

All three weights are positive, sum to one, and exactly cancel both parameter coefficients:

[
rac{w_0}{12}+rac{7w_K}{12}-rac{1+d}{2}w_H=0,qquad
-rac{w_0}{6}+rac{w_K}{3}+d w_H=0.
	ag{5}
]

Therefore

[
Bgeqmax(L_0,L_K,H_c)
geq w_0L_0+w_KL_K+w_HH_c
=rac{7+18d}{9+18d}=B_*.
	ag{6}
]

The bound is attained simultaneously at

[
ell_*=rac{33+8sqrt{921}}{1653},qquad M_*=1-ell_*,
qquad L_0(M_*,ell_*)=L_K(M_*,ell_*)=H_c(M_*,ell_*)=B_*.
	ag{7}
]

I separately checked (4)–(7) by exact symbolic reduction in `Q(sqrt(921))`: weight sum one, both coefficient cancellations, weighted constant and all three equality substitutions simplify identically, not approximately. This proves the **conditional lower floor for these three stated constraints only**; neither their necessity throughout the full analytic method nor the analytic zero-free theorem follows from this finite algebra. The manuscript explicitly labels wider optimality an expectation.

## 3. A conditional classical prime-counting implication and its absolute scale

Assuming the analytic zeta zero-free theorem (1), the classical explicit formula and `N(T)=O(T log T)` give, for every fixed `eta>0`,

[
psi(x):=sum_{nle x}Lambda(n)=x+O_eta(x^{B_*+eta}).
	ag{8}
]

Indeed, a standard truncated explicit formula bounds the zero contribution by `x^{B_*} sum_{|gamma|<=T} 1/|rho|=O(x^{B_*} log^2 T)`; choose polynomially large `T` and absorb the standard truncation/local endpoint errors into `x^{B_*+eta}`. For `0< H<=x`, the bound is uniform for the difference:

[
psi(x+H)-psi(x)=H+O_eta(x^{B_*+eta}).
	ag{9}
]

Removing prime powers introduces at most `O(sqrt(x) log^2 x)` on a dyadic `[x,2x]` range, hence for each fixed `theta>B_*` and `H=x^{theta}`,

[
sum_{x<ple x+H}log p
=H+O_eta(x^{B_*+eta}+sqrt{x}log^2x)
=(1+o(1))Hquad(0<eta<theta-B_*).
	ag{10}
]

In particular `theta=7/8` has the strict margin `theta-B_*=Delta_*`. The short-interval asymptotic (10) is **not new** relative to existing prime-in-short-interval methods; it merely calibrates the immediate consequence of the claimed fixed half-plane by the elementary explicit-formula route. No effective moderate-`x` bound is asserted from so small an exponent gap.

More decisively for the local Mathia source, the required absolute bow endpoint scale is `a_X=sqrt(delta X log X)` with fixed `delta>0`. The best error delivered by **this direct passage** to (8) is of size `O(X^{B_*+eta})`, whereas

[
rac{X^{B_*+eta}}{a_X}
asymp_{delta}rac{X^{B_*-1/2+eta}}{sqrt{log X}}
longrightarrowinfty .
	ag{11}
]

This comparison is a *limitation of the derived upper bound*, not a lower bound on the actual prime error. It shows that no `o(a_X)` absolute estimate can be claimed merely by inserting (1) into the global explicit formula.

## 4. Distinguished-carrier limitation and prior-art boundary

The actual bow coefficient is `r_X(n)=vartheta(n)-Q_R(n)` (ANF-149/162). Its decisive quantities concern carrier-aware sums

[
sum_{jle M}r_X(X+j)
exp(-iUlog(1+j/X)),qquad Uasymp X^2,
	ag{12}
]

and weighted high-passes with `W(T log(1+j/X))` (ANF-185), on `K=X^{1-2epsilon+o(1)}`. The nonoscillatory conclusion (9) says nothing directly about the prime-minus-rough *joint placement* against that exact phase. Partial summation at `Uasymp X^2` differentiates the phase at size `U/Xasymp X`; it does not magically turn the error in (9) into an `o(a_X)` twisted error. Nor does (8) control the `Q_R` component's relative phase.

ANF-189 shows by exact-carrier source-alphabet matched controls that even uniformly tiny saturated high-pass transforms need not control endpoint energy without additional prefix-localization structure. ANF-190 proves height-mean bounds for the **actual** source but explicitly leaves its prescribed `U` exceptional-set membership unresolved. Neither issue is settled by a half-plane theorem for zeta.

**Prior art / novelty:** Liu's Theorem 21.1 is the external source of the zero-free statement, and his Proposition 25.1 already contains the dual certificate; the proof above is an independent algebraic *recheck*, not a Mathia discovery. Equations (8)–(10) are classical explicit-formula consequences. The line-specific contribution is to pin down the exact improvement/margin and expose, quantitatively, the mismatch between its untwisted `X^{B_*+eta}` error and the distinguished source's `a_X` absolute scale. No improved signed phase estimate, independent analytical validation of Liu's proof, or exclusion of every off-critical zero is obtained. The live RH-facing gate remains a source-specific distinguished-height correlation or Fejer-slope estimate that survives the existing matched controls.
