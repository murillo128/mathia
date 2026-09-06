# ANF-080 — sorted prefix variation replaces geometric band count in the real-multiplicity gate

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY + SORTED-PREFIX-DECOMPOSITION + INTRINSIC-SCALE-VARIATION + SUPPORT-UNBOUNDED + OCCUPANCY-MAGNITUDE-UNBOUNDED + EXPONENTIAL-CAP-SHARPENING`. `ANF-079` shows that a central-notch profile survives every real multiset whose occupancies meet only finitely many geometric weight bands. The geometric partition is not intrinsic. Sorting the occupancies and decomposing them into nested prefixes yields a strictly finer scale-complexity parameter: the total relative variation of the multiplicity profile. Every fixed bound on this variation can be closed with one central-notch affine certificate, with no bound on support cardinality or on the largest multiplicity.

Let the distinct real support sites be relabelled so that their positive integer occupancies satisfy

\[
k_1\ge k_2\ge\cdots\ge k_r\ge1,
\qquad k_{r+1}:=0.
\tag{1}
\]

Define

\[
\delta_j:=k_j-k_{j+1},
\qquad
A_j:=k_j^2-k_{j+1}^2,
\tag{2}
\]

and the intrinsic variation

\[
\boxed{
\mathcal V(k)
:=
\sum_{j:\delta_j>0}
\frac{k_j-k_{j+1}}{k_j+k_{j+1}}
=
\sum_{j:\delta_j>0}
\frac{\delta_j^2}{A_j}.
}
\tag{3}
\]

The terminal drop `k_r -> 0` contributes exactly `1`, so `mathcal V(k)>=1`. A huge isolated jump contributes less than `1`, independent of its absolute ratio. Consequently `mathcal V` detects the **number and cumulative relative size of genuine scale changes**, rather than logarithmic diameter or an arbitrarily chosen geometric binning.

For every fixed `V_*>=1` there are central-notch parameters

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0,
\qquad
F_s=\widehat J_s,
\tag{4}
\]

and a positive amplitude `t` such that every finite real multiset with

\[
\boxed{\mathcal V(k)\le V_*}
\tag{5}
\]

obeys

\[
\boxed{
\sigma\ge2N-tE_{F_s}(k;X),
}
\tag{6}
\]

while

\[
\boxed{
2-tC(J_s)>2-C_{\rm MT}.
}
\tag{7}
\]

Here `N=sum_i k_i` and `sigma=#\{i:k_i=1\}`. There is no restriction on `r`, `max k_i`, the positions `x_i`, or the gaps between occupied multiplicity scales.

For the simpler bounded-occupancy corollary, (3) gives

\[
\boxed{
\mathcal V(k)
\le1+\frac12\log K
\qquad(1\le k_i\le K).
}
\tag{8}
\]

Hence, if `eta -> 0` and `L^{-1}=o(eta)` in the near-face estimate below, one profile can close every real multiset with

\[
\boxed{
K\le\exp\!\left(\frac{c}{\eta}\right)
}
\tag{9}
\]

for every fixed

\[
\boxed{
c<\frac{c_0}{2C_{\rm MT}}
=0.3400466335773675\ldots,}
\tag{10}
\]

where

\[
c_0=\int_{-1}^{1}
\left(\frac{\sin\pi u}{\pi u}\right)^2du.
\]

This improves the sufficient exponential constant `c_0/(8eC_MT)=0.03127404138...` from `ANF-079` by the factor `4e`. The constant in (10) is a sufficient constant for this proof, not a claim of optimality.

## 1. Sorted prefixes give an exact coefficient layer cake

For `1<=j<=r` put

\[
Y_j:=\{x_1,\ldots,x_j\}.
\tag{11}
\]

The ordering is only by multiplicity; the points themselves remain in their original geometry. If

\[
S_Y(\alpha):=\sum_{x\in Y}e^{2\pi i\alpha x},
\qquad
S_k(\alpha):=\sum_i k_i e^{2\pi i\alpha x_i},
\]

then telescoping (1)--(2) gives the exact nested-prefix decomposition

\[
\boxed{
S_k
=
\sum_{j=1}^r\delta_j S_{Y_j}.
}
\tag{12}
\]

This is the decreasing-rearrangement version of the elementary layer-cake representation. The useful point is that it has only one term for each **actual drop of the sorted multiplicity profile**; a long plateau costs nothing.

Let

\[
R:=R_{\rm MT}=\widehat J_{\rm MT}\ge0,
\qquad
\Phi_\eta:=\widehat\phi_\eta,
\tag{13}
\]

and write

