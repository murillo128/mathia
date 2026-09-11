# WP-259 — The permutation-fixed prime Fock sector aligns the thermodynamic boundary with Weil criticality while retaining the ambient Mangoldt selector, but not the Weil pairing

**Status:** `EXACT-DERIVED + PRIME-FREE-FOCK + PERMUTATION-FIXED-SECTOR + BOSONIC-RIEMANN-GAS + CRITICALITY-ALIGNMENT + AMBIENT-SPECTRAL-MULTIPLICITY + EXACT-MANGOLDT-HALF-DENSITY + POSITIVE-CARRIER + SOURCE-QUOTIENT-ESCAPE + PRIMON-GAS-CLASSICALIZATION + MATCHED-CONTROLS + ARCHIMEDEAN-MISSING + ORIENTATION-MISSING + SUBSTANTIVE-INTERMEDIATE + NOT-A-WEIL-BRIDGE`.

`WP-256` derives the exact positive finite-place carrier

\[
P_{\rm simp}HN^{-1}e^{-H/2}
\]

on the full free prime Fock space. `WP-257` then finds a genuine mismatch: the free-word Gibbs normalization threshold is the unique `beta_*>1` satisfying `P(beta_*)=1`, whereas the exact Weil half-density requires the one-particle boundary `beta=1`. `WP-258` shows that the canonical full-Fock gauge determinant produces a Gamma shape only at that same free-word boundary `beta_*`, not at `beta=1`.

There is, however, a canonical source-derived sector that removes the `WP-257` thermodynamic mismatch without destroying the `WP-256` prime-power selector: the permutation-fixed, equivalently symmetric/bosonic, sector of the **same ambient full Fock space**.

Let `S_m` permute tensor positions in `K^{\otimes m}` and let

\[
P_{\rm sym}
=1_{\mathbb C\Omega}\oplus\bigoplus_{m\ge1}
\frac1{m!}\sum_{\sigma\in S_m}U_\sigma
\]

be the orthogonal projection onto the fixed vectors. Because the arithmetic Hamiltonian `H` and word number `N` are sums of identical one-particle observables, they commute with every `U_sigma`. The fixed sector therefore reduces both operators.

Its canonical basis has one vector for each prime-exponent vector `alpha=(alpha_p)` of finite support, hence by unique factorization one vector for each integer

\[
n=\prod_p p^{\alpha_p}.
\]

Consequently

\[
\operatorname{Tr}_{P_{\rm sym}\mathcal F}(e^{-\beta H})
=\sum_{n\ge1}n^{-\beta}
=\zeta(\beta),
\]

so the normal bosonic Gibbs region is exactly `beta>1` and its sharp boundary is **`beta=1`**. The shifted free-Fock packing threshold `beta_*` disappears after canonical permutation radialization.

Crucially, the ambient multiplicity projection `P_simp` from `WP-256` commutes with `P_sym`. On an energy shell `log n`, `P_simp` is nonzero exactly when the **ambient ordered-word shell** has multiplicity one, which occurs exactly for `n=p^k`. Thus the symmetric-sector compression

\[
\boxed{
T_{\rm sym}
:=P_{\rm sym}P_{\rm simp}HN^{-1}e^{-H/2}P_{\rm sym}
\succeq0
}
\]

satisfies, on the one-per-integer symmetric basis,

\[
\boxed{
T_{\rm sym}e_n^{\rm sym}
=\frac{\Lambda(n)}{\sqrt n}e_n^{\rm sym}.
}
\]

This is a real improvement over the raw full-Fock thermodynamic picture. In one canonical two-level geometry, the noncommutative free cover supplies the prime-power selector, while its permutation-fixed commutative sector supplies a Gibbs boundary at exactly the Weil parameter.

But the construction still does **not** yield Weil positivity. The positive operator remains a diagonal coefficient carrier. Its passage to the Weil translation/autocorrelation geometry has the same orientation obstruction as `WP-005`, `WP-216`, and `WP-256`. The bosonic fixed sector also does not intrinsically supply the Gamma or polar terms: its Gibbs-weighted gauge trace is already divergent in length one at `beta=1`. Thus the result repairs one canonicity mismatch from `WP-257` but does not repair the global sign problem or the archimedean completion.

## 1. The canonical permutation-fixed sector of the free prime Fock space

