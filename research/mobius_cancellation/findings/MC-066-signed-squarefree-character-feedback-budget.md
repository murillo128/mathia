# MC-066 — Signed squarefree-character feedback removes the conductor-zero L1 floor but exposes a power-weighted split-prime budget

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `PRIOR-ART-CORRECTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let `q` be an odd prime, let

\[
\chi(n)=\left(\frac{n}{q}\right),
\]

and define the square-free quadratic comparator

\[
f_\chi(n):=\mu(n)^2\chi(n),
\qquad
F_\chi(X):=\sum_{n\le X}f_\chi(n).
\tag{1}
\]

`MC-065` showed that the **absolute coefficient-transfer** route from `F_chi(X)` to `M(X)` pays an internal-conductor mismatch of order at least `X/q` and, after coupling to the classical Munsch/Burgess squarefree-character bound, bottoms out at the method-specific exponent `11/19`.

There is an exact signed alternative. Put

\[
h_\chi:=1*f_\chi
\]

under Dirichlet convolution. Then

\[
\boxed{f_\chi=\mu*h_\chi}
\tag{2}
\]

and, for every prime `p` and integer `a>=1`,

\[
\boxed{h_\chi(p^a)=1+\chi(p).}
\tag{3}
\]

Thus the local positive kernel has three exact regimes:

\[
h_\chi(p^a)=
\begin{cases}
0,&\chi(p)=-1,\\
2,&\chi(p)=+1,\\
1,&p=q.
\end{cases}
\tag{4}
\]

Consequently, for every real `X>=1`,

\[
\boxed{
F_\chi(X)=\sum_{d\le X}h_\chi(d)M(X/d),
}
\tag{5}
\]

so

\[
\boxed{
M(X)=F_\chi(X)-\sum_{2\le d\le X}h_\chi(d)M(X/d).
}
\tag{6}
\]

This converts the surviving signed escape in `MC-065` into a precise feedback budget. For `theta>0`, define

\[
R_\theta(X;\chi)
:=
\sum_{2\le d\le X}\frac{h_\chi(d)}{d^\theta}.
\tag{7}
\]

If an inductive bound

\[
|M(y)|\le C y^\theta
\qquad(1\le y<X)
\tag{8}
\]

is already available, then `(6)` gives the exact one-step estimate

\[
\boxed{
|M(X)|
\le
|F_\chi(X)|+C X^\theta R_\theta(X;\chi).
}
\tag{9}
\]

Hence, for any `delta in (0,1)`, the two inequalities

\[
|F_\chi(X)|\le \delta C X^\theta,
\qquad
R_\theta(X;\chi)\le1-\delta
\tag{10}
\]

are sufficient to close the same exponent at scale `X`.

The crucial correction to the `MC-065` frontier is that the character zero at its conductor no longer forces an `X/q` loss in this signed architecture. The conductor prime contributes to the feedback kernel only through its prime powers,

\[
\sum_{1\le j:\ q^j\le X}q^{-j\theta}
\le
\frac{q^{-\theta}}{1-q^{-\theta}},
\tag{11}
\]

and in the full Euler upper envelope it multiplies the remaining kernel by only `(1-q^{-theta})^{-1}` when `q<=X`. For a moving conductor `q->infinity`, this is `1+O(q^{-theta})`.

The price is elsewhere and is stronger than ordinary prime-harmonic agreement. Let

\[
B_X(\chi)
:=\{p\le X:\ p\ne q,\ \chi(p)=+1\}.
\tag{12}
\]

Because every split prime contributes the term `2p^{-theta}` directly to `(7)`, a necessary condition for the triangle-inequality closure `R_theta<1` is

\[
\boxed{
2\sum_{p\in B_X(\chi)}p^{-\theta}
+\mathbf 1_{q\le X}q^{-\theta}
<1.
}
\tag{13}
\]

More generally, positivity and `(4)` give

\[
\boxed{
1+R_\theta(X;\chi)
\le
Q_\theta(q;X)
\prod_{p\in B_X(\chi)}
\frac{1+p^{-\theta}}{1-p^{-\theta}},
}
\tag{14}
\]

where

\[
Q_\theta(q;X)=
\begin{cases}
(1-q^{-\theta})^{-1},&q\le X,\\
1,&q>X.
\end{cases}
\tag{15}
\]

The product in `(14)` is an upper envelope obtained by dropping the truncation `d<=X`; `(13)` is an exact necessary lower-bound test from the prime terms of `(7)`.

Therefore signed feedback genuinely removes the **specific conductor-zero absolute-fidelity charge** behind `11/19`, but it does not produce a cheap Mertens bootstrap. It replaces that charge by a power-sensitive control problem for the quadratic-residue primes. Near the RH exponent, the relevant weight is approximately `p^{-1/2}`, not the ordinary `1/p` weight used by the one-scale defect `A_X(chi)`.

No improved bound for `M(X)` is claimed.

## 1. Exact convolution and local kernel

Since `f_chi` is square-free-supported,

\[
f_\chi(p)=\chi(p),
\qquad
f_\chi(p^a)=0\quad(a\ge2).
\tag{16}
\]

For `h_chi=1*f_chi`, multiplicativity gives

\[
h_\chi(p^a)
=\sum_{j=0}^a f_\chi(p^j)
=1+\chi(p),
\]

proving `(3)` and `(4)`. Because `mu*1` is the Dirichlet-convolution identity,

\[
\mu*h_\chi
=\mu*(1*f_\chi)
=(\mu*1)*f_\chi
=f_\chi,
\]

which proves `(2)`.

Summing `(2)` through `X` and grouping by the `h_chi` divisor gives `(5)`. The `d=1` term is `M(X)`, giving `(6)`. These are finite coefficient identities; they use no analytic continuation, zero-free region, or asymptotic character-sum theorem.

At the Dirichlet-series level, the same standard Euler algebra is

\[
\sum_{n\ge1}\frac{f_\chi(n)}{n^s}
=
\prod_p(1+\chi(p)p^{-s})
=
\frac{L(s,\chi)}{L(2s,\chi^2)}
\qquad(\operatorname{Re}s>1),
\tag{17}
\]

and multiplication by `zeta(s)` generates `h_chi`. The finite convolution, rather than continuation of `(17)`, is the object used here.

## 2. The conductor zero is signed-feedback benign, not absent

When `q<=X`, `MC-065` observes that `chi(q)=0` creates coefficient mismatches on every square-free multiple of `q`. Any coefficientwise absolute transfer therefore pays a cost of power scale at least `X/q`.

Equation `(6)` reorganizes those same coefficients before taking absolute values. The local conductor factor is now

\[
1+q^{-\theta}+q^{-2\theta}+\cdots,
\]

so the isolated `q`-adic feedback tail is exactly bounded by `(11)`. In the special case where `B_X(chi)` is empty, `(5)` becomes the transparent recurrence

\[
F_\chi(X)
=
\sum_{0\le j:\ q^j\le X}M(X/q^j),
\tag{18}
\]

and the total nontrivial feedback weight is at most `q^{-theta}/(1-q^{-theta})`. Thus for `q^theta>2`, the conductor-only part is absorbable in a same-exponent induction.

This does **not** mean conductor dependence has disappeared. Munsch's comparator bound from `MC-S38` still carries the factor `q^(3/16)` in `F_chi(X)`, and mixed terms `q^j b` replicate whatever split-prime feedback is present. The correction is narrower: the internal character zero does not itself force the `q >= X^(1-theta)` lower bound that arose from absolute coefficient fidelity in `MC-065`.

## 3. Split primes become the exact power-aware obstruction

For every `p in B_X(chi)`, equation `(4)` gives

\[
h_\chi(p)=2.
\]

Since `h_chi` is nonnegative, the prime terms alone imply

\[
R_\theta(X;\chi)
\ge
2\sum_{p\in B_X(\chi)}p^{-\theta}
+\mathbf1_{q\le X}q^{-\theta},
\]

which proves `(13)`.

The complete local weighted sums are

\[
1+\sum_{a\ge1}\frac{2}{p^{a\theta}}
=
\frac{1+p^{-\theta}}{1-p^{-\theta}}
\qquad(\chi(p)=+1)
\tag{19}
\]

and

\[
1+\sum_{a\ge1}\frac1{q^{a\theta}}
=
\frac1{1-q^{-\theta}}.
\tag{20}
\]

Extending the finite positive sum in `(7)` to all products generated by primes through `X` gives `(14)`.

This identifies the information carrier required by the simplest signed bootstrap. A small ordinary defect

\[
A_X(\chi)=\sum_{p\le X}\frac{|1+\chi(p)|}{p-1}
\]

controls the same split primes only with approximately `1/p` weight. For every fixed `theta<1`, `(13)` instead demands control at the much stronger `p^{-theta}` scale. The gap is exactly the kind of ordinary-versus-power cancellation distinction established abstractly by Jung and Lemke Oliver (`MC-S7`) and already exposed for terminal-prime perturbations in `MC-047`--`MC-048`.

In particular, a quadratic comparator that is merely close to the Möbius prime signs in the harmonic metric used by `MC-060`--`MC-063` need not have a small feedback budget `(7)`. Signed transfer does not let that one-scale information silently upgrade itself.

## 4. Coupling to the classical squarefree-character bound

`MC-S38` gives for prime `q`, at power level,

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16}\,\operatorname{polylog}(Xq).
\tag{21}
\]

Thus an attempted exponent `theta>1/2` through `(9)` must satisfy two qualitatively different requirements: enough conductor control to make `(21)` fit inside the `delta C X^theta` budget, and enough **power-weighted nonresidue structure** to make `R_theta(X;chi)<1`.

Ignoring logarithmic margins, the first asks roughly

\[
q\lesssim X^{\frac{16}{3}(\theta-1/2)}.
\tag{22}
\]

Unlike the absolute route of `MC-065`, there is no opposing lower bound `q\gtrsim X^{1-theta}` coming solely from the zero at `q`. But `(13)` supplies a new opposing condition: the selected low-conductor character must have so little `p^{-theta}` mass on quadratic-residue primes through `X` that its entire positive feedback remains absorbable.

For a fixed nonprincipal quadratic character this cannot persist as `X` grows: primes with `chi(p)=+1` occupy the usual positive-density residue classes, so standard primes-in-progressions theory makes their `p^{-theta}` mass diverge for every fixed `theta<1`. A successful scheme must therefore remain genuinely moving and nonuniform, or exploit signed cancellation among the feedback terms beyond the triangle inequality in `(9)`.

The direct frontier is therefore sharper than simply asking for a better squarefree-character theorem: **small conductor helps the comparator sum, while the same character must simultaneously suppress a power-weighted population of split primes.**

## 5. Prior art and novelty boundary

No standalone novelty is claimed for the convolution identities. `MC-051` already proves, for the larger class of real square-free-supported amplitudes, that `h=1*f` is coefficientwise nonnegative and that its local coefficients are `1+f(p)`. The present finding is the finite-scale specialization `f=mu^2 chi`, with special attention to the internal-conductor regime left open by `MC-065`.

`MC-S7` is the primary prior-art anchor for the fact that ordinary pretentiousness does not automatically detect power cancellation and for stronger prime-power-sensitive transfer notions. `MC-047`--`MC-048` already show the same distinction on explicit terminal-prime perturbations. `MC-S38` is the direct classical squarefree-character bound used for `F_chi`.

A targeted literature audit of squarefree character sums and power-cancellation-aware pretentiousness found these established surrounding mechanisms and no basis for treating `(2)`--`(6)` as a new analytic-number-theory theorem. The durable contribution here is the exact research-frontier correction: the `11/19` conductor-zero floor is specific to **absolute coefficient transfer**; the natural signed convolution escape survives that floor but immediately exposes a stronger power-weighted split-prime feedback obligation.

## 6. Boundaries and falsification tests

The result is deliberately a mechanism audit, not a Mertens theorem.

- Equation `(9)` takes absolute values after the signed convolution recurrence. It does not exploit cancellation between distinct terms `M(X/d)`. A more structured signed argument may beat the `R_theta<1` requirement.
- Equation `(14)` is an upper envelope, not an equality for the truncated sum, because products exceeding `X` are included after the truncation is dropped. Equation `(13)` is the exact necessary prime-term test for this triangle-inequality bootstrap.
- The conductor-zero correction applies to the **transfer** side only. The comparator bound `(21)` remains conductor-dependent.
- A small harmonic defect `A_X(chi)` is not claimed to imply a small `R_theta`; the point of the finding is precisely that it does not supply the required weight scale.
- The fixed-character divergence statement uses standard distribution of primes in residue classes and is not asserted uniformly for a conductor moving with `X`.
- The result neither proves existence nor nonexistence of moving characters satisfying both `(21)` and `(13)` at useful scales.

The exact claims are falsified if `(3)` fails, if `(5)` does not follow from Dirichlet convolution, if the conductor local coefficient is not one, or if the positive prime terms do not force `(13)`. Each of these steps is finite and coefficient-level.

## Consequence for the active frontier

`MC-065` correctly identified `11/19` as the best exponent certified by its **absolute** one-character package. The signed convolution shows that this number is not an intrinsic barrier created by putting the conductor inside the prefix. The conductor zero can be reorganized into a geometrically decaying feedback tail.

The surviving quadratic-comparator question is now more precise: can one control a moving character simultaneously in the Munsch/Burgess conductor budget and in the power-weighted split-prime feedback budget, or can one exploit cancellation among the feedback terms strongly enough to avoid the positive-kernel triangle bound? Ordinary `1/p` agreement, by itself, is below the information scale required by this escape.