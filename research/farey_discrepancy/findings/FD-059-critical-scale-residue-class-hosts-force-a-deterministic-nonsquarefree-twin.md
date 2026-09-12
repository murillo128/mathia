# FD-059 — critical-scale residue-class hosts force a deterministic nonsquarefree twin

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + ZERO-FRONTIER-SPIKE + CRITICAL-HOST-SCALE + RESIDUE-CLASS-SELECTION + ADDITIVE-NONSQUAREFREE-WITNESS + QUADRATIC-OCCUPATION + ROUTE-REFINEMENT`.

`FD-054` gives the exact local criterion

\[
\frac{q\,|\mathcal H(X)|}{X}\to\infty
\]

for a squarefree host row `q` to transfer a shell spike to a bounded-distance nonsquarefree row with **first-order equality**. Its power-scale corollary was stated with the strict exponent condition `q=X^{c+o(1)}`, `c>1-\Theta`. `FD-055` then uses genuine short-interval Möbius cancellation to place the host a logarithmic factor *below* the natural scale `X/|\mathcal H(X)|` when `\Theta>0.55`.

For quadratic occupation, however, first-order equality is stronger than necessary. A fixed positive fraction of the spike already gives a comparable nonsquarefree energy term. Once the host is selected in the favorable squarefree residue class `3 mod 4`, the deterministic one-Lipschitz source law reaches the exact natural host scale

\[
q\asymp \frac{X}{|\mathcal H(X)|}
\]

with no short-interval theorem at all.

Let

\[
A_X:=|\mathcal H(X)|,
\qquad
Q_X:=\frac{X}{A_X},
\]

and suppose along an unbounded sequence that

\[
A_X\to\infty,
\qquad
Q_X\to\infty.
\tag{1}
\]

Fix any constants

\[
\lambda>1,
\qquad
\varepsilon>0.
\]

Then for all sufficiently large members of the sequence there exists a squarefree integer

\[
\boxed{
q\equiv3\pmod4,
\qquad
\lambda Q_X\le q\le(\lambda+\varepsilon)Q_X.
}
\tag{2}
\]

Put

\[
T=qX,
\qquad
q^*:=q+1,
\qquad
x^*:=\left\lfloor\frac{T}{q^*}\right\rfloor.
\]

Since `q+1` is divisible by four, `q^*` is nonsquarefree. Moreover

\[
X-x^*
=
\left\lceil\frac{X}{q+1}\right\rceil
\le
\frac{X}{q}+1
\le
\frac{A_X}{\lambda}+1.
\tag{3}
\]

The exact source coefficient law from `FD-033` gives `|\Delta\mathcal H(n)|\le1`; hence

\[
\boxed{
|\mathcal H(x^*)|
\ge
\left(1-\frac1\lambda\right)A_X-1.
}
\tag{4}
\]

For every fixed Schur-head dimension `D`, `q^*>D` eventually. Since every Jordan weight satisfies

\[
w(r)=\frac{J_2(r)}{r^2}\ge\frac1{\zeta(2)},
\]

the single row `q^*` gives

\[
\boxed{
U_{T,D}
\ge
\frac1{\zeta(2)}
\left(
\left(1-\frac1\lambda\right)A_X-1
\right)^2.
}
\tag{5}
\]

In particular, if

\[
J_q(T):=w(q)A_X^2
\]

is the squarefree host-row energy, then

\[
\boxed{
U_{T,D}
\ge
\left(
\frac{(1-1/\lambda)^2}{\zeta(2)}-o(1)
\right)J_q(T).
}
\tag{6}
\]

Thus **a comparable nonsquarefree quadratic twin already exists at the exact deterministic scale `q\asymp X/A_X`**. The condition `qA_X/X\to\infty` in `FD-054` is the threshold for preserving the spike to relative error `o(1)`, not the threshold for preserving a positive fraction of its quadratic energy.

## 1. Squarefree hosts in the favorable residue class are elementary and plentiful

For completeness, (2) requires no prime-distribution theorem. For real `Y<Z`, inclusion-exclusion gives

\[
\sum_{\substack{Y<n\le Z\\n\equiv3\ (4)}}\mu(n)^2
=
\sum_{\substack{d\le\sqrt Z\\d\ \mathrm{odd}}}
\mu(d)
\#\left\{
\frac{Y}{d^2}<m\le\frac{Z}{d^2}:m\equiv3\pmod4
\right\}.
\]

Because `d` is odd, `d^2\equiv1 mod 4`, so

\[
\#\left\{
\frac{Y}{d^2}<m\le\frac{Z}{d^2}:m\equiv3\pmod4
\right\}
=
\frac{Z-Y}{4d^2}+O(1).
\]

Therefore

\[
\boxed{
\#\{Y<n\le Z:n\equiv3\pmod4,\ \mu(n)^2=1\}
=
\frac{Z-Y}{3\zeta(2)}+O(\sqrt Z).
}
\tag{7}
\]

Here

\[
\sum_{d\ \mathrm{odd}}\frac{\mu(d)}{d^2}
=
\prod_{p>2}(1-p^{-2})
=
\frac{4}{3\zeta(2)}.
\]

Taking `Y=\lambda Q_X` and `Z=(\lambda+\varepsilon)Q_X`, condition (1) makes the main term in (7) dominate the error. This proves (2). The residue condition is useful only because it makes the nearest nonsquarefree witness **exactly one row away**.

## 2. The zero-frontier row exponent is inclusive for adaptive host existence

Now take the false-RH zero-frontier spike sequence used in `FD-054`--`FD-058`, with

\[
A_X=X^{\Theta+o(1)},
\qquad
\frac12<\Theta<1.
\tag{8}
\]

Then

\[
Q_X=X^{1-\Theta+o(1)},
\]

so every host selected by (2) satisfies

\[
q=X^{1-\Theta+o(1)}.
\tag{9}
\]

At the physical horizon `T=qX`, this becomes

\[
\boxed{
q=T^{\alpha_\Theta+o(1)},
\qquad
\alpha_\Theta:=\frac{1-\Theta}{2-\Theta}.
}
\tag{10}
\]

Equations (5)--(6) therefore give a comparable nonsquarefree quadratic twin **at the exact row exponent `\alpha_\Theta` for every `\Theta>1/2`**, including the strip `1/2<\Theta\le0.55` where the all-short-interval theorem used in `FD-055` is unavailable.

This does not contradict the strict-exponent statement in `FD-054`. There the power comparison `c>1-\Theta` was a convenient sufficient condition ensuring `qA_X/X\to\infty` for an arbitrary host family described only by its power exponent. The present result changes the quantifier: it **selects** a host in a positive-density residue class at the actual adaptive scale `X/A_X`, and asks only for constant-factor energy transfer.

There is also a first-order endpoint version. Let `\lambda_X\to\infty` with `\lambda_X=X^{o(1)}` and choose a squarefree `q\equiv3 mod 4` in

\[
[\lambda_XQ_X,(1+\varepsilon)\lambda_XQ_X].
\]

The same count (7) supplies such a host, while (3) gives

\[
X-x^*=o(A_X).
\]

Hence

\[
\mathcal H(x^*)=\mathcal H(X)+o(A_X),
\tag{11}
\]

but still

\[
q=X^{1-\Theta+o(1)}
=T^{\alpha_\Theta+o(1)}.
\tag{12}
\]

So even first-order deterministic transfer reaches the **power-exponent boundary** when a subpower factor above `X/A_X` is retained. What deterministic bounded increments cannot do is cross to hosts with

\[
\frac{qA_X}{X}\to0.
\tag{13}
\]

That is the genuinely different regime opened by `FD-055` and targeted by `FD-056`--`FD-058`.

## 3. The short-interval and maximal-localization targets move below the natural scale

The correct three-way distinction is now explicit.

If

\[
\frac{qA_X}{X}\to\infty,
\]

`FD-054` gives first-order deterministic transfer. If

\[
\frac{qA_X}{X}\asymp1,
\]

the present residue-class selection gives deterministic constant-factor transfer, which is already enough to force a comparable positive quadratic contribution. If

\[
\frac{qA_X}{X}\to0,
\]

the quotient displacement is larger than the spike height and bounded increments alone no longer prevent complete cancellation.

This sharpens the interpretation of the later short-interval findings. `FD-055` chooses

\[
q\asymp\frac{X}{A_X(\log X)^B},
\]

so `qA_X/X\asymp(\log X)^{-B}\to0`: its real gain is **logarithmic penetration below the deterministic critical scale**, not merely attainment of the power exponent `\alpha_\Theta`. Likewise, the maximal ambient-window program of `FD-056`--`FD-058` becomes load-bearing when the allowed source displacement is

\[
R_X=A_XL_X,
\qquad
L_X\to\infty,
\]

which corresponds to hosts `q\asymp X/R_X=o(X/A_X)`. At `L_X\asymp1`, a suitable residue-class host already supplies constant-factor occupation without any exceptional-set localization theorem.

This does not solve the global occupation problem. A single comparable nonsquarefree row can still be overwhelmed by unrelated low-row contributions to `E_{T,D}`, so no fixed lower bound for `U_{T,D}/E_{T,D}` follows. The durable correction is narrower: **the unresolved source-regularity bill begins only after crossing below the natural host scale `X/A_X`; it is not needed merely to reach the zero-frontier row exponent.**

## 4. Adversarial and prior-art boundary

The argument is deliberately elementary. The exact displacement identity in (3), the one-Lipschitz source law, the uniform Jordan lower bound, and the squarefree residue-class count (7) are all explicit. The result fails to give a positive constant when `\lambda\le1`, and it says nothing about an arbitrary preassigned critical-scale host: it proves existence of a favorable squarefree host at the same scale. It also does not upgrade one-row transfer to a pointwise lower bound for `U/E`.

There is no conflict with `FD-057`: its inverse-length barrier concerns arguments that must locate a good **represented start** inside the sparse reciprocal-floor sample when the desired transfer length exceeds the deterministic spike scale. There is no conflict with `FD-058` either: maximal ambient-window localization remains a valid way to bypass that sample sparsity, but its quantitative exceptional-measure problem is relevant to the below-critical regime (13), not to the constant-factor critical host constructed here.

A targeted prior-art search around squarefree Farey denominators, Jordan-totient weighting, Mertens/Farey transforms, and adjacent nonsquarefree rows found the expected literature on restricted Farey subsequences but no matching statement about the present adaptive shell-source/Jordan transfer. No novelty is claimed for squarefree counting in arithmetic progressions, the multiple-of-four observation, or bounded increments. The Mathia-specific content is the exact scale separation relative to `FD-054`--`FD-058`. No new external theorem is load-bearing, so `SOURCES.md` remains unchanged.