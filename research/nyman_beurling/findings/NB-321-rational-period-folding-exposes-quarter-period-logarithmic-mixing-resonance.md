# NB-321 — Rational-period folding exposes a quarter-period logarithmic mixing resonance

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-316, NB-320
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + QUADRATIC-RESONANCE + RATIONAL-PERIOD-FOLDING + ADJACENT-WITNESS + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

and let `R_n` be the far-external rank-one operator from `NB-314`. For the scaled adjacent cancellation

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1},
\tag{1}
\]

write

\[
P_n:=n(n-1),
\qquad
\widetilde F_n:=\widetilde F_{u_n},
\qquad
G_n(T):=\int_0^T\widetilde F_n(s)\,ds.
\tag{2}
\]

The centered profile `widetilde F_n` and its primitive `G_n` are `P_n`-periodic, with `G_n(P_n)=0`.

Fix an integer `q>=2`. On every subsequence for which `q | P_n`, put

\[
m_{n,q}:=\frac{P_n}{q},
\qquad
L_q:=\operatorname{lcm}(2,q),
\tag{3}
\]

and define the residue kernel

\[
K_{L_q}(t):=\sum_{\ell\ge0}\frac1{(t+\ell L_q)^2}.
\tag{4}
\]

Then the actual weighted rank-one mixing coefficient against `g_2` admits the finite rational-period boundary reduction

\[
\boxed{
\begin{aligned}
\mathcal E_{n,q}
&:=
\left\langle
(\sqrt{m_{n,q}}T_{n,m_{n,q}}-R_n)g_2,u_n
\right\rangle\\[1mm]
&=
\frac1{2m_{n,q}}
\sum_{\substack{1\le r<L_q\\ r\ {m odd}}}
\Bigl[
G_n((r+1)m_{n,q})K_{L_q}(r+1)
-
G_n(rm_{n,q})K_{L_q}(r)
\Bigr]
+O_q(n^{-2}).
\end{aligned}
}
\tag{5}
\]

Thus every fixed rational quadratic scale `m=P_n/q` is governed, to first order, by finitely many centered-primitive samples on the `q`-grid of one adjacent period. The half-period calculation of `NB-320` is the case `q=2`; it is not an isolated folding mechanism.

At the next dyadic rational scale, `q=4`, the boundary sum can be evaluated explicitly. If `n congruent 0 (mod 4)`, then

\[
\boxed{
\mathcal E_{n,4}
=
\frac{\pi^2}{64(n-1)}
+O(n^{-2}).
}
\tag{6}
\]

If `n congruent 1 (mod 4)`, then

\[
\boxed{
\mathcal E_{n,4}
=
-\frac{\pi^2(n-1)}{64n^2}
+O(n^{-2})
=
-\frac{\pi^2}{64n}+O(n^{-2}).
}
\tag{7}
\]

An explicit absolute remainder valid in both congruence classes is

\[
\left|\mathcal E_{n,4}-\mathcal B_{n,4}\right|
\le
\frac{16\bigl(\zeta(3)+3\zeta(4)\bigr)}{(n-1)^2},
\tag{8}
\]

where `mathcal B_(n,4)` denotes the displayed boundary main term in (6) or (7).

Using the adjacent-witness norm bounds from `NB-304`/`NB-320`,

\[
\frac{H_{\lfloor n/2\rfloor}-1}{4n^2}
\le
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{9}
\]

and `||g_2||_2^2=log 2/4`, equations (6)--(9) imply along either admissible congruence class

\[
\boxed{
\frac{|\mathcal E_{n,4}|}{\|g_2\|_2\,\|u_n\|_2}
=\Theta\!\left(\frac1{\sqrt{\log n}}\right).
}
\tag{10}
\]

Consequently

\[
\boxed{
\left\|\sqrt{m_{n,4}}T_{n,m_{n,4}}-R_n\right\|
\gg
\frac1{\sqrt{\log n}},
\qquad
m_{n,4}=\frac{n(n-1)}4.
}
\tag{11}
\]

Together with `NB-320`, this gives logarithmic weighted resonances at two distinct macroscopic quadratic ratios, `m/n^2 -> 1/2` and `m/n^2 -> 1/4`. Therefore the `NB-320` obstruction is not tied specifically to the half-period point. It is the first instance of a finite rational-period boundary mechanism.

## 1. Exact rational-period folding

`NB-314` gives, for `u,v in U_n`,

\[
\left\langle(\sqrt m T_{n,m}-R_n)v,u\right\rangle
=
\int_1^\infty
F_v(t)\widetilde F_u(mt)\,\frac{dt}{t^2}.
\tag{12}
\]

For `v=g_2`,

