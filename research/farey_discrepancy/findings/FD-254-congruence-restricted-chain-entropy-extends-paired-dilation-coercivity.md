# FD-254 — Congruence-restricted chain entropy extends paired dilation coercivity

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / paired increments / companion incidence / restricted ordered factorizations / polynomial coercivity window
- **Depends on:** FD-225, FD-248, FD-251, FD-253
- **Classification:** `EXACT-DERIVED + PAIRED-COEFFICIENT-UPPER-BOUND + CONGRUENCE-RESTRICTED-CHAIN-ENTROPY + POLYNOMIAL-DEFECT-COERCIVITY`

## Claim

FD-253 reduces pure-dilation exact omissions to the divisibility conditioning of their companion set. That companion geometry has a stronger arithmetic restriction than the unrestricted support treated in FD-251.

Fix an integer `L>=2`. Let `D` be any finite subset of `{1,...,M}`, put

\[
E:=LD=\{Ld:d\in D\},
\qquad
C:=LD+1=\{Ld+1:d\in D\},
\qquad
H:=LM+1,
\tag{1}
\]

and let `K=|D|`. Suppose

\[
Y(m)=(\mathscr A b)(m),\qquad Y(0)=0,
\qquad |b_n|\le C_b n\quad(1\le n\le H),
\tag{2}
\]

with `Y` supported on `E` up to `H`.

Define `rho_L>1` as the unique real solution of

\[
\boxed{
\sum_{j\ge1}(1+jL)^{-\rho_L}=1.
}
\tag{3}
\]

Then for every fixed `epsilon>0`,

\[
\boxed{
\kappa(C)\ll_{\epsilon,L}H^{\rho_L-1+\epsilon},
}
\tag{4}
\]

and consequently

\[
\boxed{
\sum_{n\le H}|b_n|
\ll_{\epsilon,L}
C_b K H^{\rho_L+\epsilon}.
}
\tag{5}
\]

Therefore, if

\[
K\le H^{\alpha+o(1)}
\qquad\text{with}\qquad
\alpha<2-\rho_L,
\tag{6}
\]

then

\[
\boxed{
\frac{\sum_{H/2<n\le H}|b_n|}
     {\sum_{H/2<n\le H}n}
\longrightarrow0.
}
\tag{7}
\]

For the parity case `L=2`, equation (3) becomes

\[
(1-2^{-\rho_2})\zeta(\rho_2)=2,
\tag{8}
\]

with

\[
\boxed{
\rho_2=1.377785169837541\ldots,
\qquad
2-\rho_2=0.622214830162459\ldots .
}
\tag{9}
\]

Thus parity-dilated paired omissions are coefficient-capacity coercive throughout the polynomial window

\[
\boxed{
K\le H^{\alpha+o(1)},
\qquad
\alpha<0.6222148301\ldots .
}
\tag{10}
\]

This is much wider than the support-only FD-251 window

\[
\alpha<2-\rho_*=0.2713527610\ldots,
\qquad \zeta(\rho_*)=2.
\]

The improvement comes from the actual paired companion geometry, not from a better estimate for unrestricted divisor supports.

## Pure dilation forces every companion-chain ratio into one congruence class

Every element of `C` is congruent to `1 mod L`. If

\[
c_0<c_1<\cdots<c_\ell
\]

is a strict divisibility chain inside `C`, write

\[
a_i=\frac{c_i}{c_{i-1}}.
\]

Because `c_i=c_{i-1}a_i` and both endpoints are `1 mod L`,

\[
\boxed{a_i\equiv1\pmod L.}
\tag{11}
\]

Every strict ratio is therefore at least `L+1`. This is the information lost in the unrestricted chain count of FD-251.

Let `H_L(r)` denote the number of ordered factorizations of `r` into factors belonging to

\[
\mathcal P_L:=\{1+Lj:j\ge1\},
\]

with `H_L(1)=1`. The chain-to-ordered-factorization injection from FD-251 now gives, for `q|c` in `C`,

\[
\boxed{
|\mu_C(q,c)|\le H_L(c/q).
}
\tag{12}
\]

The same argument works for every induced subposet of a single congruence class `1 mod L`; no special ordering of `D` is required.

## Restricted ordered factorizations have exponent `rho_L`

