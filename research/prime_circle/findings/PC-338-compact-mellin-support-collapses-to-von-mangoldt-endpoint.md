# PC-338 — compact Mellin-frequency support collapses to the von Mangoldt endpoint

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the compactly supported distributional Mellin continuation left open by PC-337.

PC-179 gives the exact signed cyclotomic radial-flux Mellin transform

\[
\mathcal R_n(s)
=U(s)A_n(s),
\qquad
U(s):=-\Gamma(s)\zeta(s),
\qquad
A_n(s):=n^{1-s}\prod_{p\mid n}(1-p^{s-1}),
\tag{1}
\]

for `n>1`, with the removable endpoint value

\[
\mathcal R_n(1)=\Lambda(n).
\tag{2}
\]

PC-335 rules out bounded shell-independent Mellin multipliers, PC-336 classifies distributions supported at the endpoint, and PC-337 proves that any selector supported at finitely many Mellin frequencies is either shell-invisible or the classical von Mangoldt endpoint. The finite-support hypothesis in PC-337 is not the real boundary.

Fix `sigma>0` and let `T` be **any compactly supported distribution in the real Mellin frequency `t`** on the vertical line

\[
s=\sigma+it.
\tag{3}
\]

Define the shell response

\[
L_T(n):=\left\langle T,\mathcal R_n(\sigma+it)\right\rangle.
\tag{4}
\]

Then

\[
\boxed{
L_T(pq)=0
\quad\text{for every pair of distinct primes }p,q
}
\tag{5}
\]

implies

\[
\boxed{
\begin{array}{ll}
\sigma\neq1:&L_T(n)=0\quad\text{for every }n>1,\\[1mm]
\sigma=1:&L_T(n)=c\Lambda(n)\quad\text{for every }n>1
\end{array}}
\tag{6}
\]

for one constant `c` depending on `T`.

Thus **every compact Mellin-frequency window fails as a new exact prime-power selector**. On the endpoint line the only visible semiprime-null response is the already-known common-vertex von Mangoldt observable; away from that line the entire compactly supported response is shell-invisible.

## 1. Semiprime nulls force an entire function to vanish identically

For a prime `p`,

\[
A_p(s)=p^{1-s}-1,
\tag{7}
\]

and for distinct primes `p,q`,

\[
A_{pq}(s)=A_p(s)A_q(s).
\tag{8}
\]

The product

\[
g_p(t):=\mathcal R_p(\sigma+it)
\tag{9}
\]

is smooth on the whole real `t` axis. This remains true for `sigma=1`: the simple zero of `A_p(s)` at `s=1` cancels the simple pole of `zeta(s)`, and `g_p(0)=log p`.

Multiplication therefore defines another compactly supported distribution

\[
S_p:=g_pT.
\tag{10}
\]

Put `beta=1-sigma`. For a complex scale variable `z`, define

\[
F_p(z)
:=\left\langle S_p,
 e^{(\beta-it)z}-1
\right\rangle.
\tag{11}
\]

At `z=log q` with `q!=p` prime, equations (5), (7), and (8) give

\[
F_p(\log q)=L_T(pq)=0.
\tag{12}
\]

Because `S_p` has compact support and finite distributional order, (11) is entire. If its support is contained in `[-tau,tau]` and its order is at most `m`, the defining seminorm estimate for a compactly supported distribution gives directly

\[
|F_p(z)|\le C(1+|z|)^m e^{(|\beta|+\tau)|z|}.
\tag{13}
\]

Hence any nonzero `F_p` is an entire function of finite exponential type. Jensen's formula then gives a linear zero-counting bound

\[
N_p(R)=O(R).
\tag{14}
\]

But (12) supplies a distinct positive real zero at `log q` for every prime `q!=p`. Even the classical Chebyshev lower bound yields

\[
\#\{q:\log q\le R/2\}
=\pi(e^{R/2})+O(1)
\gg \frac{e^{R/2}}{R},
\tag{15}
\]

which contradicts (14). Therefore

\[
\boxed{F_p\equiv0\quad\text{for every prime }p.}
\tag{16}
\]

This is the compact-support analogue of PC-337's finite exponential-polynomial argument. The decisive property is not discreteness of the Mellin frequencies but Paley-Wiener type exponential growth forced by compact support.

## 2. Off the endpoint line every compactly supported response is invisible

For real `x`, equation (16) says

\[
e^{\beta x}\widehat S_p(x)
=\langle S_p,1\rangle=:C_p,
\tag{17}
\]

with the Fourier-transform convention induced by `e^{-itx}`. Thus

\[
\widehat S_p(x)=C_pe^{-\beta x}.
\tag{18}
\]

Assume first `sigma!=1`, so `beta!=0`. The Fourier transform of a compactly supported distribution has at most polynomial growth on the real axis, while the right side of (18) grows exponentially at one real end unless `C_p=0`. Hence

\[
S_p=0
\qquad\text{for every prime }p.
\tag{19}
\]

In particular

\[
(UA_2)T=(UA_3)T=0.
\tag{20}
\]

Set `S=UT`; here `U` is smooth on the line because `sigma!=1`. Then

\[
A_2S=A_3S=0.
\tag{21}
\]

The two functions `A_2` and `A_3` have no common zero on this vertical line. Indeed, simultaneous vanishing would imply

\[
(1-s)\log2=2\pi ik,
\qquad
(1-s)\log3=2\pi i\ell,
\tag{22}
\]

