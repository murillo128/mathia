# PC-468 — Generic admissible cotangent limits are purely singular continuous

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE. In the product topology on prime-admissible integer supports, a dense `G_delta` of the moving-center limits has the entire PC-466 spectrum and is purely singular continuous **on its retained coordinate space**. A distant admissible duplication splits every finite eigenvalue and halves each old coordinate's atomic weight asymptotically; this supplies the density argument missing from mere trace-class perturbation. In contrast, the only translation-invariant probability on this hull is concentrated on the empty support. The category and measure-theoretic machinery is classical. This is a spectral-type and selection boundary, not a canonical center, a zeta-zero identification, an RH implication, or a historical-priority claim.

## 1. Object, topology and theorem

Let
\[
\mathcal A=\{S\subset\mathbb Z:|S\bmod p|<p\text{ for every prime }p\}
\]
carry the product topology inherited from `{0,1}^Z`. A neighborhood fixes exactly which coordinates occur in a finite window. Write
\[
(A_S)_{ab}=\begin{cases}i/[\pi(a-b)],&a,b\in S,\ a\ne b,\\0,&a=b,\end{cases}
\quad\text{on }\ell^2(S),
\qquad L_S=A_S\oplus0\quad\text{on }\ell^2(\mathbb Z).
\tag{1}
\]
The empty support has zero-dimensional retained space. Define
\[
\Sigma=\overline{\bigcup_{F\text{ finite nonempty admissible}}\sigma(A_F)},
\qquad \beta=\sup_F\|A_F\|.
\tag{2}
\]
[[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]] proves boundedness `||A_S||<=beta` and realizes every `L_S` as a strong moving-center limit of the conductor-scaled primorial cotangent matrices. [[research/prime_circle/findings/PC-466-full-primorial-cotangent-spectra-converge-to-the-admissible-pattern-spectrum]] identifies `Sigma` with their full uniform-in-refinement Hausdorff spectral limit. [[research/prime_circle/findings/PC-467-admissible-cotangent-spectrum-is-perfect-and-has-a-purely-singular-realization]] proves that `Sigma` is perfect and constructs one full-spectrum realization with no absolutely continuous part, without resolving its atomic component.

**Theorem.** There is a dense `G_delta` subset `G subset A` consisting of infinite supports for which
\[
\boxed{\quad
\sigma(A_S)=\sigma_{\rm ess}(A_S)=\Sigma,
\qquad \mathcal H_{\rm pp}(A_S)=\mathcal H_{\rm ac}(A_S)=\{0\}.
\quad}
\tag{3}
\]
Thus `A_S` is purely singular continuous on its whole retained space, including at the spectral point zero. Its zero extension `L_S` still has the artificial zero eigenspace `ell^2(Z\S)` and must **not** be called purely singular continuous on `ell^2(Z)`.

Nevertheless, for the translation action `S -> S-c`,
\[
\boxed{\quad \mathcal P_{\rm inv}(\mathcal A)=\{\delta_{\varnothing}\}.\quad}
\tag{4}
\]
In particular `G` has probability zero under every invariant probability. More quantitatively, for every fixed `v in ell^2(Z)`,
\[
\lim_{H\to\infty}\sup_{S\in\mathcal A,\ a\in\mathbb Z}
\frac1H\sum_{c=a}^{a+H-1}\|L_{S-c}v\|^2=0.
\tag{5}
\]
Baire genericity and stationary sampling therefore select different behavior. Neither is a geometry-forced choice of moving centers. Equation (3) does not determine gaps or Lebesgue measure of `Sigma`, nor spectral type for all admissible supports.

## 2. Continuous active spectral measures on a complete hull

The hull `A` is closed: failure of admissibility modulo a prime has finitely many witnesses and is an open condition. It is compact metrizable and hence a Baire space. Finite admissible supports are dense, by truncating any support outside the prescribed window.

The map `S -> L_S` is strongly continuous. If `S_j -> S` pointwise, each fixed column converges on every finite window. For `R>|k|`, its Cauchy tail is bounded uniformly by
\[
\sum_{|h|>R}|(L_S)_{hk}|^2\le\frac2{\pi^2(R-|k|)}.
\tag{6}
\]
This gives column convergence in `ell^2`; the common norm bound `beta` extends it to every vector. Polynomial approximation on a common compact spectral interval then gives strong continuity of `f(L_S)` for continuous `f`.

