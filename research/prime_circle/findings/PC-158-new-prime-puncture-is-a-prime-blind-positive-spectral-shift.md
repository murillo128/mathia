# PC-158 — new-prime puncture is a prime-blind positive spectral shift

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for extracting a growing family of order-one normalized edge/outlier modes from the **one-missing-residue-per-fiber defect** left open by PC-157. PC-157 proved only an `O(1/q)` bulk Wasserstein collapse of a new-prime shell toward a fixed Bloch limit and explicitly left sparse edge modes open. The puncture can be classified more sharply before attempting any microscopic or scattering interpretation.

Fix `d>=2` and let `q` be a prime with `q∤d`. Put `r=phi(d)`. On the semi-primitive ambient set

\[
S_{d,q}=\{x\bmod dq:(x,d)=1\}
\]

PC-157 identifies the genuine primitive shell `U(dq)` as the result of deleting exactly one old point from each of the `r` complete `q`-fibers. Let `M_{d,q}` be the normalized inverse-square chord Laplacian on `S_{d,q}`, let `A_{dq}` be the normalized induced Laplacian on `U(dq)`, and pad `A_{dq}` by `r` zero coordinates on the deleted old set. Then the difference is not merely small in empirical measure: it is **exactly a positive weighted-graph Laplacian**,

\[
\boxed{
K_{d,q}:=M_{d,q}-(A_{dq}\oplus0_r)\succeq0.
}
\tag{1}
\]

Its trace norm therefore equals its trace, and that trace is explicit. Define

\[
\rho_d:=\prod_{p\mid d}\left(1-\frac1p-\frac1{p^2}\right)>0.
\tag{2}
\]

Then

\[
\boxed{
\|K_{d,q}\|_1
=\operatorname{Tr}K_{d,q}
=\frac{r}{12}
\left[
2\rho_d-\frac{\rho_d+d^{-2}}{q^2}
\right].
}
\tag{3}
\]

Consequently, if the two `rq` eigenvalue lists are arranged increasingly, every displacement is nonnegative and their total displacement is exactly (3). Equivalently, for the equally weighted empirical spectral measures,

\[
\boxed{
W_1\!\left(\mu_{M_{d,q}},\mu_{A_{dq}\oplus0_r}\right)
=
\frac1{12q}
\left[
2\rho_d-\frac{\rho_d+d^{-2}}{q^2}
\right]
<\frac1{6q}.
}
\tag{4}
\]

For every fixed `epsilon>0`, at most

\[
\boxed{
\frac{r}{12\epsilon}
\left[
2\rho_d-\frac{\rho_d+d^{-2}}{q^2}
\right]
<\frac{r}{6\epsilon}
}
\tag{5}
\]

ordered spectral positions can move by at least `epsilon`. Thus adjoining a new prime creates `r(q-1)` primitive fine degrees of freedom, but the one-point puncture can move only `O(r)` of the padded Bloch eigenvalue positions by an order-one normalized amount, uniformly in `q`. It cannot generate a `q`-proportional family of macroscopic defect modes.

More importantly for the Prime-Circle falsification controls, **none of (1)--(5) uses primality of the fiber size**. For every integer `m>=2` coprime to `d`, delete the single section consisting of the `m`-divisible point from each complete `m`-fiber of `S_{d,m}`. The same positivity and the same formulas hold with `q` replaced by `m`. When `m=q` is prime the survivor is exactly `U(dq)`; for composite `m` the survivor is a matched one-hole geometric control rather than the true primitive shell. Therefore the positive spectral-shift budget created by the missing section is **prime-blind**. Any prime-specific surviving mechanism must use information beyond the fact that one residue is missing from each complete fiber.

## 1. The puncture difference is exactly an edge Laplacian

The prime case is a specialization of a slightly more general statement. Let `m>=2` satisfy `(m,d)=1` and put

\[
S_{d,m}:=\{x\bmod dm:(x,d)=1\}.
\tag{6}
\]

Reduction modulo `d` identifies this set with `r` complete cyclic `m`-fibers. Let

\[
O_{d,m}:=\{x\in S_{d,m}:m\mid x\},
\qquad
X_{d,m}:=S_{d,m}\setminus O_{d,m}.
\tag{7}
\]

