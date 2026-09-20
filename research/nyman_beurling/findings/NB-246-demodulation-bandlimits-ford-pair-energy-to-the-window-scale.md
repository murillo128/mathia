# NB-246 — Demodulation bandlimits Ford pair energy to the window scale

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + HARMONIC-ANALYSIS + LOCAL-L2-SUFFICIENT-CONDITION + NB-243/NB-245-REFINEMENT + SOURCE-ONLY`.

`NB-243` reduced the live source problem to decay of a depth-marked carrier pair energy. `NB-245` then showed that random-height Cauchy/Stieltjes laws do not control the exceptional deterministic Ford block selected by the source argument. There is, however, an intermediate quantifier between a pointwise selected-height theorem and a macroscopic/random-height average that had not yet been isolated.

For the **full smooth shell current**, freeze the Ford parameters at a target height `t_0` and view the same current as a function of a nearby center `t`. The raw current contains the fast carrier `e^{-iXt}`. After demodulating that carrier, its remaining `t`-Fourier support is only the shell bandwidth `H supp(phi)`. Consequently its energy `|R(t)|^2` is band-limited at width `O(H)`, not `O(X)`.

This gives an exact reproducing-kernel implication: a **uniform weighted local second moment on center-height scale `1/H`** forces the pointwise Ford energy to be small. Thus a future source theorem need not estimate the selected current at one exact height. It is enough to control a Ford-scale local `L^2` mean uniformly around every possible selected height, with the Ford depth marks retained.

This does not revive the random-height route rejected in `NB-245`. A long-interval or convergence-in-distribution statement can still miss sparse bad blocks entirely. The new sufficient condition is local on the shrinking scale `1/H`, uniform in the center, and attached to the same frozen source parameters. It also does not remove the carrier resolution `1/X` from the zero geometry: that scale remains inside the pair phase `e^{iX(gamma_j-gamma_k)}`. What becomes `O(H)`-band-limited is only the **energy as the observation center moves**.

## 1. Freeze the source scales at one selected height

Fix a target height `t_0` and freeze the parameters already used in `NB-230`--`NB-245`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
X:=YR,
\qquad
J:=\frac RH,
\tag{1}
\]

with `Y asymp 1` and, in the conservative regime,

\[
1\ll J\le \log Q.
\tag{2}
\]

Let the smooth shell profile be

\[
\phi\in C_c^\infty((0,1)),
\qquad
\operatorname{supp}\phi\subset[a,b]\Subset(0,1),
\tag{3}
\]

and use the Fourier convention already implicit in the shell transform,

\[
F(z)
:=
\int_a^b \phi(u)e^{izu}\,du.
\tag{4}
\]

For a nontrivial zero `rho=beta+i gamma`, freeze also its horizontal/depth mark. It is enough for the argument to write this as a coefficient `c_rho` independent of the moving center `t`; in the Ford application it contains the multiplicity, the fixed critical-depth cutoff and the damping factors established in `NB-230`--`NB-243`. Put

\[
\eta_\rho:=H(\sigma_X-\beta),
\tag{5}
\]

where `sigma_X` is likewise frozen at `t_0`.

Define the **frozen-scale moving-center current**

\[
\mathcal R_{t_0}(t)
:=
C_{t_0}
\sum_\rho
c_\rho\,
 e^{iX(\gamma-t)}
 F\!\left(H(\gamma-t)+i\eta_\rho\right).
\tag{6}
\]

The constant `C_{t_0}` contains the harmless fixed normalizations, including the `1/J` Ford normalization. At the selected center,

\[
\mathcal R_{t_0}(t_0)
\tag{7}
\]

is exactly the critical smooth-shell current whose pointwise decay is sought. The auxiliary values at nearby `t` are introduced only to expose the harmonic structure; they do **not** require replacing the frozen parameters by the parameters naturally associated with those neighboring heights.

That distinction removes a possible bookkeeping ambiguity. The statement below is exact for the frozen family (6). Passing to a family in which `X,H,J,sigma_X` themselves vary with `t` would require a separate perturbative argument and is not used here.

## 2. Demodulation leaves only shell bandwidth `H`

Insert (4) into one summand of (6):

\[
\begin{aligned}
&e^{iX(\gamma-t)}
F\!\left(H(\gamma-t)+i\eta_\rho\right)
\\
&\qquad=
\int_a^b
\phi(u)e^{-\eta_\rho u}
 e^{i(X+Hu)(\gamma-t)}\,du.
\end{aligned}
\tag{8}
\]

Now remove the common carrier by defining

\[
S_{t_0}(t)
:=
e^{iXt}\mathcal R_{t_0}(t).
\tag{9}
\]

Then

\[
S_{t_0}(t)
=
\int_a^b A_{t_0}(u)e^{-iHu t}\,du,
\tag{10}
\]

where

\[
A_{t_0}(u)
:=
C_{t_0}\phi(u)
\sum_\rho
c_\rho e^{-\eta_\rho u}e^{i(X+Hu)\gamma}.
\tag{11}
\]

All dependence on the moving center `t` in (10) is therefore carried by frequencies `Hu` with `u in [a,b]`. For a finite symmetric ordinate truncation of the zero sum this is literal Fourier support:

\[
\operatorname{supp}\widehat S_{t_0}
\subset H[a,b]
\tag{12}
\]

up to the harmless sign convention for the Fourier transform.

The infinite zero sum causes no new frequency. Because `F` is Schwartz in the real direction uniformly for `eta_rho` in the fixed depth support, standard zero counting makes the symmetrically truncated currents converge locally after choosing enough decay. Equivalently, one may formulate (12) first for every finite truncation and pass to the resulting tempered-distribution limit. The support inclusion survives that limit.

The important point is that the large frequency `X` has disappeared from (12). It was a **common modulation** in the center variable and can be removed exactly. The horizontal depth `eta_rho` changes only the amplitude through `e^{-eta_rho u}`; it does not enlarge the center-frequency support.

## 3. The energy envelope is band-limited at `O(H)`

The Ford quantity needed for decay is the modulus, so define

\[
E_{t_0}(t)
:=
|\mathcal R_{t_0}(t)|^2
=
|S_{t_0}(t)|^2.
\tag{13}
\]

Since multiplication in `t` convolves Fourier supports,

\[
\operatorname{supp}\widehat E_{t_0}
\subset
H\bigl(\operatorname{supp}\phi-\operatorname{supp}\phi\bigr)
\subset
[-H(b-a),H(b-a)].
\tag{14}
\]

Thus

\[
\boxed{
\text{the selected-height Ford energy has center bandwidth }O(H).
}
\tag{15}
\]

This must not be confused with the resolution of the zeros themselves. Expanding (13) still gives the carrier pair phase

\[
 e^{iX(\gamma_j-\gamma_k)},
\tag{16}
\]

as in `NB-243`. Hence the zero geometry remains sensitive to ordinate differences of size `1/X`. Equation (14) says something different: **once the complete smooth current is formed, its squared magnitude cannot change arbitrarily on center scales much shorter than `1/H`.**

The scale separation is substantial in the Ford regime:

\[
\frac{1/H}{1/X}
=
\frac XH
=YJ
\longrightarrow\infty.
\tag{17}
\]

So a single moving-center energy envelope averages over many carrier cells, even though the pair statistic inside that envelope still resolves those cells.

This also explains why the conclusion depends on retaining the full smooth shell transform. If one multiplies the zero sum by an additional hard moving cutoff such as

\[
\mathbf 1_{|\gamma-t|\le 1/H},
\tag{18}
\]

then that cutoff has noncompact Fourier support and destroys the exact bandlimit (14). The localization supplied by the Schwartz shell itself is the source-compatible object here.

## 4. A Ford-scale local `L^2` mean reproduces the pointwise energy

Choose a Schwartz function `kappa` whose Fourier transform satisfies

\[
\widehat\kappa(\xi)=1
\tag{19}
\]

on an open neighborhood of

\[
\operatorname{supp}\phi-\operatorname{supp}\phi.
\tag{20}
\]

Set

\[
\kappa_H(v):=H\kappa(Hv).
\tag{21}
\]

By (14), Fourier multiplication gives the exact reproducing identity

\[
E_{t_0}=E_{t_0}*\kappa_H.
\tag{22}
\]

Evaluating at the selected height and taking absolute values,

\[
\begin{aligned}
|\mathcal R_{t_0}(t_0)|^2
&=E_{t_0}(t_0)
\\
&\le
H\int_{\mathbb R}
E_{t_0}(s)
\left|\kappa\!\left(H(t_0-s)\right)\right|ds.
\end{aligned}
\tag{23}
\]

For every fixed sufficiently large `A`, Schwartz decay yields

\[
\boxed{
|\mathcal R_{t_0}(t_0)|^2
\ll_{\phi,A}
H\int_{\mathbb R}
|\mathcal R_{t_0}(s)|^2
\bigl(1+H|s-t_0|\bigr)^{-A}\,ds.
}
\tag{24}
\]

Therefore the following **uniform Ford-local mean condition** is sufficient:

\[
\boxed{
\sup_{t_0}
H\int_{\mathbb R}
|\mathcal R_{t_0}(s)|^2
\bigl(1+H|s-t_0|\bigr)^{-A}\,ds
=o(1).
}
\tag{25}
\]

It implies immediately

\[
\mathcal R_{t_0}(t_0)=o(1)
\tag{26}
\]

uniformly over the same Ford parameter range.

Equation (25) is weaker in quantifier than direct pointwise control, but much stronger than a macroscopic average. It asks for a local second moment around **every** candidate selected height, on precisely the natural envelope scale `1/H`, with a rapidly decaying tail. A compact box average alone is not asserted to suffice here; the reproducing estimate naturally produces a Schwartz-weighted local mean unless one adds separate tail information.

## 5. Relation to the pair-energy target of `NB-243`

There is no contradiction between (14) and the carrier pair energy. Expanding (13) before demodulation gives

\[
E_{t_0}(t)
=
|C_{t_0}|^2
\sum_{\rho_j,\rho_k}
 c_j\overline{c_k}
 e^{iX(\gamma_j-\gamma_k)}
\mathcal F_j(t)\overline{\mathcal F_k(t)},
\tag{27}
\]

where

\[
\mathcal F_j(t)
:=
F\!\left(H(\gamma_j-t)+i\eta_j\right).
\tag{28}
\]

At `t=t_0`, after the Ford normalization is unpacked, (27) is exactly the depth/profile-marked pair energy isolated in `NB-243`. The `1/X` carrier scale is still present in the factor `e^{iX(gamma_j-gamma_k)}`. What the shell structure adds is that the **coefficient with which that fixed pair energy is sampled as the center moves** has only `O(H)` bandwidth.

This changes the sufficient source theorem from

\[
\text{pointwise marked pair energy at every selected }t_0=o(1)
\tag{29}
\]

to the weaker target

\[
\text{uniform Ford-scale local mean of that smooth current}=o(1).
\tag{30}
\]

A bad selected block cannot hide at one isolated center on a scale much smaller than `1/H`: band limitation forces its energy to have a correspondingly non-negligible local footprint. This is the exact sense in which local averaging becomes legitimate here.

It does **not** say that an unmarked pair correlation suffices. The factors `c_rho` and `eta_rho` retain the horizontal Ford depth, so the phase-depth locking obstruction of `NB-233` remains visible. Nor does it say that a fixed test at mean-zero spacing suffices: the underlying zero-pair phase in (16) remains tuned to `X`, as required by `NB-240` and `NB-243`.

## 6. Why this does not reopen the random-height shortcut

`NB-245` showed that a statistic sampled uniformly from an interval of length comparable to `T` can ignore sparse exceptional Ford blocks whose total measure is `o(T)`. Equation (25) does not weaken that conclusion.

The averaging radius in (25) is

\[
\asymp\frac1H=\frac JR=o(1),
\tag{31}
\]

and the estimate must hold **uniformly for every target center `t_0`**. A sparse family of bad blocks is therefore not diluted by the ambient height interval: each bad block is tested by its own local mean. Conversely, a theorem that controls only

\[
\frac1T\int_T^{2T}|\mathcal R(t)|^2dt
\tag{32}
\]

or gives convergence in law for a uniformly random `t` can still be compatible with isolated windows violating (25).

The distinction is now clean:

\[
\text{macroscopic/random-height mean}
\quad\not\Rightarrow\quad
\text{selected-height decay},
\tag{33}
\]

while for the exact smooth shell,

\[
\boxed{
\text{uniform local mean on scale }1/H
\quad\Rightarrow\quad
\text{selected-height decay}.
}
\tag{34}
\]

Thus `NB-245` rules out averaging at the wrong quantifier and scale; the present finding identifies the smallest natural center scale on which averaging is automatically source-faithful.

## 7. Prior-art and representation audit

The harmonic-analysis mechanism is classical. Compact Fourier support and reconstruction from a reproducing kernel are standard Paley--Wiener/Shannon phenomena; no novelty is claimed for the implication from band limitation to local reconstruction. The line-local content is the exact identification of the bandwidth after inserting the **particular Mellin shell carrier** of `NB-218`--`NB-243`: the apparent frequency `X` is a removable common modulation in the center variable, so the energy envelope is governed by `H`.

A fresh literature check also revisited the closest current zeta pair-correlation input. Biao Wang, [*Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*](https://arxiv.org/abs/2609.07918) (submitted 7 September 2026), proves a Montgomery-type pair-correlation result in short intervals. Its short intervals are still of power length in the height parameter and its published statistic does not provide the uniform depth-marked Ford-scale local mean (25). The search did not locate a September 2026 theorem giving deterministic uniform control on shrinking windows of length `J/R` with the near-one depth mark and moving carrier required here.

No external theorem is load-bearing in (8)--(25): those statements are direct Fourier algebra plus a smooth reproducing kernel. Accordingly this finding does not add a durable dependency to `SOURCES.md`.

The representation audit is also restrictive. If one forgets the zeta origin and begins with any marked point measure convolved against a compact-frequency window, the same bandlimit argument goes through. Hence this is **not** a new theorem about the actual zero distribution of `zeta`, and certainly not a new Nyman--Beurling distance bound. Its arithmetic relevance comes from the earlier exact source representation, which fixes the carrier `X`, shell bandwidth `H`, Ford normalization and depth marks.

## 8. Adversarial review and route consequence

Several stronger readings are not justified.

First, (25) is a **sufficient target**, not a theorem presently known for zeta. The argument converts a uniformly local second moment into pointwise decay; it does not prove that second moment. A future analytic input is still required.

Second, exact band limitation belongs to the frozen smooth current (6). Hard moving cutoffs, adaptive truncations depending nonsmoothly on the center, or silently varying `X,H,J` can introduce extra frequencies. Any future use must either keep the frozen formulation or quantify those perturbations separately.

Third, the disappearance of `X` from the center bandwidth does not make carrier coherence irrelevant. The matched packets from `NB-231` remain order-one obstructions, and their pair phases are still measured at scale `1/X`. The finding separates two coordinates that had been conflated: **zero-space carrier resolution `1/X`** and **center-height envelope resolution `1/H`**.

Fourth, the reproducing kernel has Schwartz tails. The argument does not claim that knowing an unweighted integral over exactly one hard interval of length `1/H` is automatically enough. A theorem with a hard box would need quantitative control of neighboring boxes or another way to dominate the tails in (24).

Subject to those restrictions, the research frontier can be weakened in a useful direction. Instead of demanding a deterministic pointwise theorem for the marked carrier current at every `t_0`, one may seek a theorem of the form (25): a **uniform, depth-marked, carrier-aware local second moment on the Ford envelope scale**. Such a theorem would still be microscopic and selected-height enough to survive the `NB-245` audit, but it can exploit `L^2`/pair-correlation machinery unavailable to a direct pointwise estimate.

The next useful test is therefore not another macroscopic zero statistic. It is whether the explicit-formula, local-factorization, or short-interval pair-correlation machinery already audited in `NB-237`--`NB-245` can be retuned to prove (25) for the frozen smooth current, uniformly in `t_0`. If it cannot, the failure should now be expressible as a quantitative loss relative to the natural bandwidth `H`, rather than as the vaguer requirement of controlling one exact selected height.