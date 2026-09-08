# PL-225 — The standard Bost–Connes weak completion is all of `B(ell^2(N))`; canonical infinite-prime products are trivial

## Claim

The weak/von-Neumann completion left open by `PL-223` is not a source of arithmetic spectral rigidity in the canonical positive-energy Bost–Connes representation. On

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
\mu_n\varepsilon_m=\varepsilon_{nm},
\]

let

\[
\mathcal T_{\mathcal P}=C^*(\mu_p:p\text{ prime})\subset B(\mathcal H).
\]

Then

\[
\boxed{\mathcal T_{\mathcal P}''=B(\ell^2(\mathbb N)).}
\]

In fact this already follows from the bare prime shifts, without the cyclotomic diagonal. For finite prime sets `F`, the commuting defect projection

\[
Q_F=\prod_{p\in F}(1-\mu_p\mu_p^*)
\]

converges strongly, as `F` increases through all finite subsets of the primes, to the rank-one vacuum projection

\[
Q_1=|\varepsilon_1\rangle\langle\varepsilon_1|.
\]

Consequently

\[
E_{m,n}:=\mu_mQ_1\mu_n^*
=|\varepsilon_m\rangle\langle\varepsilon_n|
\]

belongs to `T_P''` for every `m,n`, so all matrix units and therefore all of `B(ell^2(N))` lie in the bicommutant.

This gives a sharp negative for a natural infinite-prime escape: **mere membership in the strong/weak closure, or mere affiliation with its von Neumann algebra, imposes no arithmetic restriction at all.** Every bounded operator is in the weak closure, and because `B(H)'=C I`, every densely defined closed self-adjoint operator is affiliated with `B(H)`. Thus a self-adjoint operator with a prescribed spectrum can be inserted at the von-Neumann/affiliated level unless an additional source-forced condition selects it.

At the same time, the most canonical multiplicative infinite-prime products do not produce a hidden global observable. If `r_p in Q/Z` and

\[
C_F=\prod_{p\in F}\rho_p(e(r_p)),
\qquad
\rho_p(e(r))=\mu_pe(r)\mu_p^*,
\]

then `PL-224` gives a single corner supported on multiples of `L_F=prod_(p in F)p`. Hence

\[
\boxed{C_F\to0\quad\text{strongly and weakly as }F\uparrow\mathcal P,}
\]

while every finite `C_F` still has norm one. For every Bost–Connes `KMS_beta` state with `beta>0`,

\[
|\phi_\beta(C_F)|\le L_F^{-\beta}\longrightarrow0.
\]

So the two most direct weak-completion moves have opposite but equally non-rigid outcomes: arbitrary weak approximation gives the whole operator algebra, whereas the canonical all-prime corner product collapses to zero. A nontrivial infinite-prime RH mechanism must therefore specify extra structure — for example a source-forced renormalization, trace/weight, modular relation, adelic quotient, or target-relative condition — that survives matched generic controls and is not implied merely by weak closure or affiliation.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The claim is deliberately representation-specific. It concerns the standard arithmetic/Fock representation on `ell^2(N)` used for the positive-energy Hamiltonian and low-temperature Gibbs states. It does **not** identify the high-temperature `KMS_beta` GNS factors for `0<beta<=1` with `B(ell^2(N))`; `PL-213` records that those canonical GNS factors are type `III_1`.

## 1. The exponent-lattice vacuum is a strong limit of finite-prime defect projections

Put

\[
P_p=\mu_p\mu_p^*.
\]

On the basis vector `epsilon_n`, `P_p` is the divisibility projection

\[
P_p\varepsilon_n
=\begin{cases}
\varepsilon_n,&p\mid n,\\
0,&p\nmid n.
\end{cases}
\]

Therefore, for finite `F`,

\[
Q_F=\prod_{p\in F}(1-P_p)
\]

projects onto the integers whose exponent vector has zero coordinates on every prime in `F`:

\[
Q_F\varepsilon_n
=\mathbf 1_{\gcd(n,\prod_{p\in F}p)=1}\,\varepsilon_n.
\]

Order finite prime sets by inclusion. For `n=1`, every `Q_F` fixes `epsilon_1`. For every `n>1`, choose one prime divisor `p|n`; once `p in F`, `Q_F epsilon_n=0`. Thus the diagonal coefficients converge pointwise to those of the projection onto the exponent-lattice origin. Since `0<=Q_F<=1`, dominated convergence on `ell^2(N)` gives

\[
\boxed{Q_F\xrightarrow{\mathrm{SOT}}Q_1
=|\varepsilon_1\rangle\langle\varepsilon_1|.}
\]

