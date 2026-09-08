# MC-144 — Bounded Bost–Connes observables have only profinite-continuous number-state diagonals

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Let `A_BC` be the standard Bost–Connes `C^*`-algebra and use its canonical number-state representation on

\[
\ell^2(\mathbb N)=\overline{\operatorname{span}}\{\varepsilon_k:k\ge1\},
\]

with

\[
\pi(e(r))\varepsilon_k=e^{2\pi i k r}\varepsilon_k,
\qquad
\pi(\mu_n)\varepsilon_k=\varepsilon_{nk}.
\tag{1}
\]

For any bounded observable `A in A_BC`, define its number-state diagonal sequence

\[
d_A(k)=\langle\varepsilon_k,\pi(A)\varepsilon_k\rangle.
\tag{2}
\]

Then `d_A` is not an arbitrary bounded arithmetic sequence. It is always the restriction to the ordinary positive integers of a unique continuous function

\[
\widetilde d_A\in C(\widehat{\mathbb Z})
\cong C^*(\mathbb Q/\mathbb Z).
\tag{3}
\]

Equivalently, the canonical number-basis diagonal defines a contractive projection

\[
\boxed{
E_{\mathrm{diag}}:A_{BC}\longrightarrow C^*(\mathbb Q/\mathbb Z)
}
\tag{4}
\]

whose restriction to the coefficient algebra is the identity. On the standard algebraic spanning monomials it is exactly

\[
\boxed{
E_{\mathrm{diag}}(\mu_m a\mu_n^*)
=
\begin{cases}
0,&m\ne n,\\
\mu_n a\mu_n^*,&m=n,
\end{cases}
\qquad a\in C^*(\mathbb Q/\mathbb Z).
}
\tag{5}
\]

The balanced term in `(5)` again belongs to the coefficient algebra by the Bost–Connes covariance relation. Thus the semigroup/crossed-product part creates no additional information in the **canonical scalar diagonal readout**: after taking diagonal number-state matrix elements, every bounded observable has collapsed back to a profinite-continuous coefficient observable.

Combining this with `MC-143` gives the exact full-algebra obstruction

\[
\boxed{
\inf_{A\in A_{BC}}
\sup_{\substack{k\ge1\\ \mu(k)\ne0}}
\left|
\langle\varepsilon_k,\pi(A)\varepsilon_k\rangle-\mu(k)
\right|
=1.
}
\tag{6}
\]

The upper bound is attained by `A=0`; the lower bound follows because every diagonal sequence comes from `C(\widehat{\mathbb Z})` and `MC-143` proves that the square-free Möbius sign has uniform distance exactly `1` from that continuous function class.

There is a parallel equilibrium statement. If `\phi_\beta` is any Bost–Connes `KMS_\beta` state with `\beta>0`, then

\[
\boxed{
\phi_\beta(A)=\phi_\beta(E_{\mathrm{diag}}A)
\qquad(A\in A_{BC}).
}
\tag{7}
\]

Indeed `MC-139` gives zero expectation to every nonzero time-energy degree, while the degree-zero monomials in `(5)` are already coefficient elements. Hence every bounded equilibrium scalar expectation factors through the same coefficient projection.

Equations `(6)`–`(7)` close a precise part of the full-crossed-product escape left open by `MC-143`: merely allowing an arbitrary bounded Bost–Connes observable does **not** evade the profinite information barrier if the proposed Möbius carrier is read through the canonical number-state diagonal or through a KMS scalar expectation.

This does **not** rule out off-diagonal matrix coefficients, coherent families of states, non-equilibrium dynamics, unbounded/measurable observables, or aggregate statistics whose transfer to `M(x)` does not require pointwise Möbius recovery. It identifies exactly which readout operation destroys the extra crossed-product information.

## 1. Algebraic monomials have coefficient-algebra diagonals

The standard semigroup-crossed-product presentation of the Bost–Connes algebra has a norm-dense algebraic span of monomials

\[
\mu_m a\mu_n^*,
\qquad
m,n\ge1,
\quad
a\in C^*(\mathbb Q/\mathbb Z).
\tag{8}
\]

It is enough first to take `a=e(r)`. From `(1)`,

\[
\mu_n^*\varepsilon_k
=
\begin{cases}
\varepsilon_{k/n},&n\mid k,\\
0,&n\nmid k.
\end{cases}
\tag{9}
\]

Therefore

\[
\begin{aligned}
&\langle\varepsilon_k,
\pi(\mu_m e(r)\mu_n^*)\varepsilon_k\rangle\\
&\qquad=
\mathbf 1_{n\mid k}
\,e^{2\pi i (k/n)r}
\,\langle\varepsilon_k,\varepsilon_{mk/n}\rangle.
\end{aligned}
\tag{10}
\]

Since `k>0`, the last inner product is nonzero exactly when `m=n`. Hence

