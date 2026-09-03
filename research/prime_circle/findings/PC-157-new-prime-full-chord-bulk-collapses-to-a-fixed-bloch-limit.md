# PC-157 — new-prime full-chord bulk collapses to a fixed Bloch limit

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for extracting a new RH-sensitive **bulk** spectrum from the full fine primitive fiber of the canonical inverse-square chord Laplacian when a genuinely new prime is adjoined. PC-155 classified only the fiber-constant compression for new squarefree primes, while PC-156 proved an exact fixed-pencil decomposition for full fibers when no new prime support is added. The missing residue in a new-prime fiber does break exact cyclic translation symmetry, but only by an `O(1/q)` perturbation at the level of normalized empirical spectral measure.

Fix `d>=2` and a prime `q` with `q` not dividing `d`. Put `N=dq`, `r=phi(d)`, and let

\[
A_{dq}:=(dq)^{-2}L_{dq}^{\rm int}
\]

be the naturally normalized inverse-square chord Laplacian on the new primitive shell `U(dq)`, of dimension `r(q-1)`. Introduce the semi-primitive ambient set

\[
S_{d,q}:=\{x\bmod dq:\gcd(x,d)=1\}.
\]

It consists of all `q` additive lifts of every point of `U(d)`. Its normalized induced chord Laplacian has an **exact** q-sector Bloch decomposition into the same fixed quadratic metric-cotangent pencil that appeared in PC-156. The genuine primitive shell is obtained by deleting exactly one old point from each coarse fiber. Combining that finite-rank deletion with an exact trace formula for the deleted conductances gives the uniform bound

\[
\boxed{
W_1\!\left(\mu_{A_{dq}},\nu_d\right)
\le \frac{7}{8q},
}
\]

where

\[
\boxed{
\nu_d:=\int_0^1\mu_{\mathcal P_d(t)}\,dt,
\qquad
\mathcal P_d(t)
=\frac1{d^2}
\left(
L_d^{\rm int}+\frac t2 C_d-\frac{t^2}{2}I
\right)
}
\]

is independent of the new prime `q`. Thus the full normalized **bulk** spectrum of a genuinely new-prime refinement converges at rate `O(1/q)`, uniformly in the base conductor, to a fixed base-level integrated density of states. New-prime support can still survive in sparse edge modes, microscopic statistics, nonlinear cross-level observables, or the global uniformization/monodromy sector, but not as an order-one macroscopic spectral distribution of this single-level full-chord operator.

## 1. A new-prime shell is a one-point-per-fiber puncture of an exact cyclic ambient operator

Write

\[
U(M)=(\mathbb Z/M\mathbb Z)^\times,
\qquad
\kappa_M(s):=\frac1{4\sin^2(\pi s/M)}.
\]

For any subset `X` of residues modulo `M`, let `L_M[X]` denote the induced inverse-square chord Laplacian

\[
(L_M[X]f)(a)
=\sum_{\substack{b\in X\\b\ne a}}
\kappa_M(a-b)(f(a)-f(b)).
\]

Because `q` is coprime to `d`, reduction modulo `d` makes

\[
S_{d,q}=\{x\bmod dq:\gcd(x,d)=1\}
\cong U(d)\times\mathbb Z/q\mathbb Z.
\tag{1}
\]

Translation by `d` is an exact order-`q` symmetry of this semi-primitive set. The genuine primitive shell is

\[
P:=U(dq)=\{x\in S_{d,q}:q\nmid x\},
\tag{2}
\]

and the complement

\[
O:=S_{d,q}\setminus P
\tag{3}
\]

contains exactly one point in every coarse fiber. By the Chinese remainder theorem, `O` is a rotated/permuted copy of `U(d)` and therefore has cardinality `r=phi(d)`. In particular,

\[
|S_{d,q}|=rq,
\qquad
|P|=r(q-1),
\qquad
|O|=r.
\tag{4}
\]

This is the precise way in which a genuinely new prime differs from the full cyclic fibers of PC-156: the ambient q-fiber is still exact, but the primitive condition punctures one point from each fiber.

## 2. The semi-primitive ambient spectrum is exactly the PC-156 quadratic pencil

Let