There is exactly one point of `O_{d,m}` in every coarse fiber, so `|O_{d,m}|=r` and `|X_{d,m}|=r(m-1)`. If `m=q` is a new prime, then

\[
\boxed{X_{d,q}=U(dq).}
\tag{8}
\]

Let

\[
M_{d,m}:=(dm)^{-2}L_{dm}[S_{d,m}],
\qquad
A_{d,m}^{\rm hole}:=(dm)^{-2}L_{dm}[X_{d,m}].
\tag{9}
\]

Order the ambient space as `X_{d,m} sqcup O_{d,m}` and pad the induced operator by zeros,

\[
\widehat A_{d,m}:=A_{d,m}^{\rm hole}\oplus0_r.
\tag{10}
\]

A weighted graph Laplacian is a sum over edges,

\[
L=\sum_{\{x,y\}}w_{xy}(e_x-e_y)(e_x-e_y)^*.
\tag{11}
\]

The terms with both endpoints in `X_{d,m}` are exactly the terms of `A_{d,m}^{\rm hole}`. Subtracting them from the ambient operator therefore leaves precisely the edges having at least one endpoint in `O_{d,m}`:

\[
\boxed{
K_{d,m}:=M_{d,m}-\widehat A_{d,m}
=
\frac1{(dm)^2}
\sum_{\substack{\{x,y\}\subset S_{d,m}\\
\{x,y\}\cap O_{d,m}\ne\varnothing}}
\kappa_{dm}(x-y)(e_x-e_y)(e_x-e_y)^*.
}
\tag{12}
\]

Every summand is positive semidefinite. Hence

\[
\boxed{0\preceq\widehat A_{d,m}\preceq M_{d,m}.}
\tag{13}
\]

This is stronger than the finite-rank comparison used in PC-157. The defect is generally not low rank—the diagonal grounding part can be full rank—but it is positive, so its complete trace-norm budget is accessible exactly.

## 2. The old/new conductance gives an exact trace

Write `deg_d(a)` for the unnormalized inverse-square degree of `a in U(d)` inside the base primitive shell. Fix an old point `y in O_{d,m}` and let `y_0 in U(d)` be its coarse label after the natural multiplicative permutation.

The complete `m`-fiber distribution identity for `csc^2` gives `m^2 deg_d(y_0)` from all other coarse fibers. Inside the same coarse fiber, the other `m-1` points contribute the full regular-`m`-gon degree

\[
\frac{m^2-1}{12}.
\tag{14}
\]

The old-to-old points form a rotated copy of `U(d)` and contribute exactly `deg_d(y_0)`. Therefore the conductance from `y` to the surviving one-hole set is

\[
\boxed{
\operatorname{cond}(y,X_{d,m})
=(m^2-1)
\left(\operatorname{deg}_d(y_0)+\frac1{12}\right).
}
\tag{15}
\]

This is the PC-157 old/new trace calculation with no use of primality. Summing over the old section and inserting the `(dm)^{-2}` normalization gives the total normalized old/new edge weight

\[
E_{XO}
=\left(1-\frac1{m^2}\right)
\left(
\operatorname{Tr}A_d+\frac{r}{12d^2}
\right),
\tag{16}
\]

where

\[
A_d:=d^{-2}L_d^{\rm int}.
\]

PC-140 supplies the exact primitive-shell trace identity. Factoring its Euler product gives

\[
\boxed{
\operatorname{Tr}A_d+\frac{r}{12d^2}
=\frac{r\rho_d}{12},
\qquad
\operatorname{Tr}A_d
=\frac r{12}\left(\rho_d-d^{-2}\right).
}
\tag{17}
\]

The old set itself is a copy of the base primitive shell with all chord differences multiplied by `m`; after normalization its internal Laplacian therefore has trace

\[
\boxed{
\operatorname{Tr}A_{OO}
=\frac1{m^2}\operatorname{Tr}A_d.
}
\tag{18}
\]

Each old/new edge contributes twice its weight to the trace of the edge Laplacian, while (18) already counts both endpoints of every old/old edge. Thus

\[
\operatorname{Tr}K_{d,m}
=2E_{XO}+\frac1{m^2}\operatorname{Tr}A_d.
\tag{19}
\]

Substituting (16)--(18) yields the exact closed form

\[
\boxed{
\operatorname{Tr}K_{d,m}
=\frac r{12}
\left[
2\rho_d-\frac{\rho_d+d^{-2}}{m^2}
\right].
}
\tag{20}
\]

