# WP-004 — Prime-Lattice axis compression realizes the finite Weil weight but does not force the global completion

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`. The exact Riemann specialization below gives a canonical positive Prime-Lattice operator whose spectral weights are precisely `Lambda(n)/sqrt(n)` on prime powers. This is a genuine finite-place match, but not a Weil-positivity proof: a Beurling-prime matched control has the same axis mechanism and the same `1/2` Hilbert-space boundary while its zeta function has zeros far to the right of `1/2`. Thus the positive axis mechanism is **finite-place Euler geometry**, not the missing global/archimedean positivity.

## Claim

On the Prime-Lattice Hardy Hilbert space with basis `e_n` indexed by exponent vectors,

\[
n=\prod_p p^{v_p(n)},
\]

let

\[
A e_n=(\log n)e_n,
\qquad
N e_n=\Omega(n)e_n,
\qquad
R e_n=\omega(n)e_n,
\]

where `Omega` counts prime factors with multiplicity and `omega` counts distinct prime factors. Let

\[
Q=\mathbf 1_{\{1\}}(R)
\]

be the orthogonal projection onto the union of the prime coordinate axes, i.e. onto the span of `e_{p^k}` with `k>=1`. Define `N^{-1}` to vanish on the vacuum `e_1` and to act by `1/Omega(n)` otherwise.

Then the commuting diagonal operator

\[
B:=QAN^{-1}Q
\]

is exactly multiplication by the von Mangoldt function:

\[
\boxed{B e_n=\Lambda(n)e_n.}
\tag{1}
\]

Consequently

\[
T:=e^{-A/2}B
\]

is a positive compact operator satisfying

\[
\boxed{T e_n=\frac{\Lambda(n)}{\sqrt n}e_n.}
\tag{2}
\]

For every compactly supported test function `phi` on `[0,infinity)`, `T phi(A)` is finite rank and

\[
\boxed{
\operatorname{Tr}(T\phi(A))
=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\phi(\log n)
=
\sum_p\sum_{k\ge1}(\log p)p^{-k/2}\phi(k\log p).
}
\tag{3}
\]

Thus Prime Lattice contains an **intrinsic positive operator that exactly generates the positive-half finite-prime coefficient measure of the Riemann explicit formula**, without inserting zeta zeros.

The crucial negative is that this does **not** explain global Weil positivity. The same factorization holds verbatim for Beurling generalized prime systems. In particular, systems are known whose generalized-integer counting function is `kappa x + O(x^theta)` with `1/2<theta<1` — hence the same `1/2` `H^2`/Hilbert-Schmidt boundary — while the associated Beurling zeta function has infinitely many zeros on a curve

\[
\sigma=1-\frac{a}{\log t},
\]

well to the right of `1/2`. Therefore

\[
\boxed{
\text{prime-axis positivity + exact Mangoldt weights + the }1/2\text{ Hilbert boundary}
\not\Rightarrow
\text{global Weil positivity or RH}.
}
\tag{4}
\]

A successful Prime-Lattice route must add a structure that **entangles** the finite operator (2) with an independently forced archimedean/pole completion and distinguishes the ordinary rational-prime system from generalized-prime controls.

---

## 1. Exact axis factorization of `Lambda`

The Prime-Lattice generator from PL-007 is

\[
A=\sum_p(\log p)N_p,
\]

so on an axis state `n=p^k`,

\[
A e_{p^k}=k\log p\,e_{p^k}.
\]

On the same state,

\[
N^{-1}e_{p^k}=\frac1k e_{p^k},
\qquad
Qe_{p^k}=e_{p^k}.
\]

Therefore

\[
QAN^{-1}Qe_{p^k}=\log p\,e_{p^k}.
\]

If `n` has either zero or at least two distinct prime factors, `Qe_n=0`. Hence

\[
QAN^{-1}Qe_n
=
\begin{cases}
\log p\,e_n,&n=p^k,\ k\ge1,\\
0,&\text{otherwise},
\end{cases}
\]

which is exactly (1).

This uses only structures already intrinsic to the exponent lattice:

```text
A   logarithmic prime-flow energy,
N   total occupation number,
R   number of occupied prime coordinates,
Q   projection onto rank-one support / coordinate axes.
```

No zero data, analytic continuation, or hand-picked prime-power list is required once the exponent coordinates are present: prime powers are precisely the nonzero lattice points lying on a single coordinate axis.

---

## 2. Independent positivity and the critical attenuation

`A`, `N`, `R`, and `Q` are simultaneously diagonal and commute. On `Ran(Q)`, `N^{-1}` is positive and bounded. Thus `B=QAN^{-1}Q` is a positive diagonal operator on its natural domain.

Multiplication by `e^{-A/2}` gives

\[
T e_{p^k}
=(\log p)e^{-k\log p/2}e_{p^k}
=(\log p)p^{-k/2}e_{p^k},
\]

and annihilates non-prime-powers. Hence `T>=0` independently of any RH statement.

The eigenvalues tend to zero, so `T` is compact. More sharply, for every `q>0`,

\[
\|T\|_{S_q}^q
=
\sum_p\sum_{k\ge1}(\log p)^q p^{-kq/2}
=
\sum_p\frac{(\log p)^q}{p^{q/2}-1}.
\tag{5}
\]

Therefore

\[
\boxed{T\in S_q\iff q>2.}
\tag{6}
\]

For `q>2`, comparison with the ordinary integer sum gives convergence. At `q=2`, the prime terms dominate a constant multiple of `1/p`, and Euler's divergence of `sum_p 1/p` gives divergence; `q<2` is then also divergent. So the finite Weil weight operator is compact but not Hilbert-Schmidt, with the same critical exponent `2`/half-boundary already visible in PL-007.

This coincidence is exact, but the control below shows it is not sufficient for RH.

---

## 3. Exact finite-place trace functional

Let `phi` have compact support in `[0,infinity)`. Since `A` has eigenvalues `log n`, only finitely many basis states meet that support, so no regularization is involved:

\[
\operatorname{Tr}(T\phi(A))
=
\sum_n\frac{\Lambda(n)}{\sqrt n}\phi(\log n).
\]

Decomposing `n=p^k` gives (3). In measure notation, the positive spectral measure generated by `(A,T)` is

\[
\mu_{\mathrm{axis}}
=
\sum_p\sum_{k\ge1}
(\log p)p^{-k/2}\,\delta_{k\log p}.
\tag{7}
\]

This is exactly the positive-location finite arithmetic measure appearing in the centered Riemann explicit formula; the negative locations are its reflected copy under the usual symmetric test-function convention.

The distinction from Weil positivity is essential. In the Weil quadratic functional the finite-place correlations occur with the explicit-formula sign and are balanced by the archimedean and pole/global contributions. Equation (7) identifies the **coefficient measure**, not a termwise positive decomposition of the Weil form. WP-001 already proves that the actual local prime-ray Weil block is indefinite, so (2) does not evade that obstruction.

---

## 4. Beurling matched control: the construction is generic finite-place geometry

Let `P={q_j}` be a Beurling generalized-prime system and index the corresponding formal generalized integers by finite exponent vectors

\[
g=\prod_j q_j^{\alpha_j}.
\]

On the same free exponent Hilbert space define

\[
A_P e_g=(\log|g|)e_g,
\qquad
N e_g=\Big(\sum_j\alpha_j\Big)e_g,
\qquad
Qe_g=\mathbf 1_{\{\text{one occupied coordinate}\}}e_g.
\]

Exactly the same calculation gives

\[
Q A_P N^{-1}Qe_g=\Lambda_P(g)e_g,
\tag{8}
\]

where the generalized von Mangoldt function is `log q_j` on `q_j^k` and zero off generalized prime powers. Thus

\[
T_P=e^{-A_P/2}Q A_P N^{-1}Q\ge0
\]

has weights

\[
\Lambda_P(g)|g|^{-1/2}.
\tag{9}
\]

This is not an artificial countermodel: generalized von Mangoldt functions and their logarithmic-derivative identity are standard in Beurling prime theory.

Diamond, Montgomery, and Vorhauer construct a Beurling system with

\[
N_P(x)=\kappa x+O(x^\theta),
\qquad \frac12<\theta<1,
\tag{10}
\]

while its Beurling zeta has infinitely many zeros on

\[
\sigma=1-a/\log t.
\tag{11}
\]

Equation (10) implies that

\[
\sum_g |g|^{-2\sigma}
\]

has convergence boundary `sigma=1/2`, just as for the ordinary integers. Therefore the generalized Prime-Lattice semigroup has the same structural Hilbert-Schmidt threshold:

\[
e^{-\sigma A_P}\in S_2
\iff
\sigma>1/2.
\tag{12}
\]

Yet (11) gives infinitely many zeros with real part approaching `1`, not `1/2`.

So the following package survives a matched generalized-prime control that emphatically does not satisfy an RH conclusion:

```text
free prime-exponent lattice
+ coordinate-axis prime-power selector Q
+ positive logarithmic generator A_P
+ exact generalized Mangoldt operator Q A_P N^{-1} Q
+ positive critical attenuation e^{-A_P/2}
+ H^2 / Hilbert-Schmidt boundary at 1/2.
```

This is the decisive audit. The Riemann specialization of that package is exact and useful, but the package itself is not the sought global positivity mechanism.

---

## 5. Prior-art and novelty audit

The ingredients are deliberately separated from the Mathia consequence.

- Hedenmalm--Lindqvist--Seip's Hardy space of Dirichlet series and Bohr lift make the prime-exponent Hilbert basis classical.
- The prime-gas/logarithmic Hamiltonian `A=sum_p(log p)N_p` is classical and already audited in PL-004/PL-007.
- The von Mangoldt definition and `-zeta'/zeta` logarithmic-derivative identity are classical; their Beurling analogues are standard as well.
- Beurling generalized-prime systems are classical, and Diamond--Montgomery--Vorhauer provide the strong off-line-zero control used above.
- Connes-style and Weil explicit-formula programs already insist that finite and archimedean places must be assembled globally; no novelty is claimed for that principle.

