# PL-381 — Semibounded log-prime covariance forces global Wold regularity

**Evidence:** `DERIVED+LOCAL-CANONICAL-DEPENDENCIES + DECISIVE-STRUCTURAL-BOUNDARY`.

**Parent finding:** `PL-380`.

**Related findings:** `PL-004`, `PL-007`, `PL-023`, `PL-024`, `PL-379`, `PL-380`.

**Status:** `POSITIVE-ENERGY-EXACT-LOG-PRIME-COVARIANCE-DOES-EXCLUDE-THE-DIFFUSE-COUNTABLE-WOLD-PATHOLOGY-LEFT-OPEN-BY-PL-379, BUT-ONLY-BY-FORCING-THE-GLOBAL-REGULAR-PRIME-MULTISHIFT-WITH-AN-ARBITRARY-PRIME-INDEPENDENT-INTERNAL-ENERGY-SECTOR. THE-COERCIVE-LOCALLY-FINITE-WEIGHTS-LOG-P-MAKE-EVERY-BOUNDED-ENERGY-SUBSPACE-DEPEND-ON-ONLY-FINITELY-MANY-PRIME-DIRECTIONS, SO-FINITE-WOLD-ORTHOGONALITY-GLOBALIZES. THIS-MECHANISM-WORKS-FOR-ANY-COUNTABLE-POSITIVE-LOCALLY-FINITE-WEIGHT-FAMILY-AND-THEREFORE-PROVIDES-NO-RATIONAL-PRIME-SPECIFIC-RH-RIGIDITY`.

## Claim

Let `P` be the rational primes and let

\[
\{V_p:p\in\mathcal P\}
\tag{PL381-1}
\]

be commuting, doubly commuting isometries on a Hilbert space `H`:

\[
V_pV_q=V_qV_p,
\qquad
V_p^*V_q=V_qV_p^*
\quad(p\ne q).
\tag{PL381-2}
\]

Let `A` be self-adjoint and bounded below,

\[
m:=\inf\sigma(A)>-\infty,
\tag{PL381-3}
\]

and write `U_t=e^{itA}`. Assume the exact strong covariance

\[
U_tV_pU_t^*=e^{it\log p}V_p
\qquad(t\in\mathbb R,\ p\in\mathcal P).
\tag{PL381-4}
\]

Then every `V_p` is pure, the joint wandering subspace

\[
W:=\bigcap_{p\in\mathcal P}\ker V_p^*
\tag{PL381-5}
\]

is generating, and hence the family is globally the regular prime multishift:

\[
\mathcal H
=\bigoplus_{\alpha\in\mathbb N_0^{(\mathcal P)}}V^\alpha W,
\qquad
V^\alpha:=\prod_pV_p^{\alpha_p},
\tag{PL381-6}
\]

with mutually orthogonal summands. Equivalently, the unitary from `PL-380`,

\[
\Phi:\ell^2(\mathbb N_0^{(\mathcal P)})\otimes W\to\mathcal H,
\qquad
\Phi(e_\alpha\otimes w)=V^\alpha w,
\tag{PL381-7}
\]

satisfies

\[
\Phi^*V_p\Phi=S_p\otimes I_W.
\tag{PL381-8}
\]

Moreover `W` reduces `U_t`. If `B` denotes the self-adjoint generator of `U_t|_W`, then under (PL381-7)

\[
\Phi^*A\Phi
=
N_{\log}\otimes I_W+I\otimes B,
\tag{PL381-9}
\]

where

\[
N_{\log}e_\alpha
=
\Big(\sum_p\alpha_p\log p\Big)e_\alpha
=
(\log n)e_\alpha,
\qquad n=\prod_pp^{\alpha_p}.
\tag{PL381-10}
\]

Thus semibounded exact log-prime covariance supplies a genuine globalization criterion missing from `PL-379`: it forbids the diffuse infinite-coordinate type fields that defeat naive passage from finite Wold decompositions to the countable prime family. But the output is exactly the standard prime Fock/Bohr shift with multiplicity `W`, plus a prime-independent internal Hamiltonian `B`. It therefore repairs representation theory without producing analytic continuation, the functional equation, a zero-sensitive determinant, or critical-line localization.

## 1. Semibounded covariance makes every prime isometry pure

Fix a prime `p` and put `lambda_p=log p>0`. The unitary part in the ordinary Wold decomposition of `V_p` is

\[
K_p:=\bigcap_{k\ge0}V_p^k\mathcal H.
\tag{PL381-11}
\]