Retain the one-particle prime Hilbert space and full Fock space of `WP-256`,

\[
\mathcal K=\ell^2(\mathbb P),
\qquad
\mathcal F
=\mathbb C\Omega\oplus\bigoplus_{m\ge1}\mathcal K^{\otimes m},
\]

with

\[
H e_{(p_1,\ldots,p_m)}
=\left(\sum_{j=1}^m\log p_j\right)e_{(p_1,\ldots,p_m)},
\qquad
N e_{(p_1,\ldots,p_m)}=m e_{(p_1,\ldots,p_m)}.
\tag{1}
\]

For each `m`, the symmetric group acts unitarily by tensor-position permutations,

\[
U_\sigma
(e_{p_1}\otimes\cdots\otimes e_{p_m})
=
 e_{p_{\sigma^{-1}(1)}}\otimes\cdots\otimes e_{p_{\sigma^{-1}(m)}}.
\tag{2}
\]

The orthogonal fixed-point projection is

\[
P_{{\rm sym},m}
=\frac1{m!}\sum_{\sigma\in S_m}U_\sigma,
\qquad
P_{\rm sym}=1_{\mathbb C\Omega}\oplus\bigoplus_{m\ge1}P_{{\rm sym},m}.
\tag{3}
\]

Both `H` and `N` commute with the permutation action because they depend only on the multiset of letters and on total length:

\[
[H,P_{\rm sym}]=[N,P_{\rm sym}]=0.
\tag{4}
\]

Therefore

\[
\mathcal F_{\rm sym}:=P_{\rm sym}\mathcal F
\tag{5}
\]

is a canonical reducing sector. Abstractly it is the bosonic symmetric Fock space `Gamma_s(K)`, but here it is important to retain its realization **inside the ordered free cover**, because the ambient shell multiplicities will still be used below.

Fix a finitely supported occupation vector

\[
\alpha=(\alpha_p)_{p\in\mathbb P},
\qquad
|\alpha|:=\sum_p\alpha_p=m.
\tag{6}
\]

Let

\[
n(\alpha):=\prod_p p^{\alpha_p}.
\tag{7}
\]

The normalized symmetric vector is the normalized sum over all distinct words with this multiset. Distinct occupation vectors give orthogonal vectors. Unique factorization gives a bijection

\[
\{\alpha:\alpha_p\in\mathbb N_0,\ |\operatorname{supp}\alpha|<\infty\}
\longleftrightarrow
\mathbb N,
\qquad
\alpha\mapsto n(\alpha).
\tag{8}
\]

Write the resulting orthonormal basis as `e_n^sym`, including `e_1^sym=Omega`. Then

\[
H e_n^{\rm sym}=(\log n)e_n^{\rm sym},
\qquad
N e_n^{\rm sym}=\Omega(n)e_n^{\rm sym}.
\tag{9}
\]

Thus the permutation-fixed sector is precisely the commutative multiplicative shadow of the ordered prime-word cover.

## 2. Symmetrization moves the full thermodynamic boundary from `beta_*` to exactly `1`

On the full free Fock space, `WP-257` obtains

\[
\operatorname{Tr}_{\mathcal F}(e^{-\beta H})
=\sum_{m\ge0}P(\beta)^m
\tag{10}
\]

when this converges, so ordinary Gibbs normalization requires `P(beta)<1` and begins only for `beta>beta_*>1`.

On the fixed sector, equation (8) instead gives

\[
\begin{aligned}
Z_{\rm sym}(\beta)
&:=\operatorname{Tr}_{\mathcal F_{\rm sym}}(e^{-\beta H})\\
&=\sum_{n\ge1}n^{-\beta}\\
&=\prod_p(1-p^{-\beta})^{-1}\\
&=\zeta(\beta)
\end{aligned}
\tag{11}
\]

for `beta>1`.

Hence

\[
\boxed{
Z_{\rm sym}(\beta)<\infty
\quad\Longleftrightarrow\quad
\beta>1.
}
\tag{12}
\]

The normal Gibbs state on this sector exists for every `beta>1`; at `beta=1` its total mass diverges, but the usual diagonal Gibbs expression still defines a semifinite weight on finite-rank operators. The sharp thermodynamic boundary is therefore

\[
\boxed{\beta_c^{\rm sym}=1.}
\tag{13}
\]

This is exactly the parameter required by the finite Weil half-density.

