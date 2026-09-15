# FD-140 — every fixed congruence-coordinate alphabet misses a finer prime-color wall

**Status:** `LITERATURE+DERIVED + EXACT-MATCHED-CONTROL + MULTIVARIATE-SQUAREFREE-SATHE-SELBERG + JOINT-LOCAL-PRIME-FACTOR-LAW + EXACT-VECTOR-CONDITIONING + FACTOR-TWO-SCALE-LOCALIZATION + ALL-PRIME-UNIFORMITY + COMMON-SOURCE + FINER-PRIME-COLOR-WALL + FIXED-CONGRUENCE-ALPHABET-NEGATIVE/BOUNDARY`.

`FD-139` showed that exact conditioning on `omega(n)` does not recover coercivity: the source can rotate its sign wall into the independent mod-4 prime-color coordinate. The live question was whether this is merely a one-coordinate defect, or whether a sufficiently rich **finite** family of additive prime-factor coordinates can close every transverse direction.

For the natural and broad class of fixed congruence-periodic coordinates, the answer is negative. Even if one conditions on the **entire vector of exact prime-factor counts in every reduced residue class modulo a fixed modulus `Q`**, a common source can place its wall in a quadratic color modulo a new prime `ell` not dividing `Q`. The Chinese remainder theorem leaves that finer color with square-root conditional fluctuations inside every central exact coarse cell, so its two-point sign boundary again has vanishing relative mass.

More precisely, fix an integer `Q>=1`, write

\[
d:=\varphi(Q),
\qquad
\mathcal A_Q:=(\mathbb Z/Q\mathbb Z)^\times,
\tag{1}
\]

and choose an odd prime `ell` with `ell\nmid Q`. Let `psi` be the nonprincipal quadratic character modulo `ell`, extended by `psi(ell)=0`, and define the strongly additive color

\[
G(n):=\sum_{q\mid n}\psi(q).
\tag{2}
\]

For each reduced class `a in mathcal A_Q`, put

\[
\omega_a^{(Q)}(n)
:=
\#\{q\mid n:q\equiv a\pmod Q\}.
\tag{3}
\]

Primes dividing `Q` are a finite exceptional set and are not included in (3). Fix `K>=0` and define one infinite source

\[
b_{K,Q,\ell}(n):=
\begin{cases}
+1,&n\text{ squarefree and }(\omega(n)\le K\text{ or }G(n)\ge0),\\
-1,&n\text{ squarefree},\ \omega(n)>K,\ G(n)<0,
\end{cases}
\qquad
a_n^{(K,Q,\ell)}:=\mu(n)b_{K,Q,\ell}(n),
\tag{4}
\]

with `a_n^(K,Q,ell)=0` on nonsquarefree integers.

For `T>=3`, let

\[
L_T:=\log\log T,
\tag{5}
\]

and for a prime `p` and vector `mathbf k=(k_a)_(a in mathcal A_Q)` define the exact coarse-coordinate parent cell

\[
\mathcal C^{(Q)}_{p,\mathbf k}(T)
:=
\left\{
 n:T<n\le2T,\ \mu^2(n)=1,\ p\nmid n,
 \ \omega_a^{(Q)}(n)=k_a\ \forall a\in\mathcal A_Q
\right\}.
\tag{6}
\]

Finite divisibility patterns at primes dividing `Q` are left free in (6); equivalently one may split (6) into finitely many such patterns. For `1<=r<infinity`, set

\[
\mathfrak E^{(Q)}_{p,\mathbf k,r}(T;a)
:=
\frac1{|\mathcal C^{(Q)}_{p,\mathbf k}(T)|}
\sum_{n\in\mathcal C^{(Q)}_{p,\mathbf k}(T)}|a_{pn}+a_n|^r,
\tag{7}
\]

with value `0` when the cell is empty, and define the reciprocal-weighted analogue

\[
\mathfrak E^{(Q),\log}_{p,\mathbf k,r}(T;a)
:=
\frac{\displaystyle\sum_{n\in\mathcal C^{(Q)}_{p,\mathbf k}(T)}|a_{pn}+a_n|^r/n}
{\displaystyle\sum_{n\in\mathcal C^{(Q)}_{p,\mathbf k}(T)}1/n}.
\tag{8}
\]

Then for every fixed `C>0`, uniformly over the central exact-vector cells

\[
\left|k_a-\frac{L_T}{d}\right|\le C\sqrt{L_T}
\qquad(a\in\mathcal A_Q),
\tag{9}
\]