\[
d_{\mu_m e(r)\mu_n^*}(k)=0
\qquad(m\ne n),
\tag{11}
\]

while for `m=n`,

\[
d_{\mu_n e(r)\mu_n^*}(k)
=
\mathbf 1_{n\mid k}e^{2\pi i(k/n)r}.
\tag{12}
\]

The Bost–Connes relation

\[
\mu_n e(r)\mu_n^*
=
\frac1n\sum_{ns=r}e(s)
\tag{13}
\]

shows directly that the right side of `(12)` is the restriction to the integers of a coefficient-algebra element. Linearity and norm density in the coefficient variable extend this to arbitrary `a`, proving `(5)` on the algebraic span.

This calculation is stronger than the KMS energy selection rule in `MC-139` for the present purpose. `MC-139` says a nonzero energy mode has zero **equilibrium expectation**. Equation `(11)` says every such mode already has zero **pointwise number-state diagonal**, before choosing a temperature or state.

## 2. Norm completion preserves profinite continuity

Let `A_j` be algebraic finite sums of the monomials `(8)` with

\[
\|A_j-A\|\to0.
\tag{14}
\]

By the previous section there is `f_j in C(\widehat Z)` whose restriction to the positive integers is `d_{A_j}`. For any `j,l`,

\[
\sup_{k\ge1}|d_{A_j}(k)-d_{A_l}(k)|
\le
\|A_j-A_l\|,
\tag{15}
\]

because every diagonal matrix coefficient is a norm-one bounded functional.

The positive integers are dense in `\widehat{\mathbb Z}`. Hence for the continuous difference `f_j-f_l`,

\[
\|f_j-f_l\|_{C(\widehat Z)}
=
\sup_{k\ge1}|d_{A_j}(k)-d_{A_l}(k)|.
\tag{16}
\]

Equations `(15)`–`(16)` make `(f_j)` uniformly Cauchy, so it converges to a unique

\[
f_A\in C(\widehat Z).
\tag{17}
\]

For each fixed `k`, norm convergence in `(14)` also gives

\[
d_{A_j}(k)\to d_A(k),
\]

therefore

\[
f_A(k)=d_A(k)
\qquad(k\ge1).
\tag{18}
\]

This proves `(3)` for every bounded `A`, not only for finite crossed-product words.

Identifying `f_A` with its coefficient-algebra element defines `(4)`. The map is linear and contractive by `(15)`–`(16)`, fixes `C^*(Q/Z)`, and is positive because `A>=0` implies every number-state diagonal value is nonnegative and hence the continuous extension is nonnegative on the closure `\widehat Z`. Thus it is a norm-one positive projection onto the coefficient algebra; equivalently, by the standard C*-algebra projection theorem it is a conditional expectation.

The key information statement does not require that terminology. What matters is exact: **norm completion of the full bounded crossed product does not enlarge the class of canonical diagonal sequences beyond continuous profinite functions.**

## 3. The square-free Möbius sign remains a full unit away

`MC-143` proves

\[
\inf_{f\in C(\widehat Z)}
\sup_{\mu(k)\ne0}|f(k)-\mu(k)|=1.
\tag{19}
\]

Its lower bound uses an exact collision at one profinite point. For growing factorial moduli, Dirichlet's theorem supplies primes `p_K,q_K,r_K` all congruent to `1` modulo `K!`; then

\[
p_K\to1,
\qquad
q_Kr_K\to1
\quad\text{in }\widehat Z,
\tag{20}
\]

but

\[
\mu(p_K)=-1,
\qquad
\mu(q_Kr_K)=+1.
\tag{21}
\]

Every `A in A_BC` produces `\widetilde d_A in C(\widehat Z)` by `(3)`. Substituting `f=\widetilde d_A` into `(19)` gives the lower bound in `(6)`. The zero observable has identically zero diagonal and gives error exactly `1`, proving equality.

Thus the extra semigroup operators can change off-diagonal matrix elements dramatically, but if one subsequently asks only for the scalar diagonal sequence indexed by `k`, that additional information has been projected away before the Möbius comparison is made.

This is not a statement that the Bost–Connes algebra fails to contain arithmetic information. It is a statement that one particular natural readout has exactly the same continuity quotient already classified in `MC-143`.

## 4. Every KMS first moment factors through the same projection

The time evolution satisfies

\[
\sigma_t(\mu_m a\mu_n^*)
=
(m/n)^{it}\mu_m a\mu_n^*.
\tag{22}
\]

`MC-139` derives directly from the KMS identity that every homogeneous element of degree different from `1` has zero `KMS_beta` expectation for every `beta>0`. Hence

\[
\phi_\beta(\mu_m a\mu_n^*)=0
\qquad(m\ne n).
\tag{23}
\]

For `m=n`, the monomial is the coefficient element `\mu_n a\mu_n^*`, so `(5)` gives

\[
\phi_\beta(\mu_n a\mu_n^*)
=
\phi_\beta(E_{\mathrm{diag}}(\mu_n a\mu_n^*)).
\tag{24}
\]