For `k in Z`, use the **active** measure
\[
\mu_k^S(B)=\mathbf1_S(k)\langle\delta_k,E_{L_S}(B)\delta_k\rangle.
\tag{7}
\]
It is a positive measure of mass `m_k(S)=1_S(k)`, supported in `[-beta,beta]`, and varies weakly continuously with `S`. The mass is a clopen coordinate function. When `k notin S`, (7) is zero, not the padded operator's unit atom at zero. When `k in S`, it is exactly the spectral measure of `delta_k` for `A_S`.

If all these active coordinate measures are atomless and singular with respect to Lebesgue measure, the same is true on the entire retained Hilbert space: the continuous and singular spectral subspaces are closed and contain its coordinate basis. Equivalently, the countable union of their null carriers supports the whole spectral resolution, and an eigenvector would have a nonzero coordinate giving an atom in one of (7).

## 3. Distant duplication halves every coordinate atom

Fix a nonempty finite admissible `F={a_1,...,a_n}` and put `A=A_F`, `e=(1,...,1)^T`. With `X=diag(a_1,...,a_n)`,
\[
[X,A]=\frac i\pi(ee^*-I).
\tag{8}
\]
For any unit eigenvector `v`, its commutator expectation is zero, so
\[
|e^*v|^2=1.
\tag{9}
\]
Every eigenspace is one-dimensional, since a higher-dimensional eigenspace would contain a nonzero vector orthogonal to `e`. These are the classical finite Cauchy facts recorded in PC-467 and in Preissmann–Leveque, Corollary 1 and Lemma 7. They apply to arbitrary distinct real coordinates, including an odd-dimensional zero eigenvalue.

Let `Q=prod_(p<=2n) p` and take arbitrarily large positive multiples `b` of `Q`. Then
\[
F_b=F\sqcup(b+F)
\tag{10}
\]
is admissible once the copies are disjoint. At primes at most `2n` it occupies exactly the same residues as `F`; larger primes cannot be covered by `2n` points. Taking `b` large also keeps the new copy outside any prescribed cylinder window.

In the copy ordering, with `t=1/b`, the actual Cauchy matrix has the finite-dimensional expansion
\[
A_{F_b}=
\begin{pmatrix}A&0\\0&A\end{pmatrix}
+tB+O_F(t^2),
\qquad
B=\frac1\pi\begin{pmatrix}0&-i ee^*\\i ee^*&0\end{pmatrix}.
\tag{11}
\]
The sign follows from `1/(a-c-b)=-1/b+O_F(b^{-2})`. No cross-copy entry is suppressed. For a simple eigenpair `(lambda_j,v_j)` of `A`, the double eigenspace of the first term has basis `(v_j,0),(0,v_j)`. Its compression of `B`, by (9), is exactly
\[
B_j=\frac1\pi\begin{pmatrix}0&-i\\i&0\end{pmatrix}.
\tag{12}
\]
The two eigenvalues and their rank-one eigenprojections consequently obey
\[
\lambda_{j,\pm}(b)=\lambda_j\pm\frac1{\pi b}+O_F(b^{-2}),
\qquad
w_{j,\pm}(b)\longrightarrow\frac1{\sqrt2}(v_j,\ \pm i v_j)
\tag{13}
\]
after phase choices. To justify the degenerate step, first isolate `lambda_j` from the other old eigenvalues by its fixed positive gap. Hermitian norm-perturbation bounds leave exactly two eigenvalues in this cluster. The eigenvector equation on the complementary subspace gives a component `O_F(t)`; substitution into the double eigenspace gives `lambda_j I+t B_j+O_F(t^2)`. The two eigenvalues of `B_j` are distinct, so its normalized eigenvectors and the associated rank-one projections are the limits. This also handles `n=1`, when the complementary subspace is absent. The constants may deteriorate at later duplications; only finitely many duplications are needed for each prescribed accuracy.

