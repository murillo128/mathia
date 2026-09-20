# NB-247 — Bellotti population turns hard Ford-window energy into pointwise control

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC-REGULARITY + HARD-WINDOW-L2-SUFFICIENT-CONDITION + NB-230/NB-246-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-246` shows that, after removing the common carrier, the frozen critical Ford current has center-frequency width `O(H)`. A Schwartz-weighted local second moment on the natural center scale `1/H` therefore controls the selected value by an exact reproducing kernel. That argument deliberately did **not** claim that a hard box of length `O(1/H)` is sufficient, because compact Fourier support alone does not justify deleting the reproducing-kernel tails.

For the actual Ford current there is extra source information that `NB-246` did not use. The Bellotti weighted population estimate of `NB-230`, combined with the smooth shell profile, gives a **uniform Lipschitz bound for the demodulated current on the scaled center variable**. Consequently an order-one selected value cannot disappear immediately outside the selected point: it persists on a fixed fraction of a Ford window. This removes the tail issue.

More precisely, in the conservative critical regime

\[
1\ll J=\frac RH\le \log Q,
\]

fix any `A>0`. If `R_{t_0}` is the frozen critical smooth-shell current of `NB-243`/`NB-246`, then there is a constant `L_A`, independent of `Q,J,t_0`, such that its demodulated envelope `G_{t_0}` satisfies

\[
\sup_{|z|\le A}|G'_{t_0}(z)|\le L_A.
\]

Hence, with

\[
I_A(t_0)
:=
H\int_{t_0-A/H}^{t_0+A/H}
|\mathcal R_{t_0}(s)|^2\,ds,
\]

one has the quantitative implication

\[
|\mathcal R_{t_0}(t_0)|
\ll_A
I_A(t_0)^{1/3}+I_A(t_0)^{1/2}.
\]

Therefore

\[
\boxed{
\sup_{t_0} I_A(t_0)=o(1)
\quad\Longrightarrow\quad
\sup_{t_0}|\mathcal R_{t_0}(t_0)|=o(1).
}
\]

So the sufficient source theorem left by `NB-246` can be sharpened from a Schwartz-tailed local mean to a **single hard Ford-scale box mean**. The gain does not come from band limitation alone; it comes from combining band-scale center motion with the already-audited near-one population law. The analytic problem remains open: no current zeta theorem located in the prior-art audit supplies this uniformly depth-marked mean square on a shrinking interval of length `J/R`.

## 1. Freeze the same critical current as in `NB-243` and `NB-246`

Keep

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty,
\tag{1}
\]

and assume

\[
J\le \log Q.
\tag{2}
\]

Let

\[
F(z)=\int_0^1\phi(u)e^{izu}\,du,
\qquad
\phi\in C_c^\infty((0,1)),
\tag{3}
\]

and let `chi in C_c^infty(R)` be the fixed cutoff to the critical Ford layer. For a zero `rho=beta+i gamma`, counted with multiplicity, put

\[
d_\rho:=X(1-\beta)-\log J,
\qquad
\eta_\rho:=H(\sigma_X-\beta)
=\frac{r+\log J+d_\rho}{YJ}.
\tag{4}
\]

On the support of `chi`, `d_rho=O(1)` and `eta_rho=o(1)` uniformly. The frozen-scale critical current can be written exactly in the normalization of `NB-243` as

\[
\mathcal R_{t_0}(t)
=
\frac{e^{-r}}J
\sum_\rho
m(\rho)e^{-d_\rho}\chi(d_\rho)
 e^{iX(\gamma-t)}
F\!\left(H(\gamma-t)+i\eta_\rho\right).
\tag{5}
\]

Only the observation center `t` moves in (5); `Q,R,X,H,J,sigma_X,d_rho,eta_rho` remain frozen at `t_0`, exactly as required in `NB-246`.

Introduce the scaled center displacement

\[
z:=H(t-t_0),
\qquad
\tau_\rho:=H(\gamma-t_0),
\qquad
\omega:=\frac XH=YJ,
\tag{6}
\]

and remove the common carrier by defining

\[
G_{t_0}(z)
:=
e^{i\omega z}
\mathcal R_{t_0}\!\left(t_0+\frac zH\right).
\tag{7}
\]

Then

\[
\boxed{
G_{t_0}(z)
=
\frac{e^{-r}}J
\sum_\rho
m(\rho)e^{-d_\rho}\chi(d_\rho)
 e^{iX(\gamma-t_0)}
F(\tau_\rho-z+i\eta_\rho).
}
\tag{8}
\]

Since the prefactor in (7) has modulus one,

\[
|G_{t_0}(z)|
=
\left|\mathcal R_{t_0}\!\left(t_0+\frac zH\right)\right|.
\tag{9}
\]

Equation (8) is the form in which the Bellotti population law becomes useful: after demodulation, differentiating in the scaled center differentiates only the smooth profile.

## 2. Bellotti plus shell smoothness gives a uniform scaled derivative bound

Differentiate (8):

\[
G'_{t_0}(z)
=
-\frac{e^{-r}}J
\sum_\rho
m(\rho)e^{-d_\rho}\chi(d_\rho)
 e^{iX(\gamma-t_0)}
F'(\tau_\rho-z+i\eta_\rho).
\tag{10}
\]

Because

\[
F'(w)
=i\int_0^1u\phi(u)e^{iwu}\,du,
\]

`F'` is the Fourier transform of another compactly supported smooth profile. Hence for every `B>0`, uniformly for bounded nonnegative imaginary part,