\[
M_{d,q}:=(dq)^{-2}L_{dq}[S_{d,q}].
\tag{5}
\]

The derivation of PC-156 uses only a complete additive fiber and the chord-difference kernel, so it applies verbatim to `S_{d,q}` even though `S_{d,q}` is not the primitive shell of level `dq`. Fiber Fourier transform therefore gives

\[
\boxed{
M_{d,q}
\cong
\bigoplus_{k=0}^{q-1}
D_{q,k}\,\mathcal P_d(k/q)\,D_{q,k}^{-1},
}
\tag{6}
\]

where the `D_{q,k}` are diagonal fiber gauges and

\[
\boxed{
\mathcal P_d(t)
=\frac1{d^2}
\left(
L_d^{\rm int}+\frac t2 C_d-\frac{t^2}{2}I
\right),
\qquad
C_d=H_d+J_d.
}
\tag{7}
\]

Consequently, if `mu_T` denotes normalized empirical spectral measure,

\[
\boxed{
\mu_{M_{d,q}}
=\frac1q\sum_{k=0}^{q-1}\mu_{\mathcal P_d(k/q)}.
}
\tag{8}
\]

All `q`-dependence of the exact ambient bulk spectrum is thus only the Bloch sampling grid. The genuinely new-prime arithmetic enters solely through deleting the old set `O`.

## 3. Deleting the old residue in every fiber is only an `O(1/q)` bulk-rank perturbation

Order `S_{d,q}=P\sqcup O`. The principal `P` block of `M_{d,q}` is not exactly `A_{dq}` because its diagonal still counts the edges from primitive points to old points. Write

\[
M_{d,q}
=
\begin{pmatrix}
H&-B\\
-B^*&G
\end{pmatrix},
\qquad
\boxed{H=A_{dq}+\Delta,}
\tag{9}
\]

where `Delta>=0` is diagonal and records the normalized conductance from each primitive vertex to `O`.

Embed `H` back into the ambient `rq`-dimensional space as

\[
\widetilde H:=H\oplus0_r.
\]

Then

\[
M_{d,q}-\widetilde H
=
\begin{pmatrix}
0&-B\\
-B^*&G
\end{pmatrix}.
\]

Its image is contained in `Ran(B)` on the primitive side plus the full `r`-dimensional old space, so

\[
\boxed{
\operatorname{rank}(M_{d,q}-\widetilde H)\le2r.
}
\tag{10}
\]

The standard Hermitian rank/interlacing inequality for empirical distribution functions therefore gives

\[
\boxed{
d_K(\mu_{M_{d,q}},\mu_{\widetilde H})\le\frac2q.
}
\tag{11}
\]

But

\[
\mu_{\widetilde H}
=\frac{q-1}{q}\mu_H+\frac1q\delta_0,
\]

hence

\[
\boxed{
d_K(\mu_H,\mu_{M_{d,q}})\le\frac3q.}
\tag{12}
\]

This is already enough to show that puncturing one residue per fiber cannot change a positive fraction of the bulk eigenvalue count as `q` grows. The remaining issue is whether the diagonal correction `Delta` could move all primitive eigenvalues by an order-one amount. Its trace can be computed exactly.

## 4. The total old-point conductance has an exact primitive-shell trace formula

Fix an old point `y in O`, and let `y_0 in U(d)` be the corresponding coarse residue. In the full semi-primitive q-fiber, the ordinary multiplication identity for `csc^2` gives `q^2` times the coarse conductance from every other coarse fiber. Within the fiber of `y`, the remaining `q-1` points form the full q-gon around `y`, whose inverse-square degree is

\[
\frac{q^2-1}{12}.
\]

The old-to-old points form a copy of the base primitive shell and contribute exactly `deg_d(y_0)`. Therefore the conductance from this old point to the genuine new primitive shell is

\[
\boxed{
(q^2-1)\left(\deg_d(y_0)+\frac1{12}\right).
}
\tag{13}
\]

Summing over the `r` old points and counting each old/new edge once gives the unnormalized diagonal correction

\[
\boxed{
T_{d,q}
=(q^2-1)
\left(
\operatorname{Tr}L_d^{\rm int}+\frac r{12}
\right).
}
\tag{14}
\]

PC-140 records the exact identity