Directed searches around Bohr lifts, Hardy spaces of Dirichlet series, von Mangoldt operators, prime-power axes, Fock/occupation-number formulations, and Weil positivity found the classical components but no reason to claim that the elementary factorization

\[
M_\Lambda=QAN^{-1}Q
\]

is a new theorem. **No novelty claim is made for the identity itself.**

The durable result is instead the Mathia-specific two-sided audit:

1. Prime Lattice is the first tested Mathia branch here whose canonical positive operator reproduces the finite Weil prime-power support and weights exactly, rather than missing the support (WP-002) or losing the arithmetic scale (WP-003).
2. A strong Beurling control proves that this exact local success, even together with the `1/2` Hilbert boundary, is generic enough to coexist with zeros far off the critical line. It therefore cannot supply the missing global Weil positivity by itself.

---

## 6. Boundary conditions and possible escapes

This finding does **not** rule out Prime Lattice as an ingredient of a successful global construction. It rules out treating its positive axis/Mangoldt operator, its critical attenuation, or its `1/2` Schatten boundary as sufficient.

A genuine escape must introduce an additional Mathia-native structure that fails the Beurling control for a principled reason. In particular it should do all of the following:

1. retain the exact finite operator (2), or derive an equivalent finite-place boundary response without hand-inserting `Lambda`;
2. produce the Riemann archimedean gamma/pole contribution from the **same** global object rather than adjoining it as a known explicit-formula term;
3. impose a self-duality/functional-equation or cohomological/intersection structure strong enough to distinguish ordinary primes from Beurling systems such as (10)-(11);
4. prove nonnegativity from that global structure independently of RH and without importing the zero divisor;
5. recover the signed Weil quadratic form after assembly, consistent with WP-001's local indefiniteness obstruction.

