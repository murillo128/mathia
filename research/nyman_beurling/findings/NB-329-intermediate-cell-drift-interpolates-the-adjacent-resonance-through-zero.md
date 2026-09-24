# NB-329 — Intermediate cell drift interpolates the adjacent resonance through zero

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-327, NB-328
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + INTERMEDIATE-OFF-LATTICE-DRIFT + ADJACENT-WITNESS + RANK-ONE-ERROR + AFFINE-PHASE-LAW + CANCELLATION-WINDOW + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

let `R_n` be the rank-one comparison operator from `NB-314`, and use the adjacent cancellation

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1}.
\tag{1}
\]

For integers

\[
n\ge3,
\qquad d\ge1,
\qquad 0\le r\le d,
\]

put

\[
\rho:=\frac rd\in[0,1],
\qquad
m_{n,d,r}:=d(n-1)+r=d(n-1+\rho),
\tag{2}
\]

and define

\[
\mathcal E_{n,d,r}
:=
\left\langle
(\sqrt{m_{n,d,r}}\,T_{n,m_{n,d,r}}-R_n)g_2,u_n
\right\rangle.
\tag{3}
\]

Then the entire one-cell drift between the two neighboring resonant lattices of `NB-327` and `NB-328` obeys the finite estimate

\[
\boxed{
\left|
\mathcal E_{n,d,r}
-
\left(1-2\frac rd\right)\frac{\log2}{4n}
\right|
\le
\frac{9d}{4(n-1)^2}.
}
\tag{4}
\]

Consequently, for any integer sequences `d_n=o(n)` and `0<=r_n<=d_n` such that

\[
\frac{r_n}{d_n}\longrightarrow\rho\in[0,1],
\tag{5}
\]

one has

\[
\boxed{
 n\mathcal E_{n,d_n,r_n}
\longrightarrow
(1-2\rho)\frac{\log2}{4}.
}
\tag{6}
\]

Thus `NB-327` and `NB-328` are the two endpoints `rho=0` and `rho=1` of one affine phase law. The adjacent rank-one-error coefficient crosses through zero at half-cell drift:

\[
\boxed{
\frac{r_n}{d_n}\longrightarrow\frac12
\quad\Longrightarrow\quad
n\mathcal E_{n,d_n,r_n}\longrightarrow0.
}
\tag{7}
\]

In particular, when `d` is even and `r=d/2`,

\[
\boxed{
|\mathcal E_{n,d,d/2}|
\le
\frac{9d}{4(n-1)^2}.
}
\tag{8}
\]

Away from the half-drift phase, the same logarithmic operator-norm obstruction as in `NB-327`--`NB-328` persists. If `rho != 1/2`, then using `NB-304`,

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_{n,d_n,r_n}}T_{n,m_{n,d_n,r_n}}-R_n\|
\ge
|1-2\rho|\frac{\sqrt{\log2}}{2\sqrt2}.
}
\tag{9}
\]

Equation (7) is deliberately weaker than an operator-mixing theorem. It proves a genuine cancellation window for the explicit adjacent channel, not that the optimized operator norm vanishes there. Another source direction may remain resonant at `rho=1/2`. The statement is source-side and gives no target occupation, finite-section excess, Nyman approximation rate, or RH consequence.

## 1. Keep the selector cell-aligned and move the adjacent profile

The exact rank-one-error identity from `NB-314` gives

\[
\mathcal E_{n,d,r}
=
\int_0^\infty
F_{g_2}(t)\widetilde F_n(m_{n,d,r}t)
\frac{dt}{t^2},
\tag{10}
\]

where the centered reciprocal profile of the adjacent witness is

\[
\widetilde F_n(z)
=
\left\{\frac zn\right\}
-
\frac{n-1}{n}
\left\{\frac z{n-1}\right\}
-
\frac1{2n}.
\tag{11}
\]

The useful scaling for the full drift interval is not by `m/(n-1)` but simply by the integer `d`. Set

\[
h_{n,\rho}(y)
:=
\widetilde F_n((n-1+\rho)y),
\qquad
s_d(y):=F_{g_2}(y/d).
\tag{12}
\]

Changing variables `y=dt` in (10) gives the exact identity

