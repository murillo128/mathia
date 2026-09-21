# AF-474 — Best-s-term tail mass gives sharp additive Hilbert fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-RESTRICTION`, `APPROXIMATE-SPARSITY`, `POSITIVE-RECOVERY`, `SCALE-AWARE`, `SHARP-ADDITIVE-ERROR`, `NO-NOVELTY-CLAIM`

## Claim

AF-472 gives exact multiplicative Hilbert fidelity for a hard support cap, while AF-473 shows that any positive diffuse tail destroys **scale-free** multiplicative fidelity on the full soft-sparse class. The remaining question is whether the tail mass can be priced explicitly when the downstream task tolerates an additive or finite-resolution error.

It can.

Let `A` be a finite or countable alphabet, let `s>=1`, and for a probability law `mu` define its best `s`-term tail mass

\[
\tau_s(\mu)
:=
\inf_{S\subset A,\ |S|\le s}\mu(A\setminus S).
\tag{1}
\]

For two probability laws `mu,nu`, write

\[
d_1(\mu,\nu)=\|\mu-\nu\|_1.
\]

Then the canonical coordinate embedding into `ell^2(A)` satisfies the exact additive estimate

\[
\boxed{
 d_1(\mu,\nu)
 \le
 \sqrt{2s}\,\|\mu-\nu\|_2
 +\tau_s(\mu)+\tau_s(\nu).
}
\tag{2}
\]

Together with the probability-simplex inequality

\[
\|\mu-\nu\|_2\le \frac1{\sqrt2}d_1(\mu,\nu),
\tag{3}
\]

this gives, for the scaled Hilbert embedding `H(mu)=sqrt(2) mu`,

\[
\boxed{
\frac{\bigl(d_1(\mu,\nu)-\tau_s(\mu)-\tau_s(\nu)\bigr)_+}{\sqrt{s}}
\le
\|H(\mu)-H(\nu)\|_2
\le
 d_1(\mu,\nu).
}
\tag{4}
\]

Hence on the soft-sparse class of AF-473,

\[
\Delta_{s,\varepsilon}^{\mathrm{soft}}(A)
=
\{\mu:\tau_s(\mu)\le\varepsilon\},
\]

one has

\[
\boxed{
\frac{(d_1(\mu,\nu)-2\varepsilon)_+}{\sqrt{s}}
\le
\|H(\mu)-H(\nu)\|_2
\le
 d_1(\mu,\nu).
}
\tag{5}
\]

Thus approximate sparsity **does** interpolate quantitatively with hard sparsity once fidelity is allowed to be additive or resolution-aware. The price of the unresolved tail is exactly its total two-source mass in `(2)`, and the hard-support `sqrt(s)` conditioning of AF-472 survives above that additive floor.

For any declared resolution `delta>2epsilon`, restricting attention to pairs with

\[
d_1(\mu,\nu)\ge\delta
\]

gives the ordinary multiplicative comparison

\[
\boxed{
\frac{1-2\varepsilon/\delta}{\sqrt{s}}\,d_1(\mu,\nu)
\le
\|H(\mu)-H(\nu)\|_2
\le
 d_1(\mu,\nu),
}
\tag{6}
\]

so the coordinate representation has distortion at most

\[
\boxed{
\frac{\sqrt{s}}{1-2\varepsilon/\delta}.
}
\tag{7}
\]

Equation `(7)` is the scale-aware positive complement to AF-473: the latter rules out one finite distortion valid at **all** nonzero scales, while `(7)` gives a finite explicit conditioning constant once the downstream problem declares a separation scale exceeding the unresolved tail diameter.

## Derivation from a two-support truncation

Fix `eta>0`. Choose sets `S_mu,S_nu` with cardinality at most `s` such that

\[
\mu(A\setminus S_\mu)\le \tau_s(\mu)+\eta,
\qquad
\nu(A\setminus S_\nu)\le \tau_s(\nu)+\eta.
\]

Let

\[
U=S_\mu\cup S_\nu,
\qquad |U|\le 2s,
\]

and set `x=mu-nu`. Split the `ell^1` norm into the retained coordinates and the tail:

\[
\|x\|_1
\le
\|x|_U\|_1+\|x|_{A\setminus U}\|_1.
\tag{8}
\]

The retained term obeys Cauchy--Schwarz,

\[
\|x|_U\|_1
\le
\sqrt{2s}\,\|x|_U\|_2
\le
\sqrt{2s}\,\|x\|_2.
\tag{9}
\]

For the discarded part,