\[
W_2:=\sum_i k_i^2,
\qquad
\nu:=\frac{E_R(k;X)}{W_2}-1\ge0.
\tag{14}
\]

For each prefix define its simple-support Montgomery--Taylor excess

\[
\Delta_j
:=
\frac{E_R(Y_j)}{j}-1
\ge0.
\tag{15}
\]

Two telescoping identities are load-bearing. First,

\[
\boxed{
\sum_{j=1}^r jA_j=W_2.
}
\tag{16}
\]

Second,

\[
\begin{aligned}
\sum_{j=1}^r A_jj\Delta_j
&=
2\sum_{i<\ell}R(x_i-x_\ell)
\sum_{j\ge\ell}A_j\\
&=
2\sum_{i<\ell}k_\ell^2R(x_i-x_\ell)\\
&\le
2\sum_{i<\ell}k_ik_\ell R(x_i-x_\ell)\\
&=
\boxed{W_2\nu.}
\end{aligned}
\tag{17}
\]

The inequality uses exactly the sorted order `k_i>=k_ell` and the pointwise nonnegativity `R>=0`. Thus the full weighted Montgomery--Taylor excess controls the prefix excesses with the same quadratic weights that appear in (16).

## 2. The simple-set near-face estimate lifts with the intrinsic variation

Retain the notation of `ANF-078`--`ANF-079`:

\[
B_{\eta,L}
:=
\frac4{c_0}\left(\eta+\frac4L\right),
\qquad
E_L(u)
:=
2\sqrt{a_Lu(1+u)}+a_Lu,
\tag{18}
\]

where `a_L=1+2/kappa_L`. Their support-uniform simple-set estimate is

\[
\boxed{
E_{\Phi_\eta}(Y)
\le
|Y|\left[b_\eta B_{\eta,L}+E_L(\Delta(Y))\right]
}
\tag{19}
\]

for every finite set of distinct real points; no small-excess hypothesis is present.

Because `phi_eta>=0`, `E_{Phi_eta}` is the squared norm in the Hilbert space `L^2(phi_eta d alpha)`. Minkowski applied to (12) and then (19) gives

\[
\sqrt{E_{\Phi_\eta}(k;X)}
\le
\sum_j\delta_j\sqrt{j}
\sqrt{b_\eta B_{\eta,L}+E_L(\Delta_j)}.
\tag{20}
\]

Use the elementary bound already employed in `ANF-078`,

\[
E_L(u)
\le
2\sqrt{a_L}\,u^{1/2}
+\bigl(2\sqrt{a_L}+a_L\bigr)u.
\tag{21}
\]

Put

\[
p_L:=\sqrt{2\sqrt{a_L}},
\qquad
q_L:=\sqrt{2\sqrt{a_L}+a_L}.
\tag{22}
\]

Then

\[
\sqrt{E_L(u)}
\le p_Lu^{1/4}+q_Lu^{1/2}.
\tag{23}
\]

For every nonzero drop set

\[
c_j:=\frac{\delta_j^2}{A_j}
=\frac{k_j-k_{j+1}}{k_j+k_{j+1}},
\tag{24}
\]

so `sum c_j=mathcal V(k)` and

\[
\delta_j\sqrt j=\sqrt{c_jA_jj}.
\tag{25}
\]

Equations (16)--(17), Cauchy, and Hölder with exponents `2,4,4` now give the three estimates

\[
\sum_j\delta_j\sqrt j
\le
\sqrt{\mathcal V(k)W_2},
\tag{26}
\]

\[
\sum_j\delta_j\sqrt j\,\Delta_j^{1/2}
\le
\sqrt{\mathcal V(k)W_2\nu},
\tag{27}
\]

and

\[
\sum_j\delta_j\sqrt j\,\Delta_j^{1/4}
\le
\sqrt{\mathcal V(k)W_2}\,\nu^{1/4}.
\tag{28}
\]

For (28), write `X_j=A_jj` and `Z_j=X_jDelta_j`; then the summand is `c_j^{1/2}X_j^{1/4}Z_j^{1/4}` and apply Hölder using `sum X_j=W_2` and `sum Z_j<=W_2nu`.

Substituting (23), (26)--(28) into (20) proves the main weighted notch estimate

\[
\boxed{
\frac{E_{\Phi_\eta}(k;X)}{W_2}
\le
\mathcal V(k)
\left(
\sqrt{b_\eta B_{\eta,L}}
+p_L\nu^{1/4}
+q_L\nu^{1/2}
\right)^2.
}
\tag{29}
\]

This is the replacement for the `rho^2D_rho(k)` factor in `ANF-079`. It is support-uniform and contains no arbitrary geometric ratio. The only multiplicity information retained is the intrinsic variation (3).