The mechanism is transparent. Full free Fock counts every ordering of a prime multiset and therefore weights integer `n` by the multinomial multiplicity

\[
M(n)=\frac{\Omega(n)!}{\prod_p v_p(n)!}.
\tag{14}
\]

The fixed sector replaces each entire permutation orbit by one normalized invariant vector. It therefore changes

\[
\sum_n M(n)n^{-\beta}
\quad\text{into}\quad
\sum_n n^{-\beta}.
\tag{15}
\]

The same word-order multiplicities that moved the free-Fock normalization boundary to `beta_*` are exactly what canonical symmetrization removes.

## 3. The ambient simple-spectrum selector survives the fixed-sector compression

If one discarded the free cover and kept only `F_sym`, then equation (9) would make every arithmetic energy eigenspace one-dimensional. The symmetric Hamiltonian by itself therefore cannot distinguish prime powers from mixed composites by spectral multiplicity.

But the construction here does not discard the cover: `F_sym` is a canonical reducing subspace **inside** `F`. The ambient projection from `WP-256`,

\[
P_{\rm simp}
=\sum_{\substack{\lambda>0\\
\operatorname{rank}1_{\{\lambda\}}(H)=1}}
1_{\{\lambda\}}(H),
\tag{16}
\]

is defined before symmetrization. It is a sum of complete energy-shell projections and therefore commutes with all tensor permutations:

\[
[P_{\rm simp},P_{\rm sym}]=0.
\tag{17}
\]

By the multinomial argument of `WP-256`,

\[
P_{\rm simp}1_{\{\log n\}}(H)\ne0
\quad\Longleftrightarrow\quad
n=p^k.
\tag{18}
\]

Because the unique `p^k` word is already permutation-fixed,

\[
P_{\rm sym}P_{\rm simp}=P_{\rm simp}P_{\rm sym}
\tag{19}
\]

has, inside the symmetric sector, exactly the span of

\[
\{e_{p^k}^{\rm sym}:p\in\mathbb P,\ k\ge1\}.
\tag{20}
\]

Thus symmetrization collapses the thermodynamic multiplicities without erasing the **ambient record** of which energy shells were simple before the quotient.

This two-level feature is the substantive point. The bosonic Riemann gas alone is classical and has simple spectrum at every integer. The free cover alone has the useful multiplicity selector but the shifted normalization threshold. Keeping the cover together with its canonical fixed sector retains both pieces of information.

## 4. Exact positive Mangoldt half-density at the now-aligned boundary

On a prime-power symmetric vector `e_{p^k}^sym`, equations (9) and (20) give

\[
HN^{-1}e_{p^k}^{\rm sym}
=\frac{k\log p}{k}e_{p^k}^{\rm sym}
=(\log p)e_{p^k}^{\rm sym}.
\tag{21}
\]

At the fixed-sector boundary `beta=1`,

\[
e^{-H/2}e_n^{\rm sym}=n^{-1/2}e_n^{\rm sym}.
\tag{22}
\]

Define, with `N^{-1}Omega=0`,

\[
T_{\rm sym}
:=P_{\rm sym}P_{\rm simp}HN^{-1}e^{-H/2}P_{\rm sym}.
\tag{23}
\]

All factors strongly commute on the common diagonal basis, and every nonzero scalar factor is nonnegative. Hence

\[
T_{\rm sym}\succeq0.
\tag{24}
\]

For `n=p^k`, equations (21)--(22) give

\[
T_{\rm sym}e_n^{\rm sym}
=(\log p)p^{-k/2}e_n^{\rm sym}.
\tag{25}
\]

For every `n` with at least two distinct prime factors, the ambient `P_simp` kills its full energy shell. Therefore

\[
\boxed{
T_{\rm sym}e_n^{\rm sym}
=\frac{\Lambda(n)}{\sqrt n}e_n^{\rm sym}
\qquad(n\ge1),
}
\tag{26}
\]

with the vacuum/`n=1` value zero.

The nonzero spectrum is exactly the same prime-power list as in `WP-256`, but the thermodynamic provenance has improved:

\[
\boxed{
\text{fixed-sector Gibbs boundary }\beta=1
\quad=\quad
\text{finite Weil half-density parameter }\beta=1.
}
\tag{27}
\]