\[
\boxed{
\mathcal E_{n,d,r}
=
d\int_0^\infty
s_d(y)h_{n,\rho}(y)\frac{dy}{y^2}.
}
\tag{13}
\]

Because `d` is an integer, the selector remains exactly constant on every unit cell throughout the entire interpolation:

\[
s_d(y)=
\begin{cases}
0,&y\in[2jd,(2j+1)d),\\[1mm]
1/2,&y\in[(2j+1)d,(2j+2)d),
\end{cases}
\qquad j\ge0.
\tag{14}
\]

At `rho=0`, `h_(n,rho)` is the left-pulse profile `f_n` of `NB-327`. At `rho=1`, it is the reflected right-pulse profile `h_n` of `NB-328`. Intermediate drift therefore moves the profile continuously while preserving the exact cell-aligned square-wave selector.

## 2. The first cells split into a left pulse and a right pulse

Write

\[
A:=n-1+\rho.
\]

Fix an integer cell

\[
1\le k\le n-2,
\qquad
y=k+x,
\qquad 0\le x<1.
\]

Since both accumulated fractional corrections remain below one in this range,

\[
\left\{\frac{A(k+x)}n\right\}
=
 x-rac{(1-\rho)(k+x)}n
+
\mathbf 1_{\{x<\alpha_k\}},
\tag{15}
\]

where

\[
\alpha_k:=\frac{(1-\rho)k}{A},
\tag{16}
\]

and

\[
\left\{\frac{A(k+x)}{n-1}\right\}
=
 x+rac{\rho(k+x)}{n-1}
-
\mathbf 1_{\{x\ge\beta_k\}},
\tag{17}
\]

where

\[
\beta_k:=\frac{n-1-\rho k}{A}.
\tag{18}
\]

Substitution into (11) cancels every affine `x` term and gives

\[
\boxed{
h_{n,\rho}(k+x)
=
\mathbf1_{\{x<\alpha_k\}}
+
\frac{n-1}{n}\mathbf1_{\{x\ge\beta_k\}}
-
\frac{k+1/2}{n}.
}
\tag{19}
\]

Moreover,

\[
\beta_k-\alpha_k
=
\frac{n-1-k}{A}>0,
\tag{20}
\]

so the two pulses are disjoint. Their lengths are

\[
\alpha_k=\frac{(1-\rho)k}{A},
\qquad
1-\beta_k=\frac{\rho(k+1)}{A}.
\tag{21}
\]

Thus the left pulse loses exactly the fraction `rho` of its endpoint geometry while a reflected right pulse gains it.

## 3. Every complete selected cell has an exact affine drift coefficient

Integrating (19) against the physical weight on `[k,k+1)` yields an exact simplification. First,

\[
\int_k^{k+\alpha_k}\frac{dy}{y^2}
=
\frac{1-\rho}{nk},
\tag{22}
\]

because `k+alpha_k=kn/A`. Likewise,

\[
\frac{n-1}{n}
\int_{k+\beta_k}^{k+1}\frac{dy}{y^2}
=
\frac{\rho}{n(k+1)},
\tag{23}
\]

because `k+beta_k=(n-1)(k+1)/A`. Finally,

\[
\frac{k+1/2}{n}
\int_k^{k+1}\frac{dy}{y^2}
=
\frac{k+1/2}{n\,k(k+1)}.
\tag{24}
\]

Combining (22)--(24),

\[
\boxed{
\int_k^{k+1}
 h_{n,\rho}(y)\frac{dy}{y^2}
=
\frac{1-2\rho}{2n\,k(k+1)}.
}
\tag{25}
\]

This identity is the central point of the finding. The sign reversal in `NB-328` is not a separate endpoint phenomenon: **the weighted cell coefficient is exactly affine in the drift phase**.

Since a selected cell has `s_d=1/2`, the contribution from all complete cells before `n-1` is