\[
|F'(x+i\eta)|
\ll_{B,\phi}(1+|x|)^{-B}.
\tag{11}
\]

Fix `A>0`. For `|z|<=A`, (11) implies

\[
|F'(\tau_\rho-z+i\eta_\rho)|
\ll_{A,B,\phi}
(1+|\tau_\rho|)^{-B}.
\tag{12}
\]

Now translate the critical-depth cutoff into the `NB-230` depth coordinate

\[
D_\rho:=R(1-\beta).
\tag{13}
\]

If `supp chi subset [-C_chi,C_chi]`, then every zero occurring in (10) satisfies

\[
D_\rho
=
\frac{\log J+d_\rho}{Y}
\le
D_*:=\frac{\log J+C_\chi}{Y}.
\tag{14}
\]

Under (2),

\[
D_*=O(\log\log Q)=o(\log Q),
\tag{15}
\]

so for large `Q` this lies inside the Bellotti range used in `NB-230`. Its weighted local population estimate gives, for sufficiently large fixed `B`,

\[
\sum_{D_\rho\le D_*}
 m(\rho)(1+H|\gamma-t_0|)^{-B}
\ll
D_*+J
\ll J.
\tag{16}
\]

The factor `e^{-d_rho} chi(d_rho)` is uniformly bounded on the fixed support of `chi`. Combining (10), (12), and (16) therefore yields

\[
\boxed{
\sup_{|z|\le A}|G'_{t_0}(z)|
\ll_{A,\phi,\chi,r,Y}1.
}
\tag{17}
\]

The bound is uniform in the selected height and in the allowed `J` range. The same argument applies to every fixed derivative because `F^(k)` is again generated by the compactly supported smooth profile `u^k phi(u)`. Thus, for every fixed `k,A`,

\[
\sup_{|z|\le A}|G^{(k)}_{t_0}(z)|
\ll_{k,A}1.
\tag{18}
\]

Only the first derivative is needed below. Equation (18) is useful conceptually: the critical Ford currents form an equicontinuous family on the natural scaled center coordinate. An order-one current cannot be a delta-like center spike.

## 3. A hard Ford box now controls the selected value

Fix `A>0` once and for all and let `L_A>=1` be a uniform constant in (17). Put

\[
a:=|G_{t_0}(0)|
=|\mathcal R_{t_0}(t_0)|
\tag{19}
\]

and

\[
I_A(t_0)
:=
\int_{-A}^{A}|G_{t_0}(z)|^2\,dz.
\tag{20}
\]

By the change of variables `z=H(s-t_0)`,

\[
\boxed{
I_A(t_0)
=
H\int_{t_0-A/H}^{t_0+A/H}
|\mathcal R_{t_0}(s)|^2\,ds.
}
\tag{21}
\]

The Lipschitz bound gives

\[
|G_{t_0}(z)|
\ge a-L_A|z|.
\tag{22}
\]

