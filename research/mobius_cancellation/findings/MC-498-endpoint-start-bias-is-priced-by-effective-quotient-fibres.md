# MC-498 — Endpoint-start bias is priced by effective quotient fibres

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-DYADIC/HYPERBOLA+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-497` shows, for the quadratic repeated-residue cross-root phase, that a fixed-length short interval can have order-one normalized bias only on a sparse set of physical conductor starts. The exact Fourier-Parseval sharpening there gives, uniformly for `1<=L<=p`,

\[
\sum_{x\bmod p}|S_{c,x}(L)|^2\ll pL,
\qquad
S_{c,x}(L)=\sum_{j=1}^{L}F_c(x+j).
\tag{1}
\]

For variable overlap lengths in one dyadic band, this implies the maximal estimate

\[
\boxed{
\sum_{x\bmod p}
\max_{1\le L\le H}|S_{c,x}(L)|^2
\ll pH\log^2(2H)
}
\tag{2}
\]

for `1<=H<=p`.

Let `\mathcal I` be any finite family of physical intervals with starts `x_i mod p`, lengths

\[
H/2\le L_i\le H,
\tag{3}
\]

and nonnegative weights `lambda_i`. Define

\[
w(x)=\sum_{i:x_i=x}\lambda_i,
\qquad
R_{\rm start}=\frac{\|w\|_1^2}{\|w\|_2^2},
\tag{4}
\]

and

\[
B=\sum_i\lambda_i S_{c,x_i}(L_i),
\qquad
M=\sum_i\lambda_iL_i.
\tag{5}
\]

Then

\[
\boxed{
\frac{|B|}{M}
\ll
\sqrt{\frac{T_{p,H}}{R_{\rm start}}},
\qquad
T_{p,H}:=\frac pH\log^2(2H).
}
\tag{6}
\]

The previous version of this finding contained an additional `sqrt(p) log(2H)` term inherited from the lag-by-lag autocorrelation estimate in the original `MC-497`. That term disappears after the corrected Fourier-Parseval second moment. The surviving tariff is purely `p/H` up to the dyadic maximalization loss.

The physical endpoint map then prices `R_start` deterministically. For a positive source interval and one dyadic first-exit block `Q<=q,r<=2Q` with `q congruent r congruent a (mod p)`, set

\[
u_q=\left\lceil\frac Xq\right\rceil,
\qquad
v_r=\left\lceil\frac{X+h}{r}\right\rceil.
\tag{7}
\]

Whenever the two shortened intervals overlap, their physical start is

\[
\boxed{x_{q,r}=\max(u_q,v_r).}
\tag{8}
\]

For `Z>=4Q`, define

\[
D(Z;Q,p)
:=
\left(2+\frac{Z}{2Qp}\right)
\left(1+\frac{8Q^2}{Zp}\right).
\tag{9}
\]

Then for every `xi mod p`, even before imposing primality,

\[
\boxed{
\#\left\{q\in[Q,2Q]\cap\mathbf Z:
q\equiv a\pmod p,
\left\lceil\frac Zq\right\rceil\equiv\xi\pmod p
\right\}
\le D(Z;Q,p).
}
\tag{10}
\]

Now give each selected nonempty overlap `(q,r)` a factorable endpoint weight `alpha_q beta_r>=0`. Split pairs according to which endpoint wins `(8)`, assigning ties to the plus side, and define

\[
\gamma_q
:=\alpha_q\!\sum_{\substack{r:(q,r)\in\mathcal P\\u_q\ge v_r}}\!\beta_r,
\qquad
\delta_r
:=\beta_r\!\sum_{\substack{q:(q,r)\in\mathcal P\\v_r>u_q}}\!\alpha_q.
\tag{11}
\]

Put

\[
C_+=\sum_q\gamma_q,
\quad C_- =\sum_r\delta_r,
\quad C=C_++C_-,
\quad \theta_\pm=C_\pm/C,
\tag{12}
\]

and

\[
\kappa_+
:=\frac{C_+^2}{\sum_q\gamma_q^2},
\qquad
\kappa_-
:=\frac{C_-^2}{\sum_r\delta_r^2}.
\tag{13}
\]

Let `D_+=D(X;Q,p)` and `D_-=D(X+h;Q,p)` when the displayed fibre hypothesis holds. Then the weighted start pushforward satisfies

\[
\boxed{
\frac1{\sqrt{R_{\rm start}}}
\le
\theta_+\sqrt{\frac{D_+}{\kappa_+}}
+
\theta_-\sqrt{\frac{D_-}{\kappa_-}}.
}
\tag{14}
\]

Combining `(6)` and `(14)` gives

\[
\boxed{
\frac{|B|}{M}
\ll
\left(
\theta_+\sqrt{\frac{D_+}{\kappa_+}}
+
\theta_-\sqrt{\frac{D_-}{\kappa_-}}
\right)
\sqrt{\frac pH}\,\log(2H).
}
\tag{15}
\]

Thus endpoint-only bias is negligible whenever the winning-endpoint populations carrying nonnegligible mass satisfy

\[
\boxed{
\frac{\kappa_\pm}{D_\pm}
\gg
\frac pH\log^2(2H).
}
\tag{16}
\]

A surviving order-one bias must therefore exhibit low effective endpoint participation, large quotient fibres, or concentration in another length band. No random-start or equidistribution hypothesis is used.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Dyadic maximalization of the corrected MC-497 second moment

Let `H_0` be the least power of two at least `H`, so `H<=H_0<2H`. Every prefix `{1,...,L}`, `L<=H`, is a disjoint union of at most

\[
J=1+\lceil\log_2 H\rceil
\tag{17}
\]

canonical dyadic blocks, with at most one block at each scale. Cauchy on that decomposition and enlargement to all canonical blocks gives

\[
\sum_x\max_{L\le H}|S_{c,x}(L)|^2
\ll
J\sum_k\frac{H_0}{2^k}
\sup_I\sum_x\left|\sum_{j\in I}F_c(x+j)\right|^2.
\tag{18}
\]

Translation in `x` does not change the energy of a block of length `2^k`, and `MC-497` now gives `O(p2^k)`. Hence each scale costs `O(pH)`, while there are `O(log H)` scales and the outer Cauchy contributes another `O(log H)`. This proves `(2)`.

Grouping intervals by their start gives

\[
|B|
\le
\sum_x w(x)\max_{L\le H}|S_{c,x}(L)|.
\tag{19}
\]

Cauchy, `(2)`, and `M>=(H/2)\|w\|_1` prove `(6)`. Length may depend adversarially on the start; no independence is assumed.

## 2. The physical endpoint map is a reciprocal quotient map

For `Z>=4Q`, put

\[
u(q)=\left\lceil\frac Zq\right\rceil,
\qquad Q\le q\le2Q.
\tag{20}
\]

For a fixed integer `u>=2`,

\[
u(q)=u
\quad\Longleftrightarrow\quad
\frac Zu\le q<\frac{Z}{u-1}.
\tag{21}
\]

On the dyadic q-range the interval in `(21)` has length at most `8Q^2/Z`, so it contains at most

\[
1+\frac{8Q^2}{Zp}
\tag{22}
\]

integers in the fixed residue class `a mod p`. The possible exact quotient values occupy an interval of width at most `Z/(2Q)+2`, so one quotient residue `xi mod p` contributes at most

\[
2+\frac{Z}{2Qp}
\tag{23}
\]

exact values. Multiplication proves `(10)`. Restricting labels to primes or active first-exit rows can only reduce the fibre.

## 3. Winning-endpoint participation controls the pushforward

The start measure decomposes as

\[
w(\xi)
=
\sum_{q:u_q\equiv\xi\ (p)}\gamma_q
+
\sum_{r:v_r\equiv\xi\ (p)}\delta_r.
\tag{24}
\]

Cauchy inside each plus fibre gives

\[
\sum_\xi
\left(\sum_{q:u_q\equiv\xi}\gamma_q\right)^2
\le D_+\sum_q\gamma_q^2,
\tag{25}
\]

and similarly on the minus side. Minkowski in `l2(F_p)` yields

\[
\|w\|_2
\le
\sqrt{D_+}\,\|\gamma\|_2
+
\sqrt{D_-}\,\|\delta\|_2,
\tag{26}
\]

which becomes `(14)` after division by `\|w\|_1=C`.

Arbitrary overlap selection is therefore absorbed into the actual induced weights `gamma` and `delta`. Selection may still defeat `(16)`, but only by producing a quantitatively small participation ratio or a large quotient fibre.

## Prior art and novelty boundary

The corrected analytic input is the Fourier-Weil/Parseval second moment in `MC-497`, itself built from the classical mixed character estimate recorded as `MC-S55`. The maximalization is elementary dyadic bookkeeping. The quotient geometry `(20)`--`(23)` is the classical hyperbola/floor-quotient mechanism, and Cauchy, Minkowski, and participation ratios are standard Hilbert-space tools.

No novelty is claimed for any of those ingredients. The durable Mathia result is their exact composition with the first-exit physical start map, which turns short quadratic endpoint bias into the source-frame criterion `(15)`--`(16)`.

## Boundaries and falsification tests

- **Quadratic character.** Higher-order characters require an independent Fourier-envelope audit of their cross-root phase.
- **Endpoint-only amplitude.** Lower-prime pair-sieve masks and q-dependent signed/complex inner coefficients are outside `(15)`.
- **One repeated conductor residue.** Distinct residues correspond to different phase directions and cannot be pooled without derivation.
- **One dyadic q-block and one dyadic length band.** Global reconstruction must charge the number of scales.
- **Positive large source endpoints for `(10)`.** When `Z<4Q`, count the short quotient regime directly.
- **Effective participation remains load-bearing.** This finding gives a test, not a proof that the exact source weights pass it.
- **No Möbius summatory conclusion.** The result prices one endpoint mechanism inside the normalized first-exit architecture.

## Consequence for the research line

The source-frame tariff has no intrinsic `sqrt(p)` floor after the corrected `MC-497` diagonalization. For a dyadic overlap band, the exact reconstruction should first compare effective start participation with

\[
T_{p,H}=\frac pH\log^2(2H),
\]

then price quotient folding through `(10)` and `(14)`. `MC-499` and `MC-500` apply cheap source-cardinality ceilings to this corrected tariff before any detailed coefficient audit.