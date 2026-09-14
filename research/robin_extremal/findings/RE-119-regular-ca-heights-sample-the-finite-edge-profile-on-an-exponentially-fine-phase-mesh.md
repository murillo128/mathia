# RE-119 — regular CA heights sample the finite-edge profile on an exponentially fine phase mesh

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + GLOBAL-REGULAR-CA-PROJECTION + DENSE-PHASE-SAMPLING + EDGE-SCALE-OSCILLATION + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED`.

Assume RH is false with a finite attained zero edge

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
c:=1-\Theta\in(0,1/2),
\tag{1}
\]

and retain the actual edge profiles from `RE-113`--`RE-118`,

\[
F(u)=F_\Theta(u),
\qquad
G(u)=G_\Theta(u),
\qquad
J(u):=F(u)+G(u).
\tag{2}
\]

The recent finite-edge analysis selected special adaptive maxima and then showed that their endpoint, recovery and block-maximality constraints all collapse to the same stable-filter state `J`. A remaining interpretation was that the **arithmetic placement of the actual CA states inside the compatible spectral windows** might already be a leading-order obstruction.

At the edge scale it is not. The stable profile is in fact the uniform pointwise asymptotic for **every sufficiently large regular colossally abundant state**, without first selecting an adaptive witness or a block maximum.

Let `C` be any sufficiently large regular CA state, and put

\[
Y:=\log C,
\qquad
u:=\log Y,
\qquad
h(C):=\log\frac{\sigma(C)}{C\log\log C}-\gamma.
\tag{3}
\]

Then, uniformly over all such regular CA states,

\[
\boxed{
Y^c\nu\,h(C)=J(\nu)+o(1).
}
\tag{4}
\]

Equivalently, for the edge-normalized Robin functional of `RE-115`--`RE-118`,

\[
B_\Theta(C)
:=Y^c\nu\,\bigl(e^{h(C)}-1\bigr),
\tag{5}
\]

one has the global regular-CA projection

\[
\boxed{
B_\Theta(C)=J(\nu)+o(1)
}
\tag{6}
\]

with a remainder uniform as `C->infinity` through regular CA states.

The regular CA phase set is much finer than every inverse power of `nu`. If `nu_-<nu_+` are consecutive regular-state phases across one event group at physical scale `Y=e^nu`, then the event-mass bound already used in `RE-117` gives

\[
\boxed{
\nu_+-\nu_-
=O\!\left(Y^{-1/2}(\log Y)^{3/2}\right)
=O\!\left(e^{-\nu/2}\nu^{3/2}\right).
}
\tag{7}
\]

In particular, for every fixed `A>0`,

\[
\boxed{
\nu_+-\nu_-=o(\nu^{-A}).
}
\tag{8}
\]

Consequently, for every fixed `L>0`, uniformly as `U->infinity`,

\[
\boxed{
\sup_{\substack{C\ \mathrm{regular\ CA}\\ U\le\log\log C\le U+L}}
B_\Theta(C)
=
\sup_{0\le t\le L}J(U+t)+o(1),
}
\tag{9}
\]

and likewise

\[
\boxed{
\inf_{\substack{C\ \mathrm{regular\ CA}\\ U\le\log\log C\le U+L}}
B_\Theta(C)
=
\inf_{0\le t\le L}J(U+t)+o(1).
}
\tag{10}
\]

Since `J` is a nonzero real uniformly almost-periodic function of zero Bohr mean (`RE-114`), it has positive and negative sign-margin phases with bounded gaps. Equations (6)--(8) force the actual regular CA sequence to sample both kinds of phases. Thus there are constants `m>0` and `L<infinity` such that every sufficiently late phase interval `[U,U+L]` contains regular CA states `C_+` and `C_-` satisfying

\[
\boxed{
 h(C_+)\ge
 m\frac{(\log C_+)^{\Theta-1}}{\log\log C_+},
\qquad
 h(C_-)\le
 -m\frac{(\log C_-)^{\Theta-1}}{\log\log C_-}.
}
\tag{11}
\]

Hence an attained off-critical edge does more than supply Robin's classical `Omega_+((log n)^(-b))` CA excursions for every fixed `b>1-Theta`: the full regular CA staircase itself has **two-sided, syndetic-in-`log log C` excursions at the natural edge scale** `(log C)^(Theta-1)/log log C`.

The research consequence is negative but sharper than the frontier after `RE-118`: at leading edge order there is no sparse arithmetic-placement problem to solve. The actual regular CA phases form an exponentially fine mesh and their normalized heights uniformly read out the same `J`. Any finite-edge contradiction must therefore act on the lower-order remainder in (6), on a source coordinate not contained in `J`, or on a selection property whose resolution is genuinely finer than `o(1)` after edge normalization.

## 1. Every regular CA state has an exact selector parameter

Let `C` be regular. By the CA event construction used throughout the line, there is an open event chamber and hence a parameter `Z` in that chamber for which the selected exponent vector is exactly that of `C`. With the event staircase `Phi`,

\[
\boxed{Y=\Phi(Z).}
\tag{12}
\]

Because `Z` is not an event coordinate, left and right conventions coincide there. The uniform extreme-face expansion of `RE-113` therefore gives

\[
Z-Y
=Z^\Theta\bigl(F(\log Z)+r_\Phi(Z)\bigr),
\qquad
\sup_{x\ge X}|r_\Phi(x)|\longrightarrow0.
\tag{13}
\]

Since `F` is bounded and `Theta<1`,

\[
\frac{Z-Y}{Z}=O(Z^{-c}),
\qquad
\frac YZ\to1,
\qquad
\log Y-\log Z=O(Z^{-c})
\tag{14}
\]

uniformly over regular states. The sign of `Z-Y` is unrestricted here; unlike the adaptive witnesses of `RE-113`--`RE-115`, a generic regular CA state need not lie on a positive selector ray.

The important point is that no extremal choice inside the CA sequence has entered. Equation (12) is simply the exact exponent-threshold encoding of a regular CA state.

## 2. The Euler-product height adds the two edge coordinates into `J`

For a regular CA selector, the exact Euler-product accounting used in `RE-034` and recalled in `RE-115` is

\[
 h(C)
 =E(Z)-\delta_\ell(Z)-T(C)
 +\log\frac{\log Z}{\log Y},
\tag{15}
\]

where

\[
E(Z)
=\sum_{p\le Z}-\log(1-p^{-1})-\gamma-\log\log Z,
\tag{16}
\]

and uniformly

\[
\delta_\ell(Z)=O(Z^{-1}),
\qquad
T(C)=O(Z^{-1/2}).
\tag{17}
\]

`RE-114` supplies the matching reciprocal edge projection

\[
E(Z)
=\frac{Z^{-c}}{\log Z}
\bigl(G(\log Z)+r_E(Z)\bigr),
\qquad
\sup_{x\ge X}|r_E(x)|\longrightarrow0.
\tag{18}
\]

Write

\[
\delta_Z:=\frac{Z-Y}{Z}
=Z^{-c}\bigl(F(\log Z)+o(1)\bigr).
\tag{19}
\]

Then

\[
\log Y
=\log Z+\log(1-\delta_Z)
=\log Z-\delta_Z+O(\delta_Z^2),
\tag{20}
\]

so

\[
\log\frac{\log Z}{\log Y}
=\frac{\delta_Z}{\log Z}
+O\!\left(\frac{\delta_Z^2}{\log Z}
+\frac{\delta_Z^2}{(\log Z)^2}\right).
\tag{21}
\]

Multiplying by `Z^c log Z`, equations (19)--(21) give

\[
\boxed{
Z^c\log Z
\log\frac{\log Z}{\log Y}
=F(\log Z)+o(1).
}
\tag{22}
\]

The finite-exponent tail and boundary correction disappear at this scale because `c<1/2`:

\[
Z^c\log Z\,T(C)
=O(Z^{c-1/2}\log Z)=o(1),
\tag{23}
\]

\[
Z^c\log Z\,\delta_\ell(Z)
=O(Z^{c-1}\log Z)=o(1).
\tag{24}
\]

Combining (15), (18), and (22)--(24) yields

\[
Z^c\log Z\,h(C)
=F(\log Z)+G(\log Z)+o(1)
=J(\log Z)+o(1).
\tag{25}
\]

Now (14), boundedness of `J`, and uniform continuity of its absolutely convergent edge series let us replace `Z` by `Y` in both the normalization and phase. This proves (4) uniformly.

This calculation also explains why the stable filter kept reappearing in `RE-114`--`RE-118`. It is not only the coordinate selected by the adaptive ray or the macroscopic recovery convolution: after complete Euler-product normalization it is the **pointwise leading edge profile of the whole regular CA staircase**.

## 3. The exponential map does not change the edge profile

Equation (4) and boundedness of `J` imply

\[
h(C)=O\!\left(\frac{Y^{-c}}{\log Y}\right)
\tag{26}
\]

uniformly on regular CA states. Hence

\[
e^{h(C)}-1=h(C)+O(h(C)^2).
\tag{27}
\]

The normalized quadratic remainder satisfies

\[
Y^c\log Y\,h(C)^2
=O\!\left(\frac{Y^{-c}}{\log Y}\right)
=o(1).
\tag{28}
\]

Therefore (4) immediately gives (6).

This pointwise formula is consistent with the corridor formula of `RE-118`. There, relative normalization at a starting phase `U` produced the known weight `(U+t)/U`; on a fixed phase corridor that factor is `1+O(1/U)` and was below the available `o(1)` projection error. Equation (6) identifies the more intrinsic pointwise normalization but does **not** claim an `o(1/U)` remainder. In particular it does not retroactively justify multiplying the `o(1)` errors of `RE-118` by `U`.

That boundary is essential: the new result removes leading-order placement as an obstruction, but it does not yet determine the first lower-order correction that could move a discrete block maximizer inside a nearly degenerate `J` lobe.

## 4. Regular CA phases form an exponentially fine mesh

Consider one event group at coordinate `eta`, with physical left mass

\[
x:=\Phi(\eta^-)
\tag{29}
\]

and total jump mass `m_e`. The regular state in the chamber immediately before the group has logarithmic size `x`, and the regular state in the chamber immediately after has logarithmic size `x+m_e`.

`RE-117` bounds the total higher-layer mass below a fixed multiple of the physical scale by

\[
O\!\left(x^{1/2}(\log x)^{3/2}\right),
\tag{30}
\]

while a first-layer contribution is `O(log x)`. Therefore every individual simultaneous group satisfies, uniformly,

\[
\boxed{
 m_e
 =O\!\left(x^{1/2}(\log x)^{3/2}\right).
}
\tag{31}
\]

This bound is deliberately insensitive to unresolved two-prime CA ties; no Four-Exponentials input is needed. Since `m_e=o(x)`, the corresponding phase jump is

\[
\begin{aligned}
\Delta\nu
&=\log(x+m_e)-\log x\\
&=O(m_e/x)\\
&=O\!\left(x^{-1/2}(\log x)^{3/2}\right).
\end{aligned}
\tag{32}
\]

Writing `x=e^nu` gives (7), hence (8).

On a fixed phase interval `[U,U+L]`, the physical logarithmic-size range has length comparable with `e^U`, while each jump is at most `O(e^{U/2}U^{3/2})`. Thus the interval contains at least

\[
\gg_L \frac{e^{U/2}}{U^{3/2}}
\tag{33}
\]

regular CA chambers for all large `U`. The exact count is unimportant; the decisive fact is that the phase mesh tends to zero exponentially fast, whereas every correction considered in `RE-115`--`RE-118` varies only on inverse-logarithmic or fixed phase scales.

## 5. Dense sampling transfers the whole leading profile to the CA sequence

Fix `L>0`. From (6),

\[
\sup_{\substack{C\ \mathrm{regular\ CA}\\ U\le\log\log C\le U+L}}
|B_\Theta(C)-J(\log\log C)|
\longrightarrow0.
\tag{34}
\]

The phase mesh bound (7) and uniform continuity of `J` imply that the regular CA phases in `[U,U+L]` are an `o(1)`-net. Hence their sampled supremum and infimum of `J` converge to the continuous supremum and infimum on the whole interval. Combining this with (34) proves (9)--(10).

`RE-114` proves that `J` is nonzero, real, uniformly almost periodic, and has zero Bohr mean. Therefore it takes both signs. Choose one phase with `J>0` and one with `J<0`; uniform almost periodicity makes sufficiently small translates of those sign-margin neighborhoods relatively dense. Consequently there are constants `a>0`, `L_0<infinity`, and fixed-width intervals with bounded gaps on which respectively

\[
J\ge 2a
\qquad\text{and}\qquad
J\le-2a.
\tag{35}
\]

For sufficiently late translates, the exponentially fine CA mesh puts a regular state inside each such interval, while (34) changes the normalized height by less than `a`. Thus those states satisfy

\[
B_\Theta(C_+)\ge a,
\qquad
B_\Theta(C_-)\le-a.
\tag{36}
\]

Since `h(C)=o(1)` uniformly, (36) is equivalent after reducing `a` by an absolute factor to (11).

This is stronger than merely saying that compatible spectral phases exist. The **actual regular CA staircase necessarily samples them** at leading edge resolution.

## 6. Stress tests and representation boundary

Several stronger readings would be invalid.

First, (6) is an `o(1)` normalized asymptotic, not an asymptotic expansion through order `1/nu`. The unknown remainder can dominate the deterministic `1/nu` drift used in the moving-ray equations of `RE-115`--`RE-118`. Thus (6) does not locate a block maximizer to `o(1/nu)`, determine a second-derivative sign, or identify which of several nearly equal lobe maxima the discrete CA functional chooses.

Second, the mesh theorem removes **sampling sparsity**, not arithmetic information. The CA points are not replaced by an arbitrary grid: their lower-order height remainder still comes from the exact prime-exponent staircase. A contradiction may therefore live entirely in

\[
\mathcal R(C)
:=B_\Theta(C)-J(\log\log C),
\qquad
\mathcal R(C)=o(1),
\tag{37}
\]

provided one can expose sign, correlation, or rigidity at the finer scale required by the selector. The present theorem says only that no obstruction depending on a fixed positive separation in the leading `J` profile can distinguish the actual CA sequence from the spectral model.

Third, the result is conditional on a finite attained edge. If the supremum `Theta` is not attained, the edge profile is empty and the same normalization gives only an `o(1)` statement; `RE-113` already treats the near-minimal recovery consequence of that branch. If `Theta=1`, the stable filter used here loses its positive exponential decay and the argument does not apply.

Finally, regularity is used only to choose `Z` in an open selector chamber so that (12) and the exact Euler-product accounting apply without a boundary convention. Singular CA states at simultaneous-event parameters are not needed for the dense sampling or the two-sided excursion conclusion because every event group is bracketed by regular chambers.

## 7. Prior-art and novelty boundary

The ingredients are individually classical or already anchored in the line. Alaoglu--Erdos provides the CA exponent-threshold structure; Robin proves the false-RH CA excursion theorem; explicit formulas organize prime errors by zeta zeros; Mertens-product zero coefficients and almost-periodic recurrence are classical; Kalyabin's 2026 work gives a sharp unconditional relation between modified Mertens remainders and maximal Gronwall values at fixed greatest prime; Zimov studies consecutive-CA Robin-ratio changes; and Mantovanelli develops the exact prime-layer event sweep and workload.

The current literature audit found no source stating the specific uniform **attained-edge pointwise profile** (4)--(6) for every regular CA state, nor the consequence that the regular CA phase mesh transfers the continuous stable-filter extrema back to actual CA values as in (9)--(11). No new external theorem is load-bearing: the proof is a splice of the line's already-audited edge projections (`RE-113`, `RE-114`), exact CA Euler-product accounting (`RE-034`, `RE-115`), and event-mass control (`RE-117`). Therefore `SOURCES.md` requires no new anchor.

Novelty should be understood narrowly. The claim is not that zeta-zero oscillations or false-RH Robin violations are new. The line-specific delta is that, once the finite attained edge is projected exactly, **the complete regular CA staircase itself becomes a dense sampler of one stable profile `J` at the full edge scale**. This removes a leading-order selector-placement escape that remained after `RE-118` and isolates the genuinely finer remainder (37) as the next source-specific object.

## 8. Consequence for the research line

The attained finite-edge branch can now be organized more sharply:

\[
\boxed{
\text{regular CA height at edge scale}
=J(\log\log C)+o(1),
}
\tag{38}
\]

and the sample mesh is exponentially finer than every inverse power of `log log C`. The adaptive rays, first-recovery lobes, and block-maximality packets of `RE-114`--`RE-118` are therefore special constraints imposed on a staircase whose **entire leading height field is already known**.

A useful next theorem should not ask whether actual CA states enter favorable `J` windows: they necessarily do. It should instead expose the first nonvanishing term of `mathcal R(C)`, prove a source-specific restriction on that remainder along block maxima or recovery endpoints, or identify another coordinate not reconstructible from `J`. Any candidate whose conclusion is stable under an arbitrary `o(1)` perturbation of the normalized height is already defeated by (6)--(11).