# FD-063 — four-adic density makes subcritical packet transfer uniform over a host corridor

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + SHORT-INTERVAL-MOBIUS + FOUR-ADIC-NONSQUAREFREE-DENSITY + HOST-CORRIDOR-UNIFORMITY + BELOW-CRITICAL-HOST + ROUTE-REFINEMENT`.

`FD-062` proves that known all-short-interval Möbius cancellation can carry a growing packet of nonsquarefree Jordan rows while the host lies logarithmically below the deterministic scale `X/|\mathcal H(X)|`. Its construction uses a nested CRT system to force **every** row `q+1,...,q+K_X` to be nonsquarefree and then finds one squarefree host in the resulting sparse progression.

For the occupation lower bound, that much arithmetic engineering is unnecessary. Every interval of `K` consecutive row indices already contains `K/4+O(1)` multiples of four, hence that many nonsquarefree rows. Combining this elementary four-adic density with the same source estimate makes the whole packet transfer **uniform over an interval of host rows** rather than existential in one CRT class.

Let

\[
A_X:=|\mathcal H(X)|,
\qquad
L_X:=\log X,
\qquad
R_X:=A_XL_X^B.
\]

Fix

\[
\vartheta>0.55,
\qquad B>0,
\qquad \kappa>0,
\qquad B+\kappa<\frac13,
\tag{1}
\]

and suppose along an unbounded sequence that

\[
\boxed{R_X\ge X^\vartheta.}
\tag{2}
\]

Put

\[
K_X:=\lfloor L_X^\kappa\rfloor,
\qquad
Y_X:=\frac{X}{8R_X},
\tag{3}
\]

and consider **every integer host**

\[
\boxed{Y_X\le q\le2Y_X.}
\tag{4}
\]

For `1\le d\le K_X` set

\[
T_q:=qX,
\qquad
x_{q,d}:=\left\lfloor\frac{T_q}{q+d}\right\rfloor.
\tag{5}
\]

Then, uniformly in both `q` and `d`,

\[
\boxed{
\mathcal H(x_{q,d})
=
\mathcal H(X)+o(A_X).
}
\tag{6}
\]

Consequently, for every fixed Schur-head dimension `D`, uniformly for all integer hosts in (4),

\[
\boxed{
U_{T_q,D}
\ge
\left(\frac1{4\zeta(2)}-o(1)\right)
K_XA_X^2.
}
\tag{7}
\]

At the same time every such host lies below the deterministic critical scale:

\[
\boxed{
\frac1{8L_X^B}
\le
\frac{qA_X}{X}
\le
\frac1{4L_X^B}
\longrightarrow0.
}
\tag{8}
\]

Thus the logarithmic short-interval budget of `FD-062` buys not merely one growing packet on one carefully engineered host. It buys a growing nonsquarefree packet on an **entire host corridor of length `\asymp X/(A_XL_X^B)`**. The CRT restriction was sufficient for `FD-062` but is not intrinsic to the occupation mechanism.

## 1. The same source estimate is uniform over the whole host corridor

The Davenport-type source bound already used in `FD-062` gives, for every fixed `C>0`,

\[
\mathcal H(X)
\ll_C
\frac{X}{(\log X)^C}+X^{1/2}.
\tag{9}
\]

Taking `C` sufficiently large relative to `B+\kappa` gives

\[
R_XK_X=A_XL_X^{B+\kappa}=o(X),
\qquad
Y_X/K_X\to\infty.
\tag{10}
\]

Hence every host in (4) satisfies `q\to\infty` and `K_X=o(q)` uniformly.

For `1\le d\le K_X`, since `X` is integral,

\[
h_{q,d}:=X-x_{q,d}
=
\left\lceil\frac{dX}{q+d}\right\rceil.
\tag{11}
\]

Eventually `q+d\le2q`. Using (4),

\[
\boxed{
2R_X\le h_{q,d}\le9K_XR_X
}
\tag{12}
\]

uniformly in the corridor. The lower bound follows from `q\le X/(4R_X)` and `d\ge1`; the upper bound follows from `q\ge X/(8R_X)` and `d\le K_X`.

By (2), every transfer interval has length at least `2X^\vartheta`, while (10) gives `h_{q,d}=o(X)` and therefore `x_{q,d}\sim X` uniformly. The `FD-048` transfer of the Matomäki--Teräväinen all-short-interval theorem applies to `(x_{q,d},X]`: for every fixed `0<\eta<1/3`,

\[
|\mathcal H(X)-\mathcal H(x_{q,d})|
\ll_{\vartheta,\eta}
\frac{h_{q,d}}{L_X^{1/3-\eta}}.
\tag{13}
\]

Choose `\eta>0` so that

\[
B+\kappa+\eta<\frac13.
\tag{14}
\]

Equations (12)--(14) give

\[
\max_{\substack{Y_X\le q\le2Y_X\\1\le d\le K_X}}
|\mathcal H(X)-\mathcal H(x_{q,d})|
\ll
A_XL_X^{B+\kappa-1/3+\eta}
=o(A_X),
\tag{15}
\]

which is (6). No residue condition, squarefreeness condition, or CRT selection is used in this transfer step.

## 2. Multiples of four supply the packet for every host

For a fixed host `q`, define

\[
\mathcal D_q
:=
\{1\le d\le K_X:4\mid q+d\}.
\tag{16}
\]

Among any `K_X` consecutive integers there are at least `\lfloor K_X/4\rfloor` multiples of four, so

\[
|\mathcal D_q|
\ge
\left\lfloor\frac{K_X}{4}\right\rfloor
=
\frac{K_X}{4}+O(1).
\tag{17}
\]

For every `d\in\mathcal D_q`, the Jordan row `q+d` is nonsquarefree. By (10), these rows eventually exceed every fixed `D`. The uniform Jordan bound

\[
w(r)=\frac{J_2(r)}{r^2}
\ge\frac1{\zeta(2)}
\tag{18}
\]

and (6) therefore give

\[
\begin{aligned}
U_{T_q,D}
&\ge
\sum_{d\in\mathcal D_q}
 w(q+d)\mathcal H(x_{q,d})^2\\
&\ge
\left(\frac1{\zeta(2)}-o(1)\right)
|\mathcal D_q|A_X^2,
\end{aligned}
\tag{19}
\]

uniformly over the corridor. Equation (17) proves (7).

The factor `1/4` is deliberately elementary, not optimized. The natural density of nonsquarefree integers is larger, but no density theorem is needed: divisibility by `4` alone already supplies a deterministic packet with the required linear-in-`K_X` cardinality.

## 3. Squarefree hosts remain plentiful without sacrificing host entropy

If one wants to retain the `FD-062` comparison with a selected squarefree host row, no sparse progression is necessary. The elementary squarefree count in a dyadic interval gives

\[
\#\{Y_X\le q\le2Y_X:\mu(q)^2=1\}
=
\frac{6}{\pi^2}Y_X+O(\sqrt{Y_X}).
\tag{20}
\]

Equation (9) implies `Y_X\to\infty`, so a positive proportion of the entire corridor consists of squarefree hosts. For every such `q`,

\[
J_q(T_q)
:=w(q)\mathcal H(X)^2
\le A_X^2,
\]

and (7) yields

\[
\boxed{
\frac{U_{T_q,D}}{J_q(T_q)}
\ge
\left(\frac1{4\zeta(2)}-o(1)\right)K_X
\longrightarrow\infty.
}
\tag{21}
\]

The strengthening relative to `FD-062` is therefore not the power exponent or the logarithmic budget. Those remain exactly the same. The strengthening is the **quantifier on the host**: packet transfer holds for every host in a macroscopic row corridor, and there are `\asymp Y_X` squarefree hosts available inside it.

On a false-RH frontier sequence

\[
A_X=X^{\Theta+o(1)},
\qquad \Theta>0.55,
\tag{22}
\]

this corridor contains

\[
X^{1-\Theta+o(1)}
\]

integer hosts up to logarithmic factors, while every one of their horizons carries the lower bound (7). Thus any future same-horizon denominator argument may choose a favorable `q` from a full corridor rather than first intersecting its criterion with the sparse CRT class from `FD-062`.

## 4. What changes in the live obstruction

This does not improve the current polynomial lower-rate exponent for

\[
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}.
\]

Applying only the generic zero-frontier envelope `E_{T,D}\ll_{D,\sigma}T^{2\sigma}` still loses the same uncontrolled subpower factors discussed in `FD-061`--`FD-062`. Host multiplicity by itself does not upper-bound the denominator at any particular horizon.

What the result removes is a separate combinatorial bottleneck. The growing packet no longer consumes host entropy through a modulus

\[
M_{K_X}=\prod_{d\le K_X}p_d^2.
\]

The next same-horizon theorem is therefore free to average over hosts, impose an additional denominator condition, or select a host after estimating `E_{qX,D}` without having to preserve a growing CRT congruence class. If such a denominator estimate still fails, the failure is genuinely in the physical energy across the host corridor rather than in packet availability.

The all-short-interval restriction is unchanged. The argument still needs `\vartheta>0.55` and the same budget `B+\kappa<1/3`; it gives no new transfer theorem in the unresolved `\Theta\le0.55` range. It also proves no positive lower bound for `U/E` and no new zero-free region.

## 5. Prior-art and falsification boundary

The only analytic input is the Matomäki--Teräväinen all-short-interval Möbius estimate already transferred to the physical source in `FD-048` and already anchored in `SOURCES.md`. The Jordan lower bound, the source convolution, and the squarefree dyadic count are existing line ingredients. No new external theorem is load-bearing, so `SOURCES.md` remains unchanged.

A targeted prior-art search across Farey discrepancy, Möbius short intervals, Jordan-totient energies, and nonsquarefree denominator occupation located the expected separate Farey/Jordan and short-interval literature but no statement matching this host-uniform reciprocal-floor packet transfer. No novelty is claimed for the elementary observation that one quarter of the integers in a long interval are divisible by four, or for squarefree counting. The Mathia-specific delta is that these trivial row facts, combined with the physical quotient-shell transfer, remove the CRT host-selection cost from `FD-062` entirely.

The claim is falsified if the transfer estimate (15) is not uniform over the corridor, if `K_X=o(q)` fails under the stated physical source bound, or if the rows counted in (16) do not enter the same `U_(T_q,D)` normalization. It must not be cited as improving the `1/3` logarithmic saving, lowering the `0.55` all-interval threshold, or controlling the full same-horizon denominator. Its exact contribution is **uniform growing nonsquarefree occupation across an entire below-critical host corridor**.