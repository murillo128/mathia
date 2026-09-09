# MC-161 — Tail-centered prime commutator charge is Mertens-complete but power-unstable

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state prime commutator from `MC-156`–`MC-160`,

\[
b_p(n)=\mu(pn)-\mu(n)
      =-2\mu(n)+\mu(n)\mathbf 1_{p\mid n}.
\tag{1}
\]

For every fixed integer `n`, the prime row `p\mapsto b_p(n)` is eventually constant. Its canonical tail-centered representative is

\[
\tau(n):=\lim_{p\to\infty}b_p(n)=-2\mu(n),
\qquad
d_p(n):=b_p(n)-\tau(n)=\mu(n)\mathbf 1_{p\mid n}.
\tag{2}
\]

Thus the raw row lies in

\[
\mathbb C\mathbf 1\oplus c_{00}(\mathcal P),
\]

and quotienting by the constant prime direction identifies its class canonically with `d(n)\in c_{00}(\mathcal P)`.

This quotient does **not** create a linear information middle layer. Every algebraic linear functional on `c_{00}(\mathcal P)` is specified by an arbitrary prime-weight sequence `w=(w_p)` through

\[
f_w(n):=\sum_p w_p d_p(n)
       =\mu(n)\sum_{p\mid n}w_p,
\tag{3}
\]

where the sum is finite for each `n`; no `\ell^1` or boundedness hypothesis on `w` is required. If `w` is nonzero and `q` is the least prime with `w_q\ne0`, then the full summatory scale family

\[
F_w(x):=\sum_{n\le x}f_w(n)
\tag{4}
\]

reconstructs the Mertens function exactly by a lower-triangular recursion. Hence **every nonzero algebraic linear reading of the canonical tail quotient is Mertens-complete across scales**.

The most natural nonsummable calibration, `w_p\equiv1`, is nevertheless independently tractable:

\[
f_1(n)=\mu(n)\omega(n),
\qquad
F_1(x)=M_\omega(x):=\sum_{n\le x}\mu(n)\omega(n),
\tag{5}
\]

and established Selberg–Delange theory gives

\[
M_\omega(x)=\frac{x}{\log^2x}+O\!\left(\frac{x}{\log^3x}\right).
\tag{6}
\]

This is a useful counterexample to a tempting inference from exact invertibility: the coefficient transform `(5)` is pointwise Möbius-complete for `n\ge2`, since

\[
\mu(n)=\operatorname{sgn}(\mu(n)\omega(n)),
\tag{7}
\]

but its cumulative statistic has an unconditional deterministic drift of order `x/log^2 x`.

The reason this independent source estimate does not improve Mertens cancellation is quantitative conditioning. The exact triangular inverse for `w_p\equiv1` has a prime-power tail whose absolute power-weight mass diverges for every exponent `0<\theta\le1`. In particular, it cannot be a uniform contraction at the RH scale. This supplies a concrete answer to the accepted decoder-stability clue: **independent source tractability and exact recovery can coexist while power-scale transfer fails completely**.

## 1. The eventual-tail quotient is canonical on the actual commutator rows

Equation `(1)` follows from the three Möbius cases already audited in `MC-149` and used in `MC-156`: if `n` is not squarefree both terms vanish; if `n` is squarefree and `p\nmid n`, then `\mu(pn)=-\mu(n)`; and if `p\mid n`, then `\mu(pn)=0`.

For fixed `n`, only finitely many primes divide `n`. Therefore `b_p(n)=-2\mu(n)` for every sufficiently large prime `p`, proving `(2)`. The centered row is finitely supported exactly on the prime divisors of a squarefree `n` and vanishes identically when `\mu(n)=0`.

Let

\[
E=\mathbb C\mathbf 1\oplus c_{00}(\mathcal P).
\]