If

\[
a\le2L_AA,
\]

then on `|z|<=a/(2L_A)` one has `|G(z)|>=a/2`. Therefore

\[
I_A(t_0)
\ge
\frac{a^3}{4L_A}.
\tag{23}
\]

If instead

\[
a>2L_AA,
\]

then throughout the whole hard box `|z|<=A`,

\[
|G(z)|>\frac a2,
\]

and hence

\[
I_A(t_0)
\ge
\frac A2a^2.
\tag{24}
\]

The two cases give the uniform quantitative estimate

\[
\boxed{
|\mathcal R_{t_0}(t_0)|
\le
(4L_AI_A(t_0))^{1/3}
+
\left(\frac{2I_A(t_0)}A\right)^{1/2}.
}
\tag{25}
\]

In particular,

\[
\boxed{
\sup_{t_0}
H\int_{t_0-A/H}^{t_0+A/H}
|\mathcal R_{t_0}(s)|^2\,ds
=o(1)
\quad\Longrightarrow\quad
\sup_{t_0}|\mathcal R_{t_0}(t_0)|=o(1).
}
\tag{26}
\]

Because `A` is fixed, replacing the integral in (26) by its usual box average only changes a fixed factor. Thus a theorem stated as a genuine short-interval mean square is enough; no Schwartz tail is logically required once (17) is retained.

## 4. Why this is stronger than the pure bandlimit statement in `NB-246`

`NB-246` obtained

\[
|\mathcal R_{t_0}(t_0)|^2
\ll
H\int_{\mathbb R}
|\mathcal R_{t_0}(s)|^2
(1+H|s-t_0|)^{-B}\,ds
\tag{27}
\]

from a reproducing kernel. That proof uses only center-frequency support. Its tails are therefore part of the argument, and `NB-246` correctly declined to replace (27) by one hard box without further information.

Equation (17) supplies exactly that further information. It is not a generic Paley--Wiener statement: it uses the actual Ford depth cutoff and Bellotti's near-one weighted population law. Once the family is uniformly Lipschitz after Ford rescaling, a large selected value must occupy positive local `L^2` mass before it has room to fall.

The logical hierarchy is therefore

\[
\text{bandlimit alone}
\Longrightarrow
\text{Schwartz-tailed local observability},
\tag{28}
\]

whereas

\[
\boxed{
\text{band-scale current}
+
\text{Bellotti population}
\Longrightarrow
\text{hard-box local observability}.
}
\tag{29}
\]

This makes the next analytic target easier to state and potentially easier to match to existing methods. One may now seek a uniform estimate over the literal interval

\[
\left[t_0-\frac A H,
      t_0+\frac A H\right],
\tag{30}
\]

rather than a weighted mean with infinite tails.

## 5. The matched packet still saturates the strengthened target

The new implication is a representation improvement, not a proof that the local mean is small for the actual zeta zeros. The `NB-231` matched packet remains the decisive stress test.

For the packet

\[
\gamma_j=t_0+\frac{2\pi qj}{X},
\qquad
M\sim\delta J,
\qquad
X(1-\beta_j)=\log J+w,
\tag{31}
\]

with fixed bounded `w`, the scaled ordinates satisfy

\[
\tau_j
=
\frac{2\pi q}{Y}\frac jJ.
\tag{32}
\]

After demodulation, its current is

\[
G_J(z)
=
\frac{e^{-r-w}}J
\sum_{j=1}^{M}
F\!\left(
\frac{2\pi q}{Y}\frac jJ-z+i\eta_J
\right),
\qquad
\eta_J=o(1).
\tag{33}
\]

This is a Riemann sum. Uniformly for `z` in compact sets,

\[
G_J(z)
\longrightarrow
 e^{-r-w}
\int_0^\delta
F\!\left(\frac{2\pi q}{Y_*}u-z\right)du.
\tag{34}
\]

Choosing the same small `delta` as in `NB-231` makes the limit nonzero near `z=0`. Consequently, for every sufficiently small fixed `A>0`,

\[
\liminf_{J\to\infty}
\int_{-A}^{A}|G_J(z)|^2dz
>0.
\tag{35}
\]

