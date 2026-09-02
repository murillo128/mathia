# AF-073 — Coherent finite approximants exactly characterize compact-transversal fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real Banach space with unit sphere

\[
\mathbb S_V=\{u\in V:\|u\|=1\}.
\]

Let `\mathcal K` be a nonempty family of **closed cones** in `V`, each containing `0`, and let `L\subseteq V` be a closed cone containing `0`. Retain AF-072's compact unit-direction transversals and compact-transversal margin

\[
\tau_{\mathcal K}(L)
=
\sup_{C\in\mathfrak T_c(\mathcal K)} d(C,L),
\tag{1}
\]

with `\tau_{\mathcal K}(L)=0` when no compact unit-direction transversal exists. Here

\[
C\in\mathfrak T_c(\mathcal K)
\iff
C\subseteq\mathbb S_V\text{ is nonempty compact and }C\cap K\ne\varnothing
\quad\forall K\in\mathcal K.
\tag{2}
\]

For nonempty compact sets `A,B\subset V`, write `d_H(A,B)` for Hausdorff distance. For nonempty `F\subseteq\mathbb S_V` and a cone `K`, put

\[
g(F,K)
=
\inf\{\|f-u\|:f\in F,\ u\in K\cap\mathbb S_V\},
\tag{3}
\]

with `g(F,\{0\})=+\infty`, and put

\[
m_L(F)=d(F,L)=\inf_{f\in F}d(f,L).
\tag{4}
\]

A **coherent finite transversal tower at margin `\eta\ge0`** is a pair consisting of a positive summable sequence `(q_n)_{n\ge1}` and nonempty finite sets

\[
F_n\subseteq\mathbb S_V
\]

such that, for every `n`,

\[
\sum_{n=1}^{\infty}q_n<\infty,
\qquad
d_H(F_n,F_{n+1})\le q_n,
\tag{5}
\]

and simultaneously

\[
g(F_n,K)\le q_n
\quad\forall K\in\mathcal K,
\qquad
m_L(F_n)\ge\eta.
\tag{6}
\]

Define the **coherent finite-approximation margin**

\[
\theta_{\mathcal K}(L)
=
\sup\{\eta\ge0:\text{a coherent finite transversal tower at margin }\eta\text{ exists}\},
\tag{7}
\]

with value `0` if there is no tower.

Then:

1. **Coherent finite approximants recover exactly the compact-transversal margin.**
   \[
   \boxed{
   \theta_{\mathcal K}(L)=\tau_{\mathcal K}(L).
   }
   \tag{8}
   \]
   Thus AF-072's compact simultaneous witness can be replaced exactly by finite witnesses at successively finer scales, provided the finite witnesses are themselves coherent across scales.

2. **Compact-target fidelity has a finite multiscale certificate.** By AF-072,
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \theta_{\mathcal K}(L)=0.
   }
   \tag{9}
   \]
   Positive compact-target failure is equivalent to the existence of a uniformly `L`-separated finite tower whose approximation errors are summable and whose successive finite states form one Hausdorff-Cauchy object.

3. **Per-resolution approximation without cross-resolution coherence is insufficient.** There exists a countable family of closed cones in a separable infinite-dimensional Hilbert space, with `L=\{0\}`, such that for every `\varepsilon>0` there is a **singleton** `F\subset\mathbb S_V` satisfying
   \[
   g(F,K)<\varepsilon
   \qquad\forall K\in\mathcal K,
   \tag{10}
   \]
   while no compact unit-direction transversal exists. Hence
   \[
   \tau_{\mathcal K}(\{0\})
   =
   \theta_{\mathcal K}(\{0\})
   =0
   \tag{11}
   \]
   despite arbitrarily accurate finite approximate transversals at every scale and maximal separation `m_{\{0\}}(F)=1`.

4. **The new load-bearing datum is provenance across scale.** Finite approximation at each tolerance certifies only that every resolution admits *some* approximate simultaneous witness. Equation (8) shows that compact fidelity requires more: those witnesses must be realizable as approximations of one Hausdorff-limit object. Summable inter-scale motion is a concrete sufficient-and-complete certificate for that common provenance.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{arbitrarily fine finite observations do not by themselves imply a surviving compact structure;}\\
\text{the observations must remain coherent as resolution changes;}\\
\text{Hausdorff-Cauchy coherence is exactly enough to reconstruct AF-072's compact witness.}
\end{array}}
\tag{12}
\]

## Derivation

### A compact transversal generates a coherent finite tower

Fix

\[
C\in\mathfrak T_c(\mathcal K)
\]

and write

\[
m=d(C,L).
\tag{13}
\]

Because `C` is compact, it is totally bounded. Choose

\[
a_n=2^{-n-2},
\qquad
q_n=2^{-n},
\tag{14}
\]

