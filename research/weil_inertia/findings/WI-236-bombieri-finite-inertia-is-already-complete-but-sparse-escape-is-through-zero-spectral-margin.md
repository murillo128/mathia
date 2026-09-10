# WI-236 — Bombieri finite inertia is already complete; the sparse escape is through zero spectral margin

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

A proposed Master clue asked whether Bombieri's cofinal finite truncations need a new negative-index persistence theorem in order to see an infinite zero-density off-critical divisor. A primary-source reconstruction changes that diagnosis. Bombieri's finite-dimensional theorem is already stronger than the finite-total summary usually quoted: for **every finite symmetric multiset** `Gamma`, Theorem 8 gives the exact negative index of `H(Gamma;t)`. Applied separately to the canonical height truncations `Gamma_N`, this gives exact finite-scale inertia even when the full off-line divisor is infinite. The finite-total hypothesis enters only when one wants the finite count to stabilize to a global finite number and, more importantly, when passing eigenvectors/eigenvalues to an infinite Weil witness.

Thus an infinite sparse off-line divisor cannot hide by making the **negative index** of later Bombieri truncations disappear. The genuine escape is subtler: finite negative eigenvalues may run into `0` as the truncation grows, while their eigenvectors fail to yield a nonzero limiting test function. In Bombieri's reciprocal resolvent variable `Lambda=1/lambda`, this is escape of the corresponding real roots to infinity, fully compatible with compact-uniform convergence of the Fredholm determinants. This closes the proposed Schur/interlacing route as stated and replaces it by a sharper target: prove a uniform spectral-margin/tightness statement for the negative eigensector, or exclude the limiting linear relations that Bombieri identifies when the margin collapses.

## 1. The exact finite theorem has no global finite-defect hypothesis

Bombieri writes each point as

\[
\rho=\frac12+i\gamma
\]

and, for a finite multiset with the zeta symmetries, constructs the matrix `H(Gamma;t)` in Sections 7--8 of *Remarks on Weil's quadratic functional in the theory of prime numbers, I*. His Theorem 8 states:

\[
\boxed{
 n_-\bigl(H(\Gamma;t)\bigr)
 = J(\Gamma),
}
\tag{1}
\]

where `J(Gamma)` is the number of **distinct complex-conjugate pairs** `(gamma, conjugate(gamma))` in the finite multiset. Lemma 10 separately accounts for repeated points: repetitions create zero eigenvalues, while if every `gamma` is real all eigenvalues are nonnegative. Consequently (1) must not be paraphrased as a multiplicity-counted formula without this caveat.

Now let `Gamma` be the actual infinite zeta multiset and

\[
\Gamma_N:=\{\gamma\in\Gamma:|\gamma|\le N\}.
\tag{2}
\]

Every `Gamma_N` is finite and retains the conjugation and sign symmetries, so Theorem 8 applies **for each N independently**, without assuming that the full set of nonreal `gamma` is finite. If

\[
J_N:=J(\Gamma_N),
\]

then

\[
\boxed{
 n_-\bigl(H(\Gamma_N;t)\bigr)=J_N
 \qquad\text{for every finite }N.
}
\tag{3}
\]

In particular, if there are infinitely many distinct off-critical zero packets, `J_N` is unbounded along the height cutoffs and so is the finite negative index. If the total off-line divisor is finite, then eventually `J_N` becomes constant, which is the finite-total stabilization advertised in Bombieri's abstract. The global finiteness hypothesis is therefore **not** a hypothesis of the finite inertia identity itself.

This is classical prior art. The Mathia contribution here is the corrected logical boundary: the proposed missing theorem

\[
\text{``cofinal negative-index persistence for an infinite sparse defect''}
\]

is already supplied, at the finite-matrix level, by Theorem 8 plus the canonical truncation (2). The unsolved passage is from that integer-valued finite inertia to a nonvanishing negative witness for the full Weil functional.

## 2. Why ordinary Hermitian interlacing is not the missing proof

It is tempting to argue that `H(Gamma_N;t)` is a principal block of `H(Gamma_{N'};t)` and hence a negative Rayleigh direction survives by zero extension. That argument would be automatic for nested Hermitian compressions, but Bombieri's off-line matrix is not presented in that form.

His equations (7.1) and (7.3) give

\[
\left(\frac14+x^2\right)K^*(x,y;t)
=
\left(\frac14+y^2\right)K^*(y,x;t),
\]

and

\[
H(x,y;t)=
\frac{2tK^*(x,y;t)}{\frac14+y^2}.
\]

Combining them yields the exact symmetry

\[
\boxed{H(x,y;t)=H(y,x;t).}
\tag{4}
\]

For off-line zeros the labels `gamma` are complex, so (4) makes the matrix complex symmetric, not generally Hermitian in the standard `ell^2` inner product. Bombieri correspondingly has to prove separately, through Lemma 9 and the associated differential eigenvalue problem, that its eigenvalues are real. Theorem 8 is then proved by deformation while preventing real eigenvalues from crossing zero.