we have

\[
\boxed{
\sup_{p\ \mathrm{prime}}
\sup_{\mathbf k\ \mathrm{satisfying}\ (9)}
\mathfrak E^{(Q)}_{p,\mathbf k,r}
\bigl(T;a^{(K,Q,\ell)}\bigr)
\ll_{Q,\ell,C,r}\frac1{\sqrt{L_T}}
\longrightarrow0,
}
\tag{10}
\]

and

\[
\boxed{
\sup_{p\ \mathrm{prime}}
\sup_{\mathbf k\ \mathrm{satisfying}\ (9)}
\mathfrak E^{(Q),\log}_{p,\mathbf k,r}
\bigl(T;a^{(K,Q,\ell)}\bigr)
\ll_{Q,\ell,C,r}\frac1{\sqrt{L_T}}
\longrightarrow0.
}
\tag{11}
\]

The same source nevertheless remains macroscopically non-Möbius:

\[
\boxed{
\frac1H\#\{n\le H:a_n^{(K,Q,\ell)}\ne\mu(n)\}
\longrightarrow\frac1{2\zeta(2)}.
}
\tag{12}
\]

Thus exact localization in the **maximal fixed congruence coordinate vector modulo `Q`** is still noncoercive. In particular, no finite family of strongly additive prime coordinates whose prime weights are periodic modulo one fixed common modulus can be complete: their values are determined by (3), while a finer quadratic coloring modulo `ell\nmid Q` remains transverse to that entire alphabet.

## 1. The ancestry defect still lives on a two-value wall

For a squarefree parent `n` with `p\nmid n`,

\[
\mu(pn)=-\mu(n),
\tag{13}
\]

and therefore

\[
a_{pn}^{(K,Q,\ell)}+a_n^{(K,Q,\ell)}
=
\mu(n)\bigl(b_{K,Q,\ell}(n)-b_{K,Q,\ell}(pn)\bigr).
\tag{14}
\]

Inside the cells (9), `omega(n)` tends to infinity uniformly after allowing the finitely many primes dividing `Q`, so the finite anchor `omega<=K` is eventually inactive for both parent and child. The new color changes by exactly

\[
G(pn)=G(n)+\psi(p).
\tag{15}
\]

With the same tie convention as `FD-138`--`FD-139`, namely `G>=0` on the positive side,

\[
|a_{pn}^{(K,Q,\ell)}+a_n^{(K,Q,\ell)}|
=
\begin{cases}
0,&\psi(p)=0,\\
2\,\mathbf1_{\{G(n)=-1\}},&\psi(p)=+1,\\
2\,\mathbf1_{\{G(n)=0\}},&\psi(p)=-1.
\end{cases}
\tag{16}
\]

Hence every defective parent, for every prime direction simultaneously, belongs to the fixed arithmetic boundary

\[
\boxed{G(n)\in\{-1,0\}.}
\tag{17}
\]

The only question is whether exact knowledge of all coarse counts (3) makes that boundary macroscopically visible. It does not.

## 2. Exact coarse-vector cells have mass `T (log log T)^(-d/2)`

The relevant multivariate squarefree Dirichlet series is

\[
F_Q(s,\mathbf z)
:=
\prod_{q\nmid Q}
\left(1+\frac{z_{a(q)}}{q^s}\right),
\tag{18}
\]

where `a(q)` is the reduced residue class of `q mod Q`. By the prime number theorem in arithmetic progressions, each class has reciprocal prime mass

\[
\sum_{\substack{q\le x\\q\equiv a\ (Q)}}\frac1q
=
\frac1d\log\log x+O_Q(1).
\tag{19}
\]

For fixed `Q`, the usual multivariate Selberg--Delange factorization of (18) has one singular exponent `z_a/d` per class and a regular Euler product on every fixed compact `mathbf z`-set. Coefficient extraction in the central range (9) gives the squarefree multivariate Sathe--Selberg scale

\[
\#\left\{
 n\le x:\mu^2(n)=1,
 \ \omega_a^{(Q)}(n)=k_a\ \forall a
\right\}
\asymp_{Q,C}
 xL_x^{-d/2},
\tag{20}
\]

uniformly for `|k_a-L_x/d|<=C sqrt(L_x)`.

The finite primes dividing `Q` merely split this count into finitely many nondegenerate Euler-factor patterns. Excluding the active prime `p` also costs only one Euler factor. If `p\nmid Q`, the factor in its residue coordinate is