This convergence is genuinely non-norm. For every finite `F`, choose a prime `q notin F`; then `Q_F epsilon_q=epsilon_q` while `Q_1 epsilon_q=0`, so

\[
\|Q_F-Q_1\|=1.
\]

Hence this step crosses exactly the topology that `PL-223` left outside its all-prime norm-closure theorem.

## 2. Prime shifts plus the vacuum generate every matrix unit in the bicommutant

Because `Q_1 in T_P''` and `mu_m,mu_n in T_P` for every positive integer `m,n`,

\[
\mu_mQ_1\mu_n^*\in\mathcal T_{\mathcal P}''.
\]

Acting on the standard basis,

\[
\mu_mQ_1\mu_n^*\varepsilon_k
=\begin{cases}
\varepsilon_m,&k=n,\\
0,&k\ne n.
\end{cases}
\]

Therefore

\[
\boxed{\mu_mQ_1\mu_n^*=E_{m,n}.}
\]

The linear span of these matrix units is the finite-rank algebra, whose strong closure is `B(ell^2(N))`. Since `T_P''` is already a von Neumann algebra,

\[
B(\ell^2(\mathbb N))
\subseteq\mathcal T_{\mathcal P}''
\subseteq B(\ell^2(\mathbb N)),
\]

which proves the claim.

This also proves directly that the standard representation of the prime-shift algebra is irreducible. The corresponding irreducibility of the standard arithmetic Bost–Connes representations is classical; the original Bost–Connes representation and its later Q-lattice formulations use the same `ell^2(N)` shifts. The present argument does not claim a new representation-theoretic theorem: it isolates the consequence relevant to the surviving `prime_lattice` weak-completion route.

## 3. Weak closure and affiliation are maximally programmable

The bicommutant theorem now makes the information loss exact. Every bounded `T in B(ell^2(N))` is a strong/weak operator limit of elements of the represented prime-shift `C*`-algebra. Thus a proposed bounded spectral observable is not source-forced merely because it belongs to the weak closure.

The unbounded escape is equally unconstrained if the only requirement is affiliation. A closed densely defined operator `A` is affiliated with a von Neumann algebra `M` when it commutes, in the standard affiliation sense, with the unitaries in `M'`. For

\[
M=B(\mathcal H),
\qquad
M'=\mathbb C I,
\]

this condition is automatic. In particular, every self-adjoint operator on `ell^2(N)` is affiliated with this weak completion. One may therefore prescribe an arbitrary discrete real spectrum, including any desired sequence of candidate zero ordinates, without using the arithmetic dynamics at all.

This is a stronger matched-control failure than merely saying that a particular candidate operator is artificial. The ambient von Neumann algebra has become so large that **affiliation itself carries zero discriminating content**. Any serious Hilbert–Pólya proposal in this representation must identify an additional canonical construction or relation that distinguishes its operator from the continuum of programmable alternatives.

## 4. The canonical infinite-prime corner product instead vanishes

The opposite extreme is obtained by following the intrinsic multiplicative corner hierarchy of `PL-224` rather than allowing arbitrary weak approximants. For finite `F`, let

\[
C_F=\prod_{p\in F}\rho_p(e(r_p)).
\]

`PL-224` gives

\[
C_F=\rho_{L_F}(e(R_F)),
\qquad
L_F=\prod_{p\in F}p,
\]

for an explicit transported phase `R_F`. Its support projection is `P_(L_F)=mu_(L_F)mu_(L_F)^*`, so

\[
\|C_F\xi\|\le\|P_{L_F}\xi\|.
\]

For each fixed integer `n`, once `F` contains a prime not dividing `n`, `L_F` cannot divide `n` and hence `P_(L_F)epsilon_n=0`. Equivalently, requiring

\[
v_p(n)\ge1
\]

for every prime in an increasing family eventually excludes every finite-support exponent vector. Dominated convergence therefore yields

\[
P_{L_F}\xrightarrow{\mathrm{SOT}}0
\quad\Longrightarrow\quad
\boxed{C_F\xrightarrow{\mathrm{SOT}}0.}
\]

Strong convergence implies weak convergence. Yet `||C_F||=1` at every finite stage, because the corner acts by a phase on infinitely many multiples of `L_F`; again there is no norm convergence.

For a `KMS_beta` state, `PL-224` gives

\[
\phi_\beta(C_F)
=L_F^{-\beta}\phi_\beta(e(R_F)),
\]

and `|phi_beta(e(R_F))|<=1`, hence

\[
|\phi_\beta(C_F)|\le L_F^{-\beta}\to0
\qquad(\beta>0).
\]

No analytic continuation is involved in this limit. It is a real-temperature operator/state statement valid in the domain where the KMS state exists.

## 5. Prior-art and novelty audit

