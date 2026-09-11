# FD-049 — zeta zero frontier caps pointwise polynomial occupation and Schur saturation loss

**Status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + POINTWISE-OCCUPATION-DECAY + POINTWISE-SCHUR-SATURATION + ZERO-FRONTIER-BOUND + LINEAR-PRIME-BREADTH + RH-SUBPOWER-BARRIER`.

`FD-034` and `FD-047` give the same four-adic lower-scale injection in two different physical quantities: the normalized Schur projective defect and the actual nonsquarefree Jordan occupation. `FD-033` proves that the lower-scale physical energy is superlinear at **every** sufficiently large horizon, while `FD-046` calibrates the upper polynomial envelope of the same energy by the rightmost zeta-zero frontier. Combining those facts removes the sparse-chain qualifier from one important part of the picture.

Fix a Schur-head dimension `D>=1`. Write

\[
E_{H,D}
=\sum_{r>D}\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

\[
U_{H,D}
=\sum_{\substack{r>D\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\qquad
u_{H,D}:=\frac{U_{H,D}}{E_{H,D}},
\]

and let

\[
\varepsilon_{H,D}
:=\frac{\rho_{H,D}^2}{E_{H,D}}
\]

be the normalized Schur distance from the distinguished equality ray. Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Then for every `eta>0`,

\[
\boxed{
H^{\,2\Theta-1+\eta}\,\nu_{H,D}
\longrightarrow\infty,
\qquad
H^{\,2\Theta-1+\eta}\,\varepsilon_{H,D}
\longrightarrow\infty.
}
\tag{1}
\]

Equivalently, if

\[
\Gamma_D^{\rm ns}
:=
\limsup_{H\to\infty}
\frac{\log(E_{H,D}/U_{H,D})}{\log H},
\]

\[
\Gamma_D^{\rm proj}
:=
\limsup_{H\to\infty}
\frac{\log(1/\varepsilon_{H,D})}{\log H},
\]

then

\[
\boxed{
0\le \Gamma_D^{\rm ns}\le 2\Theta-1,
\qquad
0\le \Gamma_D^{\rm proj}\le 2\Theta-1.
}
\tag{2}
\]

`FD-036` independently gives `epsilon_(H,D) >>_D H^(-1/2)`, so for the projective defect the combined bound is

\[
\boxed{
\Gamma_D^{\rm proj}
\le
\min\!\left\{\frac12,\,2\Theta-1\right\}.
}
\tag{3}
\]

In particular, under RH (`Theta=1/2`), both the nonsquarefree occupation fraction and the Schur projective defect may still tend to zero, but **neither can do so at any positive polynomial rate**:

\[
\boxed{
\mathrm{RH}
\Longrightarrow
H^\eta\nu_{H,D}\to\infty,
\quad
H^\eta\varepsilon_{H,D}\to\infty
\quad\text{for every }\eta>0.
}
\tag{4}
\]

Conversely, a polynomial occupation or projective loss of exponent `gamma>0` along even one unbounded subsequence would force

\[
\boxed{
\Theta\ge\frac{1+\gamma}{2}.
}
\tag{5}
\]

Thus a sufficiently sharp physical geometric escape would itself certify a corresponding off-critical zero frontier. This does not prove a positive pointwise occupation constant: inverse logarithms, stretched exponentials in `log H`, and other subpower losses remain compatible with (4).

## 1. Nonsquarefree rows are an exact part of the Schur residual

The distinguished Schur equality direction has zero Jordan coordinate at every nonsquarefree row, as proved in `FD-032`--`FD-034`. Therefore the squared residual contains the entire nonsquarefree physical energy as a positive sub-sum:

\[
\boxed{
\rho_{H,D}^2\ge U_{H,D}.
}
\tag{6}
\]

After division by `E_(H,D)`,

\[
\boxed{
\varepsilon_{H,D}\ge\nu_{H,D}.
}
\tag{7}
\]

Now apply the exact four-adic row injection of `FD-047`. Multiplication of every lower-horizon row by `4` lands inside the nonsquarefree rows, the nested-floor identity preserves the sampled shell argument, and

\[
\frac{J_2(4r)}{(4r)^2}
\ge
\frac34\frac{J_2(r)}{r^2}.
\]

Hence, with

\[
X_H:=\left\lfloor\frac H4\right\rfloor,
\]

one has for all sufficiently large `H`

\[
\boxed{
\varepsilon_{H,D}
\ge
\nu_{H,D}
\ge
\frac34\,
\frac{E_{X_H,D}}{E_{H,D}}.
}
\tag{8}
\]

The first and last quantities in (8) had previously been used mainly to obtain, respectively, a projective chain obstruction and a nonsquarefree chain-average obstruction. The pointwise consequence below comes from calibrating **both numerator and denominator** of the same ratio.

## 2. Superlinear lower energy plus the zero-frontier upper envelope gives a pointwise power barrier

Define

\[
L_D(X):=\frac{E_{X,D}}{X}.
\tag{9}
\]

`FD-033` proves the unconditional all-horizon limit

\[
\boxed{L_D(X)\longrightarrow\infty.}
\tag{10}
\]

On the other hand, `FD-046` transfers the classical Mertens/zeta zero-frontier bound through the exact invertible floor transform and obtains, for every `sigma>Theta`,

\[
\boxed{
E_{H,D}\ll_{D,\sigma} H^{2\sigma}.
}
\tag{11}
\]

Insert (9)--(11) into (8). Since `X_H=(1/4+o(1))H`, for every fixed `sigma>Theta` there is `c_(D,sigma)>0` such that

\[
\boxed{
\nu_{H,D}
\ge
c_{D,\sigma}
L_D(X_H)H^{1-2\sigma},
}
\tag{12}
\]

and the same bound holds with `nu` replaced by `epsilon`.

Fix `eta>0` and choose

\[
\sigma=\Theta+\frac\eta4.
\]

Then (12) gives

\[
H^{2\Theta-1+\eta}\nu_{H,D}
\ge
c_{D,\eta}
L_D(X_H)H^{\eta/2},
\]

whose right side tends to infinity by (10). This proves the first limit in (1); (7) gives the second. Taking logarithms proves (2). No zero is assumed to occur on the line `Re(s)=Theta`; as in `FD-046`, an arbitrary exponent strictly to the right of the supremum is sufficient.

Equation (3) is obtained by intersecting this new zero-frontier barrier with the independent physical Lipschitz estimate of `FD-036`. The two mechanisms control different things. `FD-036` gives an unconditional half-power floor from a nearby squarefree/nonsquarefree row pair. The present argument can be much stronger when the zeta-zero frontier is close to the critical line; at RH it improves the allowed projective decay exponent from `1/2` all the way to `0`.

## 3. Polynomial geometric escape forces zeros to the right

Suppose there is an unbounded sequence `H_j` and some `gamma>0` such that

\[
\nu_{H_j,D}\le H_j^{-\gamma}.
\tag{13}
\]

Then by definition `Gamma_D^(ns)>=gamma`. Equation (2) therefore implies

\[
\gamma\le2\Theta-1,
\]

which is exactly (5). The same argument applies if

\[
\varepsilon_{H_j,D}\le H_j^{-\gamma}.
\tag{14}
\]

For the projective defect, (3) adds the unconditional restriction `gamma<=1/2`: a faster polynomial collapse is already excluded by `FD-036`, independently of zeta zeros.

This implication is one-way. Failure to observe polynomial occupation loss says nothing new about RH, and `Theta>1/2` does not imply that the maximal exponent `2Theta-1` is actually attained by either ratio. The theorem only caps the possible rate of physical concentration.

The statement is also genuinely pointwise. `FD-046` alone gives only equality of limsup power exponents for `E` and `U`, which still permits one energy to realize its peaks on scales disjoint from the other. `FD-047` alone gives a positive geometric mean on every fixed four-adic chain, which still permits sparse bad horizons across different chains. Equation (1) combines the four-adic injection with the **all-horizon** superlinear numerator (10), so the polynomial-rate exclusion holds eventually at every horizon.

## 4. The same exponent bounds linear-prime-prefix saturation of the GCD ceiling

For the linear-prime-prefix relaxation of `FD-031`,

\[
R_H(a)
\le
\widehat R_{H,D}
:=C_D+\frac{\beta_{H,D}^2}{E_{H,D}}
\le C_H,
\]

and `FD-032` gives

\[
\boxed{
C_H-\widehat R_{H,D}
=\mathfrak D_{H,D}
=\Delta_{H,D}\varepsilon_{H,D},
\qquad
\Delta_{H,D}=C_H-C_D.
}
\tag{15}
\]

For fixed `D`,

\[
C_H\longrightarrow\zeta(2),
\qquad
\Delta_{H,D}\longrightarrow\zeta(2)-C_D>0.
\tag{16}
\]

Thus multiplication by `Delta_(H,D)` does not change the polynomial decay exponent. Equations (1)--(3) therefore imply

\[
\boxed{
\limsup_{H\to\infty}
\frac{
\log\!\bigl(1/(C_H-\widehat R_{H,D})\bigr)
}{\log H}
\le
\min\!\left\{\frac12,2\Theta-1\right\}.
}
\tag{17}
\]

Since every admissible source satisfies `R_H(a)<=hat R_(H,D)`, the same lower barrier applies to its gap from `C_H`.

The conclusion is uniform over every fixed positive linear ancestry breadth. Fix `0<lambda<1` and allow

\[
\lambda H\le Y<H,
\qquad
D(H,Y)=\left\lfloor\frac{H}{Y+1}\right\rfloor.
\]

Then `D(H,Y)` ranges over a finite set depending only on `lambda`. The superlinear limit (10) is uniform on bounded `D`, the upper envelope (11) can be bounded uniformly over that finite set, and the limits in (16) have a positive finite-set minimum. Consequently, for every `eta>0`,

\[
\boxed{
\inf_{\lambda H\le Y<H}
\inf_{a\ \mathrm{admissible}}
H^{2\Theta-1+\eta}
\bigl(C_H-R_H(a)\bigr)
\longrightarrow\infty.
}
\tag{18}
\]

Here a zero endpoint is harmless because then `R_H(a)=0`. Under RH, (18) says that no admissible linear-prime-prefix source can approach the finite-horizon GCD ceiling at any positive polynomial rate. If a family were observed or proved to satisfy

\[
C_H-R_H(a_H)\le H^{-\gamma}
\]

on an unbounded sequence, then necessarily `Theta>=(1+gamma)/2`; if `gamma>1/2`, `FD-036` already rules the family out entirely.

## 5. Relation to the occupation frontier and matched controls

This result narrows, but does not settle, `CLUE-joint-nonsquarefree-jordan-energy-occupation`. Under RH a physical escape `U/E->0` is forced into the **subpower** regime. That is much stronger than merely saying that `U` and `E` have the same limsup polynomial exponent: it forbids polynomial separation at every sufficiently large horizon.

The remaining gap is real. A ratio such as

\[
\exp(-\sqrt{\log H})
\]

is smaller than every fixed inverse logarithm but still satisfies (4), because it is larger than `H^(-eta)` for every fixed `eta>0` once `H` is large enough. This is exactly the qualitative scale of escape exhibited by the near-half-power-smooth synthetic construction in `FD-048`. Thus the new theorem does **not** invalidate that matched control and does not smuggle in the missing multiplicative placement of the physical increments.

That consistency check is important. The argument here uses only three durable physical facts already proved independently: the four-adic nonsquarefree injection, all-horizon superlinear Schur energy, and the zero-frontier polynomial upper envelope. It does not use short-interval cancellation, spectral finiteness, or any unproved regular variation. Therefore the surviving pointwise occupation problem is now confined to a slowly varying/subpower factor. A future positive theorem must control that factor using the exact arithmetic placement

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\]

or an equivalent divisibility coupling; another comparison of polynomial exponents cannot close the clue.

## 6. Prior art, proof boundary, and falsification checks

The external analytic ingredient is the classical Mertens/zeta zero-frontier growth theorem already anchored through Titchmarsh in `SOURCES.md` and transferred to the quotient-shell source by `FD-046`. The GCD/Schur/Jordan identities and the four-adic row injection are internal exact results from `FD-031`--`FD-047`. A targeted literature search around Farey discrepancy, Mertens growth, GCD/Jordan matrices, and squarefree/nonsquarefree energy located the expected classical GCD-matrix literature and recent Farey--Mertens discrepancy formulas, but no external theorem matching the pointwise occupation/saturation exponent bridge (1)--(5). No new source is load-bearing, so `SOURCES.md` requires no addition.

The main falsification checks are elementary but strict. The numerator input must be the **all-horizon** limit `E_(X,D)/X->infinity`; a mere limsup would not prove (1). The denominator input must be a uniform upper power envelope for every exponent to the right of `Theta`; equality of limsup exponents alone would again be insufficient. The head dimension must remain fixed or range over a bounded set; allowing `D->infinity` is outside the uniformity used in (10) and (18). Finally, (1) is a lower-rate statement only: it does not imply that `nu` or `epsilon` has a limit, stays bounded away from zero, or has decay exponent exactly `2Theta-1`.
