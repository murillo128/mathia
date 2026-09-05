# PF-168 — tail Dirichlet Laplacians are norm-resolvent composite-blind

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + LITERATURE-CLASSIFIED + DECISIVE-NEGATIVE/TAIL-SPECTRAL-BOUNDARY`. PF-125 constructs one globally coherent marking from the exact prime flute `X` to the exact all-composite shift clone `X_+` whose bilipschitz constant tends uniformly to `1` on the complete escaping tail. PF-166 used the same fact to collapse the entire marked tail length function. At the Laplace level the consequence is stronger than the fixed global compact-resolvent statement of PF-125: after cutting farther and farther out and imposing the matched Dirichlet boundary condition, the two tail Laplacians converge to each other in **generalized norm resolvent sense**, with an error controlled only by the tail bilipschitz defect.

Thus every bounded spectral filter in `C_0([0,infinity))`, including every fixed positive-time Dirichlet heat operator, becomes asymptotically identical on the prime and all-composite tails. This does not settle the accepted global Schatten or wave-operator clues: a norm-small infinite-rank relative operator need not belong to any Schatten class, and the moving Dirichlet cut removes precisely the global assembly/head interaction that scattering can retain.

## Claim

Let `F:X->X_+` be the PF-125 marking. For `N` sufficiently large, cut the two surfaces along the matched distinguished cuff before pant `P_N` and write

\[
T_N\subset X,
\qquad
T_N^+\subset X_+,
\]

for the corresponding closed tails. Put

\[
F_N:=F|_{T_N}:T_N\to T_N^+,
\qquad
K_N:=\operatorname{Bilip}(F_N).
\]

PF-125/PF-166 give

\[
\boxed{K_N\longrightarrow1.}
\tag{1}
\]

Let `Delta_N^D` and `Delta_{N,+}^D` be the nonnegative Dirichlet Laplacians on the two tails. Let

\[
J_N:L^2(T_N^+,d\mu_+)\to L^2(T_N,d\mu)
\]

be pullback by `F_N` (equivalently, after transporting the clone metric to `T_N`, the identity on functions). Then there is an absolute function `eta(K)->0` as `K->1` and a constant `C` bounded for `K` in a fixed neighborhood of `1` such that

\[
\boxed{
\left\|
J_N(\Delta_{N,+}^D+1)^{-1}
-(\Delta_N^D+1)^{-1}J_N
\right\|
\le C\,\eta(K_N)
\longrightarrow0.
}
\tag{2}
\]

One may take, non-optimally,

\[
\eta(K)=K^4-1
\qquad(K\ge1).
\tag{3}
\]

Therefore the matched Dirichlet tail Laplacians are generalized norm-resolvent equivalent in the limit `N->infinity`.

Standard generalized norm-resolvent functional calculus then gives, for every `phi in C_0([0,infinity))`,

\[
\boxed{
\|J_N\phi(\Delta_{N,+}^D)-\phi(\Delta_N^D)J_N\|
\longrightarrow0.
}
\tag{4}
\]

In particular, for every fixed `t>0`,

\[
\boxed{
\|J_N e^{-t\Delta_{N,+}^D}
-e^{-t\Delta_N^D}J_N\|
\longrightarrow0.
}
\tag{5}
\]

The conclusion is uniform over the **whole tail Hilbert space**; it is not a statement about finitely many test functions, finitely many pants, or one family of closed geodesics.

## 1. PF-125 gives uniform coefficient closeness on each complete tail

Transport the clone metric to `T_N` by `F_N` and denote it by `g_N^+`; let `g` be the prime metric. A `K_N`-bilipschitz comparison implies, almost everywhere,

\[
K_N^{-2}g
\le g_N^+
\le K_N^2 g
\tag{6}
\]

as quadratic forms on tangent vectors. In dimension two the volume density

\[
\rho_N:=\frac{d\mu_{g_N^+}}{d\mu_g}
\]

therefore satisfies

\[
K_N^{-2}\le \rho_N\le K_N^2.
\tag{7}
\]

Writing the clone Dirichlet energy with respect to `dmu_g`, there is a positive measurable endomorphism `C_N` of the cotangent bundle such that

\[
q_N^+(u,v)
=
\int_{T_N}\langle C_Ndu,dv\rangle_g\,d\mu_g.
\tag{8}
\]

The eigenvalues of `C_N` are bounded between powers of `K_N`; the conservative bounds

\[
K_N^{-4}I\le C_N\le K_N^4I
\tag{9}
\]

are enough. Hence, with

\[
\epsilon_N:=K_N^4-1,
\]

we have

\[
\boxed{
\|C_N-I\|_{L^\infty}
+
\|\rho_N-1\|_{L^\infty}
\le C\epsilon_N,
\qquad
\epsilon_N\to0.
}
\tag{10}
\]

No injectivity-radius lower bound, cusp truncation, or summation of pantwise defects enters (10). The PF-125 maps glue to one map on the entire tail, so `K_N` is a single supremum constant rather than a product of local errors.

## 2. The resolvent estimate is an elementary coercive-form estimate

The two uniformly equivalent metrics define the same Dirichlet form domain as a set,

\[
V_N=H_0^1(T_N).
\]

Put

\[
a(u,v)
=
\int_{T_N}
\bigl(\langle du,dv\rangle_g+u\bar v\bigr)d\mu_g,
\tag{11}
\]

and

\[
a_+(u,v)
=
\int_{T_N}
\bigl(\langle C_Ndu,dv\rangle_g+\rho_Nu\bar v\bigr)d\mu_g.
\tag{12}
\]

Equation (10) gives

\[
|a_+(u,v)-a(u,v)|
\le C\epsilon_N\|u\|_{V_N,g}\|v\|_{V_N,g}.
\tag{13}
\]

Now fix `f in L^2(T_N,dmu_g)`. Let

\[
u=(\Delta_N^D+1)^{-1}f,
\]

and let `u_+` be the clone resolvent applied to the same function after the identity/pullback identification. Variationally,

\[
a(u,v)=(f,v)_g,
\tag{14}
\]

whereas

\[
a_+(u_+,v)=\int_{T_N}\rho_N f\bar v\,d\mu_g.
\tag{15}
\]

The `+1` term makes both forms uniformly coercive. From (10), (12), and (15),

\[
\|u_+\|_{V_N,g}
\le C\|f\|_{L^2_g}
\tag{16}
\]

with `C` independent of sufficiently large `N`. Subtracting (14) and (15), using (13) and the density error in (10), and testing with `u_+-u`, gives

\[
\|u_+-u\|_{V_N,g}
\le C\epsilon_N\|f\|_{L^2_g}.
\tag{17}
\]

In particular,

\[
\|u_+-u\|_{L^2_g}
\le C\epsilon_N\|f\|_{L^2_g}.
\tag{18}
\]

Accounting for the fact that the `L^2` norms on the two sides differ by the factor `rho_N=1+O(epsilon_N)` yields (2). The proof uses only measurable uniformly elliptic coefficients and the matched Dirichlet form domain, so the piecewise-smooth seam/interpolation structure already admitted in PF-125 causes no additional regularity gate.

## 3. This is stronger than compact relative resolvent but weaker than Schatten control

PF-125/PF-123 concern one **fixed global pair** and prove that its first resolvent difference is compact because the metric coefficients tend to each other at infinity. Compactness alone does not say that the operator norm of a relative resolvent on an escaping tail tends to zero.

Equation (2) supplies that moving-tail statement:

\[
\boxed{
\text{discard farther finite heads}
\quad\Longrightarrow\quad
\text{the complete remaining Dirichlet spectral response converges in norm}.}
\tag{19}
\]

This still does not resolve `CLUE-shift-clone-sharp-schatten-threshold`. Operator norm controls only the largest singular value. An infinite-rank operator can have arbitrarily small norm while failing `S_r` for every finite `r`; no summability of singular values follows from (2). In particular, PF-112's local non-`S_1` result is perfectly compatible with PF-168.

Nor does (2) resolve `CLUE-shift-clone-wave-operator-equivalence`. The tails carry an artificial Dirichlet boundary which moves to infinity with `N`. Global wave/scattering theory compares one fixed uncut pair and can retain accumulated body/interface effects and repeated interaction with the finite head. Generalized norm-resolvent equivalence of moving tails is therefore a boundary theorem, not a scattering theorem.

## 4. Matched-control consequence

The control `X_+` is exact and all-composite: for every odd prime label `p_n`, its corresponding boundary label is `q_n=p_n+1`, hence composite. The comparison is not a random or smoothed surrogate; it uses the exact hyperbolic surface produced by the same construction rule from those replacement vertices.

PF-166 shows that all individual marked tail geodesic lengths are asymptotically clone-blind. PF-168 now shows the same phenomenon after **linear spectral assembly on an entire escaping tail** whenever the readout is continuous in generalized norm-resolvent topology. In particular, fixed positive-time heat propagation cannot recover primality merely by moving the observation window farther out.

This rules out a broad but precise class of proposed escapes: one cannot take farther tails, impose the canonical matched cut, apply a fixed `C_0` spectral filter of the Dirichlet Laplacian, and interpret a nonvanishing limiting operator response as a prime-specific signal. The all-composite control has the same limit in operator norm.

What remains possible is necessarily more singular or collective: rescale the vanishing relative operator before taking the limit; sum a nonsummable family of tiny differences; keep the full uncut surface so that scattering/head coupling survives; use a spectral operation discontinuous in norm-resolvent topology; or exhibit a genuinely prime-specific invariant outside the PF-125 asymptotic metric class. None of those mechanisms is established here.

## 5. Prior-art and novelty audit

No novelty is claimed for norm-resolvent stability of coercive elliptic forms under uniformly small coefficient perturbations, or for functional-calculus consequences of norm-resolvent convergence. The estimate (17) is the standard Lax--Milgram/form-perturbation argument specialized to the two PF-125 tail metrics.

For varying Hilbert spaces, the relevant established framework is generalized norm-resolvent convergence / quasi-unitary equivalence. Olaf Post and Sebastian Zimmer, *Generalised norm resolvent convergence: comparison of different concepts*, Journal of Spectral Theory 12 (2022), 1459--1506, DOI `10.4171/JST/442`, compare the standard notions and their convergence consequences. Olaf Post and Jan Simmer's quasi-unitary-equivalence work likewise records that closeness of energy forms yields norm estimates for resolvents and then for suitable functions of the operators; see *Graph-like spaces approximated by discrete graphs and applications*, Mathematische Nachrichten 294 (2021), DOI `10.1002/mana.201900108`, and their 2025 survey arXiv:`2503.22611`.

PF-123 already audits Georgescu--Golénia for the weaker fixed-pair conclusion `metric coefficients ->1 at infinity => compact relative resolvent`. That theorem does not make PF-168 new in abstract operator theory; PF-168 simply uses the stronger **uniform whole-tail** estimate actually available from PF-125 to upgrade the project-specific matched control from compactness to a quantitative moving-tail norm-resolvent collapse.

Directed searches for `infinite-type hyperbolic surface + asymptotic isometry + norm resolvent`, `flute surface + norm resolvent`, and `length-spectrum asymptotic isometry + Laplacian norm resolvent` located general norm-resolvent/quasi-unitary theory and geometric perturbation examples, but no source asserting this exact prime/shift-clone specialization. Search absence is not evidence of historical novelty.

## 6. Falsification surface

A later audit can falsify the finding by breaking any one of the following steps:

1. PF-125/PF-166 fail to provide a single globally coherent tail map with `K_N->1` on the **whole** `T_N` rather than only pantwise maps;
2. the bilipschitz estimate does not imply uniform closeness of the pulled-back metric energy coefficient `C_N` and density `rho_N` to `1`;
3. the matched Dirichlet form domains differ after transporting by `F_N`;
4. the coercive variational subtraction (13)--(18) contains an `N`-dependent constant that can blow up through cusp or zero-systole geometry;
5. the generalized functional-calculus implication (4) is applied outside its standard hypotheses.

Items 2--4 are exactly why the shift by `+1` is kept in the resolvent. The coercivity constant is algebraic and does not depend on a Poincare inequality, injectivity radius, finite area, or a lower systole. The boundary is matched by construction, and uniform metric equivalence gives the common `H_0^1` form domain.

The finding should **not** be falsified merely because the fixed global resolvent difference is nonzero, the first relative resolvent is not trace class, a relative Selberg/Ruelle sum amplifies infinitely many small orbit differences, or a global scattering matrix differs. Those effects are explicitly outside the moving-tail norm-resolvent claim.

## Research consequence

The all-composite shift clone now matches the prime flute at three increasingly collective tail levels: individual marked lengths (PF-166), positive primitive-length accumulation/counting pathology (PF-167), and the full fixed-filter Dirichlet Laplace response of an escaping tail (PF-168). A prime-specific spectral mechanism must therefore exploit information not continuous under this asymptotic tail metric equivalence — for example a renormalized first-order defect, a non-summable infinite assembly, or a genuinely global uncut scattering/resonance structure — rather than another fixed spectral observable applied after discarding the finite head.