The standard Bost–Connes representation, the isometries `mu_n`, the Hamiltonian `H epsilon_n=(log n)epsilon_n`, and the low-temperature Gibbs realization with partition function `zeta(beta)` are classical Bost–Connes theory; source 5 in `research/prime_lattice/SOURCES.md` remains the primary anchor. Later Q-lattice expositions state explicitly that these `ell^2(N)` arithmetic representations are irreducible. The implication “irreducible representation => bicommutant `B(H)`” is standard operator theory.

The local ingredients are also non-arithmetic in the relevant sense. `PL-223` identifies the finite/all-prime shift algebra as a tensor product of ordinary unilateral Toeplitz systems. In a vacuum tensor representation the same defect-projection mechanism isolates the vacuum and the shifts generate matrix units. Thus the full-bicommutant phenomenon is a matched **generic Toeplitz/Fock control**, not a rational-prime fingerprint.

A targeted audit around Bost–Connes irreducible representations, semigroup crossed products, Nica/Toeplitz representations, and infinite tensor products found no basis for a novelty claim. The durable Mathia delta is the closure of a specific live research escape: moving from the bounded all-prime `C*` norm closure of `PL-223` to the standard weak/von-Neumann or merely affiliated level cannot create arithmetic rigidity, because that completion is already maximal.

The strong-zero statement for canonical all-prime corner products is an elementary consequence of the exact lcm support law in `PL-224`. It is stored here because it closes the other natural interpretation of “take an infinite-prime weak limit”: following the canonical corner net itself gives zero rather than a new global invariant.

## 6. Boundaries and adversarial controls

**Representation dependence matters.** The theorem is about the standard positive-energy/Fock representation on `ell^2(N)`. The canonical high-temperature KMS GNS representations are type `III_1` by `PL-213`; their von Neumann algebras are not being identified with `B(ell^2(N))`.

**Maximal ambient algebra does not forbid distinguished arithmetic operators.** A source-forced operator may still be interesting if it is characterized by an additional equation, covariance, positivity, trace formula, modular relation, arithmetic domain condition, or target-relative universality property. The negative is only that weak membership or affiliation supplies none of that structure.

**The canonical product limit is unrenormalized.** Multiplying `C_F` by divergent scalar factors, taking logarithms/determinants, changing states or weights, or subtracting counterterms can produce different limits. Such a renormalization is precisely extra data and must be justified and matched against generalized-prime/Toeplitz controls; this finding does not classify all of them.

**Weak closure is not analytic continuation.** The equality `T_P''=B(H)` is an operator-topology statement at fixed representation. It does not continue `zeta(s)`, the Euler product, or a KMS state into the critical strip.

**The zeta partition function does not rescue the ambient algebra.** For `beta>1`, `Tr(e^{-beta H})=zeta(beta)` is source-forced because both `H` and the Gibbs trace are specified. The fact that the same representation has weak closure `B(H)` shows why an additional arbitrary affiliated operator cannot inherit that arithmetic meaning merely from sharing the ambient factor.

## Falsification / audit tests

The claim would require correction or narrowing if any of the following failed:

1. `P_p=mu_p mu_p^*` did not project onto the divisibility event `p|n` in the standard representation;
2. `Q_F=prod_(p in F)(1-P_p)` did not converge strongly to the rank-one projection onto `epsilon_1`;
3. `mu_m Q_1 mu_n^*` were not the matrix unit `E_(m,n)`;
4. the von Neumann algebra generated by all matrix units were not `B(ell^2(N))`;
5. affiliation with `B(H)` imposed a nontrivial restriction on self-adjoint operators despite `B(H)'=C I`;
6. the `PL-224` corner support for `C_F` were not the multiples of `L_F=prod_(p in F)p`; or
7. a fixed finite-support exponent vector survived the requirement `v_p>=1` for every prime in an exhausting family.

All seven tests are exact and independent of RH.

## Consequence for the research line

`PL-223` showed that the bounded all-prime semigroup-isometry sector is the norm inductive limit/infinite tensor product of generic Toeplitz factors. The present finding closes its most direct weak-completion loophole in the same standard representation:

\[
\boxed{
C^*(\mu_p:p\in\mathcal P)''=B(\ell^2(\mathbb N)).
}
\]

Going to weak closure therefore destroys rather than creates selectivity. At the same time, the canonical infinite product of positive divisibility/cyclotomic corners collapses strongly to zero. A surviving infinite-prime mechanism must live between these two failures: it needs a mathematically forced global operation whose limit is nontrivial but whose admissible outputs remain much smaller than arbitrary `B(H)`/affiliated data, and it must still distinguish the rational-prime system from the generic Toeplitz controls already established in `PL-223`.