Covariance gives

\[
U_tV_p^k=e^{itk\lambda_p}V_p^kU_t,
\tag{PL381-12}
\]

so every range `V_p^k H`, and therefore their intersection `K_p`, is invariant under `U_t` for all real `t`. Hence `K_p` reduces the unitary group and the restriction `A_p=A|_{K_p}` is self-adjoint and still bounded below by `m`.

On `K_p`, the restriction of `V_p` is unitary. Equation (PL381-4) therefore implies

\[
V_p^*U_tV_p=e^{it\lambda_p}U_t
\quad\text{on }K_p,
\tag{PL381-13}
\]

and Stone's theorem gives

\[
V_p^*A_pV_p=A_p+\lambda_p.
\tag{PL381-14}
\]

The left side is unitarily equivalent to `A_p`, while the right side shifts the lower spectral edge by the strictly positive number `lambda_p`. If `K_p` were nonzero, then

\[
\inf\sigma(A_p)
=
\inf\sigma(A_p+\lambda_p)
=
\inf\sigma(A_p)+\lambda_p,
\tag{PL381-15}
\]

which is impossible. Thus `K_p=0`, so every coordinate `V_p` is a pure isometry.

This first step already shows what semiboundedness contributes. Without a lower spectral edge, exact translation covariance is compatible with a unitary coordinate whose spectrum extends indefinitely downward; the positive-energy hypothesis removes that sector.

## 2. Finite energy sees only finitely many prime directions

Let `E_A` be the spectral measure of `A`, choose `M>=m`, and set

\[
\mathcal H_M:=E_A([m,M])\mathcal H.
\tag{PL381-16}
\]

Define

\[
F_M:=\{p:\log p\le M-m\}
=\{p:p\le e^{M-m}\}.
\tag{PL381-17}
\]

This set is finite. The covariance relation implies the spectral-shift identities

\[
E_A(B)V_p=V_pE_A(B-\log p),
\qquad
V_p^*E_A(B)=E_A(B-\log p)V_p^*
\tag{PL381-18}
\]

for Borel sets `B`.

Because the tuple indexed by the finite set `F_M` is doubly commuting and every coordinate is pure, the finite Wold construction can be iterated coordinate by coordinate. Writing

\[
W_{F_M}:=\bigcap_{p\in F_M}\ker V_p^*,
\tag{PL381-19}
\]

one obtains

\[
\mathcal H
=
\bigoplus_{\alpha\in\mathbb N_0^{F_M}}
V^\alpha W_{F_M}.
\tag{PL381-20}
\]

No countable-globalization theorem is being assumed here: (PL381-20) uses only finitely many coordinates.

The subspace `W_{F_M}` is invariant under every `U_t`, because each kernel `ker V_p^*` is invariant by (PL381-4). Hence every sector `V^alpha W_{F_M}` in (PL381-20) is invariant under all `U_t`; its orthogonal projection therefore commutes with every spectral projection of `A`.

Take `x in H_M` and write its finite-prime Wold expansion as

\[
x=\sum_\alpha x_\alpha,
\qquad
x_\alpha=V^\alpha w_\alpha,
\quad w_\alpha\in W_{F_M}.
\tag{PL381-21}
\]

Each `x_alpha` still belongs to `H_M`. Put

\[
\Lambda(\alpha):=\sum_{p\in F_M}\alpha_p\log p.
\tag{PL381-22}
\]

Applying `(V^alpha)^*` and using (PL381-18) shows that `w_alpha` has no spectral support above `M-Lambda(alpha)`. Consequently

\[
w_\alpha\ne0
\quad\Longrightarrow\quad
\Lambda(\alpha)\le M-m.
\tag{PL381-23}
\]

There are only finitely many such multi-indices because `F_M` is finite and all its weights are positive.

Now let `q notin F_M`. Then `log q>M-m`, and another application of (PL381-18) gives

\[
V_q^*w_\alpha
\in
E_A(( -\infty,\,M-\Lambda(\alpha)-\log q])\mathcal H.
\tag{PL381-24}
\]

The upper endpoint in (PL381-24) is strictly smaller than `m`; semiboundedness therefore forces

\[
V_q^*w_\alpha=0.
\tag{PL381-25}
\]

Together with `w_alpha in W_{F_M}`, this proves

\[
w_\alpha\in\bigcap_{p\in\mathcal P}\ker V_p^*=W.
\tag{PL381-26}
\]