This points naturally toward a quotient/compression, boundary-response, relative/scattering, or cohomological construction in which `T` is only the finite boundary component and the archimedean completion is forced by global self-duality.

---

## 7. Audit / falsification test

The exact part is auditable on basis vectors:

1. check that `Q` selects exactly `p^k`;
2. check that `A/N` maps `p^k` to `log p`;
3. multiply by `e^{-A/2}` to obtain `(log p)p^{-k/2}`;
4. trace against compactly supported `phi(A)` to recover (3);
5. sum the eigenvalue powers to verify (5)-(6).

The negative control is falsified only if one of the following fails:

- the Beurling axis calculation (8)-(9);
- the linear generalized-integer counting law (10) and the resulting `1/2` `S_2` boundary;
- the cited existence of zeros (11).

A future global Prime-Lattice construction escapes rather than falsifies this finding if it adds a canonical archimedean/self-dual datum not shared by the Beurling control.

## Consequence for the research line

The search map changes in a useful way:

```text
Prime Circle:
    exact prime-power scale -> local Weil block indefinite                 [WP-001]

Prime Circle uniformization energy:
    genuine positivity -> wrong arithmetic support                         [WP-002]

Prime Flute projective energy:
    genuine positivity -> exact all-composite isometric clone              [WP-003]

Prime Lattice axis operator:
    genuine positivity + exact finite Weil support + exact finite weights
    -> survives generalized-prime systems with off-critical zeros          [WP-004]
    -> therefore finite arithmetic matching is finally achieved,
       but global/archimedean forcing is still absent.
```

The highest-value next target is no longer another way to manufacture the finite von Mangoldt weights. Prime Lattice already does that canonically. The missing object is a **single global positive construction that forces the archimedean/pole completion and breaks the Beurling control while retaining (2) as its finite-place boundary data**.