Every actual row `b(n)` belongs to `E`. The quotient `E/\mathbb C\mathbf1` has the canonical representative obtained by subtracting the eventual constant, so it is naturally identified with `c_{00}(\mathcal P)`. Its algebraic dual consists of arbitrary coordinate weights `w_p`, because every vector in `c_{00}` has finite support. Hence `(3)` classifies **all algebraic linear scalarizations of this tail-centered quotient**, not only continuous or absolutely summable ones.

This is a different object from `MC-160`. There the raw uncentered row was summed against `a\in\ell^1(\mathcal P)` so that the infinite constant tail was absolutely summable. Here the constant direction is first quotiented out; after that renormalization, arbitrary prime weights are algebraically legitimate on each actual row.

## 2. Every nonzero centered linear reading has an exact prime-power decoder

For a prime-weight sequence `w`, define the arithmetic kernel

\[
\kappa_w(m)=
\begin{cases}
w_p,&m=p^j\text{ for a prime }p\text{ and }j\ge1,\\
0,&\text{otherwise}.
\end{cases}
\tag{8}
\]

Then

\[
\boxed{\quad f_w=-\kappa_w*\mu.\quad}
\tag{9}
\]

It is enough to verify one prime direction. For fixed `p`,

\[
-\sum_{j\ge1,\ p^j\mid n}\mu(n/p^j)
=\mu(n)\mathbf1_{p\mid n}.
\tag{10}
\]

If `v_p(n)=1`, only the `j=1` term can be nonzero after squarefree support is enforced, and it equals `-\mu(n/p)=\mu(n)`. If `v_p(n)\ge2`, the only potentially nonzero final two terms cancel; if the complementary factor is itself nonsquarefree, both sides are zero. Summing `(10)` with weights `w_p` gives `(9)`.

Summing `(9)` up to `x` and changing the finite order of summation gives

\[
\boxed{
F_w(x)
=-\sum_p w_p\sum_{j\ge1}M(x/p^j),
}
\tag{11}
\]

where terms with `p^j>x` vanish.

Now let `q` be the least prime with `w_q\ne0`. Evaluating `(11)` at `qx` and isolating `(p,j)=(q,1)` yields

\[
\boxed{
M(x)
=-\frac{F_w(qx)}{w_q}
-\sum_{j\ge2}M(x/q^{j-1})
-\sum_{p>q}\frac{w_p}{w_q}\sum_{j\ge1}M(qx/p^j).
}
\tag{12}
\]

Every Mertens argument on the right after the source term is strictly below `x`. At every fixed `x` the sums are finite. Together with the trivial base values below the first integer, `(12)` is an exact lower-triangular reconstruction of `M` from the scale family `F_w`.

Thus tail-centering removes the blatant constant-row copy `\tau(n)=-2\mu(n)`, but **any nonzero linear functional on what remains still determines Mertens across scales**.

## 3. The unit charge is exactly the classical `mu omega` transform

For `w_p=1`, equation `(3)` becomes `(5)`. Equation `(9)` specializes to

\[
\mu(n)\omega(n)=-(\chi_{\mathcal P^*}*\mu)(n),
\tag{13}
\]

where `\chi_{\mathcal P^*}` is the indicator of positive prime powers. Hence

\[
\boxed{
M_\omega(x)
=-\sum_{p^j\le x}M(x/p^j).
}
\tag{14}
\]

This identity is established prior art. Alladi and Johnson derive the same prime-power convolution in equations (2.9)–(2.10) of *Duality between prime factors and the prime number theorem for arithmetic progressions—II*, The Ramanujan Journal 69 (2026), article 52, DOI `10.1007/s11139-026-01325-5` (preprint `arXiv:2410.18259`). Their Section 3 records the Selberg–Delange evaluation, credited there to Tenenbaum,

\[
M_\omega(x)
=x\sum_{0\le k\le N}\frac{\lambda_k}{\log^{k+2}x}
+O\!\left(xR_{N+2}(x)\right),
\qquad \lambda_0=1,
\tag{15}
\]