\[
\begin{aligned}
\|x|_{A\setminus U}\|_1
&\le \mu(A\setminus U)+\nu(A\setminus U)\\
&\le \tau_s(\mu)+\tau_s(\nu)+2\eta.
\end{aligned}
\tag{10}
\]

Combining `(8)`--`(10)` and sending `eta` to zero proves `(2)`.

For `(3)`, write `x=x_+-x_-`. Because `mu` and `nu` have equal total mass,

\[
\|x_+\|_1=\|x_-\|_1=\frac12\|x\|_1.
\]

Since `||u||_2<=||u||_1` for nonnegative `u`,

\[
\|x\|_2^2
=\|x_+\|_2^2+\|x_-\|_2^2
\le
2\left(\frac{\|x\|_1}{2}\right)^2,
\]

which is `(3)`. Equations `(4)`--`(7)` are immediate rearrangements.

The proof needs no finite ambient dimension, no linear measurement model, and no reconstruction algorithm. It is a source-geometry statement about how best `s`-term tail mass controls the loss incurred by the canonical Hilbert representation.

## Sharpness of the two resources

Both terms in `(2)` are load-bearing.

First, the `sqrt(2s)` coefficient multiplying the Hilbert distance is sharp already at zero tail. Let `mu` and `nu` be uniform laws on two disjoint `s`-point supports. Then

\[
\tau_s(\mu)=\tau_s(\nu)=0,
\qquad
\|\mu-\nu\|_1=2,
\qquad
\|\mu-\nu\|_2=\sqrt{\frac2s},
\]

and equality holds in `(2)`. This is the same endpoint that makes the coordinate distortion in AF-472 exactly `sqrt(s)`.

Second, the coefficient `1` on the sum of tail masses cannot be uniformly reduced while keeping any finite coefficient in front of `||mu-nu||_2`. Fix `epsilon in (0,1)` and, for large `k`, choose one common anchor `a` and two disjoint `k`-point tail sets `{b_j}` and `{c_j}`. Define

\[
\mu_k=(1-\varepsilon)\delta_a
+\frac{\varepsilon}{k}\sum_{j=1}^k\delta_{b_j},
\qquad
\nu_k=(1-\varepsilon)\delta_a
+\frac{\varepsilon}{k}\sum_{j=1}^k\delta_{c_j}.
\tag{11}
\]

For each fixed `s`, once `k` is large enough the anchor is among the largest coordinates and

\[
\tau_s(\mu_k),\tau_s(\nu_k)\longrightarrow\varepsilon,
\]

while

\[
\|\mu_k-\nu_k\|_1=2\varepsilon,
\qquad
\|\mu_k-\nu_k\|_2
=\varepsilon\sqrt{\frac2k}
\longrightarrow0.
\tag{12}
\]

Therefore an inequality of the form

\[
\|\mu-\nu\|_1
\le C_s\|\mu-\nu\|_2
+c\bigl(\tau_s(\mu)+\tau_s(\nu)\bigr)
\]

with finite `C_s` cannot hold uniformly for any `c<1`. The additive tail coefficient in `(2)` is consequently sharp.

The same family also shows why `(5)` cannot yield a positive scale-free lower Lipschitz constant at the boundary `d_1=2epsilon`: its source distance remains exactly `2epsilon` while the coordinate Hilbert distance tends to zero. AF-473 strengthens this boundary phenomenon from the coordinate map to an arbitrary-Hilbert all-scales obstruction by inserting Hamming cubes into the same tail budget.

## Relation to AF-472 and AF-473

AF-472 and AF-473 initially look discontinuous:

\[
\varepsilon=0
\quad\Rightarrow\quad
c_2=\sqrt{s},
\qquad
\varepsilon>0
\quad\Rightarrow\quad
c_2=\infty
\]

for uniform multiplicative distortion on the full class. AF-474 identifies the missing parameter: **absolute resolution**.

The discontinuity is real only when the inverse comparison is required down to arbitrarily small nonzero scales. A tail of mass `epsilon` can hide unbounded combinatorial complexity, but all of that purely tail-supported variation fits inside `ell^1` diameter `2epsilon`. Once the downstream theorem only needs to distinguish source pairs separated by a fixed `delta>2epsilon`, the elementary coordinate map recovers a finite conditioning bound, degrading continuously as `delta` approaches the tail scale.

This separates three source guarantees that should no longer be conflated:

1. hard sparsity gives scale-free multiplicative fidelity with sharp cost `sqrt(s)`;
2. soft sparsity alone gives no scale-free multiplicative Hilbert fidelity on an infinite alphabet;
3. soft sparsity plus a declared resolution gives additive fidelity `(5)` and multiplicative fidelity `(6)` above that resolution.

