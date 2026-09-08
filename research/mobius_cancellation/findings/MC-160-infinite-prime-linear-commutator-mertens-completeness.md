# MC-160 — Absolutely summable infinite-prime linear commutator readouts are zero or Mertens-complete

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical prime commutators from `MC-156`–`MC-159`,

\[
B_p\varepsilon_n=b_p(n)\varepsilon_n,
\qquad
b_p(n)=\mu(pn)-\mu(n).
\tag{1}
\]

`MC-159` proves that every **finite-prime** scalarization either deletes Möbius orientation or remains exactly Mertens-complete across multiplicative scales. The most immediate infinite-prime escape is to place the whole prime row in a standard Banach sequence space and apply a bounded linear functional.

That escape also collapses.

Let

\[
a=(a_p)_{p\in\mathbb P}\in \ell^1(\mathbb P)
\tag{2}
\]

and define the absolutely convergent scalar readout

\[
c_a(n):=\sum_p a_p b_p(n),
\qquad
T_a(x):=\sum_{n\le x}c_a(n).
\tag{3}
\]

Write

\[
A:=\sum_p a_p.
\tag{4}
\]

Then for every real `x>=0`,

\[
\boxed{
T_a(x)
=-2A\,M(x)
-\sum_p a_p\sum_{j\ge1}M(x/p^j).
}
\tag{5}
\]

The inner sum is pointwise finite, and only primes `p<=x` contribute to the second term.

Consequently there is an exact dichotomy.

1. If `a_p=0` for every prime, then `c_a` and `T_a` vanish identically.
2. If `a` is nonzero, the scale family `T_a` reconstructs the entire Mertens function exactly by a triangular recursion.

If `A!=0`, equation `(5)` gives

\[
\boxed{
M(x)
=-\frac1{2A}
\left[
T_a(x)+\sum_p a_p\sum_{j\ge1}M(x/p^j)
\right],
}
\tag{6}
\]

and every Mertens argument on the right is strictly smaller than `x`.

If `A=0`, let `q` be the least prime with `a_q!=0`. Evaluating `(5)` at `qx` isolates

\[
\boxed{
M(x)
=-\frac1{a_q}
\left[
T_a(qx)
+\sum_{\substack{p,j\ge1\\(p,j)\ne(q,1)}}
a_p M(qx/p^j)
\right].
}
\tag{7}
\]

Every remaining active Mertens argument is again strictly smaller than `x`: coefficients at primes below `q` vanish by minimality, the terms `(q,j)` with `j>=2` have argument `x/q^{j-1}`, and every `p>q` gives `qx/p^j<x`.

Thus a nonzero absolutely summable infinite-prime **signed linear** readout is not a new intermediate cancellation statistic. Even when its total coefficient `A` is tuned to zero so that the direct `M(x)` component in `(5)` disappears, its least active prime exposes a shifted triangular copy of `M`.

This closes the bounded-linear part of the infinite-prime topology escape left open by `MC-159`. In particular, let `1<=r<infinity`, choose a row weight `w=(w_p)\in\ell^r(\mathbb P)`, and form

\[
R_w(n):=(w_p b_p(n))_p\in\ell^r.
\tag{8}
\]

For any bounded linear functional `Lambda` on `ell^r`, duality gives coefficients `lambda_p` with

\[
a_p=\lambda_p w_p\in\ell^1
\tag{9}
\]

by Hölder (with `lambda\in\ell^infinity` when `r=1`). Therefore every bounded linear scalarization `Lambda(R_w(n))` falls under `(2)`–`(7)`: its effective coefficient sequence is either zero or Mertens-complete.

The result does **not** close nonlinear infinite-prime observables, nonseparable `ell^infinity` duals, genuinely noncommutative relations between prime directions, or state-to-state/order information. It says that passing from finite joint scalarization to a standard weighted `ell^r` completion does not by itself create a useful lossy middle layer if the final readout is bounded and linear.

## 1. Pointwise prime commutators have only one signed degree of freedom

For every prime `p`, `MC-156` gives

\[
b_p(n)=
\begin{cases}
0,&\mu(n)=0,\\
-2\mu(n),&\mu(n)\ne0\text{ and }p\nmid n,\\
-\mu(n),&\mu(n)\ne0\text{ and }p\mid n.
\end{cases}
\tag{10}
\]

Equivalently, on squarefree `n`,

\[
\boxed{
b_p(n)=-\mu(n)\bigl(2-\mathbf 1_{p\mid n}\bigr).}
\tag{11}
\]

Since `|b_p(n)|<=2`, condition `(2)` makes `(3)` absolutely convergent uniformly in `n`. Summing `(11)` over `p` gives the pointwise formula