\[
\operatorname{Tr}L_d^{\rm int}+\frac r{12}
=
\frac{d^3}{12}
\prod_{p\mid d}
\left(1-\frac2p+\frac1{p^3}\right).
\tag{15}
\]

Since `Delta` includes the `(dq)^{-2}` normalization, equations (14)--(15) yield

\[
\boxed{
\frac{\operatorname{Tr}\Delta}{r(q-1)}
=
\frac{q+1}{12q^2}
\prod_{p\mid d}
\left(1-\frac1p-\frac1{p^2}\right)
\le\frac1{8q}.
}
\tag{16}
\]

Here the local factor follows from

\[
\frac{1-2/p+1/p^3}{1-1/p}
=1-\frac1p-\frac1{p^2},
\]

and the last inequality is uniform in `d` and every prime `q>=2`.

Because `H=A_{dq}+Delta` with `Delta>=0`, Weyl monotonicity orders the eigenvalues so that each eigenvalue of `H` lies above the corresponding one of `A_{dq}`. In one dimension the monotone coupling is optimal for Wasserstein distance, hence

\[
\boxed{
W_1(\mu_{A_{dq}},\mu_H)
=\frac{\operatorname{Tr}\Delta}{r(q-1)}
\le\frac1{8q}.
}
\tag{17}
\]

Thus the full-rank diagonal correction is nevertheless spectrally small **on average**, uniformly in the coarse conductor.

## 5. All normalized spectra live in the universal interval `[0,1/8]`

The full regular `N`-gon inverse-square chord Laplacian has the classical Calogero--Perelomov spectrum

\[
\lambda_k=\frac{k(N-k)}2,
\qquad 0\le k<N.
\tag{18}
\]

After normalization by `N^2`, its operator norm is at most `1/8`. Every induced-subset Laplacian is dominated, in Loewner order, by the corresponding principal compression of the full regular-polygon Laplacian. Therefore

\[
\boxed{
0\le A_{dq},H,M_{d,q}\le\frac18 I.
}
\tag{19}
\]

Equation (6), together with continuity of the finite-dimensional pencil and the density of the sampled rational Bloch parameters as new primes vary, gives the same bound for every `t in [0,1]`:

\[
\boxed{
0\le\mathcal P_d(t)\le\frac18 I.
}
\tag{20}
\]

For probability measures supported on `[0,1/8]`, the integral representation of `W_1` by cumulative distribution functions and (12) now give

\[
\boxed{
W_1(\mu_H,\mu_{M_{d,q}})
\le\frac18\,d_K(\mu_H,\mu_{M_{d,q}})
\le\frac{3}{8q}.
}
\tag{21}
\]

The important point is not the optimized constant but the uniform `O(1/q)` control: neither the old-point deletion nor the associated diagonal grounding can move an order-one fraction of the normalized bulk spectrum by an order-one distance.

## 6. The q-point Bloch sample converges to a q-independent integrated density of states

Define the base-level continuous Bloch measure

\[
\boxed{
\nu_d:=\int_0^1\mu_{\mathcal P_d(t)}\,dt.
}
\tag{22}
\]

Differentiating (7) gives

\[
\mathcal P_d'(t)
=\frac1{d^2}\left(\frac12C_d-tI\right).
\]

PC-156 proves `||C_d||<=2d`, so

\[
\boxed{
\|\mathcal P_d'(t)\|
\le\frac{d+1}{d^2}
\le\frac34
\qquad(d\ge2).
}
\tag{23}
\]

Weyl's eigenvalue perturbation inequality then makes `t -> mu_{mathcal P_d(t)}` Lipschitz in `W_1` with the same constant. Coupling each interval `[k/q,(k+1)/q]` to its left endpoint gives the elementary Riemann-sum estimate

\[
\boxed{
W_1(\mu_{M_{d,q}},\nu_d)
\le\frac{3}{8q}.
}
\tag{24}
\]

Combining (17), (21), and (24) yields the main result:

\[
\boxed{
W_1\!\left(\mu_{A_{dq}},\nu_d\right)
\le
\frac1{8q}+\frac3{8q}+\frac3{8q}
=
\frac{7}{8q}.
}
\tag{25}
\]

