# AF-274 — Fixed local Euler degree gives sharp finite-depth fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `EULER-LOCAL`, `NEWTON-GIRARD`, `FINITE-DEPTH-CERTIFICATE`, `SHARP`, `BREADTH-BOUNDARY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-273 shows that reflection symmetry, exact ordinate matching, Bohr periodicity, and even full support on one rational-prime-power ray do not make any fixed source prefix faithful: a cyclotomic block of orbit size `M` can hide its first `M-1` coefficient defects. That escape uses a local polynomial whose degree grows with `M`.

A fixed Euler-local degree bound removes that depth escape exactly.

Fix a rational prime `p`, put

\[
z:=p^{-s},
\qquad \lambda:=\log p,
\]

and let `\mathcal E_d` be the class of normalized reciprocal polynomial Euler factors

\[
E(z)=\prod_{j=1}^{r}(1-\alpha_j z)^{-1},
\qquad 0\le r\le d,
\tag{1}
\]

where the `\alpha_j\in\mathbb C` are counted with multiplicity. Write

\[
c_k(E):=\sum_{j=1}^{r}\alpha_j^k,
\qquad k\ge1.
\tag{2}
\]

Equivalently, on a right half-plane of convergence,

\[
-\frac{E'}{E}(p^{-s})
=\lambda\sum_{k\ge1}c_k(E)p^{-ks}.
\tag{3}
\]

Then:

1. **Sharp local finite-depth fidelity.** If `E,F\in\mathcal E_d` and
   \[
   c_k(E)=c_k(F)\qquad(1\le k\le d),
   \tag{4}
   \]
   then `E=F` as rational functions. Thus the first `d` prime-power source coefficients determine every normalized local Euler factor of degree at most `d`.

2. **The depth `d` is best possible in the unrestricted degree-`d` class.** For every `d\ge1` and nonzero `A,B` with `A^d\ne B^d`,
   \[
   E_A(z)=\frac1{1-(Az)^d},
   \qquad
   E_B(z)=\frac1{1-(Bz)^d}
   \tag{5}
   \]
   both lie in `\mathcal E_d`, have identical source coefficients through depth `d-1`, and differ at depth `d`.

3. **Global Euler products need finite depth per prime but still infinite prime breadth.** Suppose
   \[
   Z(s)=\prod_p E_p(p^{-s}),
   \qquad
   W(s)=\prod_p F_p(p^{-s})
   \tag{6}
   \]
   converge absolutely in a common right half-plane and every `E_p,F_p\in\mathcal E_d`. If `(4)` holds for every rational prime `p`, then every local factor agrees and hence `Z=W` in that half-plane. But no finite set of primes can certify the same conclusion: an unobserved prime can be changed while all inspected local data remain identical.

4. **For the Riemann zeta local category, one coefficient per prime fixes the whole ray.** Here `d=1` and
   \[
   E_p(z)=(1-z)^{-1}.
   \]
   Any competing degree-one local factor `(1-\beta_p z)^{-1}` with the same coefficient at `p` has `\beta_p=1`, hence the same coefficients at every `p^k`.

Therefore AF-273 does not show that arbitrarily deep prime-power information is required inside a fixed-degree Euler-product category. It shows instead that its hidden-prefix construction escapes by paying **unbounded local Euler degree**. Bounded degree collapses the prime-power depth bill to `d`, but it does not compress away the separate bill of identifying infinitely many prime locations.

## Exact derivation

### 1. The local logarithmic derivative is a power-sum sequence

For one factor in `(1)`,

\[
-\frac{d}{ds}\log(1-\alpha p^{-s})^{-1}
=\lambda\frac{\alpha p^{-s}}{1-\alpha p^{-s}}
=\lambda\sum_{k\ge1}\alpha^k p^{-ks}.
\tag{7}
\]

Summing over the local parameters gives `(3)`. Thus the normalized prime-power coefficients are precisely the power sums of the multiset of local parameters.

Pad a factor of degree `r<d` by adjoining `d-r` zero parameters. This changes neither the Euler factor nor any positive power sum. Every member of `\mathcal E_d` may therefore be represented by a `d`-tuple

\[
(\alpha_1,\ldots,\alpha_d)
\tag{8}
\]

with zero padding allowed.

### 2. Newton-Girard reconstructs the local polynomial from the first `d` moments

Let

\[
p_k:=\sum_{j=1}^{d}\alpha_j^k
\]

and let `e_m` be the elementary symmetric functions of the padded parameters, with `e_0=1`. Newton-Girard gives, for `1\le m\le d`,

\[
m e_m
=\sum_{k=1}^{m}(-1)^{k-1}e_{m-k}p_k.
\tag{9}
\]

Hence `p_1` determines `e_1`; then `p_1,p_2` determine `e_2`; continuing recursively, the first `d` power sums determine every `e_m` for `m\le d`.

The reciprocal local polynomial is

\[
P_E(z)
:=\prod_{j=1}^{d}(1-\alpha_j z)
=\sum_{m=0}^{d}(-1)^m e_m z^m.
\tag{10}
\]

Consequently equality of the first `d` source coefficients forces equality of all coefficients of `P_E` and `P_F`, hence `P_E=P_F` and `E=F`. Repeated parameters cause no problem because Newton identities work with multiplicity, and zero padding exactly represents lower local degree.

This is stronger than applying AF-272 naively to the quotient `E/F`. AF-272 must allow a general signed quotient divisor, whose support may contain up to the union of the two input supports. Here each input is not an arbitrary signed divisor: it is a positive root multiset of total cardinality at most `d`. Newton-Girard reconstructs each local polynomial from `d` moments, so the generic `2d` union bound is unnecessary in this structured subclass.

### 3. The certificate length is sharp

Let `\omega_d=e^{2\pi i/d}`. The elementary factorization

\[
1-(Az)^d
=\prod_{j=0}^{d-1}(1-A\omega_d^j z)
\tag{11}
\]

puts `E_A` in `\mathcal E_d`. Its local parameters are `A\omega_d^j`, so

\[
c_k(E_A)
=A^k\sum_{j=0}^{d-1}\omega_d^{jk}.
\tag{12}
\]

The root-of-unity sum vanishes for `1\le k<d` and equals `d` at `k=d`. Therefore

\[
c_k(E_A)=c_k(E_B)=0
\qquad(1\le k<d),
\tag{13}
\]

while

\[
c_d(E_A)=dA^d\ne dB^d=c_d(E_B).
\tag{14}
\]

So no universal depth below `d` identifies all degree-`d` normalized Euler factors. The same cyclotomic filtering that powers AF-273 is therefore also the exact sharpness witness for the bounded-degree theorem; the difference is that its orbit size can no longer grow past the declared local degree budget.

### 4. Local depth does not remove global breadth

Under absolute convergence, equality of all local factors implies equality of the Euler products in `(6)`. By the local theorem it is enough to compare `d` power-sum coefficients at each prime.

This remains an infinite family of local tests. Given any finite set `S` of inspected primes, choose `q\notin S`. Keeping `F_p=E_p` for every `p\ne q` and replacing `E_q` by any distinct factor in `\mathcal E_d` produces another Euler product with identical inspected data and a different source. Equivalently, any finite Dirichlet-coefficient cutoff can be evaded by changing a prime larger than that cutoff.

The information boundary is therefore two-dimensional:

\[
\boxed{
\text{bounded local Euler degree}
\Longrightarrow
\text{finite prime-power depth per prime},
}
\tag{15}
\]

but not

\[
\boxed{
\text{bounded local Euler degree}
\Longrightarrow
\text{finite total arithmetic certificate}.
}
\tag{16}
\]

Local degree controls **depth along a prime ray**; it does not control **breadth across prime rays**.

## Application to the AF-273 cyclotomic escape

AF-273 hides the first `M-1` source defects by factors of the form

\[
1-cz^M.
\tag{17}
\]

In the `z` coordinate this is a degree-`M` polynomial and splits into `M` linear local parameters. The reflection-symmetric quotient uses several such `M`-orbits. Making the hidden prefix longer therefore necessarily increases local polynomial degree.

This identifies the precise resource missing from the AF-273 control class. Reflection symmetry, exact ordinate counts, and full frequency support do not bound local Euler degree. Once a bounded-degree Euler-local category is imposed independently, the hidden-depth mechanism terminates at that bound.

For `\zeta`, the genuine local factor has degree one. Inside the declared degree-one rational-prime local category, the coefficient of `p^{-s}` fixes the parameter and hence every coefficient on the `p^k` ray. AF-273 cannot realize an arbitrarily long hidden prefix without leaving that category.

This does **not** prove that a zero/spectral representation of `\zeta` retains the degree-one Euler category. That is exactly the remaining Arithmetic Fidelity gate. AF-017 already shows that passing from exact Euler-product data to the meromorphic divisor can discard generator information. The present result says what must be retained if one wants a finite-depth local source certificate: not merely prime-power frequency labels, but membership in a fixed-degree normalized Euler-factor class.

## Prior art and novelty assessment

The mathematics used here is classical.

Newton-Girard identities are the standard conversion between power sums and elementary symmetric functions; see I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Clarendon Press/Oxford University Press (1995), Chapter I. They immediately imply that the first `d` power sums determine a polynomial of degree at most `d` once zero padding is allowed.

Fixed-degree local Euler factors are standard in the theory of `L`-functions. Stephen Gelbart, **“An Elementary Introduction to the Langlands Program,”** *Bulletin of the American Mathematical Society* (New Series) 10(2) (1984), 177–219, describes the unramified `GL_n` local factor as

\[
\det(I-A_v N(v)^{-s})^{-1},
\]

an Euler factor of degree `n`, with degree at most `n` at general places. The reviewed LMFDB description of abelian-variety `L`-functions similarly records local `L`-polynomials of degree at most `2g`.

No novelty is claimed for Newton identities, reconstruction of a characteristic polynomial from traces/power sums, Satake parameters, or bounded-degree local Euler factors. The Arithmetic Fidelity contribution is the placement of this classical fact against AF-272/AF-273: **local Euler degree is a sharp finite-depth information budget**. It explains exactly why the cyclotomic hidden-prefix obstruction disappears in fixed-degree Euler categories while an independent infinite-prime breadth problem remains.

## Boundaries and failure modes

- The theorem assumes normalized reciprocal **polynomial** local factors with total degree at most `d`. General rational local factors with numerator and denominator, signed divisor multiplicities, or arbitrary zero-free local factors return to the broader quotient-complexity setting of AF-272.
- The parameters may be complex and repeated; no positivity, Ramanujan bound, self-duality, or functional equation is used.
- The result is exact, not numerically stable. Near-colliding parameter multisets can make inversion from noisy power sums ill-conditioned even though exact Newton reconstruction remains valid.
- The depth `d` is sharp over the full degree-`d` class, but extra structure can reduce it. Degree one needs one coefficient; special self-dual or determinant-normalized subclasses may need fewer independent coordinates than their raw degree suggests.
- The global statement requires checking the finite-depth data at every prime. It does not turn infinitely many local factors into finitely many observations.
- The theorem does not prove that a candidate spectral, zero, determinant, or positivity compression retains bounded local Euler degree. Treating that source-category membership as automatically preserved would simply assume the missing information.
- The Riemann-zeta application is a category audit, not an RH implication.

## Consequence for the research line

The source-side obstruction after AF-273 splits into two independent questions rather than one generic demand for “more coefficients.”

First, **prime-power depth** is controlled sharply by local Euler degree: degree `d` needs at most `d` exact source moments, and this is optimal in the unrestricted class. Second, **prime breadth** remains unbounded: a finite set of inspected primes cannot determine the global Euler source without an additional cross-prime theorem.

The next useful audit should therefore ask which RH-facing transformations preserve or independently force a bounded normalized local Euler-factor category. If such membership survives, AF-273's unbounded-depth escape is unavailable and attention should shift to prime breadth and to the stability of local reconstruction. If it does not survive, frequency support and reflection symmetry alone remain too weak, exactly as AF-273 demonstrates.