and for every `n` choose a nonempty finite `a_n`-net

\[
F_n\subseteq C.
\tag{15}
\]

Equivalently,

\[
d_H(F_n,C)\le a_n.
\tag{16}
\]

The triangle inequality for the Hausdorff metric gives

\[
d_H(F_n,F_{n+1})
\le
 d_H(F_n,C)+d_H(C,F_{n+1})
\le
a_n+a_{n+1}
<q_n.
\tag{17}
\]

Since `\sum_nq_n<\infty`, the coherence requirement (5) holds.

Now fix `K\in\mathcal K`. Since `C` is a transversal, choose

\[
u\in C\cap K\cap\mathbb S_V.
\]

The `a_n`-net property supplies some `f\in F_n` with

\[
\|f-u\|\le a_n<q_n,
\]

so

\[
g(F_n,K)<q_n.
\tag{18}
\]

Finally, `F_n\subseteq C` implies

\[
m_L(F_n)
=
\min_{f\in F_n}d(f,L)
\ge d(C,L)
=m.
\tag{19}
\]

Thus every compact transversal of margin `m` produces a coherent finite tower at the same margin. Taking suprema over compact transversals gives

\[
\theta_{\mathcal K}(L)
\ge
\tau_{\mathcal K}(L).
\tag{20}
\]

This direction uses only compactness through finite nets. No convexity or linear averaging is involved.

### A coherent tower converges to one compact transversal

Conversely, suppose `(F_n,q_n)` is a coherent finite transversal tower at margin `\eta`. For `m>n`, repeated use of (5) gives

\[
d_H(F_n,F_m)
\le
\sum_{j=n}^{m-1}q_j.
\tag{21}
\]

Because `\sum_jq_j<\infty`, the right-hand side tends to `0` as `n,m\to\infty`. Hence `(F_n)` is Cauchy in Hausdorff distance.

The sphere `\mathbb S_V` is closed in the Banach space `V`, hence complete. The hyperspace of nonempty compact subsets of a complete metric space is complete under Hausdorff distance. Every `F_n` is a nonempty finite, hence compact, subset of `\mathbb S_V`; therefore there exists a nonempty compact

\[
C\subseteq\mathbb S_V
\]

such that

\[
d_H(F_n,C)\longrightarrow0.
\tag{22}
\]

This is the exact point at which ambient completeness is needed. The summable coherence does not merely give pairwise compatibility: it produces one genuine compact limit inside the original space rather than only in its completion.

### Approximate hits become exact hits in the Hausdorff limit

For any fixed nonempty closed set `A\subset V`, the set-gap functional

\[
F\longmapsto d(F,A)
\]

is 1-Lipschitz with respect to Hausdorff distance on nonempty compact `F`:

\[
|d(F,A)-d(G,A)|\le d_H(F,G).
\tag{23}
\]

Fix a nonzero `K\in\mathcal K`. Because `K` is closed, the unit-direction section

\[
A_K=K\cap\mathbb S_V
\]

is closed and nonempty. Equations (6), (22), and (23) give

\[
d(C,A_K)
\le
 d_H(C,F_n)+d(F_n,A_K)
\le
 d_H(C,F_n)+q_n
\longrightarrow0.
\tag{24}
\]

A compact set and a closed set at distance zero must intersect: choose pairs approaching distance zero, extract a convergent subsequence on the compact side, and use closedness on the other side. Therefore

\[
C\cap A_K\ne\varnothing.
\tag{25}
\]

Since `K` was arbitrary, `C` hits every cone in `\mathcal K`.

The same Lipschitz estimate with the fixed closed cone `L` gives

\[
d(C,L)
=
\lim_{n\to\infty}d(F_n,L)
\ge\eta.
\tag{26}
\]

Thus `C\in\mathfrak T_c(\mathcal K)` and has compact-transversal margin at least `\eta`. Consequently

\[
\tau_{\mathcal K}(L)\ge\eta
\]

for every tower margin `\eta`, hence

\[
\tau_{\mathcal K}(L)
\ge
\theta_{\mathcal K}(L).
\tag{27}
\]

Combining (20) and (27) proves (8). Equation (9) then follows immediately from AF-072's exact criterion `L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)\iff\tau_{\mathcal K}(L)=0`.

### A zero cone is handled without an exception to the theorem

If some `K_0=\{0\}` belongs to `\mathcal K`, then

\[
K_0\cap\mathbb S_V=\varnothing,
\]

so by convention

\[
g(F,K_0)=+\infty
\]

for every nonempty finite `F`. No coherent finite transversal tower exists and `\theta_{\mathcal K}(L)=0`.

AF-072 likewise gives no compact unit-direction transversal and `\tau_{\mathcal K}(L)=0`; moreover compact-target consequence is automatic because the zero-cone test already forces each surviving point to belong to the target itself. Thus (8) remains exact in this degeneracy.