Because `K_{d,m}>=0`, equation (20) is simultaneously its Schatten-1 norm. There is no cancellation hidden inside the `O(1/m)` bulk estimate of PC-157.

## 3. The Wasserstein displacement is exact, not merely bounded

Let

\[
\alpha_1\le\cdots\le\alpha_{rm},
\qquad
\beta_1\le\cdots\le\beta_{rm}
\]

be the eigenvalues of `widehat A_{d,m}` and `M_{d,m}` respectively. Loewner monotonicity from (13) gives

\[
\boxed{\alpha_j\le\beta_j\quad(1\le j\le rm).}
\tag{21}
\]

For two equally weighted empirical measures on the line, monotone matching is the optimal `W_1` coupling. Hence

\[
W_1(\mu_{\widehat A_{d,m}},\mu_{M_{d,m}})
=rac1{rm}\sum_{j=1}^{rm}(\beta_j-\alpha_j)
=rac{\operatorname{Tr}K_{d,m}}{rm}.
\tag{22}
\]

Using (20),

\[
\boxed{
W_1(\mu_{\widehat A_{d,m}},\mu_{M_{d,m}})
=
\frac1{12m}
\left[
2\rho_d-\frac{\rho_d+d^{-2}}{m^2}
\right].
}
\tag{23}
\]

Since every factor in `rho_d` lies in `(0,1)`, this is strictly below `1/(6m)`. Equation (23) is stronger than an `O(1/m)` statement: it identifies the complete first absolute spectral-shift mass and shows that the scale has a smooth composite continuation.

The same positivity gives a direct macroscopic-shift count. For any `epsilon>0`, put

\[
N_\epsilon(d,m)
:=\#\{j:\beta_j-\alpha_j\ge\epsilon\}.
\tag{24}
\]

Then

\[
\boxed{
N_\epsilon(d,m)
\le\frac{\operatorname{Tr}K_{d,m}}{\epsilon}
<\frac{r}{6\epsilon}.
}
\tag{25}
\]

The right side is independent of the fiber size. At fixed base conductor, increasing a new prime can therefore create arbitrarily many **microscopic** Bloch samples, but not arbitrarily many order-one puncture shifts.

For the actual prime shell one can also sharpen the numerical constant in PC-157. Since

\[
\mu_{A_{dq}\oplus0_r}
=\frac{q-1}{q}\mu_{A_{dq}}+\frac1q\delta_0
\]

and `A_{dq}>=0`, this padded measure is stochastically below `mu_{A_{dq}}`, so

\[
W_1(\mu_{A_{dq}},\mu_{A_{dq}\oplus0_r})
=\frac1q\int\lambda\,d\mu_{A_{dq}}(\lambda)
\le\frac1{8q}.
\tag{26}
\]

Combining (23), PC-157's `3/(8q)` Riemann-sum bound from the ambient Bloch sample to `nu_d`, and (26) gives the convenient refinement

\[
\boxed{
W_1(\mu_{A_{dq}},\nu_d)<\frac{2}{3q}.
}
\tag{27}
\]

The improved constant is secondary; the structural content is the exact positive shift (20)--(23).

## 4. Matched composite control removes primality from the puncture mechanism

The derivation above intentionally allowed arbitrary `m` coprime to `d`. For composite `m`, the one-hole survivor `X_{d,m}` is generally larger than `U(dm)`, because deleting only the residue `0 mod m` does not delete points divisible by proper prime factors of `m`. That is precisely why it is a useful matched control rather than another primitive-shell theorem.

The ambient object, chord kernel, complete fiber symmetry, deleted-section cardinality, and normalization are unchanged. Equations (12), (20), (23), and (25) therefore hold with **exactly the same functional dependence on the integer fiber size**, regardless of whether that size is prime or composite. In particular, the puncture shift has no factor such as `mu(m)`, `Lambda(m)`, `phi(m)`, a prime-only character space, or any other arithmetic discriminator of primality.

This does not prove that every microscopic eigenvalue of the one-hole family is independent of the integer `m`; the finite matrices still sample the circle at scale `m`. It proves the narrower and relevant obstruction: **positivity, total trace-class budget, macroscopic displacement count, and first spectral-shift measure created by one missing section are geometric one-hole facts, not prime facts.** A candidate that uses only those data cannot explain why the actual survivor is a primitive shell at prime `q`.