\[
F_{g_2}(t)
=
\begin{cases}
0,&t\in[2\ell,2\ell+1),\\[1mm]
1/2,&t\in[2\ell+1,2\ell+2).
\end{cases}
\tag{13}
\]

If `m=P_n/q`, then `t -> widetilde F_n(mt)` has period exactly dividing `q`, while (13) has period `2`. Hence their product has period dividing `L_q=lcm(2,q)`. Folding the nonperiodic weight `t^(-2)` over one such period gives the exact identity

\[
\mathcal E_{n,q}
=
\frac12
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\int_r^{r+1}
\widetilde F_n(m_{n,q}t)K_{L_q}(t)\,dt.
\tag{14}
\]

After `s=m_(n,q)t`,

\[
\mathcal E_{n,q}
=
\frac1{2m_{n,q}}
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\int_{rm_{n,q}}^{(r+1)m_{n,q}}
\widetilde F_n(s)K_{L_q}(s/m_{n,q})\,ds.
\tag{15}
\]

Integration by parts with `G_n'=widetilde F_n` gives exactly the boundary sum in (5), plus

\[
\mathcal R_{n,q}
=
-\frac1{2m_{n,q}^2}
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\int_{rm_{n,q}}^{(r+1)m_{n,q}}
G_n(s)K_{L_q}'(s/m_{n,q})\,ds.
\tag{16}
\]

The point of (5) is that the remainder is genuinely one order smaller than the boundary term for fixed `q`, not merely bounded by the primitive supremum.

## 2. A second primitive makes the rational folding remainder `O_q(n^-2)`

`NB-316` gives

\[
\|G_n\|_\infty
=
\frac{\lfloor n^2/4\rfloor}{2n}
\le\frac n8.
\tag{17}
\]

`NB-320` also computes the integral `J_a` of `G_n` over every complete reciprocal block of length `n` and proves

\[
|J_a|\le\frac n4.
\tag{18}
\]

It follows that for any interval `[a,b]` of length at most one period `P_n`,

\[
\boxed{
\left|\int_a^bG_n(s)\,ds\right|
\le\frac{n^2}{2}.
}
\tag{19}
\]

Indeed there are at most two partial `n`-blocks, costing at most `n^2/8` each by (17), and fewer than `n` complete blocks, costing at most `n^2/4` in total by (18). Periodicity handles intervals crossing the endpoint of a period.

For each interval in (16), anchor

\[
H_{n,r}(s):=\int_{rm_{n,q}}^sG_n(y)\,dy.
\tag{20}
\]

Because `m_(n,q)<=P_n`, equation (19) gives `||H_(n,r)||_infinity<=n^2/2`. A second integration by parts in (16), together with the fact that `L_q` is fixed and `K_(L_q)'`, `K_(L_q)''` are uniformly bounded on the finitely many compact unit cells involved, yields

\[
\mathcal R_{n,q}
=O_q\left(\frac{n^2}{m_{n,q}^2}\right)
=O_q(n^{-2}).
\tag{21}
\]

This proves the general rational-period reduction (5). Notice the distinction from the primitive-envelope route of `NB-315`/`NB-319`: here the second antiderivative is used only after the exact periodic folding and retains the signed endpoint data that creates the resonance.

## 3. Quarter-period primitive samples are explicit

Now take `q=4`, so

\[
m_{n,4}=\frac{P_n}{4},
\qquad
L_4=4.
\tag{22}
\]

The folding contains exactly the odd cells `[1,2]` and `[3,4]`. Therefore (5) has boundary part

\[
\mathcal B_{n,4}
=
\frac1{2m_{n,4}}
\Bigl[
G_n(P_n/2)K_4(2)
-G_n(P_n/4)K_4(1)
-G_n(3P_n/4)K_4(3)
\Bigr],
\tag{23}
\]

because `G_n(P_n)=0`.

The exact block formulas of `NB-316` give the required three samples. If `n=4a`, all three rational times land exactly at within-block minima:

\[
G_n(P_n/4)=G_n(3P_n/4)=-\frac{3n}{32},
\qquad
G_n(P_n/2)=-\frac n8.
\tag{24}
\]

If `n=4a+1`, all three times land at block starts:

\[
G_n(P_n/4)=G_n(3P_n/4)
=
\frac{3(n-1)^2}{32n},
\qquad
G_n(P_n/2)=\frac{(n-1)^2}{8n}.
\tag{25}
\]

The residue kernel values combine without any unevaluated arithmetic sum:

\[
K_4(1)+K_4(3)
=
\sum_{j\ge0}\frac1{(2j+1)^2}
=
\frac{\pi^2}{8},
\tag{26}
\]

\[
K_4(2)
=
\sum_{j\ge0}\frac1{(4j+2)^2}
=
\frac{\pi^2}{32}.
\tag{27}
\]