Thus every bounded-energy vector is not merely approximated but is a **finite** linear combination of translates of the global wandering space:

\[
\mathcal H_M
\subseteq
\operatorname{span}\{V^\alpha W:\alpha\in\mathbb N_0^{(\mathcal P)}\}.
\tag{PL381-27}
\]

Since `A` is semibounded self-adjoint,

\[
\overline{\bigcup_{M>m}\mathcal H_M}=\mathcal H.
\tag{PL381-28}
\]

Equations (PL381-27)--(PL381-28) prove that `W` is generating. The diffuse failure exhibited in `PL-379` is therefore impossible under (PL381-3)--(PL381-4).

## 3. The resulting energy is the canonical log lattice plus an internal sector

Once `W` is generating, `PL-380` supplies the unitary identification (PL381-7)--(PL381-8). It remains to identify `A`.

The covariance of `V_p^*` shows that every `ker V_p^*`, hence `W`, is invariant under `U_t`; because `U_t` is unitary for all positive and negative times, `W` reduces `U_t`. Let

\[
e^{itB}=U_t|_W.
\tag{PL381-29}
\]

For `alpha` of finite support and `w in W`, repeated use of (PL381-4) gives

\[
U_tV^\alpha w
=
e^{it\Lambda(\alpha)}V^\alpha e^{itB}w.
\tag{PL381-30}
\]

Transporting this through `Phi` yields

\[
\Phi^*U_t\Phi
=
e^{itN_{\log}}\otimes e^{itB}.
\tag{PL381-31}
\]

The two factors strongly commute, so Stone's theorem identifies their generator with the self-adjoint closure of

\[
N_{\log}\otimes I+I\otimes B,
\tag{PL381-32}
\]

which is (PL381-9). The only residual freedom compatible with semibounded exact covariance is therefore a multiplicity/internal sector `B` that is independent of the exponent coordinate.

When `W` is one-dimensional, `B` is a scalar and (PL381-9) reduces exactly to the `c+log n` Hamiltonian of `PL-380`. For higher multiplicity, the new result shows that semiboundedness still forces the entire prime dependence to be the canonical `log n` diagonal; all additional spectral structure lives transversely in `W`.

Under the additional trace assumption that `e^{-beta B}` is trace class, the heat trace factorizes for `beta>1` as

\[
\operatorname{Tr}(e^{-\beta A})
=
\left(\sum_{n\ge1}n^{-\beta}\right)
\operatorname{Tr}(e^{-\beta B})
=
\zeta(\beta)\operatorname{Tr}(e^{-\beta B}).
\tag{PL381-33}
\]

This is another negative check: zeta appears as the universal regular-shift partition factor in its ordinary half-plane of convergence, while the residual sector contributes multiplicatively. Nothing in (PL381-33) supplies continuation or the nontrivial zero divisor.

## 4. Generic-weight adversarial control

The proof is not specific to rational primes. Let `J` be any countable index set, let `{lambda_j:j in J}` satisfy

\[
\lambda_j>0,
\qquad
\#\{j:\lambda_j\le L\}<\infty
\quad\text{for every finite }L,
\tag{PL381-34}
\]

and let a doubly commuting isometric family satisfy

\[
e^{itA}V_je^{-itA}=e^{it\lambda_j}V_j
\tag{PL381-35}
\]

for a semibounded self-adjoint `A`. Replacing `log p` by `lambda_j` in Sections 1--3 gives

\[
\mathcal H\simeq
\ell^2(\mathbb N_0^{(J)})\otimes W,
\qquad
A\simeq
N_\lambda\otimes I+I\otimes B,
\tag{PL381-36}
\]

with

\[
N_\lambda e_\alpha
=\Big(\sum_j\alpha_j\lambda_j\Big)e_\alpha.
\tag{PL381-37}
\]

The rational-prime weights satisfy (PL381-34) because `lambda_p=log p` and only finitely many primes lie below any fixed exponential cutoff. But the same mechanism works, for example, for a purely artificial frequency sequence tending to infinity. Therefore the regularization of the infinite Wold problem is a **coercive positive-energy phenomenon**, not a zeta-specific arithmetic rigidity.

This matched control is decisive for interpretation. The condition does answer the live representation-theoretic question after `PL-379`, but it cannot by itself explain why the completed Riemann zeta function should have zeros on `Re(s)=1/2`.

## 5. Prior-art and novelty audit