for integers `k,l`. Irrationality of `log2/log3` forces `k=l=0` and hence `s=1`, excluded here.

On the compact support of `S`, the smooth Bezout identity

\[
\frac{\overline{A_2}}{|A_2|^2+|A_3|^2}A_2
+
\frac{\overline{A_3}}{|A_2|^2+|A_3|^2}A_3
=1
\tag{23}
\]

therefore gives `S=0`. Consequently

\[
\boxed{
L_T(n)=\langle UT,A_n\rangle=0
\quad(n>1),
}
\tag{24}
\]

which proves the first case of (6).

## 3. On the endpoint line only a scalar delta remains visible

Now let `sigma=1`, so `beta=0`. Equation (17) becomes

\[
\widehat S_p(x)=C_p.
\tag{25}
\]

The only compactly supported distribution with constant Fourier transform is a scalar delta at the origin, hence

\[
S_p=C_p\delta_0.
\tag{26}
\]

Take `p=2`. Since

\[
g_2(0)=\mathcal R_2(1)=\log2\neq0,
\tag{27}
\]

multiplication by `g_2` is locally invertible near `t=0`. Equation (26) therefore forces the component of `T` near the endpoint to be exactly a scalar delta, with no delta derivatives. Write

\[
T=c\delta_0+T_*,
\tag{28}
\]

where `T_*` is compactly supported away from a neighborhood of `0`.

For `p=2` and `p=3`, equation (26) then implies

\[
g_pT_*=0.
\tag{29}
\]

Away from the endpoint, `U` is smooth, so with `S_*=UT_*` this is

\[
A_2S_*=A_3S_*=0.
\tag{30}
\]

As in (22), `A_2` and `A_3` have no common zero away from `s=1`; applying the same smooth Bezout identity on the compact support of `T_*` gives

\[
UT_*=0.
\tag{31}
\]

Thus `T_*` is invisible to every shell. The visible response comes only from the endpoint delta:

\[
\boxed{
L_T(n)=c\mathcal R_n(1)=c\Lambda(n).
}
\tag{32}
\]

This proves the second case of (6). Components supported at zeros of the universal zeta envelope can survive as distributions in `T_*`, but (31) shows that they contribute **zero to every prime-circle shell** and therefore cannot constitute a shell spectral mechanism.

## 4. Prior-art and novelty audit

The analytic machinery is classical. The Fourier transform of a compactly supported distribution is entire of exponential type with polynomial growth (Paley-Wiener-Schwartz), while Jensen theory bounds the zero density of a nonzero entire function of that growth. The proof above deliberately derives the only growth estimate it needs directly in (13); the remaining contradiction uses only Jensen's formula and the classical Chebyshev lower bound for prime counting.

A directed literature check around compact-support Paley-Wiener distributions, zero sets of entire functions of exponential type, logarithms of primes as uniqueness sets, and finite/compact Mellin support found the expected classical Paley-Wiener/Jensen/Levinson-Malliavin-Rubel neighborhood. It did not identify an independent RH mechanism matching the shell-specific implication (6). No historical novelty is claimed for those analytic theorems, for Mellin transforms of von Mangoldt data, or for generalized prime-power selectors.

The line-local contribution is narrower: the exact prime-circle factorization (1) makes the set `{log q : q prime}` an overcomplete uniqueness set for every **compact-frequency** semiprime-null linear readout. PC-337's finite collection of Mellin frequencies was therefore not an exceptional finite-dimensional obstruction; compact continuous or infinite support still collapses to the same endpoint channel.

No new `SOURCES.md` entry is required for the exact claim. Paley-Wiener-Schwartz serves as the classical umbrella for the directly proved estimate (13), and the load-bearing zero-density contradiction is stated explicitly above rather than imported from a specialized theorem.

## 5. Consequence and surviving frontier

PC-337 left infinite or continuous Mellin support open. Equation (6) closes the entire **compactly supported** part of that frontier:

\[
\boxed{
\text{compact-frequency semiprime-null readout}
\Longrightarrow
\begin{cases}
0,&\sigma\neq1,\\
c\Lambda,&\sigma=1.
\end{cases}}
\tag{33}
\]

Therefore widening a finite selector into a compact interval, a compact singular measure, a compact distribution of arbitrary finite order, or any finite union of compact frequency bands does not create a new exact prime-power discriminator. The endpoint `s=1` remains the unique visible compact-support channel.

What remains outside the theorem is materially narrower: **noncompact/global Mellin-frequency support**, analytic functionals not represented by compactly supported distributions, shell-dependent selectors, nonlinear readouts, matrix-valued/non-scalar refinement operators, and genuinely cross-shell coupling before scalar evaluation. Those routes may retain information unavailable to (33); this result says nothing about their viability. It also supplies no functional equation, critical-line positivity, or Hilbert-Polya operator.

## Audit / falsification tests

A counterexample consists of a fixed `sigma>0`, a compactly supported distribution `T` on the corresponding Mellin-frequency line, and exact semiprime nulls `L_T(pq)=0` for every distinct-prime pair, together with either:

- `sigma!=1` and some `n>1` with `L_T(n)!=0`; or
- `sigma=1` and shell responses not proportional to `Lambda(n)`.

The proof reduces falsification to three exact checkpoints: the entire-function growth estimate (13), the uniqueness conclusion (16) from prime-log zero density, and the no-common-zero/Bezout step for `A_2,A_3`. Failure of any one of those would invalidate the classification.