Thus `WP-257` is not a universal obstruction attached to prime Fock geometry. It is a statement about **full free-word thermodynamic normalization**. Canonical permutation radialization supplies an allowed source-derived category change for which the two finite criticalities coincide.

## 5. Why this still does not produce the archimedean completion or the Weil sign

The aligned boundary does not repair the main problem of the research line. Equation (26) is diagonal positivity on the integer-labelled bosonic sector. The finite Weil term instead uses the same positive coefficients as **oriented off-diagonal translation/autocorrelation weights**. The sign obstruction identified in `WP-005`, `WP-216`, and `WP-256` is unchanged by replacing the full trace with the fixed-sector trace.

Nor does the fixed-sector gauge immediately repair `WP-258`. For `beta>1`, the joint arithmetic/gauge generating trace is

\[
\operatorname{Tr}_{\mathcal F_{\rm sym}}
\left(e^{-\beta H}y^N\right)
=
\prod_p(1-y p^{-\beta})^{-1}.
\tag{28}
\]

At `y=1` this is `zeta(beta)`. At the critical value `beta=1`, already the length-one contribution is

\[
\sum_p\frac1p=+\infty.
\tag{29}
\]

More generally, a shifted gauge spectral trace would have the form

\[
\sum_{n\ge1}n^{-\beta}(\Omega(n)+z)^{-u},
\tag{30}
\]

when convergent. At `beta=1` the prime subseries diverges for every fixed `u` because `Omega(p)=1`. Hence there is no ordinary Gibbs-weighted gauge zeta at the aligned boundary whose length multiplicities flatten to the Hurwitz zeta. The `WP-258` Gamma mechanism has not been recovered; its full-free-Fock `beta_*` argument has instead been bypassed by changing sector, after which a different archimedean problem remains.

The fixed-sector partition function itself being `zeta(beta)` also does not solve the mandate. Multiplying that familiar scalar function by a Gamma factor or invoking its functional equation would merely return the completed zeta representation explicitly excluded by the research contract. A new result would require a geometric real-place object and an independent sign theorem.

The polar factor is likewise absent. Thus the construction currently supplies

\[
\text{canonical finite criticality}
+\text{canonical finite coefficient carrier},
\]

but not

\[
\text{Gamma/polar completion}
+\text{Weil orientation}
+\text{independent global positivity}.
\]

## 6. Aggressive controls

### Symmetric sector without the ambient cover

If the ambient full Fock space is forgotten, every eigenvalue `log n` of the symmetric Hamiltonian has multiplicity one. Therefore a selector defined from **intrinsic symmetric spectral multiplicity** is the identity on every non-vacuum integer state, not the prime-power projection.

This is the sharp dependence of the positive result: the useful object is not merely the classical bosonic Riemann gas. It is the pair

\[
(\text{ordered free cover},\ \text{permutation-fixed sector}).
\tag{31}
\]

The free cover stores factorization-order multiplicity; the fixed sector supplies commutative thermodynamics.

### Occupied-mode count

Inside bosonic Fock one can define number operators `N_p` and the support-count observable

\[
R=\sum_p1_{(0,\infty)}(N_p),
\tag{32}
\]

which counts distinct occupied prime modes. Its `R=1` sector is again the prime-power sector. This shows that the information is not inaccessible after symmetrization.

But `R=1` is an additional sector choice. No Gibbs normalization theorem or bosonic dynamics derived above selects the eigenvalue one. It is therefore a weaker source-selection explanation than the ambient `P_simp`, whose support is characterized by simplicity of the pre-quotient energy shell. Equation (32) is a matched alternative, not an independent proof that the target support is forced by bosonic thermodynamics.

### Fermionic statistics

The exterior/fermionic prime Fock space has partition function

\[
\prod_p(1+p^{-\beta})
=\frac{\zeta(\beta)}{\zeta(2\beta)}
\tag{33}
\]

for `beta>1`, so its thermodynamic boundary is also `1`. But Pauli occupation allows each prime at most once, so states `p^k` for `k>=2` are absent. It cannot carry the full von Mangoldt prime-power tower.

This control shows that moving the boundary to `1` by changing statistics is not sufficient. The symmetric sector is special here because it keeps arbitrary prime occupation while collapsing only permutation order.

### Generalized-prime alphabet

Let a countable alphabet have multiplicatively independent generators `q_j>1` with one-particle energies `log q_j`. The same construction gives a free ordered cover, its permutation-fixed commutative sector, and