For an old coordinate `k in F`, (13) gives
\[
|w_{j,\pm}(b;k)|^2\longrightarrow\tfrac12|v_j(k)|^2.
\tag{14}
\]
If `M_k(F)` denotes the largest atom of its finite spectral measure, then, for any `epsilon>0`, sufficiently distant admissible duplication ensures simultaneously for every old coordinate
\[
M_k(F_b)\le\tfrac12 M_k(F)+\epsilon.
\tag{15}
\]
For fixed `r`, iterate (15) `r` times with errors small enough that `M_k<2^{-r}+epsilon_total` on any originally specified finite collection of coordinates. Each stage uses the actual enlarged Cauchy matrix and chooses a fresh sufficiently large multiple of the corresponding primorial. Thus, inside any nonempty cylinder, finite supports exist whose active measures on any prescribed coordinates have all atoms smaller than any requested positive threshold. Small interaction alone would not imply this: (9) prevents a decoupled old eigenmode, and (12) resolves the resonant double eigenvalue.

## 4. Baire category removes both atoms and absolutely continuous mass

Here the standard measure-space proof is included to track the zero padding and the density hypotheses explicitly.

For positive measures on a fixed compact interval, of total mass at most one, define
\[
C_r(\mu)=\sup_{x\in\mathbb R}\mu([x-r^{-1},x+r^{-1}]),\qquad r\ge1.
\tag{16}
\]
This is upper semicontinuous in the weak topology. Indeed, near-maximizing centers can be restricted to a fixed compact set; after taking a convergent subsequence of centers, the portmanteau inequality for slightly enlarged closed intervals and then continuity from above prove the assertion. Moreover, `C_r(mu)` decreases to the largest atomic mass: if a positive mass survived shrinking intervals, compactness would produce an atom at a limit center. Therefore
\[
\{\mu:\mu\text{ atomless}\}
=\bigcap_{m\ge1}\bigcup_{r\ge1}\{\mu:C_r(\mu)<1/m\}.
\tag{17}
\]
Pull back the open sets in (17) under (7). For each `k,m` their union is dense by (15): make every finite atom smaller than `1/(2m)`, then choose `r` so a closed interval of diameter `2/r` contains at most one of the finitely many spectral atoms. If `k` is absent, its active measure is already zero. Baire's theorem over all `k,m` gives a dense `G_delta` on which all active measures are atomless. This argument does not assume the existence of a continuous-spectrum approximant.

For singularity, let `O` range over finite unions of bounded open intervals with rational endpoints and write `|O|` for Lebesgue measure. For each `k,n`, the set
\[
V_{k,n}=\bigcup_{|O|<2^{-n}}
\{S:\mu_k^S(O)>m_k(S)-2^{-n}\}
\tag{18}
\]
is open: evaluation on an open set is lower semicontinuous, and `m_k` is locally constant. It contains every finite support, since a finite atomic measure can be covered by intervals of arbitrarily small total length. Hence it is dense.

For `S in intersection_n V_(k,n)`, choose the corresponding `O_n`. The sum of their Lebesgue measures is finite, so `limsup O_n` is Lebesgue-null. The sum of `mu_k^S(R\O_n)` is also finite, so this limsup carries all of `mu_k^S`. Conversely, singular finite measures admit such finite interval covers by inner and outer regularity. Thus intersection over all `k,n` is a dense `G_delta` of operators with no active absolutely continuous part.

Intersecting with (17) gives pure singular continuity on the retained space. This is the classical Simon/Lenz–Stollmann category mechanism, with the new required density input supplied by admissible duplication. One cannot apply an atom-free theorem directly to `L_S` on `ell^2(Z)`: its inactive coordinates always supply zero eigenvectors.

## 5. A residual set retains the whole essential spectrum

