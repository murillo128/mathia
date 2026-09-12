# MC-244 — The quadratic blind family collapses to one source projector, so positive blind dimension gives no exponent gain

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square smooth-dilation setup of `MC-233` and `MC-238`–`MC-243`. Let

\[
q:=Q_S=\prod_{r\in S}r^2,
\qquad
G=(\mathbb Z/q\mathbb Z)^\times,
\qquad
n:=|S|,
\]

and define the Legendre-sign map

\[
\lambda:G\longrightarrow\mathbb F_2^S,
\qquad
\lambda(a)_r
=
\frac{1-(\frac ar)}2.
\tag{1}
\]

Let

\[
W_y(S)
:=
\operatorname{span}_{\mathbb F_2}\{\lambda(p):p\le y\text{ prime}\},
\qquad
K_y(S):=W_y(S)^\perp.
\tag{2}
\]

Thus `K_y(S)` is exactly the quadratic smooth-dilation blind sector of `MC-238`. Write

\[
R:=\dim W_y(S),
\qquad
\kappa:=\dim K_y(S)=n-R.
\tag{3}
\]

For `v\in K_y(S)`, let

\[
\chi_v(a)=(-1)^{v\cdot\lambda(a)}
\qquad(a\in G),
\tag{4}
\]

and extend `chi_v` by zero off `G`, so `v=0` is the principal Dirichlet character modulo `q`.

Then the whole quadratic blind family has the exact projector identity

\[
\boxed{
\sum_{v\in K_y(S)}\chi_v(b)
=
2^\kappa\,
\mathbf 1_{\lambda(b)\in W_y(S)}
\qquad(b\in G).
}
\tag{5}
\]

Consequently, for any arithmetic function `f` with `|f|\le1`, any reduced residue `a mod q`, and

\[
S_f(N,\chi)
:=
\sum_{m\le N}f(m)\chi(m),
\]

the contribution of all quadratic blind characters to the ordinary character expansion of the progression `m\equiv a (mod q)` is

\[
\boxed{
\mathcal P_K(f;N,q,a)
:=
\frac1{\varphi(q)}
\sum_{v\in K_y(S)}
\overline{\chi_v(a)}S_f(N,\chi_v)
=
\frac{2^\kappa}{\varphi(q)}
\sum_{\substack{m\le N\\(m,q)=1\\
\lambda(a^{-1}m)\in W_y(S)}}
f(m).
}
\tag{6}
\]

The factor `2^kappa` in `(6)` does **not** turn a large blind sector into a larger worst-case obstruction. The map `lambda` is onto and every fiber has the same size. Hence

\[
\#\{a\in G:\lambda(a)\in W_y(S)\}
=
\frac{\varphi(q)}{2^\kappa}.
\tag{7}
\]

The mode count and source density therefore cancel exactly:

\[
\boxed{
|\mathcal P_K(f;N,q,a)|
\le
\frac Nq+1,
}
\tag{8}
\]

independently of every **positive** value of `kappa`. If the principal character is removed, then

\[
\boxed{
\left|
\frac1{\varphi(q)}
\sum_{0\ne v\in K_y(S)}
\overline{\chi_v(a)}S_f(N,\chi_v)
\right|
\le
2\left(\frac Nq+1\right),
}
\tag{9}
\]

while for `kappa=0` the nonprincipal blind contribution is exactly zero.

There is a stronger source-specific form for the exact smooth-inverse coordinate of `MC-233`. Put