`PL-379` is the canonical local prior-art boundary: it records an explicit countably generated doubly commuting isometric representation for which all finite-coordinate Wold decompositions exist but no atomic global pure/unitary decomposition exists. The present proof does not contradict that result; it adds a hypothesis absent from the counterexample, namely a **single semibounded generator whose exact covariance assigns a positive locally finite energy cost to every coordinate shift**.

`PL-380` is the other canonical dependency: once the joint wandering space is known to generate, the regular multishift representation and its orbit orthogonality are already established there. The new mathematical step is (PL381-16)--(PL381-28): bounded energy reduces the countable prime family to finitely many active directions, and the spectral lower edge annihilates every adjoint shift in the remaining directions. This upgrades finite Wold data to global wandering generation without assuming the latter.

A targeted external novelty audit was made against finite-tuple Wold theory, product-system/Nica-covariant shift models, positive-energy/gauge-covariant semigroup representations, and the recent infinite-coordinate Wold pathology already underlying `PL-379`. No exact source was found for the implication

\[
\text{countably many doubly commuting isometries}
+
\text{semibounded locally finite positive covariance}
\Longrightarrow
\text{global joint-wandering regularity}
\tag{PL381-38}
\]

in this form. **No theorem-level novelty claim is made.** The finite Wold ingredients and spectral covariance are standard; the durable delta is the exact line-specific boundary: a natural positive-energy repair of `PL-379` works, but it works by collapsing to the baseline regular shift plus an independent internal sector.

The audit also found that older literature contains broad claims of Wold-type decomposition for arbitrary infinite doubly commuting families, while the explicit 2025 counterexample recorded in `PL-379` rules out the strong atomic type decomposition needed here. This finding therefore relies on the direct finite-energy derivation above rather than on any unrestricted infinite-family Wold theorem.

## 6. Boundary conditions and falsification tests

The conclusion is intentionally conditional.

First, semiboundedness is essential to the proof. If `A` has spectrum extending to `-infinity`, the contradiction in (PL381-15) disappears and unitary coordinate sectors can coexist with exact translation covariance.

Second, positivity and local finiteness of the weights are both used. If infinitely many coordinate weights lie below one finite energy threshold, the set analogous to `F_M` need not be finite and the finite-Wold reduction in Section 2 no longer follows.

Third, double commutativity is essential to the finite joint-wandering decomposition. Mere commutativity does not give (PL381-20).

Fourth, exact covariance is stronger than an approximate commutator or a compact/trace-class defect. The theorem says nothing about perturbative covariance of the sort investigated elsewhere in the line.

Fifth, `W` need not be one-dimensional. The internal generator `B` in (PL381-9) can carry arbitrary additional semibounded spectral structure, subject only to the stated tensor separation. Therefore the theorem is not a uniqueness theorem for the whole Hamiltonian unless a cyclic one-dimensional vacuum is imposed.

This finding should be corrected if any of the following fails:

1. the Wold unitary subspace `K_p` need not reduce `U_t` under (PL381-4);
2. semiboundedness does not contradict the unitary spectral shift (PL381-14);
3. the finite pure doubly commuting tuple over `F_M` fails to have the joint wandering decomposition (PL381-20);
4. the sector projections in (PL381-20) fail to commute with the spectral projections of `A`;
5. the spectral shift in (PL381-24) does not force `V_q^*w_alpha=0` when `log q>M-m`;
6. bounded spectral subspaces fail to exhaust a semibounded self-adjoint operator;
7. after global wandering generation, the transported unitary group is not the tensor product in (PL381-31).

Each point is an exact operator-theoretic statement. No numerical evidence or analytic continuation assumption enters the argument.

## Consequence for `prime_lattice`

The live gap after `PL-379` and `PL-380` is now narrower. The diffuse countable-prime Wold freedom is not robust against a physically natural positive-energy condition: exact semibounded `log p` covariance kills it and forces the canonical Fock/Bohr prime shift globally. But that success is itself a negative RH result, because the same proof works for any locally finite positive frequency family and leaves only a transverse internal Hamiltonian.

Accordingly, **semibounded exact prime-shift covariance should not be pursued as the missing arithmetic mechanism**. Any surviving operator route must add data that couples the canonical exponent sector to something genuinely rational-prime-specific and analytically global: for example completed Mellin/Weil information, target-relative Nyman data, an archimedean duality, or another relation that is not reproduced by replacing `log p` with arbitrary locally finite positive weights. The representation-theoretic pathology and its most natural positive-energy repair are both now accounted for.