For `n>1`, the restricted factorization count obeys

\[
H_L(n)
=
\sum_{\substack{a\mid n\\a>1\\a\equiv1\;(\mathrm{mod}\;L)}}
H_L(n/a).
\tag{13}
\]

The series

\[
F_L(s)=\sum_{j\ge1}(1+jL)^{-s}
\]

is continuous and strictly decreasing for `s>1`, diverges as `s->1+`, and tends to zero as `s->infinity`; hence (3) defines a unique `rho_L>1`.

Induction in (13) gives the exact analogue of FD-251 with the restricted factor alphabet. Assuming the bound below for every proper divisor,

\[
\begin{aligned}
H_L(n)
&\le
\sum_{\substack{a\mid n\\a>1\\a\equiv1\;(\mathrm{mod}\;L)}}
(n/a)^{\rho_L}\\
&\le
n^{\rho_L}
\sum_{j\ge1}(1+jL)^{-\rho_L}\\
&=n^{\rho_L}.
\end{aligned}
\tag{14}
\]

Thus

\[
\boxed{H_L(n)\le n^{\rho_L}}
\tag{15}
\]

for every `n`.

Now fix `c in C`. Combining (12) and (15), including the diagonal through `H_L(1)=1`,

\[
\begin{aligned}
\sum_{\substack{q\in C\\q\mid c}}
|\mu_C(q,c)|\frac qc
&\le
\sum_{r\mid c}\frac{H_L(r)}r\\
&\le
\sum_{r\mid c}r^{\rho_L-1}\\
&\le
\tau(c)c^{\rho_L-1}.
\end{aligned}
\tag{16}
\]

The elementary divisor bound `tau(c) <<_epsilon c^epsilon` used in FD-251 proves (4).

For `L=2`, the allowed factors are precisely the odd integers at least `3`, so

\[
F_2(s)
=
\sum_{\substack{a\ge3\\a\ \mathrm{odd}}}a^{-s}
=(1-2^{-s})\zeta(s)-1.
\]

Setting `F_2(rho_2)=1` gives (8). Numerical root evaluation gives (9).

## Transfer from companion conditioning to paired exact omissions

For the pure dilation `E=LD`, no two omissions are consecutive because `L>=2`. Moreover a start can never divide a companion:

\[
Ld'\nmid Ld+1,
\tag{17}
\]

since the left side is divisible by `L` while the right side is `1 mod L`. Hence the companion-row closure hypothesis of FD-253 holds automatically.

FD-253 therefore gives

\[
\sum_{n\le H}|b_n|
\le
\left(2+\frac1{e_{\min}}\right)
C_b H K\kappa(C).
\tag{18}
\]

Since `e_min>=L`, equations (4) and (18) imply (5). Dividing by the dyadic coefficient capacity

\[
\sum_{H/2<n\le H}n\asymp H^2
\]

gives

\[
\frac{\sum_{H/2<n\le H}|b_n|}
     {\sum_{H/2<n\le H}n}
\ll_{\epsilon,L}
C_b K H^{\rho_L-2+\epsilon},
\tag{19}
\]

which proves (7) under (6).

The congruence restriction becomes progressively stronger with `L`. For every fixed `delta>0`,

\[
F_L(1+\delta)
\le
L^{-1-\delta}\zeta(1+\delta)
\longrightarrow0,
\]

so

\[
\boxed{\rho_L\downarrow1\quad\text{as }L\to\infty.}
\tag{20}
\]

Accordingly the fixed-`L` coercive exponent `2-rho_L` approaches `1`. This is consistent with the stronger antichain result of FD-253 when `L>M`; (20) is not a uniform growing-`L` replacement for that exact finite statement.

## Parity does not make companion conditioning polylogarithmic

The polynomial upper exponent in (9) should not be misread as evidence that odd companion sets are nearly primitive. The alternating-rank construction of FD-250 survives after deleting the prime `2`.

Let

\[
R_y^{\circ}=\prod_{3\le p\le y}p
\]

be the odd primorial. Repeat the rank-selected Boolean construction of FD-250 directly inside the divisor lattice of `R_y^{\circ}`. Removing the single prime `2` changes both

\[
\prod_{3\le p\le y}\left(1+\frac1p\right)
\quad\text{and}\quad
\sum_{3\le p\le y}\frac1{p+1}
\]

