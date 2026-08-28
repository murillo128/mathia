# PC-024 — same-index finite Fourier nonlinearities collapse to Möbius/squarefree zeta factors

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for fixed finite products (and hence finite polynomials) of nonzero primitive-shell Fourier modes followed by an ordinary Dirichlet transform in the level. This does **not** cover singular infinite-mode energies, shell-dependent nonlinear operators, nonseparable scale dynamics, or the global uniformization/accessory defect of PC-017.

PC-021 proved a broad no-go theorem for regular linear probes and for multilinear probes whose shell indices are transformed independently. It deliberately left open **same-index nonlinear observables** such as `B(P_n,P_n)`. The most canonical finite-dimensional version of that escape is to couple several angular Fourier amplitudes of the *same* primitive shell before transforming in `n`.

That branch also collapses exactly. Odd-degree products inherit `1/zeta(s)`; even-degree products inherit the squarefree factor `zeta(s)/zeta(2s)`, up to finitely many Euler corrections determined only by the chosen Fourier modes.

## 1. Primitive-shell Fourier amplitudes are Ramanujan sums

Let

\[
P_n=\sum_{\operatorname{ord}(\zeta)=n}\delta_\zeta
\]

be the primitive/new-vertex counting measure on the original unit circle. For any nonzero integer `k`, define the angular Fourier amplitude

\[
M_k(n)
:=\int_{S^1} z^k\,dP_n(z)
=\sum_{\zeta\in\mu_n^*}\zeta^k.
\]

Then exactly

\[
\boxed{M_k(n)=c_n(k),}
\]

where `c_n(k)` is the classical Ramanujan sum. In particular,

\[
\boxed{M_1(n)=c_n(1)=\mu(n).}
\]

Thus the fundamental angular mode already records the Möbius function in the anchored coordinate inherited from the original polygon.

PC-021 classified the **linear** transform of each `M_k`. The present question is what happens after taking a nonlinear same-level product.

## 2. Prime-power behavior makes every fixed-mode product multiplicative

Fix nonzero integers

\[
\mathbf k=(k_1,\ldots,k_r),
\qquad r\ge1,
\]

and define the same-index Fourier monomial

\[
A_{\mathbf k}(n)
:=\prod_{j=1}^r M_{k_j}(n)
=\prod_{j=1}^r c_n(k_j).
\]

For fixed `k`, `n -> c_n(k)` is multiplicative, so `A_k(n)` is multiplicative.

Write

\[
a_j=v_p(k_j).
\]

The classical prime-power formula is

\[
\boxed{
c_{p^e}(k_j)=
\begin{cases}
\varphi(p^e),& e\le a_j,\\
-p^{a_j},& e=a_j+1,\\
0,& e\ge a_j+2.
\end{cases}}
\]

Hence the local Dirichlet factor is a **finite polynomial**

\[
F_{p,\mathbf k}(x)
=
1+
\sum_{e=1}^{1+\min_j a_j}
\left(\prod_{j=1}^r c_{p^e}(k_j)\right)x^e.
\]

Let

\[
K=\prod_{j=1}^r |k_j|.
\]

For every prime `p` not dividing `K`, all `a_j=0`, so

\[
c_p(k_j)=-1,
\qquad
c_{p^e}(k_j)=0\quad(e\ge2),
\]

and therefore

\[
\boxed{F_{p,\mathbf k}(x)=1+(-1)^r x
\qquad(p\nmid K).}
\]

All non-generic local behavior is confined to the finitely many primes dividing the fixed Fourier labels.

## 3. Exact parity dichotomy of the level Dirichlet series

For fixed nonzero `k_j`, the Ramanujan sums are bounded as functions of `n`, so

\[
D_{\mathbf k}(s)
:=\sum_{n\ge1}\frac{A_{\mathbf k}(n)}{n^s}
\]

converges absolutely for `Re(s)>1` and has the Euler product

\[
D_{\mathbf k}(s)
=\prod_p F_{p,\mathbf k}(p^{-s}).
\]

Define the finite Euler correction

\[
E_{\mathbf k}(s)
:=
\prod_{p\mid K}
\frac{F_{p,\mathbf k}(p^{-s})}
{1+(-1)^r p^{-s}}.
\]

Then on `Re(s)>1`, exactly:

### Odd degree

If `r` is odd,

\[
\prod_p(1-p^{-s})=\frac1{\zeta(s)},
\]

so

\[
\boxed{
D_{\mathbf k}(s)
=\frac{E_{\mathbf k}(s)}{\zeta(s)}.
}
\]

### Even degree

If `r` is even,

\[
\prod_p(1+p^{-s})
=\frac{\zeta(s)}{\zeta(2s)},
\]

so

\[
\boxed{
D_{\mathbf k}(s)
=\frac{\zeta(s)}{\zeta(2s)}E_{\mathbf k}(s).
}
\]

Thus a fixed finite same-shell Fourier nonlinearity has only two possible **global** zeta backgrounds, determined by the parity of its degree. Everything depending on the chosen modes is a finite Euler correction.

This is an exact extension into one of the escape hatches left open by PC-021: the shell index is shared across all factors, so independent Möbius factorization does not apply, but multiplicativity plus the generic prime-power rule still collapses the result.

## 4. The fundamental quadratic energy is just the squarefree sieve

Take the first mode twice:

\[
A_{(1,1)}(n)=M_1(n)^2=\mu(n)^2.
\]

Therefore

\[
\boxed{
\sum_{n\ge1}\frac{|M_1(n)|^2}{n^s}
=
\sum_{n\ge1}\frac{\mu(n)^2}{n^s}
=
\frac{\zeta(s)}{\zeta(2s)}.
}
\]

Geometrically this is the most elementary nonlinear same-index observable that PC-021 did not cover: take the global fundamental angular moment of one birth shell and square its magnitude before any scale transform.

But it only detects **squarefreeness**. Every squarefree composite has the same value `1` as a prime, while every nonsquarefree level has value `0`.

This gives a particularly important interpretation warning. The denominator `zeta(2s)` places the rescaled nontrivial zeta-zero locus at

\[
s=\rho/2.
\]

Under RH its real part would be

\[
\boxed{\operatorname{Re}s=1/4.}
\]

Any `1/4` line produced by this quadratic Fourier mechanism is therefore not a new critical geometry: it is the completely classical squarefree Dirichlet series with the Riemann zeros rescaled by `s -> 2s`.

## 5. Finite polynomial Fourier observables are classicalized term by term

Any fixed polynomial in finitely many **nonzero** amplitudes

\[
M_{k_1}(n),\ldots,M_{k_m}(n)
\]

is a finite linear combination of monomials of the form treated above. Hence its ordinary level Dirichlet transform is a finite linear combination of terms with global factors

\[
\frac1{\zeta(s)}
\quad\text{or}\quad
\frac{\zeta(s)}{\zeta(2s)},
\]

multiplied by finite Euler corrections.

For a homogeneous polynomial, parity is decisive:

- odd total degree -> reciprocal-zeta background;
- even total degree -> squarefree `zeta(s)/zeta(2s)` background.

The zeroth Fourier mode `M_0(n)=phi(n)` is excluded from this statement; it carries the already-classical totient/Jordan-type growth rather than the bounded nonzero-mode behavior. Infinite Fourier series are also excluded because summing over infinitely many modes can introduce new convergence and interchange questions.

## 6. Research consequence

This closes a natural finite-dimensional version of the same-index nonlinear escape left open in PC-021:

\[
\boxed{
\text{one primitive shell}
\to
\text{finitely many fixed angular modes}
\to
\text{finite polynomial nonlinearity at the same level}
\to
\text{ordinary Dirichlet transform}
}
\]

cannot supply an independent zeta-zero mechanism.

The odd-degree branch returns the familiar Möbius reciprocal zeta. The even-degree branch changes the sieve from Möbius sign to squarefree support and therefore replaces `1/zeta(s)` by `zeta(s)/zeta(2s)`. Neither creates new arithmetic dynamics.

In particular, **nonlinearity by itself is not enough** to escape PC-021. The surviving region is narrower:

- singular or renormalized infinite-mode energies where fixed finite Fourier algebra is insufficient;
- shell-dependent nonlinear metrics/operators;
- genuinely nonseparable dynamics across levels;
- global anchored uniformization/accessory/Liouville data such as PC-017;
- nonlinear spatial observables whose definition cannot be reduced to a finite polynomial of fixed Ramanujan/Fourier coordinates.

## 7. Prior art and novelty audit

All arithmetic ingredients are classical.

- Ramanujan's sum is the power sum of primitive roots and has the divisor formula
  \[
  c_n(k)=\sum_{d\mid(n,k)}d\,\mu(n/d).
  \]
- The prime-power formula above is standard and immediately implies multiplicativity in `n` for fixed `k`.
- `c_n(1)=mu(n)` is classical.
- The squarefree Dirichlet series
  \[
  \sum \mu(n)^2 n^{-s}=\zeta(s)/\zeta(2s)
  \]
  is classical.
- Products and correlations of Ramanujan sums are an established topic; for example László Tóth, *Sums of products of Ramanujan sums* (Ann. Univ. Ferrara 58 (2012), 183–197; arXiv:1104.1906), studies multiplicativity and product identities for such sums.

No novelty is claimed for the Euler-product calculation. Directed searches did not identify a reason to treat the parity factorization above as a new theorem; it is an elementary fixed-mode consequence of the classical prime-power formula.

The durable prime-circle contribution is the **research boundary**: one of PC-021's explicit nonlinear escape classes can now be narrowed substantially, and an apparent quarter-line singularity from even-degree Fourier energies is identified in advance as the classical squarefree `zeta(2s)` shadow rather than new RH evidence.

## 8. Audit tests

The result can be checked without numerical fitting:

1. verify `M_k(n)=c_n(k)` directly from the primitive-root definition;
2. verify the prime-power formula for `c_{p^e}(k)`;
3. check multiplicativity of `A_k(n)`;
4. for primes `p` outside the finite support of the Fourier labels, recover the generic local factor `1+(-1)^r p^{-s}`;
5. multiply generic Euler factors to obtain `1/zeta(s)` for odd `r` and `zeta(s)/zeta(2s)` for even `r`;
6. check the special case `k_1=k_2=1`, which reduces exactly to the squarefree indicator `mu(n)^2`.

A counterexample to the claimed generic local factor for some `p` not dividing any `k_j`, or a nonzero `c_{p^e}(k_j)` with `e>=2` in that situation, would invalidate the factorization.