\[
\boxed{
c_a(n)
=-\mu(n)\left(2A-\sum_{p\mid n}a_p\right),}
\tag{12}
\]

with `c_a(n)=0` on nonsquarefree integers.

This already shows why setting `A=0` does not remove all orientation. It only cancels the common `-2mu(n)` component across prime directions; the residual still couples `mu(n)` to the finitely many active coefficients attached to prime divisors of each individual integer.

## 2. The cumulative transform is an exact infinite-prime dilation identity

Fix a prime `p` and define

\[
A_p(x):=\sum_{\substack{n\le x\\p\mid n}}\mu(n).
\tag{13}
\]

Writing `n=pm` on the squarefree support gives the recursion

\[
A_p(x)=-M(x/p)+A_p(x/p).
\tag{14}
\]

Iteration terminates pointwise and yields

\[
\boxed{A_p(x)=-\sum_{j\ge1}M(x/p^j).}
\tag{15}
\]

Now

\[
\sum_{n\le x}\mu(pn)
=-\sum_{\substack{n\le x\\p\nmid n}}\mu(n)
=-M(x)+A_p(x),
\tag{16}
\]

so

\[
\boxed{
\sum_{n\le x}b_p(n)
=-2M(x)-\sum_{j\ge1}M(x/p^j).
}
\tag{17}
\]

Multiply `(17)` by `a_p` and sum over primes. The `M(x)` terms sum to `-2AM(x)`. For the lower-scale term, primes `p>x` contribute nothing because `x/p<1`; hence that part is a finite prime sum at every fixed `x`. This proves `(5)` without analytic continuation, Perron inversion, zero-free information, or an infinite rearrangement problem.

## 3. Nonzero coefficient sequences have a triangular Mertens decoder

Suppose first that `A!=0`. Equation `(6)` expresses `M(x)` in terms of `T_a(x)` and values `M(x/p^j)` at strictly smaller arguments. Starting from `M(t)=0` for `0<=t<1`, induction on `floor(x)` reconstructs every Mertens value exactly.

The tuned case `A=0` is more revealing. Because the primes are well ordered and `a` is nonzero, there is a least active prime `q`. At the enlarged endpoint `qx`, the `(q,1)` term in `(5)` is exactly `-a_qM(x)`. Every other term is lower-scale for the reasons stated before `(7)`, so `(7)` is again triangular.

Thus cancellation of the total coefficient does not create a nontrivial kernel. It changes only where the leading copy of `M` is exposed: from the same endpoint `x` to the fixed dilated endpoint `qx`.

For finite data this has a precise cost. If `A!=0`, knowledge of `T_a` through height `X` reconstructs `M` through height `X`. If `A=0`, knowledge of `T_a` through height `qX` reconstructs `M` through height `X`. The scale enlargement is fixed by the least active prime and does not grow with `X`.

## 4. Exact reconstruction is not automatically exponent-stable

As in `MC-158`–`MC-159`, exact target completeness is an information statement, not an automatic RH-scale norm equivalence. The triangular inverse can amplify errors or power bounds.

For `theta>0` and `A!=0`, a simple sufficient contraction condition is

\[
\boxed{
\eta_\theta(a)
:=\frac1{2|A|}
\sum_p\frac{|a_p|}{p^\theta-1}<1.
}
\tag{18}
\]

Under `(18)`, a bound

\[
T_a(x)=O(x^\theta)
\tag{19}
\]

implies

\[
M(x)=O(x^\theta).
\tag{20}
\]

Indeed, inserting an inductive `C y^theta` bound into `(6)` multiplies the lower-scale constant by exactly `eta_theta(a)`, since

\[
\sum_{j\ge1}p^{-j\theta}=\frac1{p^\theta-1}.
\tag{21}
\]

When `A=0` and `q` is the least active prime, the analogous sufficient contraction factor obtained from `(7)` is

\[
\boxed{
\eta_{\theta,q}(a)
:=\frac1{|a_q|}
\left[
\frac{|a_q|}{q^\theta-1}
+q^\theta\sum_{p>q}\frac{|a_p|}{p^\theta-1}
\right]<1.
}
\tag{22}
\]

Again this is only a sufficient stability condition, not a necessary one. Failure of `(18)` or `(22)` does not prove exponent transfer impossible; it means the elementary absolute-value recursion does not supply it.

This distinction matters for the line's objective. A bounded linear infinite-prime observable may have attractive norm or summability properties while still being either exactly target-complete or badly conditioned as a route to power cancellation. Neither feature by itself supplies an independently cheaper bridge to the RH scale.