Therefore Cauchy interlacing, Loewner monotonicity, and an ordinary Hermitian Rayleigh-quotient argument cannot simply be imported into this truncation family. The finite **count** nevertheless persists exactly because (3) recomputes it from the zero symmetries at every cutoff. A Schur-complement or tail-screen estimate would become relevant only after constructing a rigorously equivalent Hermitian/congruence formulation that preserves the needed sign and controls its normalization; no such identification with the WI Montgomery--Taylor compression is established here.

## 3. The actual passage-to-limit escape is `lambda_N -> 0`

Bombieri already isolates the noncompact step in Section 10. Let `lambda_N<0` be a negative eigenvalue of `H(Gamma_N;t)`, chosen there with largest absolute value, and normalize its eigenvector `w_N` in `ell^2`. Lemma 13 proves that at least half of its squared coefficient mass lies on nonreal `gamma` coordinates:

\[
\boxed{
\sum_{\gamma\notin\mathbb R}|w_{\gamma,N}|^2\ge\frac12.
}
\tag{5}
\]

When there are only finitely many nonreal coordinates globally, (5) gives a fixed finite reservoir on which a subsequence cannot lose all of its mass. Bombieri can then extract coordinatewise limits and obtain either a genuine negative Weil witness or a degenerate limiting relation. The finite-total hypothesis is load-bearing here; if the off-line set is infinite, (5) by itself allows the mass to migrate to ever higher nonreal coordinates while every fixed coordinate tends to zero.

Even in the finite-total case, the negative spectral parameter need not stay separated from zero. Sections 10--11 explicitly retain the alternative

\[
\lambda_N\longrightarrow0.
\tag{6}
\]

For the second eigenvalue problem, Lemma 14 identifies `lambda=0` with the limiting function vanishing identically on the test interval, and Theorem 11/its corollary turns the degenerate case into a nontrivial `ell^2` linear-dependence alternative among the zero exponentials. Bombieri remarks that his numerical experiments with an inserted fake off-line zero suggested negative eigenvalues approaching zero exponentially or nearly exponentially, and points to the associated eigenvectors/linear relations as the object needing deeper study.

There is also an exact resolvent interpretation of the same escape. Section 7 uses

\[
D_N(\Lambda;t)=\det\bigl(I-\Lambda H(\Gamma_N;t)\bigr),
\qquad \Lambda=\frac1\lambda,
\tag{7}
\]

and Theorem 6 proves that `D_N` converges uniformly on compact subsets of the `Lambda`-plane to the infinite Fredholm determinant. If a negative finite eigenvalue satisfies (6), its corresponding real zero

\[
\Lambda_N=\frac1{\lambda_N}
\]

runs to `-infinity`. Hence arbitrarily many exact finite negative eigenvalues can escape every compact `Lambda`-set through infinity without contradicting the determinant convergence. **Finite negative index alone carries no uniform spectral margin.**

## 4. Consequence for the infinite sparse-defect program

The corrected hierarchy is therefore

\[
\boxed{
\text{off-line packet below }N
\Longrightarrow
\text{exact finite negative index at }N
}
\tag{8}
\]

classically, whereas the missing implication is of the form

\[
\boxed{
\text{cofinal finite negative eigensector}
\Longrightarrow
\text{nonzero negative full-Weil witness}
}
\tag{9}
\]

with enough quantitative control to prevent both spectral collapse and coefficient escape.

A sufficient route would be a no-escape theorem giving, along a cofinal family, both a negative margin and tightness of normalized negative eigenvectors in the coefficient topology needed by Bombieri's infinite eigenproblem. Another route would prove that the `lambda=0` limiting linear relations forced by collapse cannot occur for the Riemann-zeta zero divisor. Either result would attack the actual boundary in Bombieri rather than reproving the already exact integer inertia count.

For an **infinite sparse** off-line set, an especially concrete target is to strengthen (5) from aggregate mass on all nonreal coordinates to a height-tight estimate such as

\[
\exists R<\infty,\ \eta>0:
\qquad
\limsup_{N\to\infty}
\sum_{\substack{\gamma\notin\mathbb R\\|\gamma|\le R}}
|w_{\gamma,N}|^2\ge\eta,
\tag{10}
\]

for a suitably chosen negative eigensequence, together with control preventing its eigenvalues from escaping through zero. Formula (10) is a **research target**, not an established consequence of Bombieri or of the present WI ledger.

## 5. Relation to WI-232--WI-235

WI-232--WI-235 quantify how a macroscopic, density-calibrated off-line bow can be screened in local harmonic observables: local zero-count capacity, radial amplitude, and spacing surplus all carry explicit tariffs. Those results remain valid, but there is currently no theorem identifying Bombieri's coefficient mass `|w_{gamma,N}|^2`, or the rate `lambda_N -> 0`, with the selected bow amplitudes and spacing variables appearing in that ledger.

Accordingly, the proposed shortcut

