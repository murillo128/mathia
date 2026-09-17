# FD-183 — Subcritical prime-extension energy forces semiprime-scale support

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational source rigidity / two-generation prime-fan bootstrap / semiprime support lower bound / fixed-prime signed perturbations
- **Depends on:** FD-147, FD-180, FD-181
- **Classification:** `EXACT-DERIVED + RELATIONAL-RIGIDITY + TWO-GENERATION-BOOTSTRAP + SEMIPRIME-SUPPORT-LOWER-BOUND + FIXED-PRIME-SIGNED-PERTURBATIONS`

## Claim

`FD-181` proves that arbitrary signed perturbations of Möbius cannot have subcritical prime-extension defect when their changed-coordinate support is `o(x/log x)`, even if prime coordinates themselves move. That argument deliberately stops at the size of one prime fan. On the important fixed-prime fibre, the fan obstruction bootstraps through one more multiplicative generation: making the first fan almost relation-consistent forces almost all of a full squarefree semiprime layer to move.

Let `a` be a real-valued arithmetic source satisfying

\[
a(1)=1,
\qquad
a(n)=0\quad\text{whenever }\mu(n)=0,
\qquad
a(p)=-1\quad(p\text{ prime}).
\tag{1}
\]

Write

\[
\delta(n):=a(n)-\mu(n),
\qquad
S:=\{n:\delta(n)\ne0\},
\qquad
S(x):=|S\cap[1,x]|,
\tag{2}
\]

and suppose `a!=mu`. Let

\[
n_0:=\min S,
\qquad
\Delta:=|\delta(n_0)|>0.
\tag{3}
\]

For fixed `1<=q<infinity`, retain the true prime-extension energy of `FD-181`,

\[
\mathcal M_{a,q}(x)
:=
\sum_{(n,pn)\in E_x}
|a(pn)-a(p)a(n)|^q,
\tag{4}
\]

where

\[
E_x:=\{(n,pn):pn\le x,\ p\text{ prime},\ p\nmid n,\ \mu^2(n)=1\}.
\tag{5}
\]

If

\[
\boxed{
\mathcal M_{a,q}(x)=o(x/\log x),
}
\tag{6}
\]

then necessarily

\[
\boxed{
S(x)
\ge
\left(\frac1{n_0}+o(1)\right)
\frac{x\log\log x}{\log x}.
}
\tag{7}
\]

Thus screening one fixed source error below the `FD-181` prime-fan energy scale requires not merely one prime fan of changed coefficients but asymptotically a complete **second squarefree multiplicative layer**.

Equivalently, on the fixed-prime fibre (1),

\[
\boxed{
S(x)=o\!\left(\frac{x\log\log x}{\log x}\right)
\quad\text{and}\quad
\mathcal M_{a,q}(x)=o(x/\log x)
\quad\Longrightarrow\quad
a=\mu.
}
\tag{8}
\]

Using the edge count from `FD-147`,

\[
|E_x|
=
\frac{x}{\zeta(2)}\log\log x+O(x),
\tag{9}
\]

condition (6) is equivalent to the same normalized subcritical rate used in `FD-181`,

\[
\left(
\frac{\mathcal M_{a,q}(x)}{|E_x|}
\right)^{1/q}
=
o\!\left((\log x\,\log\log x)^{-1/q}\right).
\tag{10}
\]

So, after fixing the prime coordinates, the support regime in which that rate forces Möbius expands by a full factor `log log x`, from `o(x/log x)` in the general moving-prime theorem to `o(x log log x/log x)` here.

## 1. Fixed primes make every edge defect additive in `delta`

For `p` prime with `p\nmid n`, (1) gives `a(p)=-1`, while Möbius gives `mu(pn)=-mu(n)`. Therefore

\[
\begin{aligned}
a(pn)-a(p)a(n)
&=
\mu(pn)+\delta(pn)+\mu(n)+\delta(n)\\
&=
\boxed{\delta(pn)+\delta(n)}.
\end{aligned}
\tag{11}
\]

This identity is the only source-specific algebra used below. No sign, bounded-amplitude, deletion-only, or multiplicativity assumption is imposed on the composite coordinates.

Apply (11) first at the minimal changed coordinate `n_0`. For every prime `p\nmid n_0`,

\[
D_p
:=
a(n_0p)-a(p)a(n_0)
=
\delta(n_0p)+\delta(n_0).
\tag{12}
\]

Call `p` **root-bad** when

\[
|D_p|>\Delta/2.
\tag{13}
\]

If `A(t)` counts root-bad primes `p<=t`, `p\nmid n_0`, then all corresponding edges occur by scale `n_0t`, and hence

\[
A(t)(\Delta/2)^q
\le
\mathcal M_{a,q}(n_0t).
\tag{14}
\]

Under (6),

\[
\boxed{
A(t)=o(t/\log t).
}
\tag{15}
\]