and in particular `(6)`.

Therefore neither `mu(n)omega(n)`, the prime-power convolution `(13)`, nor the asymptotic `(6)` is a Mathia novelty. The line-level derived content is the exact identification of this classical transform with the **unweighted algebraic charge of the tail-centered prime-commutator quotient**, together with the decoder-conditioning audit below.

The arithmetic estimate `(6)` is genuinely independent of an RH-scale Mertens hypothesis: it is an unconditional Selberg–Delange/PNT-level result. Yet it is not a cancellation estimate of the desired type. It proves that `M_\omega(x)` itself has growth exponent `1`, with a positive leading term.

## 4. Exact invertibility does not imply power-scale stability

For a generic weight sequence, an absolute induction based on `(12)` at exponent `\theta>0` would require control of

\[
\eta_{\theta,q}(w)
=
\frac{1}{|w_q|}
\left[
\frac{|w_q|}{q^\theta-1}
+q^\theta\sum_{p>q}\frac{|w_p|}{p^\theta-1}
\right].
\tag{16}
\]

When this quantity is finite and `<1`, the usual weighted-sup induction gives a sufficient exponent-stability criterion, exactly analogous to the `A=0` contraction in `MC-160`. The importance here is that after tail-centering the weights need not be in `\ell^1`, so `(16)` can fail by an infinite-prime tail even though every finite coefficient `f_w(n)` is perfectly well-defined.

For the unit charge, `q=2` and

\[
\eta_{\theta,2}(1)
=
\frac{1}{2^\theta-1}
+2^\theta\sum_{p>2}\frac{1}{p^\theta-1}.
\tag{17}
\]

The prime sum diverges for every `0<\theta\le1`: since `p^\theta-1\le p^\theta`, each term is at least `p^{-\theta}\ge p^{-1}`, and Euler's reciprocal-prime sum diverges. Thus no absolute power-norm contraction of this decoder is available anywhere in the sublinear range, including `\theta=1/2+\varepsilon`.

This is not merely a defect of the particular induction. The forward prime-power operator

\[
(KG)(x)=\sum_{p^j\le x}G(x/p^j)
\tag{18}
\]

is itself unbounded on the generic weighted sup space `\|G\|_\theta=\sup_{x\ge1}x^{-\theta}|G(x)|` for `0<\theta\le1`: the positive test function `G(x)=x^\theta` gives

\[
x^{-\theta}(KG)(x)
=\sum_{p^j\le x}p^{-j\theta}\to\infty.
\tag{19}
\]

Any target-range stability for the **actual** Möbius recursion would therefore have to use signed arithmetic relations among the lower-scale Mertens values, not a generic norm bound on them.

For `w=1`, the exact decoder is especially transparent:

\[
\boxed{
M(x)
=-M_\omega(2x)
-\sum_{\substack{p^j\le2x\\p^j\ge3}}M(2x/p^j).
}
\tag{20}
\]

The independently known source term is of order `x/log^2x`, much larger than any `x^\theta` with fixed `\theta<1`. Recovering a small `M(x)` from `(20)` consequently requires a large cancellation between that source term and the many lower-scale prime-power terms. The easy asymptotic `(6)` has not removed the Mertens difficulty; it has moved that difficulty into the inverse tail.

## 5. Pointwise completeness and cumulative tractability coexist

The unit charge also gives a useful fidelity calibration. For every `n\ge2`,

\[
\omega(n)>0\quad\text{whenever}\quad\mu(n)\ne0,
\]

so `(7)` holds; `\mu(1)=1` is fixed separately. Thus the complete coefficient sequence `f_1(n)=\mu(n)\omega(n)` contains the exact Möbius sequence by a trivial nonlinear sign decoder.