\[
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and recall

\[
B_S(X)
=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu\!\left(
\frac Td;q,-Pd^{-1}\bmod q
\right).
\tag{10}
\]

Because every blind character is trivial on every `y`-smooth `d` and on `P`, the complete quadratic blind slice of `(10)` is not a sum of unrelated modes. It collapses to the single weighted source projector

\[
\boxed{
B_S^{(K)}(X)
=
\frac{2^\kappa}{\varphi(q)}
\sum_{\substack{m\le T\\(m,q)=1\\
\lambda(-m)\in W_y(S)}}
\mu(m)\,\Psi(T/m,y),
}
\tag{11}
\]

where

\[
\Psi(U,y)=\#\{d\le U:P^+(d)\le y\}.
\]

Taking absolute values only after this exact projection still gives a dimension-free support bound:

\[
\boxed{
|B_S^{(K)}(X)|
\ll
\frac Tq\log y+\Psi(T,y)
=
\frac{X^{1+o(1)}}q+X^{o(1)}.
}
\tag{12}
\]

At the active shell scaling

\[
q=X^{2\alpha+o(1)},
\]

this is only

\[
|B_S^{(K)}(X)|
\le X^{1-2\alpha+o(1)}.
\tag{13}
\]

Thus the blind-sector dimension does not move the existing support boundary. The target amplitude `X^{1/2+o(1)}` is reached by `(13)` only when

\[
\alpha\ge\frac14.
\tag{14}
\]

This sharply changes the live interpretation of `MC-243`. A theorem proving `kappa` small but still positive is useful structural information, but **dimension reduction alone is not a fixed-power source estimate**. To improve the hard region `alpha<1/4`, one must either prove `kappa=0` and eliminate the nonprincipal blind sector entirely, or prove genuinely signed cancellation of the Möbius-weighted projector `(11)` (or an equivalent source-coupling statement). No estimate for the full `B_S(X)`, `M(X)`, or the zeta zero set is proved here.

## 1. Subgroup orthogonality gives the exact blind projector

The map `(1)` is a group homomorphism because Legendre symbols multiply and multiplication of signs corresponds to addition in `F_2`. It is surjective: for every shell prime `r`, the quadratic character on `(Z/r^2Z)^*` takes both signs, and the Chinese remainder theorem lets the local signs be prescribed independently.

For `v\in K_y(S)`, equation `(4)` identifies the quadratic blind characters with the dual group of the quotient

\[
\mathbb F_2^S/W_y(S).
\]

For `z\in\mathbb F_2^S`, elementary finite-group orthogonality gives

\[
\sum_{v\in K_y(S)}(-1)^{v\cdot z}
=
\begin{cases}
2^\kappa,&z\in K_y(S)^\perp=W_y(S),\\
0,&z\notin W_y(S).
\end{cases}
\tag{15}
\]

which proves `(5)`.

For a reduced residue `a`, the standard Dirichlet-character identity

\[
\mathbf 1_{m\equiv a\, (q)}
=
\frac1{\varphi(q)}
\sum_{\chi\, (q)}
\overline{\chi(a)}\chi(m)
\qquad((m,q)=1)
\tag{16}
\]

lets us isolate the subfamily `chi_v`, interchange the finite sums, and apply `(5)` to `a^{-1}m`. This proves `(6)`.

The point is not merely that the blind characters can be diagonalized. Equation `(6)` gives their **inverse transform in the source variable**: together they are exactly an indicator of one affine family of Legendre-sign fibers.

## 2. Blind dimension cancels against fiber density exactly

Because `lambda` is onto, every sign vector in `F_2^S` has

\[
\frac{\varphi(q)}{2^n}
\]

preimages in `G`. Since `W_y(S)` has `2^R=2^{n-\kappa}` elements, its full preimage has

\[
2^{n-\kappa}\frac{\varphi(q)}{2^n}
=
\frac{\varphi(q)}{2^\kappa}
\]

residue classes, proving `(7)`.

Each reduced residue class modulo `q` contains at most `N/q+1` integers up to `N`. Applying this class count to `(6)` gives

\[
|\mathcal P_K|
\le
\frac{2^\kappa}{\varphi(q)}
\frac{\varphi(q)}{2^\kappa}
\left(\frac Nq+1\right),
\]

which is `(8)`.

This is the exact cancellation that a dimension-only argument misses. Shrinking the blind space from dimension `100` to dimension `1` multiplies the projector coefficient by `2^{-99}`, but simultaneously enlarges its source support by `2^{99}`. With no signed information about `f` inside those fibers, the two effects cancel.

For `(9)`, subtract the `v=0` principal contribution from `(6)`. The principal term is itself bounded by `N/q+1` after partitioning the units into reduced residue classes, so the triangle inequality gives the stated factor `2`. If `kappa=0`, there is no nonzero `v` and the nonprincipal blind slice vanishes exactly; this is qualitatively different from every positive dimension.

The conclusion is deliberately an `L^1`/worst-case statement. Dimension may still matter in combination with an independent `L^2` theorem, a coefficient-distribution theorem, or another arithmetic constraint. What fails is the inference `small positive blind dimension => fixed-power gain` without such additional source information.

## 3. The smooth-dilation family has one common source mask

For the residue in `(10)`,

\[
a_d=-Pd^{-1}\pmod q.
\]

Every prime factor of `P` and of a `y`-smooth `d` is at most `y`, so by definition of `W_y(S)`,

\[
\lambda(P),\lambda(d)\in W_y(S).
\tag{17}
\]

Equivalently every `v\in K_y(S)` satisfies

\[
\chi_v(P)=\chi_v(d)=1.
\tag{18}
\]

In the blind character contribution to `(10)`, therefore,

\[
\overline{\chi_v(a_d)}
=
\chi_v(-1)
\]

for every smooth dilation. Interchanging the `d`- and `m`-sums counts, for each `m`, exactly the smooth divisors `d\le T/m`, producing `Psi(T/m,y)`. The remaining character factor is `chi_v(-m)`. Applying `(5)` proves `(11)`.

Thus the changing residue `-Pd^{-1}` does not give the blind sector a changing source direction: after summing the blind family, **all smooth dilations see the same affine Legendre-sign projector**. This is the primal-space form of the blindness found in `MC-238`.

To prove `(12)`, first ignore the Möbius sign. The selected set in `(11)` is a union of exactly `phi(q)/2^kappa` reduced residue classes. For one selected class,

\[
\begin{aligned}
\sum_{\substack{m\le T\\m\equiv a\, (q)}}\Psi(T/m,y)
&=
\sum_{\substack{d\le T\\P^+(d)\le y}}
\#\left\{m\le T/d:m\equiv a\pmod q\right\}\\
&\le
\frac Tq
\sum_{\substack{d\le T\\P^+(d)\le y}}\frac1d
+
\Psi(T,y).
\end{aligned}
\tag{19}
\]

After multiplying by the number of selected classes and by `2^kappa/phi(q)`, the dimension cancels again. Finally,

\[
\sum_{P^+(d)\le y}\frac1d
=
\prod_{p\le y}(1-p^{-1})^{-1}
\ll\log y
\tag{20}
\]

by the classical Mertens product, while `MC-233` already gives `Psi(T,y)=X^{o(1)}` at `y=c log X`. This proves `(12)`.

## 4. Relation to `MC-243` and the live frontier

`MC-242` forces every nonzero blind vector to have support at least double-logarithmic size. `MC-243` then shows that this minimum-distance statement gives only coding-scale rank pressure and cannot by itself force `K_y(S)=0`. It leaves direct blind-dimension control and source coupling as two logically distinct next directions.

The present finding separates those directions more sharply. Suppose a future arithmetic theorem proves

\[
\dim K_y(S)=o(n)
\]

or even the much stronger bound

\[
\dim K_y(S)=1.
\]

As long as the dimension remains positive, `(8)` and `(12)` show that the naive absolute-value budget of the complete blind family remains at the same residue-support exponent. There is no factor `2^{-kappa}` left to spend after inversion to the source.

Accordingly, a useful rank theorem now has two qualitatively different outcomes:

- **full rank**, `kappa=0`, which eliminates every nonprincipal quadratic blind mode and genuinely closes this obstruction;
- **positive codimension**, however small, which still requires a signed theorem on the projected source set `(11)` before it can improve the `alpha=1/4` support boundary.

The other promising path is therefore no longer an unspecified estimate on many separate blind Fourier coefficients. It is the concrete source question exposed by `(11)`: can Möbius cancel with fixed power after restricting to the affine Legendre-sign condition

\[
\lambda(-m)\in W_y(S)
\]

and weighting by the smooth-divisor multiplicity `Psi(T/m,y)`? Any such theorem must be audited against the same parity, progression, and zero-free barriers already present in this line.

## 5. Prior art and novelty audit

The mathematical mechanisms behind `(5)`–`(7)` are classical. Character orthogonality on finite abelian groups, annihilator projectors, and Fourier inversion are standard finite harmonic analysis. The same representation-theoretic framework is already audited in `MC-190`, which uses character diagonalization to classify unit-group-equivariant quadratic statistics. The equal split of quadratic residues and nonresidues in each odd prime-power unit group and the Chinese remainder theorem are elementary classical facts.

No novelty is claimed for subgroup orthogonality, the annihilator identity, character expansion of arithmetic progressions, Mertens' product, or the CRT fiber count. A targeted prior-art audit found only these standard mechanisms; it did not identify a theorem that supplies signed cancellation for the exact source projector `(11)`.

The durable Mathia delta is the specialization to the `MC-233` smooth-dilation family after `MC-238`–`MC-243`: summing **all** quadratic blind modes gives one exact affine source projector, and the factor from blind-sector size cancels exactly against the projector's source density. This closes the idea that a merely quantitative reduction of positive blind dimension automatically buys a power of `X`, while exposing a sharper signed source-coupling target. That is a frontier reduction, not a new theorem of finite harmonic analysis.

## 6. Boundaries and decisive audit

- Equations `(5)`–`(8)` concern the quadratic blind subgroup `K_y(S)`. Higher-order blind characters from `MC-238` are not included and may require a different finite-group quotient.
- The conclusion about dimension is worst-case and absolute-value based. A theorem correlating the actual Möbius coefficients with the projector geometry could gain from dimension or rank in a way not visible to `(8)`.
- Equation `(11)` is the blind slice of the exact `MC-233` character expansion, not the whole `B_S(X)`. Nonblind characters remain and can contribute independently.
- The `Psi(T/m,y)` weight in `(11)` is source-forced by summing the smooth dilations. Replacing it by a constant, or discarding it without an error estimate, would change the problem.
- The exact class count `(7)` uses surjectivity of the joint Legendre-sign map on the full unit group modulo the shell-square modulus. It does not assert that the integers up to `N` are equidistributed among those classes; `(8)` uses only the trivial per-class count.
- The support boundary `(14)` is therefore not claimed optimal. It says only that **blind dimension itself**, without signed source information, cannot improve the existing exponent budget.
- Full rank `K_y(S)=0` remains genuinely decisive for the quadratic blind sector; the no-gain statement applies only while a nonprincipal blind character survives.

The decisive algebraic checks are finite: `K_y(S)=W_y(S)^perp`, the orthogonality sum `(15)`, CRT surjectivity/equal fibers of `lambda`, and the character expansion `(16)`. The decisive analytic boundary is equally explicit: any claimed fixed-power improvement for `alpha<1/4` must enter through cancellation in `(11)` or through information outside this quadratic blind projector, not through the cardinality `2^kappa` alone.
