# NB-252 — Single-shell dilation renormalizes `J` and preserves the Ford packet obstruction

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + SCALE-COVARIANCE + LEGAL-DILATION-AUDIT + MATCHED-CONTROL + METHOD-BOUNDARY + NB-251-REFINEMENT + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-251` isolates a genuine mesoscopic opening: if one could keep the same Ford normalization and enlarge the available carrier band from its natural width `H` to

\[
W=B_JH,
\qquad B_J\to\infty,
\]

then the standard `NB-231` matched packet would no longer force a positive normalized carrier-energy floor. That calculation was deliberately a bandwidth-only audit; it did not claim that replacing `H` by `B_JH` inside the source is a legal realization of the enlarged band.

The simplest source-side attempt is now auditable exactly. Dilate the **single Mellin shell itself** from width `H` to

\[
H_B:=B_JH.
\]

A legal Ford rescaling cannot hold the old population parameter fixed, because

\[
J=\frac RH
\]

is part of the source/window geometry. The dilated shell has instead

\[
\boxed{
J_B:=\frac{R}{H_B}=\frac{J}{B_J}.
}
\]

Provided

\[
1\ll B_J\ll J,
\]

we still have `J_B -> infinity`. Rewriting the matched control in the new variables gives exactly the original fixed-width problem with `J` replaced by `J_B`: the legal carrier band is again only a fixed multiple of its **own** shell width `H_B`, a `Theta(J_B)` carrier-locked packet fits in its `1/H_B` height window, and its normalized band energy has the same positive limiting floor.

Equivalently, the Ford critical layer slides horizontally when the shell is dilated. If

\[
d:=X(1-\beta)-\log J,
\]

then the dilated depth coordinate is

\[
\boxed{
d_B:=X(1-\beta)-\log J_B=d+\log B_J.
}
\]

Old critical zeros therefore move to depth `d_B=log B_J+O(1)`, but the new critical layer `d_B=O(1)` corresponds to zeros with

\[
d=-\log B_J+O(1).
\]

As long as `J_B -> infinity`, this replacement layer remains compatible with the same conservative matched-control geometry used in `NB-231`: its physical horizontal depth is still `log J_B+O(1)` and tends to infinity.

Thus **changing `H` is not the source-forced super-`H` operation sought after `NB-251`**. Single-shell dilation is scale-covariant. To exploit the mesoscopic opening of `NB-251`, an operation must enlarge the carrier support relative to a *fixed* Ford localization scale and a *fixed* `J`, for example through a genuinely multi-carrier or multi-shell construction whose normalization is separately audited. Merely redefining the shell width cannot do it.

## 1. Separate the fixed-`J` bandwidth audit from a legal shell dilation

Use the Ford notation stabilized in `NB-230`--`NB-251`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty.
\tag{1}
\]

The legal shell in `NB-250` has a fixed profile

\[
\phi\in C_c^\infty((0,1)),
\qquad
\operatorname{supp}\phi\subset[a,b]\Subset(0,1),
\tag{2}
\]

and therefore samples physical carrier frequencies

\[
X+H[a,b].
\tag{3}
\]

`NB-251` asks a deliberately different question. It leaves `H`, `J`, the Ford coefficients and the `Theta(J)` matched packet fixed, but tests the same packet over the hypothetical frequencies

\[
X+B_JHu,
\qquad u\in[a,b].
\tag{4}
\]

For that fixed-`J` audit, the normalized matched-packet energy tends to zero exactly when `B_J -> infinity`. This identifies how much **extra carrier averaging** would defeat that particular packet if such averaging were available without changing the rest of the Ford interface.

A literal dilation of the source shell does not satisfy that premise. Put

\[
\boxed{
H_B:=B_JH.
}
\tag{5}
\]

Then the height localization, population budget and Ford normalization must all be recomputed from `H_B`. In particular,

\[
\boxed{
J_B:=\frac R{H_B}=\frac J{B_J}.
}
\tag{6}
\]

The regime relevant to a mesoscopic dilation is

\[
\boxed{
1\ll B_J\ll J,
}
\tag{7}
\]

so that both `B_J -> infinity` and `J_B -> infinity`.

The natural carrier band of the new shell is

\[
\boxed{
\mathcal B_B=[X+aH_B,X+bH_B].
}
\tag{8}
\]

Its physical width is indeed `Theta(B_JH)`, but relative to the **new** shell/window scale it is still only

\[
\boxed{
|\mathcal B_B|=\Theta(H_B).
}
\tag{9}
\]

That is the first scale-covariance identity. A one-shell dilation produces a wider band only by simultaneously replacing the localization scale by the same wider `H_B`.

## 2. The matched packet reappears with `J_B` points

Take the same carrier-locked geometry as in `NB-231` and `NB-251`, now normalized to the dilated shell. For fixed `q>=1` and sufficiently small fixed `delta>0`, put

\[
M_B:=\lfloor\delta J_B\rfloor,
\qquad
\gamma_j-t_0:=\frac{2\pi qj}{X},
\qquad
0\le j<M_B.
\tag{10}
\]

The carrier phases remain exactly aligned:

\[
e^{iX(\gamma_j-t_0)}=1.
\tag{11}
\]

The scaled ordinates seen by the new shell are

\[
\tau_{j,B}
:=H_B(\gamma_j-t_0)
=\frac{2\pi qjH_B}{X}.
\tag{12}
\]

Using `X=YR` and `H_B=R/J_B`,

\[
\boxed{
\tau_{j,B}
=\frac{2\pi qj}{YJ_B}.
}
\tag{13}
\]

Hence `j<M_B=Theta(J_B)` keeps the entire packet in a fixed bounded `tau`-window. Its physical vertical diameter is

\[
\operatorname{diam}_\gamma(\mathcal P_B)
\asymp
\frac{J_B}{X}
=\frac1{YH_B},
\tag{14}
\]

which is precisely the new `1/H_B` localization scale.

Now place the packet at one common bounded **new** Ford depth

\[
d_{B,*}=O(1).
\tag{15}
\]

Its common normalized coefficient is

\[
c_{B,*}:=e^{-r-d_{B,*}},
\tag{16}
\]

with the overall Ford factor `1/J_B`. Across the legal band (8), the packet exponential sum is therefore

\[
\begin{aligned}
Z_B(u)
&:=
\frac{c_{B,*}}{J_B}
\sum_{j=0}^{M_B-1}
 e^{i(X+uH_B)(\gamma_j-t_0)}\\
&=
\frac{c_{B,*}}{J_B}
\sum_{j=0}^{M_B-1}
\exp\!\left(
\frac{2\pi iqu}{YJ_B}j
\right).
\end{aligned}
\tag{17}
\]

Equation (17) is exactly `NB-251`'s fixed-band formula with its dilation parameter equal to `1` and with `J` replaced by `J_B`. There is no remaining `B_J` in the dimensionless carrier geometry.

Assume along a subsequence that

\[
Y\to Y_*\in(0,\infty),
\qquad
d_{B,*}\to d_*.
\tag{18}
\]

Since `M_B/J_B -> delta`, the Riemann-sum limit gives

\[
Z_B(u)
\longrightarrow
c_*
\int_0^\delta
 e^{2\pi iqux/Y_*}\,dx,
\tag{19}
\]

uniformly for `u` in `[a,b]`. The limit is analytic and not identically zero. Therefore, for every fixed nonzero shell profile `phi`,

\[
\boxed{
\int_a^b
|\phi(u)|^2|Z_B(u)|^2\,du
\longrightarrow
|c_*|^2
\int_a^b
|\phi(u)|^2
\left|
\int_0^\delta e^{2\pi iqux/Y_*}\,dx
\right|^2du
>0.
}
\tag{20}
\]

So the legal dilated shell remains on the **positive-floor side** of the matched-packet criterion. The factor `B_J -> infinity` that killed the fixed-`J` packet in `NB-251` has been absorbed completely by the forced replacement `J -> J_B=J/B_J`.

## 3. The Ford critical layer slides by `log B_J`

The same covariance appears horizontally. The original depth coordinate is

\[
d:=X(1-\beta)-\log J.
\tag{21}
\]

For the dilated shell,

\[
d_B:=X(1-\beta)-\log J_B.
\tag{22}
\]

Using (6),

\[
\boxed{
d_B=d+\log B_J.
}
\tag{23}
\]

This identity explains why looking only at the old critical packet can give the wrong impression. If an old-layer zero has

\[
d=d_*+O(1),
\tag{24}
\]

then after dilation

\[
d_B=d_*+\log B_J+O(1).
\tag{25}
\]

Its individual normalized coefficient is nevertheless invariant:

\[
\boxed{
\frac{e^{-r-d_B}}{J_B}
=
\frac{e^{-r-d}}J.
}
\tag{26}
\]

Indeed, `e^{-d_B}=B_J^{-1}e^{-d}` while `J_B^{-1}=B_JJ^{-1}`. What changes is the height window: only `Theta(J_B)=Theta(J/B_J)` carrier cells fit after dilation, so retaining only the old horizontal layer would reduce the possible coherent mass.

But the Ford obstruction is not tied to the old coordinate. The **new** critical layer is

\[
d_B=O(1),
\tag{27}
\]

which by (23) means

\[
\boxed{
d=-\log B_J+O(1).
}
\tag{28}
\]

Equivalently,

\[
X(1-\beta)
=\log J_B+O(1).
\tag{29}
\]

Thus the critical packet simply slides closer to `Re(s)=1` as the shell is widened. At that new layer, every point carries size `Theta(1/J_B)`, there are `Theta(J_B)` available carrier cells in the new height window, and the coherent normalized contribution is again `Theta(1)`.

This sliding remains inside the conservative abstract matched-control regime whenever

\[
J_B\to\infty.
\tag{30}
\]

In particular, under the `NB-231` restriction `J<=log Q`, one also has `J_B<=log Q`, while

\[
X(1-\beta)\asymp\log J_B\to\infty.
\tag{31}
\]

So the zero-free-region input used in the earlier controls does not by itself exclude the replacement layer; nor does the already-audited local population geometry distinguish the rescaled packet. This is a matched **compatibility control**, not a claim that actual zeta zeros realize the packet.

## 4. What single-shell dilation can and cannot buy

The distinction with `NB-251` is now exact. Its bandwidth audit keeps the old Ford interface fixed and asks what would happen if one somehow acquired

\[
H\ll W=B_JH\ll X
\tag{32}
\]

without changing `H`, `J`, the depth mark or the selected-height window. Under that hypothesis, the matched packet ceases to obstruct once `B_J -> infinity`.

A one-shell dilation does something else:

\[
H\mapsto H_B=B_JH,
\qquad
J\mapsto J_B=J/B_J,
\qquad
d\mapsto d_B=d+\log B_J.
\tag{33}
\]

Its frequency width obeys

\[
W_B\asymp H_B,
\tag{34}
\]

so in the variables of its own Ford problem

\[
\boxed{
\frac{W_B}{H_B}=\Theta(1).
}
\tag{35}
\]

The operation never reaches the `W/H -> infinity` side of `NB-251`; it simply moves to a different Ford window.

This rules out several superficially different but equivalent maneuvers. Replacing `phi((u-X)/H)` by a fixed-shape profile dilated to width `B_JH`, declaring `B_JH` to be the new smoothing scale, or re-running the same one-shell explicit-formula argument with a broader support all undergo the renormalization (33). None creates independent carrier averaging at fixed Ford localization.

There is still a real escape. A source construction could keep the original `H` and `J` while producing several separated `H`-scale carrier pieces whose union spans `B_JH` with `B_J -> infinity`. Such a **multi-carrier** construction would not be equivalent to the single-shell dilation audited here. It would have to prove, rather than assume, that the pieces preserve the same Ford depth coefficients, selected-height localization, source normalization and Hardy-projection order. `NB-252` does not rule that out; it isolates it as the genuinely new architecture required to exploit the mesoscopic opening.

## 5. Adversarial checks and evidence boundary

The calculation does not prove that actual zeta zeros form the rescaled packet. As in `NB-231` and `NB-251`, the packet is a matched control showing what the presently audited source/population information fails to exclude. The conclusion is a **method boundary for one-shell source dilation**, not a zero theorem.

The assumption `B_J=o(J)` is essential to this statement. If `B_J` is comparable to `J`, then `J_B=O(1)` and the growing Ford-window asymptotic exits the regime used by the line. Such a macroscopic dilation is not evidence for a successful mesoscopic construction; it is a different scaling problem and would require a fresh derivation.

Nor may one keep the old `J` by fiat after replacing the physical shell width by `H_B`. Doing so reproduces the hypothetical fixed-`J` audit of `NB-251`; it is precisely the step whose source legality is under investigation. In the Ford scaling used throughout `NB-230`--`NB-251`, `J=R/H` is definitional, so a literal one-shell change of `H` forces (6).

The horizontal shift (28) is also not claimed to be harmless for every conceivable stronger zeta input. A future theorem could forbid coherent packets specifically at the new layer. The point is narrower: the zero-free, density and local-population constraints already used to validate the matched control remain compatible as long as `J_B -> infinity`, so those inputs do not make single-shell dilation a source-forced cure.

Finally, the positive energy in (20) concerns the same sufficient carrier-band norm audited in `NB-250`--`NB-251`. The exact hard-box quadratic form could contain additional cancellation. Nothing here upgrades the sufficient form factor to a necessary condition or closes the Nyman--Beurling distance bridge.

## 6. Prior-art audit and next route

A fresh literature check again finds the relevant external harmonic-analysis machinery to be classical. Montgomery--Vaughan separated-frequency mean-square estimates explain the hypothetical super-`H` gain in `NB-251`, while the September 2026 short-interval pair-correlation theorem of Biao Wang (arXiv:2609.07918) concerns zeta-zero pair statistics in short intervals. Neither supplies a source operation that decouples Mellin carrier width from the Ford height scale. No new external theorem is load-bearing in (6), (23) or (20), so no new durable source entry is required.

The line-local delta is the scale covariance:

\[
\boxed{
H\mapsto B_JH
\quad\Longrightarrow\quad
J\mapsto J/B_J,
\quad
\text{and the legal matched-packet problem returns to }W/H=\Theta(1).
}
\tag{36}
\]

Therefore the mesoscopic possibility opened by `NB-251` survives, but it is narrower than “choose a broader shell.” The next useful source-side question is whether one can construct a **multi-carrier family at fixed `H` and fixed `J`** whose total physical support satisfies

\[
H\ll W\ll X
\tag{37}
\]

while retaining a common Ford depth mark and selected-height localization. If every such construction necessarily changes the normalization or height window, that would close the bandwidth route; if one survives the audit, it would provide the first genuinely legal mechanism capable of using the `NB-251` crossover.