At the same time, its ordinary cumulative sum has the unconditional asymptotic `(6)`. There is no contradiction: nonlinear pointwise decoding does not commute with summation, and the prime-factor-count magnitude `\omega(n)` creates a deterministic aggregate drift.

This is a concrete example inside the actual arithmetic source where all three statements are simultaneously true:

1. the transformed coefficients determine Möbius exactly;
2. the transformed cumulative statistic admits an independent classical asymptotic;
3. that asymptotic gives no stable sublinear bound on the Mertens cumulative statistic.

It therefore sharpens the distinction in the accepted decoder-stability clue between **algebraic recovery**, **source tractability**, and **quantitative recovery stability**.

## Prior art and novelty assessment

The Möbius/prime-factor transform `\mu\omega`, its prime-power convolution, and its Selberg–Delange asymptotics are established analytic-number-theory prior art. The closest direct source located is Alladi–Johnson (2026), whose equations (2.9)–(2.10) give `(13)` and whose Section 3 records `(15)` with leading coefficient one. Their discussion explicitly contrasts the eventually one-signed `M_\omega(x)\asymp x/log^2x` behavior with the oscillatory Mertens function.

A targeted literature search for the same object in Bost–Connes/semigroup commutator language did not locate the tail-centered quotient identification above. No novelty is inferred from that absence. Equations `(2)`–`(12)` are elementary consequences of the already established Mathia commutator coefficient law plus classical Möbius inversion, and are recorded as exact line-level structure with **no novelty claim**.

## Boundaries and falsification tests

- **The quotient domain is restricted.** Tail-centering is canonical because the actual rows are eventually constant. This does not define a canonical quotient representative for an arbitrary element of `\ell^\infty(\mathcal P)` and does not classify arbitrary Banach-limit or singular dual functionals on the full raw row space.
- **The dual is algebraic, not topological.** Arbitrary weights act on `c_{00}` because every centered row has finite support. A weight sequence need not define a bounded functional on a chosen completion.
- **Mertens completeness is across scales.** A single number `F_w(x)` does not determine `M(x)`. Equation `(12)` reconstructs recursively from the full scale family.
- **Exact recovery is not declared circular.** A transform can be useful despite being invertible. The obstruction for `w=1` is quantitative: its independent source estimate has exponent one and its absolute inverse tail is nonsummable throughout the sublinear power range.
- **General weights remain a live analytic question.** Some nonzero `w` can satisfy a finite or even contractive version of `(16)` at a chosen exponent. Such a weight would still need an independently proved bound for the actual `F_w`; this finding does not rule that out.
- **Signed inverse-tail control remains open.** Divergence of `(17)` rules out generic absolute-norm contraction. It does not prove that Möbius-specific cancellation among the lower-scale terms in `(12)` is impossible.
- **Nonlinear/noncommutative quotients remain open.** The theorem classifies linear functionals on the canonical `c_{00}` tail quotient only.
- **The arithmetic formulas are directly falsifiable.** Any `n,p` violating `(2)`, any finite `x` violating `(11)`, or any nonzero weight family for which `(12)` fails would refute the exact part. The unit-weight formulas can additionally be checked against the established `mu omega` convolution literature.

## Consequence for the line

`MC-160` left open non-`\ell^1` prime-coordinate readouts because the raw commutator has a nonzero constant tail. Tail-centering is the most literal renormalization of that obstruction. The present result shows that **its entire algebraic linear dual remains Mertens-complete**, so merely permitting nonsummable or unbounded coordinate weights does not create a new information class.

The unit charge is nevertheless informative because it supplies the first explicit source-side calibration in this commutator family: `M_\omega(x)` is independently estimable, but exactly where that gain appears, the inverse has a nonsummable prime-power tail and the source statistic has exponent one. The next useful scalar candidate must therefore satisfy two obligations simultaneously: an independently proved power-scale estimate for one fixed transformed input, and an inverse-tail estimate that remains controlled near the target exponent. Satisfying only one of those obligations is not enough.