Every root-good prime satisfies

\[
|\delta(n_0p)|
\ge
\Delta-|D_p|
\ge
\Delta/2,
\tag{16}
\]

so in particular

\[
n_0p\in S.
\tag{17}
\]

Thus subcritical relation energy forces almost the entire first prime fan to become genuinely changed coordinates, not merely coordinates with a small relation error.

## 2. Root-bad primes occupy negligible reciprocal prime mass

The next generation is counted by products of two primes, so cardinal density of the exceptional prime set is not quite enough; the relevant quantity is its reciprocal prime mass.

From (15), partial summation gives

\[
\boxed{
\sum_{\substack{p\le y\\p\text{ root-bad}}}\frac1p
=o(\log\log y).
}
\tag{18}
\]

Indeed, with `A(t)` as above,

\[
\sum_{\substack{p\le y\\p\text{ root-bad}}}\frac1p
=
\frac{A(y)}y+
\int_{2^-}^{y}\frac{A(t)}{t^2}\,dt.
\tag{19}
\]

For every `epsilon>0`, (15) gives `A(t)<=epsilon t/log t` beyond a fixed threshold. The tail of (19) is then at most `epsilon log log y+O_epsilon(1)`, proving (18).

This step is important because a sparse exceptional set may still contain small primes, and one small prime participates in many semiprimes. Equation (18), rather than mere zero relative prime density, is what shows that all root-bad primes together remove only a negligible fraction of the semiprime layer.

## 3. Almost every squarefree semiprime gives a changed grandchild

Put

\[
X:=x/n_0.
\tag{20}
\]

Consider squarefree semiprimes

\[
m=p r\le X,
\qquad p<r,
\qquad p,r\nmid n_0.
\tag{21}
\]

Landau's fixed-rank asymptotic, already anchored in `SOURCES.md`, gives

\[
\#\{m\le X:\mu^2(m)=1,\ \omega(m)=2\}
\sim
\frac{X\log\log X}{\log X}.
\tag{22}
\]

Excluding the finitely many semiprimes divisible by a prime factor of `n_0` costs only `O_{n_0}(X/log X)`.

Now discard semiprimes whose smaller factor `p` is root-bad. Since `p<=sqrt X`, the prime number theorem (or a standard Chebyshev upper bound) gives uniformly

\[
\pi(X/p)
\ll
\frac{X}{p\log X}.
\tag{23}
\]

Hence the number discarded for this reason is at most

\[
\ll
\frac{X}{\log X}
\sum_{\substack{p\le\sqrt X\\p\text{ root-bad}}}\frac1p
=
o\!\left(\frac{X\log\log X}{\log X}\right)
\tag{24}
\]

by (18). Therefore the number of semiprimes (21) whose smaller factor is root-good is

\[
\boxed{
(1+o(1))\frac{X\log\log X}{\log X}.
}
\tag{25}
\]

Fix one such semiprime `m=pr`. By (16), the parent `n_0p` is changed and has

\[
|\delta(n_0p)|\ge\Delta/2.
\tag{26}
\]

If the grandchild `n_0pr` were unchanged, then (11) on the edge `(n_0p,n_0pr)` would give

\[
|a(n_0pr)-a(r)a(n_0p)|
=
|\delta(n_0p)|
\ge
\Delta/2.
\tag{27}
\]

Distinct semiprimes in (21) give distinct chosen edges because the smaller prime `p` and the child `n_0pr` determine the pair. Consequently the number of semiprimes counted in (25) whose grandchild is **not** in `S` is at most

\[
(2/\Delta)^q\mathcal M_{a,q}(x)
=
o(x/\log x).
\tag{28}
\]

This is lower order than (25). Hence almost all those grandchildren belong to `S`, and

\[
S(x)
\ge
(1+o(1))
\frac{X\log\log X}{\log X}.
\tag{29}
\]

Since `n_0` is fixed and `X=x/n_0`, (29) is exactly (7).

## 4. Why this genuinely moves the `FD-181` support boundary

The clean-fan proof in `FD-181` loses coercivity once a support of order `x/log x` is allowed, because that many changed coordinates can in principle cover the children of one erroneous parent. The present argument shows that this first screening is not stable when the prime coordinates remain physical.

If almost all children `n_0p` are changed in order to suppress the first fan, then their amplitudes are forced by (12) to stay close to `-delta(n_0)`. They therefore become new parents carrying a uniformly nonzero error. Suppressing their outgoing prime edges requires changing almost every squarefree semiprime descendant `n_0pr`. Landau's second-rank count makes that layer larger by `log log x`.

This is not just the deletion-only boundary statement of `FD-180`. The coefficients `delta(n)` may have arbitrary signs and arbitrary real amplitudes. The bootstrap uses relation energy itself to show that most first-generation amplitudes are bounded away from zero, and only then uses support counting at the second generation.