## Exact control: arbitrary finite accuracy can jump forever

The coherence condition cannot be removed and replaced by the weaker statement

\[
\forall\varepsilon>0\ \exists\text{ finite }F_\varepsilon\subset\mathbb S_V:
\sup_{K\in\mathcal K}g(F_\varepsilon,K)<\varepsilon.
\tag{28}
\]

A concrete Hilbert-space control separates the two notions maximally.

Let `H` be a separable infinite-dimensional real Hilbert space containing an orthonormal family

\[
\{e_n:n\ge1\}
\cup
\{f_{n,i}:n,i\ge1\}.
\tag{29}
\]

Set

\[
a_n=2^{-n-4}
\]

and define, for every `n,i`,

\[
u_{n,i}
=
\sqrt{1-a_n^2}\,e_n+a_n f_{n,i}.
\tag{30}
\]

These are unit vectors. For each fixed `i`, define the cone

\[
K_i
=
\{0\}
\cup
\bigcup_{n\ge1}\mathbb R_{>0}u_{n,i}.
\tag{31}
\]

Each `K_i` is closed. Indeed, for fixed `i` the unit directions `(u_{n,i})_n` are orthonormal, hence pairwise distance `\sqrt2`. A convergent sequence of nonzero points drawn from infinitely many distinct rays can therefore converge only if its norms tend to zero, in which case the limit is `0`; otherwise a convergent subsequence must eventually lie on one closed ray.

For every `n`, take the singleton

\[
F_n=\{e_n\}.
\tag{32}
\]

For every `i`, the cone `K_i` contains `u_{n,i}`, so

\[
g(F_n,K_i)
\le
\|e_n-u_{n,i}\|
=
\sqrt{2-2\sqrt{1-a_n^2}}
\le
\sqrt2\,a_n.
\tag{33}
\]

The final inequality follows from `\sqrt{1-a_n^2}\ge1-a_n^2`. Hence

\[
\sup_i g(F_n,K_i)
\longrightarrow0.
\tag{34}
\]

Given any `\varepsilon>0`, some singleton `F_n` is therefore an `\varepsilon`-approximate transversal for **every cone simultaneously**. At the same time

\[
m_{\{0\}}(F_n)=1
\tag{35}
\]

for every `n`, so no separation margin is being sacrificed.

Nevertheless there is no compact exact unit-direction transversal. Suppose a compact `C\subseteq\mathbb S_H` met every `K_i`. For each `i`, select

\[
u_{n_i,i}\in C\cap K_i.
\tag{36}
\]

There are two possibilities.

If some fixed `n` occurs for infinitely many indices `i`, then for distinct such `i,j`,

\[
\|u_{n,i}-u_{n,j}\|
=
\sqrt2\,a_n>0,
\tag{37}
\]

because the `f_{n,i}` components are orthogonal. Thus `C` contains an infinite uniformly separated subset, impossible for a compact metric space.

Otherwise every `n` occurs only finitely many times. Then an infinite subsequence of the chosen points has pairwise distinct `n_i`. Distinct `n` use mutually orthogonal `e_n` and `f_{n,i}` coordinates, so the corresponding unit vectors are orthogonal and

\[
\|u_{n_i,i}-u_{n_j,j}\|=\sqrt2
\qquad(i\ne j)
\tag{38}
\]

along that subsequence. Again compactness is impossible.

Therefore

\[
\mathfrak T_c(\{K_i:i\ge1\})=\varnothing.
\tag{39}
\]

AF-072 gives

\[
\tau_{\mathcal K}(\{0\})=0,
\]

and (8) gives `\theta_{\mathcal K}(\{0\})=0`. Yet (34) supplies uniformly valid finite approximate transversals at every tolerance.

The defect is entirely **cross-scale**: the one-point approximant must move from `e_n` toward a new orthogonal direction as accuracy increases. Its successive states do not approximate one common compact object. In fact the sequence `(F_n)` has

\[
d_H(F_n,F_m)=\sqrt2
\qquad(n\ne m),
\tag{40}
\]

so it is as far as possible from the coherent-tower regime.

This control is strictly stronger than merely observing the absence of finite-dimensional compactness. Each individual resolution has an extremely small finite certificate; what fails is the ability to identify those certificates as views of the **same surviving structure**.

## Prior art and novelty assessment

All topological mechanisms used in the equivalence are classical.

- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer/Springer (1993), DOI `10.1007/978-94-015-8149-3`. Chapters on the Hausdorff metric topology and gap/excess functionals provide the standard hyperspace language used in (21)–(26). The book explicitly treats set convergence and distance functionals as one framework.
- Dmitri Burago, Yuri Burago, and Sergei Ivanov, ***A Course in Metric Geometry***, Graduate Studies in Mathematics 33, American Mathematical Society (2001), ISBN `978-0-8218-2129-9`. Role: standard metric-geometry background for Hausdorff distance on compact subsets and compact/complete metric constructions.
- The classical compactness theorem for metric spaces says that compactness is equivalent to completeness plus total boundedness, while total boundedness is equivalent to the existence of a finite `\varepsilon`-net for every `\varepsilon>0`. This is exactly the ingredient used to approximate a compact transversal by finite sets. The Encyclopedia of Mathematics entries **“Metric space”** and **“Totally-bounded space”** give concise authoritative statements of these equivalences.

A targeted prior-art search across Hausdorff hyperspaces, finite `\varepsilon`-nets, approximate transversals/hitting sets, compact transversals, and set-valued convergence did not locate the exact equality (8) for cone-family fidelity. Search absence is not evidence of novelty, and no novelty is claimed for Hausdorff completeness, finite-net approximation, gap continuity, compactness, or transversal/hitting-set language.

The line-specific contribution is the **organization and exact boundary**: AF-072's simultaneous compact witness admits a finite multiscale presentation if and only if the finite approximants carry enough inter-scale coherence to converge to one compact object. The Hilbert control shows that arbitrarily fine finite approximability alone is strictly weaker, even when every approximation is a singleton and keeps maximal distance from the candidate consequence.

This is therefore classified as a structural Arithmetic Fidelity theorem built from classical metric/hyperspace mechanisms, not as a claim to a new compactness theorem.

## Boundary conditions and audit

- **Completeness is load-bearing.** The reverse implication uses completeness of the hyperspace of nonempty compact subsets. In an incomplete normed space, a Hausdorff-Cauchy tower can converge only in the completion and need not define a compact transversal inside the original space. The theorem is therefore stated for Banach spaces.
- **Closedness of the tested cones is load-bearing for approximate recovery.** AF-072's exact transversal criterion itself does not require the `K` to be closed, but the passage `d(C,K\cap\mathbb S_V)=0 -> C\cap K\ne\varnothing` does. Without closedness, a tower can converge to boundary directions omitted from `K`.
- **Summability is a certificate, not a uniquely canonical axiom.** What the reverse proof actually needs is that `(F_n)` be Cauchy in Hausdorff distance and that the hitting errors tend to zero. Summable one-step bounds provide a simple local condition guaranteeing both. An equivalent formulation could state the Hausdorff-Cauchy condition directly.
- **Finite approximants are not required to be nested.** Nestedness is stronger than needed and would encode an arbitrary presentation choice. Hausdorff coherence allows points to move while bounding the total unresolved motion.
- **The margin condition is intentionally uniform.** Allowing `m_L(F_n)` to drift to zero would certify only collapse toward `L`, not a surviving positive discriminator. Equation (26) shows that a fixed positive margin is precisely what passes to the compact limit.
- **The Hilbert control is not a cardinality artifact.** The family of cones is countable, and every finite-scale approximate transversal is one point. The obstruction is lack of precompact cross-scale provenance, not an enormous constraint family or high finite complexity.
- **The theorem is category-specific.** Norm-Hausdorff coherence is the right notion for AF-072's norm-compact target category. Weak compactness, Fell/Wijsman convergence, operator topologies, probability laws, or spectral convergence require their own compactness/recovery theorem rather than importing (8) by analogy.
- **No arithmetic specialization is used.** A future prime/RH application must identify what its finite resolutions are, what topology makes them views of the same retained object, and why that topology is intrinsic to the downstream analytic or spectral category.

## Consequences for Arithmetic Fidelity

AF-071 showed that pointwise directional margins can remain large while required witness directions escape every compact set. AF-072 replaced that two-mechanism description by one exact object: a compact simultaneous transversal. AF-073 now gives that object an exact **finite-resolution semantics**.

This matters because many proposed compressions are only accessible through finite truncations, bounded test families, finite spectral windows, finite moments, or finite numerical representations. The existence of increasingly accurate finite witnesses does not imply that an invariant survives the limiting compression. The missing proof obligation is a coherence theorem showing that the finite witnesses are compatible enough to define one object in the destination category.

In practical terms, an Arithmetic Fidelity audit can now separate three statements that must not be conflated:

1. every individual retained constraint has a strong discriminator;
2. every finite resolution admits an approximate simultaneous discriminator;
3. the discriminators across resolutions have a common compact limit.

AF-071 already separated item 1 from global fidelity. The Hilbert control above separates item 2 from item 3. Equation (8) identifies item 3 with AF-072's exact compact-transversal obstruction.

For later arithmetic, spectral, or positivity transfers, this creates a concrete proof obligation: a finite-level discriminator is relevant to an infinite/global RH mechanism only after one proves an intrinsic **cross-resolution provenance law** strong enough to prevent the witnesses from continually changing identity as the compression is refined.