\[
\left(1+\frac{z_{a(p)}}{p^s}\right)^{-1},
\tag{21}
\]

which, together with the finitely many derivatives used in the fixed-dimensional Selberg--Delange extraction, is uniformly bounded for all `p>=2`. If `p\mid Q`, its absence is already part of one of the finite exceptional patterns. As in `FD-139`, subtracting the asymptotics at `2T` and `T` therefore yields

\[
\boxed{
|\mathcal C^{(Q)}_{p,\mathbf k}(T)|
\gg_{Q,C}T L_T^{-d/2}
}
\tag{22}
\]

uniformly over all primes `p` and all vectors satisfying (9).

This denominator is deliberately stronger than conditioning on any prescribed finite collection of periodic additive coordinates: the full vector (3) determines all of them.

## 3. CRT leaves one square-root transverse fluctuation after all coarse counts are fixed

Refine each coarse residue class by the sign of the quadratic character modulo `ell`. For `a in mathcal A_Q` and `epsilon in {+1,-1}`, define

\[
\mathcal P_{a,\epsilon}
:=
\{q:q\nmid Q\ell,\ q\equiv a\pmod Q,\ \psi(q)=\epsilon\},
\tag{23}
\]

and

\[
\nu_{a,\epsilon}(n)
:=
\#\{q\mid n:q\in\mathcal P_{a,\epsilon}\}.
\tag{24}
\]

Because `(Q,ell)=1`, the Chinese remainder theorem and Dirichlet equidistribution give

\[
\sum_{\substack{q\le x\\q\in\mathcal P_{a,+}}}\frac1q
=
\frac1{2d}L_x+O_{Q,\ell}(1),
\qquad
\sum_{\substack{q\le x\\q\in\mathcal P_{a,-}}}\frac1q
=
\frac1{2d}L_x+O_{Q,\ell}(1).
\tag{25}
\]

Apart from the finite primes dividing `Qell`, the exact coarse constraint is

\[
\nu_{a,+}(n)+\nu_{a,-}(n)=k_a+O_{Q,\ell}(1),
\tag{26}
\]

whereas the hidden color is

\[
G(n)
=
\sum_{a\in\mathcal A_Q}
\bigl(\nu_{a,+}(n)-\nu_{a,-}(n)\bigr)
+O_{Q,\ell}(1).
\tag{27}
\]

The joint local prime-factor law for the fixed `2d` disjoint prime sets in (23), equivalently the corresponding fixed-dimensional Selberg--Delange extraction, has central lattice scale

\[
T L_T^{-d}
\tag{28}
\]

per refined vector. More precisely, after the standard Gaussian decay away from the central box is retained, summing over all refined vectors satisfying the `d` equations (26) gives the denominator scale `T L_T^{-d/2}` from (22). Imposing in addition either one fixed value `G=h` adds one independent lattice equation. The remaining Gaussian lattice sum consequently loses one factor `sqrt(L_T)`:

\[
\boxed{
\#\left\{
 n\in\mathcal C^{(Q)}_{p,\mathbf k}(T):G(n)=h
\right\}
\ll_{Q,\ell,C,h}
T L_T^{-(d+1)/2}
}
\tag{29}
\]

uniformly in `p`, in every vector (9), and for each fixed integer `h`.

It is useful to see why (29) is not dimension bookkeeping alone. The coarse equations fix the **sums** of the `+` and `-` populations in every mod-`Q` class. They do not fix their signed differences. Under (26), the total signed difference (27) retains variance `asymp L_T`; its central point masses are therefore `O(L_T^(-1/2))`. Equation (29) is precisely that conditional local statement multiplied by the exact coarse-cell mass.

Finite primes dividing `Qell` only produce finitely many shifts of (26)--(27), and excluding the active prime again removes one Euler factor. Neither operation changes the power of `L_T` or the uniformity in `p`.

Combining `h=-1,0` with (22) gives