## 5. Standard Banach row completions do not create a linear middle layer

Let `1<=r<infinity` and `w\in\ell^r`. Because `|b_p(n)|<=2`, the weighted row `(8)` lies in `ell^r` for every integer state. If `1<r<infinity`, every bounded linear functional has a coefficient sequence `lambda\in\ell^{r'}`; for `r=1`, it has `lambda\in\ell^infinity`. In both cases Hölder gives

\[
\sum_p|\lambda_pw_p|<\infty.
\tag{23}
\]

Thus

\[
\Lambda(R_w(n))
=\sum_p\lambda_pw_pb_p(n)
=c_a(n)
\tag{24}
\]

with `a\in\ell^1`, and the dichotomy applies.

This is the exact topology-level consequence missing from the finite theorem `MC-159`: the usual separable `ell^r` completions can make the infinite prime row mathematically well defined, but **bounded linear observation of that row still has no intermediate information class**. Topological completion alone does not evade the finite-joint target-leakage obstruction.

The same proof also applies to a `c_0` row followed by a bounded linear functional, because `c_0^*=ell^1` and the resulting effective coefficients are absolutely summable. It deliberately does not assert the same for arbitrary bounded functionals on `ell^infinity`, whose dual is larger than `ell^1` and can contain non-coordinate functionals.

## 6. Prior-art and novelty audit

The Bost–Connes semigroup setting, its canonical isometries, and the earlier diagonal/non-diagonal boundary are already audited in `MC-138` and the upstream `prime_lattice` finding `PL-211`. `MC-156`–`MC-159` derive the exact prime-commutator alphabet and the finite scalarization barriers used here. This finding does not claim novelty for Bost–Connes theory, Möbius identities, Banach-space duality, or prime-dilation recursions.

A targeted literature search around Bost–Connes prime semigroup commutators, Möbius commutator operators, weighted prime-dilation readouts, and Mertens reconstruction did not locate an established theorem matching equations `(5)`–`(7)` or the bounded `ell^r` scalarization consequence. Nearby literature concerns the Bost–Connes KMS/adelic structure, twisted spectral triples, or Möbius functions of unrelated semigroup posets rather than this specific scalarization problem.

The closest primary Bost–Connes reference already used by the line is Sergey Neshveyev, *Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem*, Proceedings of the American Mathematical Society **130** (2002), 2999–3003, DOI `10.1090/S0002-9939-02-06449-3`, arXiv `math/0002141`. It supplies established system structure, not the present reconstruction theorem.

Accordingly `(5)`–`(7)` and the standard Banach-row consequence are recorded as exact derivations internal to the present Mathia construction with **no external novelty claim**.

## Boundaries and falsification tests

- Absolute summability of the effective coefficient sequence is essential to the stated infinite-prime scalarization theorem. The standard weighted `ell^r`, `1<=r<infinity`, and `c_0` cases imply it automatically after bounded linear observation; arbitrary `ell^infinity` dual functionals are outside scope.
- The result is specifically about **linear signed** scalarizations. Nonlinear continuous maps of an infinite row, noncommutative products, joint distributions, or relational observables are not reduced to `(3)` by this argument.
- Exact reconstruction uses the full natural scale family of `T_a`. In the zero-total case it requires a fixed endpoint dilation by the least active prime `q`.
- Target completeness is not the same as stable power-scale equivalence. Conditions `(18)` and `(22)` are sufficient only and may fail even though exact reconstruction remains valid.
- The argument does not use, prove, or assume an RH-scale estimate for `M`; no contour shift, analytic continuation of `1/zeta`, or zero-free region enters.
- If an apparent infinite-prime construction uses a bounded linear readout but claims to retain only a cheaper fragment of Möbius orientation, its effective coefficients should be computed. If they are absolutely summable and nonzero, equations `(6)` or `(7)` expose the hidden full Mertens channel.

## Consequence for the line

The finite-prime scalarization obstruction of `MC-159` survives the most natural infinite completion: a standard weighted prime row in `ell^r` or `c_0` followed by bounded linear observation. Such a readout is either identically zero or reconstructs `M` exactly across scale, with exponent transfer requiring a separate conditioning theorem.

A surviving infinite-prime Bost–Connes/semigroup route must therefore exploit structure not captured by absolutely summable signed linear coefficients — for example a genuinely nonlinear infinite-prime observable with source-forced regularity, a non-coordinate `ell^infinity`-type functional justified intrinsically rather than chosen ad hoc, noncommutative relational data, or state/order information — and must still demonstrate a cheaper transfer to global Möbius cancellation rather than another encoding of the target.