A genuine composite primitive shell deletes additional residue sections determined by the prime factors of `m`. Any arithmetic difference seen only after those extra deletions belongs to a different multi-hole mechanism and is not evidence for the new-prime one-hole defect.

## 5. Prior-art and novelty audit

The ingredients are deliberately conservative. The regular-polygon `csc^2` degree and multiplication identities are classical and already anchored in `research/prime_circle/SOURCES.md` through Calogero--Perelomov and the cotangent/cosecant distribution literature used in PC-155--PC-157. The arithmetic simplification (17) is exactly the stored PC-140 trace formula. Positivity under adding weighted graph edges, Loewner eigenvalue monotonicity, and monotone optimal transport for one-dimensional empirical measures are standard matrix/transport facts.

The general viewpoint that deleting or locally perturbing a periodic/Bloch operator preserves its bulk while allowing localized defect modes is also classical perturbation theory. Directed searches across vertex-deleted periodic graphs, localized Bloch defects, punctured circulants, `csc^2` matrices, and spectral-shift formulations did not locate the exact one-section Prime-Circle identity (20) or its matched-composite interpretation. That absence is not evidence of historical priority, and no new general theorem about periodic defects is claimed.

The durable content is instead the **Prime-Circle classification boundary**: the specific symmetry breaking that turns the full new-prime fiber into `U(dq)` has an exact positive spectral-shift budget, and that budget extends unchanged to a composite one-hole control. Hence the most immediate edge/outlier escape left by PC-157 cannot derive prime-specific macroscopic spectral complexity merely from the missing residue.

No new literature anchor is required: every load-bearing external identity used in the derivation is already present in `research/prime_circle/SOURCES.md`.

## 6. RH consequence and remaining boundary

For the canonical normalized inverse-square chord operator, the route

\[
\boxed{
\text{new prime }q
\to
\text{one missing point per complete fiber}
\to
\text{growing family of order-one defect modes}
\to
\text{new RH spectrum}
}
\]

is ruled out. The one-hole puncture has only `O(r)` total macroscopic displacement capacity while the fine space has dimension `r(q-1)`, and the exact shift law is shared by composite one-hole controls.

This result is intentionally not a blanket no-go for the edge of the spectrum. It leaves open:

- `O(1/q)` or smaller microscopic level statistics, where an `O(r)` trace budget may be spread across `O(rq)` modes;
- finitely many order-one defect/gap modes per coarse degree, including their exact locations and any relative scattering determinant;
- the true **multi-hole** deletion pattern of composite primitive shells and interactions among the deleted sections;
- nonlinear amplification or cross-level observables that retain the defect before taking a first spectral-shift moment;
- growing-support linked clusters not represented by a fixed one-hole perturbation;
- and the global uniformization/monodromy branch.

Any successor claiming a prime-specific edge mechanism must therefore use one of those residual structures and must beat the composite one-hole control. Merely observing a sparse outlier, a nonzero puncture determinant, or a finite spectral shift at prime fiber size is not enough.

## 7. Finite audit and falsification surface

The theorem is exact and admits direct checks without asymptotics.

For `d=6`, `q=5`, one has `r=2`, `rho_6=5/36`, and (20) gives

\[
\boxed{\operatorname{Tr}K_{6,5}=\frac{61}{1350}.}
\tag{28}
\]

Direct construction of the `10 x 10` semi-primitive ambient matrix and the padded `8 x 8` primitive-shell operator gives the same trace; the smallest eigenvalue of their difference is zero up to numerical roundoff, as required by (12).

As a genuinely composite control, take `d=5`, `m=6`. The one-hole survivor is not `U(30)`, but the same derivation gives

\[
\boxed{\operatorname{Tr}K_{5,6}=\frac{337}{675}.}
\tag{29}
\]

again matching direct finite enumeration.

A counterexample to any of the following would falsify the finding: `K_{d,m}` having a negative eigenvalue; (15) failing for one old vertex; (20) failing for one coprime pair `(d,m)`; or the sorted eigenvalue displacement in (22) not summing to the trace difference. The prime-specific conclusion would also have to be withdrawn if any step in (12)--(25) were shown to require primality rather than only `(d,m)=1`.