\[
\boxed{
\sup_p\sup_{\mathbf k\ \mathrm{satisfying}\ (9)}
\frac{\#\{n\in\mathcal C^{(Q)}_{p,\mathbf k}(T):G(n)\in\{-1,0\}\}}
{|\mathcal C^{(Q)}_{p,\mathbf k}(T)|}
\ll_{Q,\ell,C}L_T^{-1/2}.
}
\tag{30}
\]

This is the exact-vector analogue of the one-extra-codimension estimate in `FD-139`.

## 4. Exact-vector ancestry vanishes while the source remains wrong

Every nonzero ancestry defect in (16) has magnitude exactly `2`, and every defective parent is contained in the boundary counted by (30). Therefore

\[
\mathfrak E^{(Q)}_{p,\mathbf k,r}
\bigl(T;a^{(K,Q,\ell)}\bigr)
\le
2^r
\frac{\#\{n\in\mathcal C^{(Q)}_{p,\mathbf k}(T):G(n)\in\{-1,0\}\}}
{|\mathcal C^{(Q)}_{p,\mathbf k}(T)|}
\ll_{Q,\ell,C,r}L_T^{-1/2},
\tag{31}
\]

which proves (10). On `(T,2T]`, reciprocal weights differ by at most a factor `2`, so

\[
\mathfrak E^{(Q),\log}_{p,\mathbf k,r}
\le2\mathfrak E^{(Q)}_{p,\mathbf k,r},
\tag{32}
\]

and (11) follows.

For the global coefficient error, outside the finite anchor we have

\[
a_n^{(K,Q,\ell)}\ne\mu(n)
\quad\Longleftrightarrow\quad
\mu^2(n)=1,\ G(n)<0.
\tag{33}
\]

The bounded strongly additive function `G` has

\[
\sum_{q\le x}\frac{\psi(q)}q=O_{\ell}(1),
\qquad
\sum_{q\le x}\frac{\psi(q)^2}q
=L_x+O_{\ell}(1).
\tag{34}
\]

The squarefree weighted Erdős--Kac theorem already anchored for `FD-138` therefore gives a centered Gaussian limit for `G/sqrt(L_x)`. In particular the negative half-space has asymptotic squarefree mass one half, while the zero boundary has vanishing relative mass. Since squarefree integers have density `1/zeta(2)`, (12) follows. Partial summation gives the analogous positive logarithmic density, and the positive `L^r` coefficient-error conclusions follow exactly as in `FD-138`.

The important separation is now explicit:

\[
\text{all exact mod-}Q\text{ prime-factor counts visible}
\quad\not\Longrightarrow\quad
\text{the finer mod-}\ell\text{ sign direction visible}.
\tag{35}
\]

## 5. Consequence for finite periodic additive coordinate families

Consider any fixed finite family of strongly additive coordinates

\[
F_j(n)=\sum_{q\mid n}w_j(q),
\qquad 1\le j\le J,
\tag{36}
\]

such that, outside a finite exceptional set of primes, every weight `w_j(q)` depends only on `q mod Q` for one fixed common modulus `Q`. Then there are constants `c_{j,a}` with

\[
F_j(n)
=
\sum_{a\in\mathcal A_Q}c_{j,a}\omega_a^{(Q)}(n)
+O_{Q,J}(1)
\tag{37}
\]

once the finite exceptional divisibility pattern is fixed. Exact knowledge of the whole vector in (3), together with that finite pattern, is therefore strictly at least as informative as exact knowledge of all `F_j`.

But (10)--(12) show that even this maximal fixed mod-`Q` information admits a common source with vanishing central-cell mean ancestry and positive-density coefficient error. Hence

\[
\boxed{
\text{no fixed finite congruence-periodic additive alphabet is coefficient-coercive by itself.}
}
\tag{38}
\]

This is stronger than merely iterating `FD-139` through more residue classes. The obstruction is structural: every fixed modulus has a strictly finer independent prime coloring available through a coprime modulus.

It is also deliberately narrower than the strongest conceivable finite-dimensional negative theorem. Equation (38) does **not** cover arbitrary nonperiodic weights `w_j(q)`, weights chosen from source geometry rather than congruence data, or a coordinate alphabet whose modulus/dimension grows with `T`.

## 6. Adversarial audit and boundary of the result

The matched control survives the following failure modes.

**One source, not one source per cell.** For fixed `Q`, `ell` and `K`, equation (4) defines one infinite sequence. It is independent of `T`, `p` and `mathbf k`. The exact cells merely test that same source.

**The conditioning really is exact and multidimensional.** There is no hidden CLT-width averaging in a coarse coordinate. Every `omega_a^(Q)` is fixed exactly. The only width in (9) specifies which exact cells are required to have the uniform asymptotic denominator.

**The transverse direction is genuinely independent of the coarse vector.** CRT splits each reduced mod-`Q` class into equal positive and negative `psi` subclasses. Thus fixing all coarse sums leaves a signed difference with variance `Theta(log log T)`; (29) is a local theorem, not an appeal to weak Gaussian convergence.

**Exceptional primes are finite, not silently discarded.** Primes dividing `Qell` generate finitely many divisibility patterns and bounded shifts. The local powers of `log log T` are unchanged in every pattern. For `p=ell`, `psi(p)=0` and the ancestry defect is identically zero.

**The active prime is excluded uniformly.** Removing one prime from a fixed-dimensional Euler product multiplies the regular factor by a uniformly bounded inverse Euler factor. The numerator estimate may also simply forget the restriction `p\nmid n`, so no favorable dependence on `p` is being imported.

**The finite anchor cannot generate the conclusion.** Central exact-vector cells have total rank `sum_a k_a+O_Q(1)=L_T+O_{Q,C}(sqrt(L_T))`, which eventually exceeds every fixed `K`. The wall calculation is therefore the asymptotic source law, not an anchor artifact.

**There is no conflict with the `L^infinity` rigidity of `FD-135`.** Whenever a bad edge exists, its defect is still exactly `2`. The present theorem only says that those edges occupy an `O(L_T^(-1/2))` fraction of each exact coarse cell. Taking a supremum rather than a mean sees the wall immediately.

**This does not prove that every finite additive coordinate family fails.** The theorem defeats every fixed congruence-periodic family because such a family factors through a finite residue-class count vector. An arbitrary finite family with nonperiodic prime weights may encode substantially more information and is outside the theorem.

**A growing alphabet is untouched.** If `Q=Q(T)` or the number of visible coordinates grows, the dimension of the local law is no longer fixed. Both the exact-cell mass and the uniform Selberg--Delange range become part of the problem. No claim is made there.

**No destination-side obstruction is asserted.** As in `FD-139`, failure of coefficient recovery from these ancestry means does not preclude a direct coercive inequality for the Farey Fourier/GCD skeleton.

## 7. Prior-art boundary

The analytic inputs are classical and already anchored in `SOURCES.md`.

- Tenenbaum's *Introduction to Analytic and Probabilistic Number Theory* supplies the Selberg--Delange/Sathe--Selberg framework used for exact central prime-factor counts. The fixed-dimensional multivariate squarefree series (18) is the same coefficient-extraction mechanism with one variable per residue class.
- Tenenbaum, *Moyennes effectives de fonctions multiplicatives complexes* (Ramanujan Journal 44 (2017), arXiv:1709.01315, with the published correction) is the existing local-law anchor for joint counts in finitely many disjoint prime sets. Here it is applied after the CRT refinement (23), with the coarse-sum constraints retained.
- Fan, *Weighted Erdos--Kac theorems via computing moments* (Acta Arithmetica 217 (2025), arXiv:2306.11289) already anchors the squarefree Gaussian law used only for the global mismatch in (12).

The general facts that multivariate prime-factor counts have local Gaussian/Poisson behavior and that residue classes may be refined by CRT are not claimed as new. The derived contribution of `FD-140` is the **matched splice**: exact localization in the entire fixed mod-`Q` coordinate vector still leaves a finer common prime-color wall whose ancestry boundary has one extra local codimension while its coefficient error remains macroscopic. The literature audit found no theorem that supplies the missing coefficient coercivity from a fixed congruence-coordinate alphabet.

No new load-bearing source is introduced, so `SOURCES.md` requires no update.

## 8. What this changes

`FD-139` left open whether adding enough exact source-native prime-factor coordinates could close the transverse direction exposed by the mod-4 witness. `FD-140` rules out one large natural class of such repairs: **no fixed finite congruence resolution is complete**. Refining from `omega` to every residue-class count modulo a fixed `Q` merely moves the escape route to a coprime modulus.

The next coefficient-side question is therefore no longer “which fixed modulus should be added?” A genuinely different positive mechanism must do at least one of the following:

1. justify a coordinate alphabet whose arithmetic resolution or dimension grows with scale and prove local laws strong enough that its exact cells remain populated;
2. use nonperiodic/source-intrinsic prime weights that cannot be refined away by an independent congruence coloring;
3. prove a structural theorem excluding half-space sign walls for the actual admissible Möbius/Farey source rather than trying to observe all possible walls; or
4. bypass coefficient recovery and establish coercivity directly in the destination-side Fourier/GCD skeleton.

For the growing-alphabet route the first quantitative subproblem is now sharp: determine how fast a modulus/dimension may grow while a central exact joint prime-factor cell still has enough mass and uniform local control to support a coercive ancestry estimate. That is where fixed-dimensional Selberg--Delange stops being a free input and source-specific information would have to enter.