only by a constant factor/additive constant relative to the estimates used there. The same reciprocal-heavy rank and alternating-rank Möbius coefficient therefore yield odd supports `C_y` for which

\[
\boxed{
\frac{\kappa(C_y)}{(\log\log R_y^{\circ})^A}\to\infty
\qquad\text{for every fixed }A>0,
}
\tag{21}
\]

while `|C_y|=(R_y^{\circ})^{o(1)}`.

Every such odd support is a legitimate parity companion set: put

\[
E_y=C_y-1,
\qquad
D_y=\frac{C_y-1}{2}.
\]

Then `E_y=2D_y` consists of isolated even omission locations and `E_y+1=C_y`.

Thus the parity restriction genuinely lowers the universal **power-law** chain-entropy ceiling, but it does not force bounded or polylogarithmic companion conditioning. Equation (21) is a stress test on the upper-bound mechanism only: it does not prove that the full paired coefficient inverse attains `kappa(C_y)` under every non-companion coefficient constraint.

## Finite audit

Take `L=2` and

\[
C=\{3,9,15,45\},
\qquad
D=\{1,4,7,22\},
\qquad
E=\{2,8,14,44\},
\qquad
H=45.
\]

The companion interval below `45` is the divisor diamond

\[
3<9<45,
\qquad
3<15<45.
\]

Its induced Möbius values are

\[
\mu_C(9,45)=\mu_C(15,45)=-1,
\qquad
\mu_C(3,45)=1,
\]

so the weighted row at `45` is

\[
1+\frac{15}{45}+\frac9{45}+\frac3{45}
=\frac85.
\]

Every strict chain ratio is odd: the ratios appearing here are `3`, `5` and `15`. For example `15` has the three allowed ordered factorizations `15`, `3*5`, `5*3`, so the chain-count majorant (12) safely dominates the actual Möbius coefficient. The corresponding omission starts are all even, making start-to-companion divisibility impossible exactly as in (17).

## Prior-art / novelty audit

The unrestricted ordered-factorization problem and its zeta-root exponent are classical; FD-251 already records the Kalmár / factorisatio-numerorum literature. More generally, ordered factorizations with factors drawn from a prescribed subset of integers have been studied, for example in the general framework of Hwang and Janson, *A Central Limit Theorem for Random Ordered Factorizations of Integers*, Electronic Journal of Probability 16 (2011), 347--361, DOI `10.1214/EJP.v16-858`.

No external theorem from that literature is load-bearing here. Equations (11)--(16) derive the only restricted-factorization bound needed for this result directly. A targeted search did not reveal the specific transfer from the congruence class `LD+1` to a weighted induced-divisibility Möbius norm, nor the resulting paired exact-omission threshold (6)--(10). No novelty is claimed for ordered factorizations from restricted factor sets themselves.

Because the proof is self-contained relative to FD-251 and FD-253, this pass introduces no new load-bearing literature dependency and does not require a `SOURCES.md` change.

## Boundary and research consequence

FD-253 left the parity case `L=2` as the first nontrivial test of companion-side conditioning. The test is now partly resolved: parity cannot reproduce the unrestricted FD-251 exponent because every companion-chain multiplier is odd. The universal paired coercive window expands from omission exponent `0.271352...` to `0.622214...`.

At the same time, the odd-primorial adaptation (21) shows that parity does not collapse companion incidence to a tame finite-depth or polylogarithmic object. There remains a wide gap between super-polylogarithmic lower conditioning and the universal `H^{rho_2-1+o(1)}` ceiling.

The next response-side question is now sharper: determine whether the **actual paired inverse**, including all non-companion coefficient rows, can realize a positive-power fraction of the odd-factor entropy ceiling, or whether those extra rows impose a further polynomial loss. On the source side, positivity, finite reservoir capacity, squarefree realization and full arithmetic coherence remain independent constraints.

## Status

**Proved.** The congruence restriction on chain ratios, the restricted ordered-factorization induction, the fixed-dilation companion bound, and the parity coercivity exponent are exact consequences of the current divisor-response framework. The odd-primorial lower stress test reuses the already established FD-250 rank-selected construction after deleting one prime and does not claim saturation of the paired inverse.