Substituting (24) or (25) into (23) gives respectively

\[
\mathcal B_{n,4}=\frac{\pi^2}{64(n-1)}
\tag{28}
\]

and

\[
\mathcal B_{n,4}=-\frac{\pi^2(n-1)}{64n^2}.
\tag{29}
\]

This proves the main terms (6)--(7).

For an explicit version of the remainder, on the selected cells `1<=t<=4`,

\[
|K_4'(t)|\le2\zeta(3),
\qquad
|K_4''(t)|\le6\zeta(4).
\tag{30}
\]

Applying the second integration by parts separately on the two selected intervals, using (19), gives

\[
|\mathcal R_{n,4}|
\le
\frac{n^2}{m_{n,4}^2}\bigl(\zeta(3)+3\zeta(4)\bigr)
=
\frac{16\bigl(\zeta(3)+3\zeta(4)\bigr)}{(n-1)^2},
\tag{31}
\]

which is (8).

## 4. The half-period resonance is part of a rational quadratic skeleton

`NB-320` found the logarithmic normalized defect at

\[
m_{n,2}=\frac{P_n}{2}
\sim\frac12n^2.
\tag{32}
\]

Equations (6)--(11) show the same normalized scale at the genuinely different dilation

\[
m_{n,4}=\frac{P_n}{4}
\sim\frac14n^2.
\tag{33}
\]

The signs depend on the residue class of `n`, but the magnitude of the leading coefficient does not disappear. In both admissible classes the unnormalized boundary residue has size `asymp 1/n`; after dividing by `||u_n||_2=Theta(sqrt(log n)/n)`, the weighted operator defect is at least order `1/sqrt(log n)`.

More structurally, equation (5) identifies what has to be analyzed for every fixed rational quadratic ratio `1/q`: not a global primitive supremum, but a finite signed functional of the primitive samples

\[
G_n\!\left(\frac{jP_n}{q}\right).
\tag{34}
\]

Those samples depend only on the adjacent block geometry and on residue classes modulo `q`. Hence fixed-denominator quadratic resonances reduce to a finite arithmetic problem. Some denominators or residue classes may cancel, and (5) does not claim a nonzero coefficient for every `q`; it supplies the exact first-order discriminator and proves non-cancellation for `q=4`.

This narrows the open source-side question left by `NB-320`. A uniform quadratic mixing theorem, if true, must tolerate a rational skeleton of logarithmically decaying resonances rather than one exceptional half-period point. Conversely, to push the true transition beyond quadratic scale one still needs an order-one normalized weighted channel; neither `q=2` nor `q=4` supplies one.

## 5. Evidence boundary and prior-art audit

This finding remains source-side. It concerns an explicit matrix coefficient of `sqrt(m)T_(n,m)-R_n`; it does not establish occupation by the first-free Ford datum, a bound for finite-section excess, a Nyman approximation rate, or any consequence for RH.

The rational arithmetic in the folding has classical neighbors. Báez-Duarte, Balazard, Landreau and Saias study the multiplicative autocorrelation

\[
A(\lambda)=\int_0^\infty\{\lambda t\}\{t\}\,\frac{dt}{t^2}
\]

and its special structure at rational `lambda` (arXiv:math/0306251; Ramanujan J. 9 (2005), 215--240). Balazard and Martin further analyze this autocorrelation through the first Bernoulli function and continued-fraction/Wilton structure (arXiv:1305.4395). Vasyunin-type and cotangent-sum formulae are therefore the correct classical boundary for claims about rational fractional-part correlation. The contemporary Nyman--Beurling Gram work of Alouges--Darses--Hillion and Carvill is also adjacent to the finite-section geometry.

The material located in the fresh audit did not expose the specific finite-section object used here: the rank-one-subtracted projected-dilation coefficient, its folding through the centered adjacent primitive, or the boundary formula (5) and quarter-period asymptotics (6)--(7). This is recorded only as a boundary from the sources reviewed, not as a claim of bibliographic novelty. No external theorem is load-bearing for the proof, so no new durable source dependency is added to `SOURCES.md`.

## Classification and next discriminator

This is a rigorous positive structural finding plus rate obstruction. It upgrades `NB-320` from one half-period example to a reusable rational-period reduction and proves a second logarithmic resonance at quarter-period scale.

The next useful discriminator is to evaluate the finite boundary functional (5) across fixed reduced denominators `q` and residue classes, looking for either a uniform logarithmic envelope or a family whose normalized coefficient stays order one. The former would support quadratic rank-one mixing with a subpower rate; the latter would force the true source-side transition beyond the quadratic scale. The key point is that this can now be asked on a finite `q`-grid without reverting to the lossy global primitive supremum.