\[
I^{(0)}_{n,d,r}
=
\frac{(1-2\rho)d}{4n}
\sum_{\substack{1\le k<n-1\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}.
\tag{26}
\]

As in `NB-327`, the infinite selected-cell sum telescopes block by block:

\[
d
\sum_{\substack{k\ge1\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
=
\log2.
\tag{27}
\]

The omitted terms have `k>=n-1`, hence

\[
0\le
\frac{\log2}{d}
-
\sum_{\substack{1\le k<n-1\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
\le
\frac1{n-1}.
\tag{28}
\]

Therefore

\[
\boxed{
\left|
I^{(0)}_{n,d,r}
-
(1-2\rho)\frac{\log2}{4n}
\right|
\le
\frac{d}{4n(n-1)}.
}
\tag{29}
\]

The half-drift cancellation is already exact at the level of every complete selected first-region cell: when `rho=1/2`, the right and left pulse contributions cancel cell by cell in the weighted integral (25).

## 4. Uniform cell centering controls the infinite tail for every drift phase

Unlike the endpoint profiles, `h_(n,rho)` need not have an integer period when `0<rho<1`. No common-period argument is needed.

Introduce the centered sawtooth

\[
\phi_q(z):=\left\{\frac zq\right\}-\frac12.
\]

Then (11) is exactly

\[
\widetilde F_n(z)
=
\phi_n(z)
-
\frac{n-1}{n}\phi_{n-1}(z).
\tag{30}
\]

For a global unit cell `[K,K+1)`, let

\[
b_K:=\int_0^1 h_{n,\rho}(K+x)\,dx.
\tag{31}
\]

After `z=Ay`, the integration interval has length `A=n-1+rho`. A centered `phi_n` integrates to zero over every interval of length `n`; extending the present interval by the missing length `1-rho<=1` therefore gives

\[
\left|\int_I\phi_n(z)\,dz\right|\le\frac12.
\tag{32}
\]

Similarly, `phi_(n-1)` integrates to zero over every interval of length `n-1`; removing the extra terminal length `rho<=1` gives

\[
\left|\int_I\phi_{n-1}(z)\,dz\right|\le\frac12.
\tag{33}
\]

Consequently,

\[
\boxed{|b_K|<\frac1A\le\frac1{n-1}.}
\tag{34}
\]

Also (30) gives `|h_(n,rho)|<1`. Put

\[
q_K(x):=h_{n,\rho}(K+x)-b_K.
\]

Then `int_0^1 q_K(x)dx=0` and, for `n>=3`, `|q_K|<=3/2`. With `w_K(x)=(K+x)^(-2)`, zero-mean cancellation gives

\[
\begin{aligned}
\left|
\int_0^1q_K(x)w_K(x)\,dx
\right|
&=
\left|
\int_0^1q_K(x)(w_K(x)-w_K(0))\,dx
\right|\\
&\le
\frac3{K^3},
\end{aligned}
\tag{35}
\]

while the mean part satisfies

\[
\left|
b_K\int_0^1w_K(x)\,dx\right|
\le
\frac1{(n-1)K(K+1)}.
\tag{36}
\]

The selector `s_d` is constant on every unit cell and has magnitude at most `1/2`. Therefore the tail beginning at `K=n-1` obeys

\[
\begin{aligned}
|\mathcal T_{n,d,r}|
&\le
\frac d2
\sum_{K=n-1}^\infty
\left(
\frac3{K^3}
+
\frac1{(n-1)K(K+1)}
\right)\\[1mm]
&\le
\boxed{\frac{2d}{(n-1)^2}}.
\end{aligned}
\tag{37}
\]

Here we used

\[
\sum_{K=L}^\infty K^{-3}\le L^{-2},
\qquad
\sum_{K=L}^\infty\frac1{K(K+1)}=L^{-1},
\qquad L=n-1\ge2.
\tag{38}
\]

Combining (29) and (37), and using `n>=n-1`, proves the advertised bound (4).

The tail estimate is phase-uniform. The absence of an integer period at intermediate `rho` therefore costs nothing at leading order: local one-cell centering is sufficient, exactly as the endpoint analyses suggested.

## 5. Consequences for the subquadratic transition

If `d_n=o(n)` and `r_n/d_n->rho`, equation (4) gives (6) directly. Together with

\[
\|g_2\|_2=\frac{\sqrt{\log2}}2
\]

and the `NB-304` adjacent-witness estimate

\[
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{39}
\]

any fixed phase `rho != 1/2` gives (9).

Thus the exact neighboring-lattice controls now have a complete first-order interpolation:

\[
\rho=0
\quad\leadsto\quad
+\frac{\log2}{4n},
\]

\[
0<\rho<1
\quad\leadsto\quad
(1-2\rho)\frac{\log2}{4n},
\]

\[
\rho=1
\quad\leadsto\quad
-\frac{\log2}{4n},
\]

up to `O(d/n^2)` uniformly in the phase.

This settles the first question left open by `NB-328`: **yes, the explicit adjacent channel passes through a genuine cancellation window under intermediate drift.** In fact the zero occurs at the geometrically natural half-cell phase `rho=1/2`.

It does **not** settle the optimized mixing question. At half drift the present matrix coefficient is only `O(d/n^2)`, but this is an upper bound on one chosen coefficient, not on

\[
\|\sqrt m\,T_{n,m}-R_n\|.
\]

A different source witness, a different probe, or a combination of nearby adjacent channels could remain of order `1/sqrt(log n)`. The next discriminating problem is therefore no longer whether this particular signed channel can cancel; it is whether the operator can route around that zero.

## 6. Adversarial checks and prior-art boundary

The derivation was stress-tested at the points where an interpolation argument could easily become formal rather than real.

- The phase parameter is `rho=r/d`, while the actual scale is `m=d(n-1+rho)`; no continuum approximation is used in (13).
- The selector remains cell-aligned because the change of variables uses the integer `d`, not the drifting factor `n-1+rho`.
- Formula (19) keeps both carries. Dropping the right-edge carry would recover `NB-327` but miss the sign reversal; dropping the left-edge carry would recover `NB-328` but miss the interpolation.
- The two pulses are disjoint by (20), so no hidden overlap term is omitted.
- The affine coefficient (25) is exact before any limit is taken.
- The tail argument does not assume periodicity of `h_(n,rho)`. It uses only the fact that the scaling length `A` differs by at most one from each of the two adjacent sawtooth periods `n` and `n-1`.
- The finite error is uniform in `rho in [0,1]`, so the midpoint cancellation is not a pointwise limiting artifact.
- Equation (7) concerns this explicit matrix coefficient only. It is not evidence that the full projected-dilation operator mixes at half drift.

A fresh literature audit found the closest classical neighbors in Michel Balazard's study of integer dilations of the fractional-part function and in the multiplicative autocorrelation work of Michel Balazard and Bruno Martin. Balazard's 2006 paper studies distances between integer dilates in `L^2((0,infinity),t^-2 dt)`; Balazard--Martin study the multiplicative autocorrelation

\[
A(\lambda)=\int_0^\infty \{t\}\{\lambda t\}\frac{dt}{t^2}
\]

and its regularity as the dilation ratio varies. These are directly relevant prior-art domains for weighted fractional-part correlations, but the audited material did not state the present finite-section adjacent-witness interpolation, the exact cell coefficient (25), or the half-cell zero of the rank-one-subtracted projected-dilation channel. Hugh Carvill's recent Beurling--Nyman Gram work concerns multiscale Gram decay rather than this drifting finite-section coefficient. No novelty claim is made beyond the line-local derived statement.

External results are not load-bearing: the proof uses only the persisted Nyman identities from `NB-304`, `NB-314`, `NB-327`, and `NB-328` plus elementary fractional-part algebra and weighted cell estimates. `SOURCES.md` therefore needs no new dependency entry.

Relevant audit anchors:

- Michel Balazard, *Sur les dilatations entières de la fonction partie fractionnaire*, Functiones et Approximatio Commentarii Mathematici 35 (2006), DOI `10.7169/facm/1229442615`.
- Michel Balazard and Bruno Martin, *Sur l'autocorrélation multiplicative de la fonction "partie fractionnaire" et une fonction définie par J. R. Wilton*, arXiv:1305.4395.
- Hugh Carvill, *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing*, arXiv:2510.18132.

## Research consequence

The `NB-327`--`NB-328` sign flip is now completely resolved at first order. It is not evidence for abrupt mixing between two neighboring lattices. The adjacent channel follows an affine phase law and has an actual zero at half-cell drift.

Therefore any subquadratic upper-mixing theorem must answer a sharper question: **does the full operator retain another resonant direction when the canonical adjacent coefficient is tuned through zero?** If yes, the resonance is structurally redundant and not tied to one phase. If no, the half-cell window is the first concrete candidate where an operator-level transition could occur.