The third regime is not an escape from AF-473; it weakens the fidelity contract in exactly the way AF-473 left open.

## Prior-art and novelty audit

The mathematical ingredients are classical, and **no theorem-level novelty is claimed** for `(2)` as a sparse-approximation inequality. The result belongs to the same best-`s`-term / robust-recovery geometry that underlies compressed sensing.

- Emmanuel J. Candès, Justin Romberg, and Terence Tao, **“Stable signal recovery from incomplete and inaccurate measurements,”** *Communications on Pure and Applied Mathematics* 59(8), 1207--1223 (2006), DOI `10.1002/cpa.20124`. Their stable-recovery framework explicitly treats sparse and approximately sparse signals and establishes the now-standard principle that model error enters recovery guarantees additively.
- Albert Cohen, Wolfgang Dahmen, and Ronald DeVore, **“Compressed sensing and best k-term approximation,”** *Journal of the American Mathematical Society* 22(1), 211--231 (2009), DOI `10.1090/S0894-0347-08-00610-3`. This develops instance optimality in terms of best `k`-term approximation and mixed-norm error, providing the closest standard language for the tail functional used here.
- The support-sensitive `ell^1`/`ell^2` comparison in `(9)` is the elementary Cauchy--Schwarz sparsity estimate. Related `sigma_s(x)_1/sqrt(s)` terms are ubiquitous in robust sparse recovery and Stechkin-type best-term approximation.

A targeted search recovered this broad and mature approximation/recovery literature rather than a distinct new metric-geometry theorem. The line-specific value is the exact specialization and sharp constants needed to close the question left by AF-473: for probability laws, the two best-`s`-term tail masses are the natural additive currency that restores a positive Hilbert statement without pretending that approximate sparsity gives all-scales bi-Lipschitz fidelity.

## Boundary and falsification audit

- **This is additive/resolution-aware fidelity, not scale-free fidelity.** Equation `(5)` permits a zero lower bound for source separations at or below `2epsilon`; it therefore does not contradict AF-473.
- **The positive theorem is for the canonical infinite-dimensional coordinate Hilbert space.** A finite-dimensional target introduces separate packing, Johnson--Lindenstrauss, or compressed-sensing questions not settled here.
- **The source tail is measured before compression.** A downstream claim must prove a bound on `tau_s` for the actual physical/arithmetic carrier; declaring a representation “approximately sparse” without such a bound supplies no theorem.
- **Both sources pay their own tail.** For nonuniform classes the correct error term is `tau_s(mu)+tau_s(nu)`, not a single global `epsilon` unless both tails are controlled by it.
- **The support budget and tail budget are different resources.** Increasing `s` improves the tail approximation but worsens the multiplicative Hilbert factor `sqrt(s)`. Any application must optimize or otherwise control this tradeoff rather than send `s` to infinity for free.
- **The theorem does not bound hidden combinatorial complexity below the tail scale.** AF-473 shows that arbitrarily many independent switches can remain there.
- **A narrower arithmetic subclass may improve `(2)`.** Correlated tails, decay laws, ordering, monotonicity, or relational constraints could yield a smaller additive error or better effective support factor, but that requires a positive theorem for the actual subclass.
- **No prime discriminator is created.** The estimate preserves source distinctions above a controlled error scale; it does not explain which source distinctions encode rational primality.

## Arithmetic-fidelity consequence

The soft-sparsity obstruction now has a precise positive counterpart. For a prime-derived carrier, approximate concentration can be useful, but only after three quantities are proved at the exact layer where compression occurs: an effective support budget `s`, a best-`s`-term tail budget `epsilon`, and the smallest source separation `delta` that the downstream zero-selection or sign theorem genuinely needs to resolve.

If `delta>2epsilon`, equation `(7)` gives an explicit conditioning cost. If `delta` approaches `2epsilon`, that cost diverges; if the theorem needs distinctions below the tail scale, AF-473 re-enters and approximate sparsity alone is insufficient.

This replaces the vague question “is the arithmetic carrier approximately sparse?” by a quantitative one:

\[
\boxed{
\text{what }(s,\varepsilon,\delta)\text{ tradeoff is forced by the arithmetic source and consumed downstream?}
}
\]

That triple is a concrete scale-aware gate for future prime-facing applications. It prices both the amount of discarded mass and the resolution at which the arithmetic discriminator must survive, rather than treating a small tail as if it were information-theoretically harmless.