Thus the hard-box formulation does **not** average away the known adversarial packet. It rejects it only if an actual-zeta theorem supplies (26). This is the desired behavior: the reformulation is source-faithful, but it does not smuggle in the missing zero-geometry information.

Equation (34) also explains why generic short-interval averaging cannot by itself create a gain. At the Ford scale the coherent packet has a nonzero continuum envelope, not a point spike. Any proof of (26) must use arithmetic information that prevents this packet geometry rather than hoping that the box average dilutes it.

## 6. Prior-art audit and surviving analytic gap

The only load-bearing zero-distribution input in the proof is the Bellotti local population estimate already anchored and audited in `NB-224`/`NB-230`. The remaining steps are direct differentiation of the exact smooth-shell current and the elementary consequence of a uniform Lipschitz bound. No new external theorem is required, so `SOURCES.md` needs no new durable dependency.

A fresh search nevertheless rechecked the natural short-interval literature because (26) is now phrased as a literal mean square. Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*, arXiv:2609.07918 (submitted 7 September 2026), remains the closest current pair-correlation input. Its intervals have power length in the height parameter and its statistic does not retain the shrinking Ford window, the near-one depth mark, and the moving carrier simultaneously. The short-interval mean-square results surfaced in the same search likewise operate on macroscopic power scales, not on intervals of length

\[
\frac1H=\frac JR=o(1).
\tag{36}
\]

So (26) is a cleaner sufficient theorem, but not one currently supplied by the literature located in this pass.

The distinction with ordinary large-sieve or mean-value heuristics is also important. The center box has exactly the natural smooth-envelope scale. The carrier pair phase `e^{iX(\gamma_j-\gamma_k)}` remains untouched inside the squared current, as in `NB-243`; the box mean does not generate an extra carrier-frequency averaging parameter. The matched limit (34) makes that limitation explicit.

## 7. Adversarial review and falsification boundary

Several restrictions are load-bearing.

First, the depth cutoff is smooth and fixed. The factor `e^{-d_rho}chi(d_rho)` is uniformly bounded, and the corresponding `R`-depth is only `O(log J)`. If the critical layer were allowed to widen so far that its upper depth left Bellotti's local range, the `O(J)` estimate in (16) would have to be re-proved.

Second, smoothness of the shell is essential for (11). A hard moving ordinate cutoff introduces boundary jumps and destroys the uniform derivative argument in this form. The result applies to the full smooth source current used in `NB-243`/`NB-246`.

Third, (17) controls the **demodulated** envelope. The raw current has derivative of size `X/H=YJ` in the scaled coordinate because of its irrelevant common carrier. Since modulus is invariant under that modulation, demodulation is mandatory before applying the Lipschitz argument.

Fourth, (26) is only a sufficient condition. It does not produce the local second moment. The matched packet (31)--(35), which is compatible with the same population information in the conservative regime, shows that Bellotti counting plus smoothness alone cannot make that mean `o(1)`.

Fifth, the argument stays source-side. It sharpens the analytic condition sufficient to kill the critical Ford residue but does not supply the independent destination bridge from Nyman--Beurling approximation error to that source current.

A decisive falsification would be an allowed sequence of frozen critical currents satisfying the same fixed-depth Bellotti weighted population law for which `|G(0)|` stays bounded below but the hard-box mean (20) tends to zero. Equations (10)--(17) exclude exactly that possibility: such a sequence would violate the uniform scaled derivative bound.

## Conclusion

The Schwartz tails in `NB-246` are not intrinsic to the actual Ford source. On the critical layer, Bellotti's weighted local zero count and the smooth shell imply that the demodulated current is uniformly Lipschitz on the scaled center variable. Therefore an order-one selected value occupies a definite amount of `L^2` mass inside one literal Ford-scale interval.

The live source theorem may consequently be stated in the cleaner form

\[
\boxed{
\sup_{t_0}
H\int_{t_0-A/H}^{t_0+A/H}
|\mathcal R_{t_0}(s)|^2ds
=o(1)
}
\]

for one fixed `A>0`, with the Ford depth marks and carrier phase kept intact. Proving that hard-window mean remains the unresolved arithmetic step; the gain here is that no infinite-tail observability estimate is any longer needed.