Equations `(23)`–`(24)` prove `(7)` on the dense algebraic span. Both sides are norm-continuous in `A`, so `(7)` holds on the whole `C^*`-algebra.

This makes the readout boundary independent of the Bost–Connes phase transition. High-temperature symmetry projection (`MC-140`) and the finite character collapses (`MC-141`–`MC-142`) provide stronger classifications for special coefficient modes, but the factorization `(7)` uses only the KMS energy rule plus the crossed-product relations and is valid for every positive inverse temperature.

The factorization should not be overinterpreted. A product such as `A^*B` may contain nontrivial crossed-product structure before `E_diag` is applied, so noncommutative correlations can generate complicated coefficient functions. Equation `(7)` says only that a scalar equilibrium expectation sees such a product **after its degree-zero coefficient projection**. It does not prove those projected functions are dynamically or arithmetically trivial.

## 5. Prior art and novelty audit

The operator-algebraic ingredients are standard.

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411–457, DOI `10.1007/BF01589495`, give the original Bost–Connes presentation, covariance relations, canonical representations, and time evolution already used throughout `MC-138`–`MC-143`.
- Marcelo Laca and Iain Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, identify the Bost–Connes Hecke algebra as the relevant semigroup crossed product. The dense monomial span used in `(8)` is standard crossed-product structure.
- Matilde Marcolli, *Arithmetic Noncommutative Geometry*, University Lecture Series **36**, American Mathematical Society (2005), gives a standard modern account of the Bost–Connes crossed-product algebra, its arithmetic representations, and quantum-statistical dynamics.
- The existence of coefficient/identity-term expectations for crossed-product and partial-crossed-product C*-algebras is standard operator-algebra machinery. The explicit derivation `(10)`–`(18)` is included so the line does not need to import a stronger abstract theorem than necessary.

A targeted literature search found the standard semigroup/partial-crossed-product presentations and canonical representations, but no need to treat `(4)` as a new general C*-algebra theorem: it is the expected identity-component/diagonal projection specialized to the Bost–Connes representation.

Accordingly **no novelty is claimed** for the conditional expectation, representation formulas, or crossed-product decomposition. The durable line-specific result is their combination with `MC-143`: the exact uniform Möbius-orientation obstruction persists even after allowing arbitrary bounded full Bost–Connes observables, provided the proposed carrier is extracted by the canonical number-state diagonal; and all KMS scalar expectations factor through that same coefficient layer.

## Boundaries and falsification tests

- **The theorem is about bounded observables.** Unbounded affiliated operators, measurable multipliers, and limits outside the `C^*` norm can have diagonal behavior not covered by `(3)`.
- **The theorem is about the canonical number-state diagonal.** Off-diagonal coefficients `\langle\varepsilon_j,\pi(A)\varepsilon_k\rangle`, `j\ne k`, can retain semigroup transport that `(2)` deliberately discards.
- **KMS factorization is a scalar-readout statement.** Noncommutative multiplication can create nontrivial degree-zero coefficient elements before expectation; `(7)` does not say the full crossed product is algebraically equivalent to its coefficient algebra.
- **Pointwise Möbius recovery is stronger than an aggregate route.** An observable whose diagonal does not approximate `mu(k)` pointwise might still yield a weighted, smoothed, or collective statistic relevant to `M(x)`. Such a claim requires an independent source-to-excursion theorem and is not excluded by `(6)`.
- **Finite-range interpolation remains possible.** The obstruction is global across unbounded square-free integers, exactly as in `MC-143`.
- **Changing the representation/readout changes the problem.** A proposed escape using coherent superpositions, a family of states depending on the observation scale, or non-equilibrium matrix coefficients must state the source-forced readout and prove why it is cheaper than reconstructing Möbius orientation itself.
- **No Mertens bound or RH implication is obtained.** This is a representation/readout no-go, not progress toward the required source-to-amplitude estimate.

## Consequence for the line

`MC-143` left the full crossed-product/semigroup part as a possible escape because its pointwise obstruction applied only to continuous coefficient observables. The present finding shows that **bounded crossed-product complexity alone is not enough**: when compressed by the canonical number-state diagonal, every full observable lands back in `C(\widehat Z)`, where the prime/semiprime collision applies with exact uniform error floor `1`.

Likewise, equilibrium scalar expectations cannot use nonzero semigroup energy directly; they factor through the same coefficient projection by `MC-139` and `(7)`.

A genuinely new Bost–Connes continuation therefore has to exploit information that survives outside this scalar diagonal quotient: off-diagonal coherence, a non-equilibrium or scale-dependent state family, controlled unbounded/measurable structure, or an aggregate coefficient statistic with an independently cheaper transfer to first-absolute Mertens excursion. Repackaging an arbitrary bounded crossed-product element and then reading only its number-state diagonal is now closed.