The theorem also identifies why moving prime coordinates were a real robustness cost in `FD-181`. If many `a(p)` are allowed to change, one changed prime label affects all edges carrying that label and the additive identity (11) disappears. The present `log log x` gain is therefore a fixed-prime refinement, not a replacement for the moving-prime theorem.

## 5. Stress tests and boundaries

**A full multiplicative alternative.** A source that changes one prime value and propagates the change multiplicatively to all squarefree multiples can have zero relation energy, but it changes a positive-density family of coefficients. This is consistent with (7), which only forces the much smaller semiprime-scale lower bound.

**Signed cancellation.** Choosing `delta(n_0p)` with the opposite sign from `delta(n_0)` is exactly what small root-edge energy demands. It does not evade the theorem: equation (16) then turns the compensating child into the next nonzero parent.

**Tiny amplitudes.** No lower bound on the amplitudes away from `n_0` is assumed. The fixed nonzero seed amplitude `Delta` supplies the threshold. Subcritical total energy forces almost all first-generation amplitudes to remain at least `Delta/2`; they cannot all be made tiny without paying on the root fan.

**Prime movement.** Equation (11) uses `a(p)=-1` for every prime. If prime coordinates move on a set large enough to screen the root fan, the proof does not apply. `FD-181` remains the robust statement in that larger class.

**Only two generations are claimed.** The same mechanism suggests a hierarchy in which subcritical energy forces successively higher fixed almost-prime layers. That iteration is not proved here. At deeper levels a boundary edge can shield many canonical descendants, so a correct proof needs weighted control of exceptional prefixes rather than a formal repetition of the semiprime argument.

**No dyadic-null construction at the new scale.** The theorem is a necessary support cost for subcritical relation energy. It does not construct a source of semiprime-scale support attaining that cost, nor show that the `x log log x/log x` scale is sharp.

**No RH consequence.** As in `FD-180`--`FD-182`, this is a source-faithfulness statement. It neither bounds the Franel--Landau discrepancy nor proves that Farey observations control prime-extension energy.

## Representation audit

Everything is stated in the original arithmetic coefficient coordinates and on the same squarefree prime-extension graph as `FD-180`--`FD-182`. No cumulative inversion, Farey-field reconstruction, spectral norm change, or source-dependent coordinate map is used.

The generic mechanism is a two-generation expansion bootstrap: if one erroneous vertex has many labelled children, low edge energy forces most children to inherit a nonzero error; those children then expose a larger second-generation layer. The arithmetic splice consists of three facts: physical prime values make the defect exactly `delta(pn)+delta(n)`, root-bad primes have negligible reciprocal prime mass, and Landau's theorem counts the squarefree semiprime layer as `X log log X/log X`.

The deliberately discarded information remains all Farey spatial data. Therefore (8) is not an observation theorem. It sharpens the source-side relation-rigidity frontier that a future Farey-to-relation bridge would be able to exploit.

## Prior-art audit

A targeted literature search was made for stability/property-testing results for multiplicative arithmetic functions, isoperimetry on divisibility graphs, squarefree divisor graphs, and sparse exceptional-prime control of semiprime counts. The search recovered general literature on multiplicative functions and unrelated divisibility/zero-divisor graph invariants, but no theorem matching this two-generation support bootstrap for a sparse perturbation of Möbius under prime-extension `L^q` energy.

The only load-bearing external asymptotic is classical Landau fixed-rank almost-prime counting, already anchored in `SOURCES.md` through E. M. Wright, *A Simple Proof of a Theorem of Landau* (1954). The prime-counting estimate used in (23) is weaker than the PNT already anchored there through Newman. No new durable source dependency is introduced, so `SOURCES.md` requires no change.

No novelty is claimed for Landau's theorem, partial summation, or the fact that a zero-density prime subset has `o(log log x)` reciprocal mass under the stronger counting hypothesis (15). The Mathia-specific result is their splice with the exact prime-extension defect identity to move the source-support rigidity threshold through a second multiplicative generation.

## Research consequence

The `x/log x` support size highlighted after `FD-181` is not a sharp escape threshold on the physical-prime fibre. A source cannot spend one prime fan of changed coefficients and stop: if it drives the relation energy below `x/log x`, those changed children propagate the defect into an asymptotically complete semiprime layer.

The immediate source-side frontier is therefore higher. One can ask whether this bootstrap continues through every fixed almost-prime rank, which would force support larger than `x(log log x)^{k-1}/log x` for every fixed `k`, and ultimately whether subcritical relation energy plus `S(x)=o(x)` already forces Möbius on the fixed-prime fibre. That extrapolation is deliberately left open.

The observation-side frontier from `FD-182` is unchanged: dyadic midpoint data alone still cannot certify the prime-extension energy. Any Farey-native advance must add spatial information that destroys the dyadic kernel before it can exploit the stronger source-side rigidity above.