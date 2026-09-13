# FD-098 — uniform short-interval cancellation thickens source-head descent by a logarithmic corridor

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-HEAD-CORRIDOR + UNIFORM-SHORT-INTERVAL-MOBIUS + LOG-ENLARGED-PHYSICAL-DESCENT + SHARP-OCCUPIED-BOUNDED-DEFECT-BLOCK + MATCHED-REGULARITY-BARRIER + NO-RH-CONTRADICTION`.

`FD-097` leaves one scale-sensitive obstruction after projective certificate loss has been reduced to an exponential-in-depth factor: an all-head chain can keep repairing the dyadic source atom while making only additive progress of order the current source amplitude. The one-Lipschitz repair in `FD-095` gives a protected backward step of order

\[
A_X:=|\mathcal H(X)|,
\]

so at a false-RH frontier record `A_X=X^{\Theta+o(1)}` with `\Theta<1` the guaranteed retreat is submacroscopic.

The physical source has more regularity than one-Lipschitz. `FD-048`, using Matomäki--Teräväinen's all-short-interval Möbius theorem, proves that for every fixed

\[
\beta>\frac{11}{20},
\qquad
0<\kappa<\frac13,
\]

one has

\[
\boxed{
|\mathcal H(x+h)-\mathcal H(x)|
\ll_{\beta,\kappa}
\frac{h}{(\log x)^\kappa}
\qquad
(x^\beta\le h\le x).
}
\tag{1}
\]

Combining (1) with the slow-doubling source records of `FD-096` gives a quantitative upgrade of the live head mechanism.

Assume

\[
\boxed{
\frac{11}{20}<\Theta<1.
}
\tag{2}
\]

Fix

\[
\frac12<\sigma<\Theta,
\qquad
\frac{11}{20}<\beta<\Theta,
\qquad
0<\kappa<\frac13.
\tag{3}
\]

Then there are infinitely many strict normalized source records `X` from `FD-096` for which, writing

\[
A:=|\mathcal H(X)|=X^{\Theta+o(1)},
\tag{4}
\]

and

\[
\mathcal P_\sigma(T)
:=
\max_{1\le n\le T}
\frac{|\mathcal H(n)|}{n^\sigma},
\tag{5}
\]

we have the fixed slow-doubling bound

\[
\mathcal P_\sigma(2X)\le K\mathcal P_\sigma(X)
=K\frac{A}{X^\sigma}
\tag{6}
\]

with an absolute fixed choice such as `K=2`.

For every such record there is a constant `c=c(\beta,\kappa)>0` such that, with

\[
L_X:=\left\lfloor
cA(\log X)^\kappa
\right\rfloor,
\tag{7}
\]

we have the **uniform backward source corridor**

\[
\boxed{
|\mathcal H(X-d)|\ge\frac A2
\qquad
(0\le d\le L_X).
}
\tag{8}
\]

Moreover every four-adic horizon in that corridor,

\[
C_d:=4(X-d),
\qquad 0\le d\le L_X,
\tag{9}
\]

is simultaneously frontier-sharp, has fixed nonsquarefree occupation, and has bounded normalized-energy record defect. More precisely, with

\[
E_{N,1}
=
\sum_{1<r\le N}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)^2,
\tag{10}
\]

\[
U_{N,1}
=
\sum_{\substack{1<r\le N\\ \mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)^2,
\tag{11}
\]

\[
F_\sigma(N):=\frac{E_{N,1}}{N^{2\sigma}},
\qquad
P_\sigma^{E}(N):=\max_{1\le M\le N}F_\sigma(M),
\qquad
\mathfrak R_\sigma(N):=
\frac{P_\sigma^{E}(N)}{F_\sigma(N)},
\tag{12}
\]

there are constants `c_{\sigma,K}>0` and `C_{\sigma,K}<\infty`, independent of `X` and `d`, such that

\[
\boxed{
E_{C_d,1}=C_d^{2\Theta+o(1)},
\qquad
\frac{U_{C_d,1}}{E_{C_d,1}}
\ge c_{\sigma,K},
\qquad
\mathfrak R_\sigma(C_d)
\le C_{\sigma,K}.
}
\tag{13}
\]

Thus the `FD-096` entry state is not isolated. Above the uniform-short-interval threshold `11/20`, every slow-doubling source record produces a backward block of good physical states whose length is larger than the one-Lipschitz block by the explicit factor

\[
\boxed{(\log X)^\kappa,\qquad \kappa<1/3.}
\tag{14}
\]

In particular, if the predecessor decomposition lands in the source-head branch at the entry horizon `H=4X`, the repair need not use the `h\asymp A` backstep from `FD-095`. It may jump directly to the far end of the corridor and obtain

\[
\boxed{
H-C_{L_X}
=4L_X
\asymp
A(\log X)^\kappa
=X^{\Theta+o(1)}(\log X)^\kappa.
}
\tag{15}
\]

This is a genuine source-specific improvement of the all-head descent guarantee. It still does **not** change the polynomial scale. Since `\Theta<1`,

\[
\boxed{
\frac{L_X}{X}
=
X^{\Theta-1+o(1)}(\log X)^\kappa
\longrightarrow0.
}
\tag{16}
\]

So the presently available uniform short-interval arithmetic enlarges the protected head retreat by a logarithm, but still does not force a fixed-factor contraction or an infinite descent. A successful scale theorem must therefore either force sufficiently many non-head multiplicative contractions, prove a genuine source-refueling statement beyond the corridor (new large source mass before the current protected block is exhausted), or use arithmetic structure of the exact coefficients stronger than the aggregate endpoint estimate (1).

The threshold matters. If `1/2<\Theta\le11/20`, the source amplitude `X^{\Theta+o(1)}` lies below the range in which the current all-interval Möbius theorem is available, and this argument gives no improvement over the one-Lipschitz amplitude corridor. At the other endpoint `\Theta=1`, equation (16) is unavailable and the present finding makes no submacroscopic claim.

## 1. A slow-doubling source record controls every quotient seen below `4X`

Take one of the infinitely many records supplied by `FD-096` and retain notation (4)--(6). For every integer `y\le2X`, (6) gives

\[
\frac{|\mathcal H(y)|}{y^\sigma}
\le
\mathcal P_\sigma(2X)
\le
K\frac{A}{X^\sigma},
\]

hence

\[
\boxed{
|\mathcal H(y)|
\le
KA\left(\frac yX\right)^\sigma.
}
\tag{17}
\]

If `N\le4X` and `r\ge2`, then

\[
\left\lfloor\frac Nr\right\rfloor\le2X,
\tag{18}
\]

so (17) applies to every source value appearing in the complete energy `E_(N,1)`. Put

\[
S_\sigma
:=
\sum_{r=2}^{\infty}
\frac{J_2(r)}{r^{2+2\sigma}}.
\tag{19}
\]

Because `J_2(r)/r^2\le1` and `2\sigma>1`, this series converges. From (17),

\[
\begin{aligned}
E_{N,1}
&\le
K^2A^2
\sum_{2\le r\le N}
\frac{J_2(r)}{r^2}
\left(\frac{N}{rX}\right)^{2\sigma}\\
&\le
K^2S_\sigma A^2
\left(\frac NX\right)^{2\sigma}.
\end{aligned}
\tag{20}
\]

Therefore throughout the whole range `N\le4X`,

\[
\boxed{
F_\sigma(N)
\le
K^2S_\sigma\frac{A^2}{X^{2\sigma}}.
}
\tag{21}
\]

This is exactly the historical denominator control that `FD-094`--`FD-097` need. Once we prove that a candidate child `C` still has one fixed nonsquarefree row carrying `\asymp A^2` energy, both fixed occupation and bounded defect follow with no further record argument at the child scale.

## 2. Uniform Möbius cancellation protects the record for `A log^kappa X` backwards

Choose `\beta` and `\kappa` as in (3). By `FD-048`, there is a constant `B_{\beta,\kappa}` such that for all sufficiently large `x` and all `h` in the range `x^\beta\le h\le x`,

\[
|\mathcal H(x+h)-\mathcal H(x)|
\le
B_{\beta,\kappa}
\frac{h}{(\log x)^\kappa}.
\tag{22}
\]

Since `A=X^{\Theta+o(1)}` and `\beta<\Theta`,

\[
X^\beta=o(A).
\tag{23}
\]

Choose a fixed `c>0` small enough that, for large `X`,

\[
2B_{\beta,\kappa}c\le\frac14.
\tag{24}
\]

Because `\Theta<1`, equation (7) gives `L_X=o(X)`. Fix `0\le d\le L_X` and put `Y=X-d`.

If `d<X^\beta`, the exact one-Lipschitz law from `FD-033` gives

\[
|\mathcal H(X)-\mathcal H(Y)|
\le d
\le X^\beta
=o(A).
\tag{25}
\]

If instead `d\ge X^\beta`, then `Y\sim X` and

\[
d\ge X^\beta\ge Y^\beta.
\tag{26}
\]

Apply (22) with starting point `Y` and interval length `d`. Since `\log Y\sim\log X`,

\[
\begin{aligned}
|\mathcal H(X)-\mathcal H(Y)|
&\le
2B_{\beta,\kappa}
\frac{d}{(\log X)^\kappa}\\
&\le
2B_{\beta,\kappa}cA
\le\frac A4.
\end{aligned}
\tag{27}
\]

Equations (25)--(27) imply, uniformly for the entire interval `0\le d\le L_X`,

\[
|\mathcal H(X-d)|
\ge
A-|\mathcal H(X)-\mathcal H(X-d)|
\ge
\frac A2
\tag{28}
\]

for sufficiently large records. This proves (8).

The distinction from `FD-073` and `FD-095` is quantitative. One-Lipschitz continuity alone certifies a fixed fraction of a spike only for backward distance `O(A)`. The physical all-short-interval theorem certifies it uniformly for the longer scale

\[
A(\log X)^\kappa,
\qquad \kappa<1/3,
\tag{29}
\]

whenever the frontier amplitude is itself above the `X^(11/20+)` applicability threshold.

## 3. Every point in the corridor is sharp, occupied, and bounded-defect

Fix `d\le L_X`, put `Y=X-d` and `C=4Y`. The row `r=4` is nonsquarefree and samples `Y` exactly:

\[
\left\lfloor\frac C4\right\rfloor=Y,
\qquad
\frac{J_2(4)}{4^2}=rac34.
\tag{30}
\]

Using (8),

\[
\boxed{
U_{C,1}
\ge
\frac34|\mathcal H(Y)|^2
\ge
\frac{3}{16}A^2.
}
\tag{31}
\]

On the other hand, (20) gives

\[
E_{C,1}
\le
K^2S_\sigma A^2
\left(\frac CX\right)^{2\sigma}
\le
K^2S_\sigma4^{2\sigma}A^2.
\tag{32}
\]

Therefore

\[
\boxed{
\frac{U_{C,1}}{E_{C,1}}
\ge
\frac{3}
{16K^2S_\sigma4^{2\sigma}}
=:c_{\sigma,K}>0.
}
\tag{33}
\]

For the record defect, (21) gives

\[
P_\sigma^{E}(C)
\le
K^2S_\sigma\frac{A^2}{X^{2\sigma}}.
\tag{34}
\]

Equation (31) gives

\[
F_\sigma(C)
\ge
\frac{3A^2}{16C^{2\sigma}}
\ge
\frac{3A^2}
{16(4X)^{2\sigma}}.
\tag{35}
\]

Hence

\[
\boxed{
\mathfrak R_\sigma(C)
\le
\frac{16}{3}K^2S_\sigma4^{2\sigma}
=:C_{\sigma,K}<\infty.
}
\tag{36}
\]

Finally (31)--(32), together with `A=X^(Theta+o(1))` and `C=4X(1-o(1))`, give

\[
E_{C,1}=C^{2\Theta+o(1)}.
\tag{37}
\]

This proves (13). Notice that no new predecessor pigeonhole is required anywhere inside the corridor: the same source record and its slow-doubling envelope pay the complete denominator history for every child simultaneously.

## 4. Consequence for the live all-head obstruction

At the `FD-096` entry horizon `H=4X`, the source-head coordinate is exactly `X`. In the head branch, the geometric repair used by `FD-095` replaces `X` by a smaller source argument `Y` and reembeds it as the nonsquarefree row `r=4` of the new horizon `C=4Y`.

The original proof took `X-Y` to be a fixed fraction of `A`, because one-Lipschitz continuity was the only input used to keep `|mathcal H(Y)|` comparable with `A`. Equation (8) allows the same exact four-adic reembedding with

\[
X-Y=L_X\asymp A(\log X)^\kappa.
\tag{38}
\]

The child at the far end is still sharp, occupied, and bounded-defect by Section 3. Thus the physical arithmetic already present elsewhere in the line improves the worst all-head step by a genuine logarithmic factor.

However, for every fixed `\Theta<1`,

\[
H-C
\asymp
H^{\Theta+o(1)}(\log H)^\kappa
=o(H).
\tag{39}
\]

So arbitrary depth, perfect preservation of projective quality, and this stronger local source regularity would still not by themselves supply a fixed-factor physical contraction if every selected branch remained head-like. The scale ledger still needs a mechanism that is absent from (1).

There are three structurally different ways such a mechanism could enter. A positive proportion of genuinely multiplicative predecessor branches would immediately accumulate fixed-factor contractions. A source-refueling theorem could show that before one protected corridor is exhausted another frontier-scale spike becomes available, allowing the additive gains to concatenate. Or one could exploit the exact coefficient law

\[
\Delta\mathcal H(n)
=
\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n
\tag{40}
\]

rather than an endpoint norm bound, forcing signed/divisibility behavior incompatible with a monotone depletion corridor.

`FD-076` does not provide the required refueling: its power-dense record statement controls record locations only on the logarithmic/power scale, so additive gaps between consecutive usable records may still be of order `X`, much larger than `X^Theta (log X)^kappa` when `Theta<1`. Likewise the 2026 almost-all short-interval theorem already audited in `FD-056` cannot simply replace (1) at the adaptive record locations: its global exceptional budget can contain the whole thin transfer corridor.

## 5. The logarithmic scale is sharp for the endpoint regularity input itself

The conclusion above is deliberately about what the **known uniform endpoint estimate** certifies, not an upper bound on the actual physical source. The actual `mathcal H` may remain large much farther backwards, oscillate into a new spike, or force a non-head branch.

There is nevertheless a sharp matched control for the regularity mechanism. At one large scale `X`, choose a height `A=o(X)` and put

\[
s_X:=\frac{1}{(\log X)^\kappa},
\qquad
W_X:=\left\lfloor A(\log X)^\kappa\right\rfloor.
\tag{41}
\]

On the local interval around `X`, define the triangular profile

\[
G_X(n)
:=
\bigl(A-s_X|n-X|\bigr)_+.
\tag{42}
\]

Then

\[
|G_X(u)-G_X(v)|
\le
s_X|u-v|
=
\frac{|u-v|}{(\log X)^\kappa}
\tag{43}
\]

through the local dyadic scale, while

\[
G_X(X)=A,
\qquad
G_X(X-W_X)=O(1).
\tag{44}
\]

Thus an endpoint estimate of the shape (1), even together with one-Lipschitz continuity, permits a spike to deplete completely after distance `asymp A(log X)^kappa`. By placing such tents on sufficiently lacunary scales one may also make their peaks strict normalized records while keeping the same local regularity. This is not a model of the exact Möbius coefficient law (40); it is a matched control showing that the logarithmic enlargement cannot be iterated into macroscopic descent from **endpoint regularity alone**.

This distinction is the useful boundary. `FD-048` already proved that aggregate short-interval smoothing does not by itself force the earlier joint-occupation target. The present finding shows the same limitation at the current, much later composition frontier: the uniform smoothing theorem does improve the head repair quantitatively, but its natural protected scale remains submacroscopic.

## 6. Prior-art and endpoint audit

The only external theorem used load-bearingly here is the Matomäki--Teräväinen all-short-interval Möbius estimate already anchored in `SOURCES.md` and transferred to the shell source in `FD-048`; no new literature dependency is introduced.

A fresh boundary check against the current literature found no newer uniform all-interval Möbius theorem that lowers the `11/20` exponent relevant to (1). The 2026 higher-uniformity result gives much stronger cancellation on almost all intervals, but that is the exceptional-set regime already audited in `FD-056`, not a uniform theorem at an adaptively selected source record. Pintz's 2026 maximal/average-order theorem supplies the source records and their abundance through `FD-076`--`FD-077`, but does not give additive record spacing on the `A(log X)^kappa` scale.

The range splits cleanly:

- for `1/2<Theta<=11/20`, this finding adds no source-head retreat beyond the `O(A)` one-Lipschitz corridor;
- for `11/20<Theta<1`, the guaranteed corridor is enlarged to `A(log X)^kappa` for every fixed `kappa<1/3`, still `o(X)`;
- at `Theta=1`, no submacroscopic conclusion is asserted.

So the live bottleneck after `FD-097` is not merely that predecessor depth lacks an effective bound. Even after reusing the strongest presently anchored **uniform** local Möbius cancellation, the worst all-head route remains additive at the power scale. The next decisive input must couple scale descent to branch type or replenish the source head on a genuinely shorter additive scale.