\[
\text{Bombieri negative packet}
\to
\text{Schur interaction}
\to
\text{WI screening tariff}
\]

is not yet justified. In particular, the complex-symmetric character of `H` makes the clue's ordinary Rayleigh/Schur wording too strong. The WI tariffs may become relevant later if one derives an exact bridge from eigenvector escape or spectral collapse to those local observables, but they cannot currently be charged as the cost of preserving Bombieri's negative index: the index is already exact without paying them.

This also sharpens the line's ultimate RH objective. Normalized first/second moments can miss an `o(N)` exceptional divisor, while Bombieri's exact finite inertia sees every finite cutoff of that divisor. The remaining problem is not more finite observability; it is **coercive passage from finite observability to the infinite completed form**.

## 6. Prior art and novelty audit

Primary source:

- Enrico Bombieri, “Remarks on Weil's quadratic functional in the theory of prime numbers, I,” *Rend. Mat. Acc. Lincei* s. 9, **11** (2000), 183--233. Digitized primary text: <https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0>. The load-bearing statements are equations (7.1), (7.3), Theorem 6, Lemmas 9--10, Theorem 8, Lemma 13, Lemma 14, and Theorems 10--11.

A recent operator-theoretic revisit is Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096 (2026), <https://arxiv.org/abs/2606.09096>. Its advertised contribution is a unified operator framework for Yoshida/Bombieri/Connes--Consani and a conjectural large-interval self-adjoint limit; the abstract does not supply the uniform Bombieri-truncation margin or eigenvector-tightness theorem required in (9)--(10), so it is contextual prior art rather than evidence for the missing step.

The bounded cross-line source authorized by the Master clue, `PL-260` at revision `fd0af64872690ee68275a94370c0390392cd3f2e`, correctly emphasizes that finite-dimensional Weil forms can see sparse defects, but its stated boundary is weaker than Bombieri's Theorem 8. The global finite-total hypothesis is needed to speak of an eventually stabilized **total** defect and in Bombieri's passage-to-limit analysis; it is not needed to compute the exact inertia of each finite `Gamma_N`. This finding records that correction locally and does not edit or silently generalize the Prime Lattice artifact.

A targeted literature/repository audit did not locate a theorem closing the infinite sparse no-escape problem above. Search absence is not evidence of originality. Theorem 8, the zero-margin/linear-relation alternative, and the finite-total analysis are Bombieri's. The only new claims made here are the exact logical diagnosis of the Master clue, the observation that the cofinal finite-index question is already settled finite-by-finite, and the resolvent reformulation of spectral collapse as roots escaping to `Lambda=infinity`.

## 7. Adversarial boundaries and falsification

1. **Equation (3) is not an RH proof.** `H(Gamma_N;t)` is built on the zero-side finite divisor. Knowing that its inertia detects every off-line packet does not by itself construct an arithmetic negative test function for the full Weil functional.

2. **Do not count multiplicities incorrectly.** Theorem 8 counts distinct complex-conjugate pairs; Lemma 10 puts repeated-point excess into the zero eigenspace. Any later multiplicity-sensitive bridge must retain that distinction.

3. **Do not use Hermitian interlacing without a new equivalence theorem.** The actual Bombieri matrix is complex symmetric off the critical line and has real spectrum for a special structural reason. A standard principal-submatrix Rayleigh argument is not available merely because the coordinate sets are nested.

4. **Negative index can coexist with vanishing usable margin.** Equation (3) constrains signs at every finite cutoff, not the distance of those eigenvalues from zero or compactness of their eigenvectors.

5. **The finite-total compactness mechanism does not extend automatically.** With infinitely many nonreal coordinates, the aggregate lower bound (5) is compatible with all mass escaping to increasing heights.

6. **WI local screening is not yet Bombieri spectral tightness.** No current finding proves a map from `lambda_N`, `w_N`, or the Bombieri resolvent to the bow variables of WI-232--WI-235. Such a map would itself be a substantive theorem.

7. **Different Weil truncation families must remain distinct.** This finding concerns Bombieri's `H(Gamma_N;t)`. It does not transfer (3) to Alpöge--Furman/Montgomery--Taylor matrices, Connes--Consani--Moscovici compressions, or other source-computable Galerkin families without an explicit equivalence/congruence proof.

## Consequence for the research line

The Master clue's proposed negative-index persistence test should not be pursued in its present form. Bombieri already gives exact finite negative-index completeness for every canonical height truncation, including truncations of a hypothetical infinite sparse off-line divisor. The decisive unresolved object is the **negative spectral margin and eigenvector tightness**, equivalently the prevention of escape through `lambda=0` / `Lambda=infinity` or the exclusion of the resulting limiting linear relations.

That replacement target is closer to the `weil_inertia` mandate than another bulk-moment refinement: it asks precisely what extra coercivity is required to turn individual finite off-line detectability into a full-form contradiction, while keeping global Weil positivity itself as the target rather than as an assumption.