\[
Z_{\rm sym}(\beta)
=\prod_j(1-q_j^{-\beta})^{-1}.
\tag{34}
\]

Ambient simple shells are again exactly the powers of one generator, and `H/N` gives that generator's logarithmic energy. Thus the free-cover/fixed-sector compatibility mechanism is **universal for free commutative monoids**. Rational primes make the boundary equal to `1` through their actual Euler product, but nothing in this construction supplies a Riemann-specific positivity law.

This matched control is decisive against overreading equation (27) as evidence for RH.

## 7. Prior art and novelty boundary

The bosonic part of the construction is classical. Bernard Julia's Riemann/primon gas interprets the Riemann zeta function as the partition function of bosonic modes with one-particle energies `log p`; see B. Julia, *Statistical Theory of Numbers*, in *Number Theory and Physics*, Springer Proceedings in Physics 47 (1990), 276--293, and B. Julia, *Thermodynamic limit in number theory: Riemann--Beurling gases*, Physica A 203 (1994), 425--436. A modern explicit formulation is J. G. Dueñas and N. F. Svaiter, *Thermodynamics of the Bosonic Randomized Riemann Gas*, arXiv:1401.8190, whose Hamiltonian is `sum_p log(p) b_p^* b_p` and whose bosonic partition function is `zeta(beta)`.

The symmetric Fock functor, the averaging projection onto tensor-permutation invariants, the Euler product, and the fermionic identity (33) are also standard. No novelty is claimed for any of them, for second quantization, or for the fact that `zeta(beta)` has abscissa/pole boundary at `1`.

The Mathia-specific durable content is the exact compatibility statement with the **ambient** construction already established in `WP-256`--`WP-258`:

\[
\boxed{
\begin{array}{c}
\text{free ordered cover}\ \Rightarrow\ \text{spectral multiplicity selects prime powers},\\[2mm]
\text{canonical permutation-fixed sector}\ \Rightarrow\ Z(\beta)=\zeta(\beta),\ \beta_c=1,\\[2mm]
\text{ambient selector restricted to that sector}\ \Rightarrow\
\Lambda(n)/\sqrt n\ \text{at the same }\beta=1.
\end{array}
}
\tag{35}
\]

A bounded prior-art search found the classical bosonic Riemann-gas dictionary but no source asserting this particular two-level use of free-word shell multiplicity together with the permutation-fixed thermodynamic sector as a Mangoldt half-density selector. The claim here is therefore deliberately limited to the exact operator identity and to the correction of the `WP-257` boundary mismatch inside Mathia; it is not a claim of a new zeta model or an independent theorem about RH.

## 8. Consequence for the Weil-positivity mandate

The free-Fock branch now has a more precise frontier than `WP-258` alone suggests. The conflict

\[
\beta=1\quad\text{versus}\quad\beta=\beta_*
\]

is not forced by the prime alphabet itself. It is forced by counting ordered free words in the **full** Gibbs trace. The canonical permutation-fixed sector restores the arithmetic commutative counting law and puts the thermodynamic boundary back at `1`, while the ambient free cover retains the representation-theoretic multiplicity information needed to select prime powers.

So one important finite-place compatibility problem is genuinely repaired:

\[
\boxed{
\text{same source geometry}
\ \supset\ 
\text{free cover + canonical symmetric sector}
\ \Longrightarrow\ 
\beta_c=1
\text{ and }
T_{\rm sym}=\Lambda/\sqrt{\cdot}\succeq0.
}
\tag{36}
\]

What remains is exactly the harder part of the research mandate. The construction must still explain how a diagonal positive coefficient carrier becomes the signed Weil autocorrelation form; it must derive a real-place Gamma contribution and the polar terms without merely reinserting the completed zeta function; and the resulting completed form must obey an independent geometric positivity/coercivity theorem that survives matched generalized-prime controls.

The next viable use of this geometry should therefore not spend effort re-solving the finite critical exponent or the prime-power coefficient list. It should test whether the **free-cover-to-symmetric-sector interface itself** has a canonical boundary response, defect form, relative modular object, or finite--archimedean correspondence whose quadratic form transports the exact coefficients with the required orientation. If that interface supplies only the scalar `zeta` partition function or passive diagonal compression, then it is another representation of known arithmetic data rather than the sought Weil-positivity mechanism.