Fix a finite nonempty admissible `F subset [-r_0,r_0]`, an integer `R>r_0`, and an integer `M>=1`. Require an occurrence
\[
S\cap[t-R,t+R]=t+F\qquad\text{for some integer }t>M.
\tag{19}
\]
This is an open condition, a union of cylinder sets. It is dense. Given a prescribed cylinder with finite occupied set `U`, let `n=|U|+|F|`. At each prime `p<=n`, choose omitted residues `r_p` of `U` and `s_p` of `F`, and solve `t=r_p-s_p mod p`. CRT allows arbitrarily large positive `t`. Then `U union(t+F)` is admissible, agrees with the original cylinder, and satisfies (19) once the new protected window is beyond `U`. Larger primes are handled by cardinality. Empty `U` causes no difficulty.

Intersect these open dense sets over all `F,R,M`. For any resulting `S`, every finite admissible block has arbitrarily distant occurrences with arbitrarily large empty buffers. For a unit eigenvector `v` of `A_F`, place it on one such copy. The residual vanishes on that copy; on the remaining rows, summing squared Cauchy column tails gives
\[
\|(A_S-\lambda)v\|
\le\sqrt{\frac{2|F|}{\pi^2(R-r_0)}}.
\tag{20}
\]
Taking disjoint copies and `R -> infinity` gives a singular Weyl sequence at every eigenvalue of every finite admissible block, including zero from a singleton. Hence `Sigma subset sigma_ess(A_S)`.

Conversely, any spectral value of bounded self-adjoint `A_S` has finite-support unit approximate eigenvectors. If `F` is such a vector's support, compressing its residual gives
\[
\operatorname{dist}(\lambda,\sigma(A_F))
\le\|(A_S-\lambda)v\|.
\tag{21}
\]
Thus `sigma(A_S) subset Sigma`, as in PC-466. Combining (20), (21), and the two category sets in §4 proves (3). This residual set consists of infinite supports because (19) supplies arbitrarily many distinct occurrences even of a singleton. No limiting eigenvector is inferred from the finite eigenvectors, and essential spectrum is obtained without dropping the long-range interactions.

## 6. Every stationary law and every averaged fixed probe sees the empty chart

For any primorial `q`, select one residue omitted by `S` at each prime dividing `q`. The complement of these residues consists of exactly `phi(q)` residue classes modulo `q` and contains `S`. Uniformly over `S,a,H`,
\[
\frac{|S\cap[a,a+H)|}{H}
\le\frac{\varphi(q)}q+\frac{\varphi(q)}H.
\tag{22}
\]
If `nu` is translation-invariant, integrating the left side yields `nu{S:0 in S}`. First let `H -> infinity`, then let `q` run through primorials; the totient density tends to zero. Every coordinate has zero probability of being occupied. Countability of `Z` proves (4). No identification with the orbit closure of the already-limited prime-free set is used.

For a vector `v` of finite support `D`, `L_(S-c)v=0` unless `S` meets `c+D`. Otherwise its squared norm is at most `beta^2 ||v||^2`. A union bound and (22) give
\[
\frac1H\sum_{c=a}^{a+H-1}\|L_{S-c}v\|^2
\le\beta^2\|v\|^2|D|
\left(\frac{\varphi(q)}q+\frac{\varphi(q)}H\right).
\tag{23}
\]
Approximation of any fixed vector by finite-support vectors, using the uniform operator bound, proves (5). This does not give operator-norm convergence: for `S in G`, every translate still has norm `beta` and spectrum `Sigma`. It also does not assert pointwise convergence along all translations; the buffered occurrences provide exceptional subsequences.

## 7. Mathematical delta, controls and prior art

PC-467 leaves the atomic versus singular-continuous decomposition of its trace-class construction open. Equation (3) resolves an independent existence and genericity question, through the resonant splitting (11)–(15), rather than asserting a type for that previously constructed support. It also shows why a generic full spectral set cannot substitute for a source-forced or stationary limiting prescription. Equation (4) is a classical zero-density consequence, included to make that limitation exact.

The duplication calculation works for arbitrary distinct real coordinates. The category proof needs a complete support space with strong-continuous bounded compressions, dense finite supports, and arbitrarily distant admissible duplications. Full spectral recovery additionally needs buffered finite-pattern gluing; stationary collapse uses uniform zero density. Any other support class with these same properties reproduces the conclusion. This does not claim that matching density alone matches `Sigma`, or that the finite sieve has lost every arithmetic invariant.

Closest prior art and its role:

- B. Simon, *Operators with singular continuous spectrum: I. General operators*, **Annals of Mathematics 141** (1995), 131–145, DOI `10.2307/2118629`, [author manuscript](https://math.caltech.edu/papers/bsimon/p234.pdf). Theorems 1.1–1.3 and 2.1 give the classical `G_delta`/Wonderland framework. We prove the needed measure pullbacks directly and do not assume its continuous-spectrum density hypothesis for this family.
- D. Lenz and P. Stollmann, *Generic sets in spaces of measures and generic singular continuous spectrum for Delone Hamiltonians*, **Duke Mathematical Journal 131** (2006), 203–217, DOI `10.1215/S0012-7094-06-13121-6`, [author manuscript](https://arxiv.org/pdf/math-ph/0410021). Theorem 2.2 and Proposition 2.6 identify the classical measure-space mechanism used in §4. Their Delone Hamiltonians are a different operator/support class; admissible zero-density supports are not uniformly relatively dense.
- The Preissmann–Leveque paper in `SOURCES.md`, [Corollary 1 and Lemma 7](https://msp.org/pjm/2013/265-1/pjm-v265-n1-p09-p.pdf), supplies the finite simplicity and eigenvector-sum prior art. The distant-double-copy expansion and admissibility-preserving atom reduction are derived here.
- The Dymek–Kasjan–Kułaga-Przymus–Lemańczyk admissible-hull source in `SOURCES.md`, [§2.8 and Example 2.45](https://arxiv.org/pdf/1509.08010), distinguishes this hull from the prime-free orbit closure. J. Kułaga-Przymus, M. Lemańczyk and B. Weiss, *Hereditary subshifts whose simplex of invariant measures is Poulsen*, [author manuscript, introduction and Theorem 3](https://www-users.mat.umk.pl/~mlem/files/KuLeWe2.pdf), arXiv:1507.00714, records the zero-entropy hereditary-system boundary behind (4). Here the direct uniform residue bound proves precisely what is used, without importing a positive-density or thin-sieve hypothesis.

Local duplication checks covered PC-465–PC-467 and targeted searches for Baire genericity, singular continuity, invariant probabilities and atom splitting. Structural literature checks locate the category and zero-density conclusions in established theory; the claimed local addition is the Cauchy duplication lemma that verifies the missing no-atom density condition for this exact admissible hull. No historical novelty is inferred from an unsuccessful exact-phrase search.

## 8. Validation and limits

The proof is analytic, not Lean-verified or independently adversarially approved. A deterministic standard-library Python audit used system LAPACK `zheev` through `ctypes` on **26** admissible shapes of sizes one through four in `[0,12]`. It checked **52** distant admissible duplications and **312** split eigenvalues. The maximum error in (13), divided by the first-order scale `1/(pi b)`, was below `4.62e-5`; the maximum error in the coordinate halving (14) was below `2.14e-9`. Singletons and odd-dimensional zero modes were included.

Three consecutive admissible duplications of a singleton reduced its original coordinate's largest atomic weight to approximately `0.5`, `0.250000250`, and `0.125000250`. Separately, **6,552** exact interval counts checked (22) for every omitted-residue profile at primorials `6,30`, every starting residue, and seven interval lengths including wraparound and multiple periods. These are finite normalization, modular and perturbation diagnostics, not a numerical proof of the Baire conclusion or singular continuity. Scratch code and output remain under `/tmp`, outside Git.

The decisive analytic gates are: retain the resonant first-order coupling; use finite simple eigenvalues before each duplication; choose every new separation after the preceding finite matrix is fixed; halve weights, not just split spectral locations; establish open small-atom conditions rather than infer continuity from weak limits of atomic measures; remove padding atoms before the category argument; preserve empty buffers for full residuals; and distinguish residual sets from invariant probability laws. All are addressed above.

No compute or formalization executor is enrolled. The substantive argument is the analytic topology/perturbation combination; its finite ingredients are classical, and no distinct bounded formalization-fertility question is asserted. The theorem does not prove an absolutely continuous realization exists, does not classify all realizations, and does not upgrade the particular PC-467 trace-class support to pure singular continuity.