## 3. Every fixed variation cap has a strict Montgomery--Taylor improvement

Fix `V_*>=1` and a parameter `theta>0`. Restrict only to `mathcal V(k)<=V_*`, and put

\[
\lambda:=sV_*.
\tag{30}
\]

Since `F_s=R-sPhi_eta`, equations (14) and (29) give

\[
\frac{E_{F_s}(k;X)}{W_2}
\ge
1+\nu
-\lambda
\left(
\sqrt{b_\eta B_{\eta,L}}
+p_L\nu^{1/4}
+q_L\nu^{1/2}
\right)^2.
\tag{31}
\]

Use

\[
(a+b)^2\le(1+\theta)a^2+(1+\theta^{-1})b^2
\]

and

\[
(p_L\nu^{1/4}+q_L\nu^{1/2})^2
\le2p_L^2\nu^{1/2}+2q_L^2\nu.
\tag{32}
\]

If

\[
\boxed{
4(1+\theta^{-1})q_L^2\lambda\le1,
}
\tag{33}
\]

then completing the square in `sqrt(nu)` yields the uniform quadratic floor

\[
\boxed{
E_{F_s}(k;X)
\ge q_*W_2,
}
\tag{34}
\]

with

\[
\boxed{
q_*
:=
1-(1+\theta)\lambda b_\eta B_{\eta,L}
-8a_L(1+\theta^{-1})^2\lambda^2.
}
\tag{35}
\]

For sufficiently small `s`, `q_*>0`. Take

\[
t:=q_*^{-1},
\qquad A:=2.
\tag{36}
\]

Then every multiset in the variation class satisfies

\[
\begin{aligned}
\sigma-2N+tE_{F_s}(k;X)
&\ge
\sigma-2N+W_2\\
&=
\sum_{k_i\ge2}k_i(k_i-2)\\
&\ge0,
\end{aligned}
\tag{37}
\]

which proves the affine inequality (6).

It remains to pay for the rescaling. The exact central-notch cost is

\[
C(J_s)
=C_{\rm MT}-sb_\eta c_\eta,
\qquad
c_\eta:=1+\frac{\eta^2}{3}.
\tag{38}
\]

Define

\[
\boxed{
G_{V_*,\theta}(\eta,L)
:=
c_\eta
-(1+\theta)V_*C_{\rm MT}B_{\eta,L}.
}
\tag{39}
\]

For every fixed `V_*` and `theta`, first choose `eta>0` sufficiently small and then `L` sufficiently large so that

\[
G_{V_*,\theta}(\eta,L)>0.
\tag{40}
\]

After that choose `s>0` small enough that `s<1`, (33) holds, `q_*>0`, and

\[
\boxed{
8C_{\rm MT}a_L(1+\theta^{-1})^2sV_*^2
<
b_\eta G_{V_*,\theta}(\eta,L).
}
\tag{41}
\]

A direct expansion gives

\[
\begin{aligned}
C(J_s)-C_{\rm MT}q_*
&=
-sb_\eta G_{V_*,\theta}(\eta,L)\\
&\quad
+8C_{\rm MT}a_L(1+\theta^{-1})^2s^2V_*^2
<0.
\end{aligned}
\tag{42}
\]

Therefore

\[
\boxed{
\frac{C(J_s)}{q_*}<C_{\rm MT},
}
\tag{43}
\]

which is exactly (7). The possibly poor `L`-dependence of `a_L` only forces the final amplitude `s` to be smaller; it does not obstruct existence because `eta,L` are fixed before `s` is chosen.

## 4. The variation is finer than geometric band count

The summand in (3) has the exact logarithmic form

\[
\frac{a-b}{a+b}
=
\tanh\!\left(\frac12\log\frac ab\right)
\qquad(a>b>0),
\tag{44}
\]

and hence

\[
\boxed{
\frac{a-b}{a+b}
\le
\min\left\{1,\frac12\log\frac ab\right\}.
}
\tag{45}
\]

This explains why `mathcal V` simultaneously handles both gradual and enormous jumps. If the occupancies meet only `D_rho(k)` nonempty geometric `rho`-bands as in `ANF-079`, the total variation from drops that stay inside one band is at most `(1/2)log rho` per band, while each transition between different occupied bands costs at most `1`. Including the terminal drop,

\[
\boxed{
\mathcal V(k)
\le
D_\rho(k)\left(1+\frac12\log\rho\right).
}
\tag{46}
\]

Thus every bounded-band class of `ANF-079` is also a bounded-variation class, but the converse description is intrinsic and can be substantially smaller. In particular, occupancies taking only two values `1` and `K` have `mathcal V(k)<2` regardless of how enormous `K` is or how many sites carry either value.