The estimate is **uniform in the base conductor `d`**. In particular it still applies along growing-base new-prime chains, including primorial-style refinements, whenever the newly adjoined prime tends to infinity.

## 7. Prior-art and novelty audit

Every ingredient used to prove (25) belongs to an already-audited classical family. The full regular-polygon `csc^2` spectrum in (18) is the Calogero--Perelomov identity already anchored in `research/prime_circle/SOURCES.md`. The weighted finite Fourier/cotangent identities behind the exact pencil (6)--(7) were audited in PC-156 against classical cotangent-sum theory and modern root-of-unity weighted trigonometric sums. Principal-submatrix interlacing, finite-rank empirical-distribution bounds, and Weyl monotonicity are standard Hermitian matrix analysis. The exact primitive-shell trace used in (15) was derived and audited in PC-140.

Directed searches for primitive-root `csc^2` matrices, reduced-residue inverse-square chord Laplacians, punctured circulant spectra, deleted-row/column `csc^2` operators, and finite-rank spectral-distribution comparisons did not locate this exact Prime-Circle decomposition of a new-prime shell as a one-point-per-fiber puncture of a q-Bloch semi-primitive ambient operator, nor the uniform estimate (25). That absence is not evidence of historical priority, and no new general matrix-analysis or trigonometric theorem is claimed.

The durable contribution is a **line-specific obstruction assembled from classical components**: the symmetry breaking caused by the missing residue in each genuinely new-prime fiber is too sparse, after natural geometric normalization, to alter the macroscopic empirical spectral distribution. This is a stronger boundary statement than PC-155's fiber-constant classification, while remaining compatible with PC-047's warning that old/new coupling can have maximal rank: maximal algebraic rank does not imply order-one bulk spectral displacement.

No new source anchor is needed; the load-bearing external ingredients are already present in `research/prime_circle/SOURCES.md`.

## 8. RH consequence, boundaries, and finite falsifiers

For the canonical single-level inverse-square chord operator, the route

\[
\boxed{
\text{new prime }q
\to
\text{retain the entire primitive fine fiber}
\to
\text{new order-one normalized bulk spectrum}
\to
\text{RH mechanism}
}
\]

is ruled out in the `q -> infinity` regime by (25). The empirical spectral measure converges instead to a fixed base-level Bloch average, with a uniform quantitative rate. Hence normalized trace statistics against Lipschitz test functions, macroscopic spectral density, and other bounded-Lipschitz bulk observables cannot carry an order-one new-prime signature beyond this inherited pencil.

This result deliberately does **not** rule out sparse edge/outlier modes, microscopic level statistics at spacings below the bulk Wasserstein scale, nonlinear functions that amplify a vanishing spectral fraction, genuinely cross-level nonseparable operators, growing-support linked clusters, or the global uniformization/monodromy program. It also does not say that the old/new block is low rank: PC-047 proves the opposite in broad composite families. The statement is about normalized **bulk measure**, not algebraic rank or every spectral observable.

The exact claim has direct finite falsifiers:

1. ordering `S_{d,q}` by coarse residue and additive q-fiber must give the exact Bloch decomposition (6);
2. deleting the unique q-divisible point from each fiber must leave the genuine primitive shell `U(dq)` and exactly `r` old points;
3. the rank bound (10) must hold for the padded principal block;
4. direct summation of old/new conductances must equal (14), and PC-140 must reduce it to (16);
5. normalized spectra of the ambient, padded, and primitive operators must remain in `[0,1/8]`;
6. numerical spectra must obey (25), and a single counterexample would falsify the stated uniform bound.

Finite checks on representative coprime pairs, including `(d,q)=(6,5),(10,3),(12,5)`, reproduced the Bloch block spectra to floating precision. Independent old/new conductance sums for `(3,5),(4,5),(5,7),(6,5),(10,7),(12,5),(15,7)` matched (14) to floating precision.

The frontier after PC-157 is therefore narrower than the one left by PC-156: **a genuinely new prime can break exact fiber translation, but that symmetry breaking does not survive as an order-one full-chord bulk spectral degree of freedom.** Any surviving Prime-Circle route must look at a finer or more nonlinear carrier than the single-level normalized empirical spectrum.