For a maximum occupancy cap `K`, telescoping (45) over all positive drops and adding the terminal contribution gives

\[
\begin{aligned}
\mathcal V(k)
&\le
1+\frac12\log\frac{k_1}{k_r}\\
&\le
\boxed{1+\frac12\log K,}
\end{aligned}
\tag{47}
\]

which is (8).

## 5. The bounded-occupancy sufficient exponent improves by `4e`

Take `L=L(eta)` with `L^{-1}=o(eta)`. Then

\[
B_{\eta,L}
=
\left(\frac4{c_0}+o(1)\right)\eta,
\qquad
c_\eta=1+o(1).
\tag{48}
\]

Fix

\[
c<\frac{c_0}{2C_{\rm MT}}.
\]

Choose `theta>0` so small that

\[
c<\frac{c_0}{2(1+\theta)C_{\rm MT}}.
\tag{49}
\]

If `K<=exp(c/eta)`, (47) gives

\[
V_*
:=1+\frac12\log K
\le1+\frac{c}{2\eta}.
\tag{50}
\]

Equations (48)--(50) imply

\[
(1+\theta)V_*C_{\rm MT}B_{\eta,L}
\le
\frac{2(1+\theta)C_{\rm MT}c}{c_0}+o(1)
<1
\tag{51}
\]

for all sufficiently small `eta`, so the margin (39) is positive. One may then choose `s=s(eta,K)>0` sufficiently small to satisfy (33), (35), and (41). The resulting single profile handles **every** support geometry and every integer occupancy vector below the cap `K`.

Since

\[
\frac{c_0}{2C_{\rm MT}}
=0.3400466335773675\ldots,
\tag{52}
\]

while `ANF-079` obtains `c_0/(8eC_MT)=0.031274041383...`, the sufficient exponential coefficient improves by

\[
\boxed{4e=10.8731273138\ldots.}
\tag{53}
\]

Again, neither coefficient is asserted to be a true obstruction threshold; they are certified ranges delivered by the corresponding decompositions.

## 6. Boundary, prior art, and decisive audit

This finding materially narrows the surviving real-multiplicity frontier. Large support, large maximum occupancy, and even many nominal weight bands are not independently decisive. A central-notch no-go robust under narrowing must force

\[
\boxed{\mathcal V(k)\to\infty.}
\tag{54}
\]

Since every nonzero term of (3) corresponds to a distinct multiplicity drop and `mathcal V(k)<=1+(1/2)log k_1`, such an obstruction must simultaneously develop unbounded support complexity and unbounded multiplicity scale variation. The relevant escape is now a long chain of genuinely non-negligible relative drops, not one gigantic repeated site or a finite collection of widely separated scales.

The sorted layer-cake representation, Minkowski, Hölder, and the relation of decreasing sequences to Lorentz/rearrangement norms are classical analytic devices. A targeted prior-art search of Lorentz-sequence/rearrangement literature, classical positive-Fourier pair-potential stability, and the current public zeta simple-zero refinement artifacts did not identify a theorem that yields (29)--(43) in this finite BGSST normalization. No novelty is claimed for decreasing rearrangements or Lorentz-space technology. The line-specific content is the exact coupling of the prefix increments to the Montgomery--Taylor excess through (17), which converts a simple-support central-mass estimate into the intrinsic weighted certificate (29). The Sütő/Procacci stability anchors and the Montgomery--Taylor/CCLM anchors already present in `SOURCES.md` remain sufficient; no source-file change is needed.

The decisive audit has six interfaces. First, sorting is only by multiplicity and does not assume any spatial ordering. Second, (12), (16), and the first equality in (17) are exact telescoping identities. Third, the inequality in (17) uses the pointwise fact `R_MT>=0`; positive definiteness alone would not justify it. Fourth, Minkowski in (20) is legal because the spectral tent `phi_eta` is nonnegative. Fifth, the simple-set estimate (19) is the already-canonical all-excess estimate, not a near-minimizer heuristic. Sixth, the parameter order in Section 3 is essential: choose the variation cap, then `eta,L`, and only then shrink `s` enough to absorb the `a_L` and `V_*^2` terms.

The result does **not** prove one fixed central-notch profile for all integer multiplicities, establish the full real-multiset affine certificate, resolve complex multi-pair geometry, improve the unconditional zeta-zero proportion, or imply RH. The remaining real scalar gate is now sharper: determine whether the prefix-variation loss in (29) can itself be removed, or construct a genuine weighted falsifier whose sorted multiplicities have `mathcal V(k)` diverging on the reciprocal-notch scale.