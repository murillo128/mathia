# FD-110 — least-prime-factor order remains a commuting rough-sieve filtration

**Status:** `EXACT-DERIVED + PHYSICAL-COEFFICIENT-LAW + LEAST-PRIME-FACTOR-PARTITION + BOOLEAN-INCIDENCE-CLASSIFICATION + COMMUTING-ROUGH-SIEVE-RESOLVENT + POSITIVE-DILATION-EXPANSION + SOURCE-RICH-CUTOFF-PRESERVED + NEGATIVE/ROUTE-RESTRICTION`.

`FD-109` shows that simultaneous divisibility by any fixed prime set is only a commuting product of one-prime resolvents, but deliberately leaves **least-prime-factor order** as a possible way to escape that flat incidence algebra. The ordered partition is worth testing because it is not a single simultaneous-divisibility condition: the packet with least prime `p` requires divisibility by `p` together with exclusion of every smaller prime, so it carries a growing prime-prefix order.

For the physical coefficient law

\[
a(n):=\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\tag{1}
\]

that escape does **not** occur at the level of linear coefficient statistics. The exclusion signs cancel against the physical prime signs, and the least-prime-factor hierarchy becomes a nested positive rough-sieve transform built from the same commuting dilation resolvents as `FD-109`.

Let

\[
(T_rF)(X):=F\!\left(\left\lfloor\frac Xr\right\rfloor\right),
\qquad
R_p:=T_p(I-T_p)^{-1}
=\sum_{j\ge1}T_{p^j},
\tag{2}
\]

where the geometric series is finite on every fixed horizon because repeated floor dilation eventually reaches zero. Define

\[
A_p:=I+(1-p^{-1})R_p
=(I-p^{-1}T_p)(I-T_p)^{-1}.
\tag{3}
\]

For a prime `p`, write

\[
B_p(X):=
\sum_{\substack{n\le X\\q\nmid n\ \forall q<p}}a(n),
\tag{4}
\]

for the physical source restricted to integers with no prime factor below `p`, and

\[
L_p(X):=
\sum_{\substack{n\le X\\P^-(n)=p}}a(n)
\tag{5}
\]

for the least-prime-factor packet. Then exactly

\[
\boxed{
B_p=
\left(\prod_{q<p}A_q\right)\mathcal H,}
\tag{6}
\]

and, if `p^+` is the next prime,

\[
\boxed{
L_p=B_p-B_{p^+}
=a(p)R_pB_p
=a(p)R_p
\left(\prod_{q<p}A_q\right)\mathcal H.}
\tag{7}
\]

All factors commute. More strongly, every `A_q` has a **positive** dilation expansion,

\[
A_q
=I+(1-q^{-1})\sum_{j\ge1}T_{q^j}.
\tag{8}
\]

Thus the alternating inclusion--exclusion needed to exclude the smaller primes leaves no signed or noncommutative exterior defect after the physical coefficient law is inserted.

Expanding (7) gives the exact ordered source formula

\[
\boxed{
L_p(X)
=a(p)
\sum_{\substack{r\ge1\\P^+(r)=p}}
\left(\prod_{\substack{q\mid r\\q<p}}(1-q^{-1})\right)
\mathcal H\!\left(\left\lfloor\frac Xr\right\rfloor\right).}
\tag{9}
\]

The weights inside the sum are nonnegative. The smallest dilation is `r=p`; every additional piece of least-prime-factor structure only moves to a **deeper** source argument `X/r`.

The same conclusion holds for every finite linear statistic built only from prime-divisibility labels. If `S` is a finite prime set, `x_p(n)=1_(p|n)`, and `F:{0,1}^S -> C`, write its unique multilinear expansion as

\[
F(x)=\sum_{T\subseteq S}c_T\prod_{p\in T}x_p.
\tag{10}
\]

Then `FD-109` gives

\[
\boxed{
\sum_{n\le X}a(n)F((x_p(n))_{p\in S})
=
\left[
\sum_{T\subseteq S}
c_Ta(q_T)
\prod_{p\in T}R_p
\right]\mathcal H(X),}
\tag{11}
\]

where `q_T=prod_(p in T)p`. Therefore exact support patterns, finite prime-prefix exclusions, and least-prime-factor labels are all polynomials in the **same commuting incidence resolvents**. They can still be useful when combined nonlinearly or across horizons, but linear prime-order bookkeeping alone does not leave the algebra isolated by `FD-109`.

## 1. Prime-prefix exclusion factorizes exactly

For a finite set `S` of primes, let

\[
D_S(X):=
\sum_{\substack{n\le X\\p\mid n\ \forall p\in S}}a(n).
\tag{12}
\]

`FD-109` proved

\[
D_S
=a(q_S)\prod_{p\in S}R_p\mathcal H,
\qquad
q_S:=\prod_{p\in S}p.
\tag{13}
\]

Let `P_<p=prod_(q<p)q`. Inclusion--exclusion for the condition `(n,P_<p)=1` gives

\[
B_p
=
\sum_{d\mid P_{<p}}
\mu(d)D_{\{q:q\mid d\}}.
\tag{14}
\]

For squarefree `d`, the physical coefficient is

\[
a(d)=\mu(d)\prod_{q\mid d}(1-q^{-1}),
\tag{15}
\]

so

\[
\mu(d)a(d)
=\prod_{q\mid d}(1-q^{-1})\ge0.
\tag{16}
\]

Substituting (13) into (14) and collecting the Boolean product therefore yields

\[
\begin{aligned}
B_p
&=
\sum_{d\mid P_{<p}}
\prod_{q\mid d}(1-q^{-1})R_q\,\mathcal H\\
&=
\prod_{q<p}\bigl[I+(1-q^{-1})R_q\bigr]\mathcal H,
\end{aligned}
\tag{17}
\]

which is (6). The alternating Möbius signs from exclusion have disappeared exactly; this is not an estimate or an average cancellation.

The factor identity in (3) follows from

\[
I+(1-q^{-1})T_q(I-T_q)^{-1}
=(I-q^{-1}T_q)(I-T_q)^{-1}.
\tag{18}
\]

Since all `T_q` commute, all `R_q` and `A_q` commute. On the finite horizon vector with `F(0)=0`, each `T_q` is strictly lower-scale and nilpotent under iteration, so every factor in (3) is triangularly invertible. Thus `B_p` is a lossless finite-horizon reparametrization of the same scalar source `mathcal H`; the prime ordering enters only through **which commuting factors have already been included**.

## 2. Least-prime packets telescope through the rough filtration

If `p^+` is the next prime, the integers counted by `B_p` but not by `B_(p^+)` are exactly those whose least prime factor is `p`. Hence

\[
L_p=B_p-B_{p^+}.
\tag{19}
\]

Using `B_(p^+)=A_pB_p`,

\[
L_p
=(I-A_p)B_p
=-(1-p^{-1})R_pB_p.
\tag{20}
\]

But `a(p)=-(1-p^{-1})`, proving (7). Expanding `R_p` and every `A_q` gives one exponent `>=1` at `p`, arbitrary nonnegative exponents at primes below `p`, and no prime above `p`. The dilation denominators are therefore exactly the integers `r` with largest prime factor `P^+(r)=p`, proving (9).

The weighted dilation mass is also explicit. If

\[
c_p(r):=
\prod_{\substack{q\mid r\\q<p}}(1-q^{-1})
\qquad(P^+(r)=p),
\tag{21}
\]

then

\[
\boxed{
\sum_{P^+(r)=p}\frac{c_p(r)}r
=
\frac1{p-1}
\prod_{q<p}\left(1+\frac1q\right).}
\tag{22}
\]

Indeed, the `p`-power contribution is `sum_(j>=1)p^(-j)=1/(p-1)`, while at a smaller prime `q` the absent/present alternatives contribute

\[
1+(1-q^{-1})\sum_{j\ge1}q^{-j}=1+q^{-1}.
\tag{23}
\]

Using only the trivial physical bound `|mathcal H(Y)|<=Y`, (9) therefore gives

\[
\boxed{
|L_p(X)|
\le
\frac Xp
\prod_{q<p}\left(1+\frac1q\right).}
\tag{24}
\]

Equation (22), rather than the bound (24), is the durable point: the ordered packet is an explicit positive mixture of deeper scalar-source samples, with no hidden cross-prime determinant.

There is an exact telescope across the whole prime ordering as well. For fixed `X`, once `p>X`, `B_p(X)=a(1)=1`; hence

\[
\mathcal H(X)-1
=\sum_{p\le X}L_p(X).
\tag{25}
\]

The least-prime-factor hierarchy is therefore a nested filtration of the original source, not an additional family of independent linear constraints.

## 3. The terminal source-rich cutoff is not extended by ordering

The line-specific question is whether the least-prime partition can beat the terminal source-depth obstruction of `FD-105`--`FD-109`. Write the terminal parent as `H=4X` and retain the adaptive source-rich cutoff

\[
L_H=\left\lfloor\frac{U_H}{H\log H}\right\rfloor,
\qquad
P_*(X)\asymp\frac X{L_H}.
\tag{26}
\]

A source sample `mathcal H(floor(X/r))` can lie above the cutoff only when

\[
r\lesssim P_*(X).
\tag{27}
\]

Every denominator in the exact least-prime expansion (9) satisfies `r>=p`. Consequently

\[
\boxed{
p>P_*(X)
\quad\Longrightarrow\quad
\text{every source sample occurring in }L_p(X)
\text{ lies below the adaptive source-rich cutoff}.}
\tag{28}
\]

When `p<=P_*`, the first possible denominator is precisely `r=p`; adjoining any smaller prime factor or increasing any exponent only increases `r` and descends to a smaller source argument. Thus least-prime order does not enlarge the one-prime source-rich range. It reorganizes the same leading sample together with increasingly deep tails.

The Boolean classification (11) gives the analogous statement for any finite prime-pattern statistic: a monomial supported on `T` reaches the source at product depth `X/q_T`. This is exactly the product budget already isolated in `FD-109`. Encoding order by a Boolean combination can change coefficients and can correlate many product depths, but it cannot turn those monomials into a Cartesian family of same-scale source-rich constraints.

On a sharp false-RH state, `FD-105`--`FD-109` give

\[
P_*(X)\le X^{2-2\Theta+o(1)},
\qquad \frac12<\Theta<1.
\tag{29}
\]

Equation (28) therefore leaves the power-critical terminal range unchanged. A successful use of least-prime-factor data has to exploit something beyond its **linear packet values**—for example a nonlinear interaction between different `L_p`, a cross-horizon persistence law, or a global amortization of the nested filtration.

## 4. Audit, prior-art boundary, and surviving target

The algebra has a decisive finite falsification test. Compute the rational coefficients (1), their cumulative source `mathcal H`, and compare the direct sums (4)--(5) against (6)--(9). An exact audit for all `X<=200` and `p in {2,3,5,7,11}` produced equality at every entry. The computation is not used as proof; any mismatch would instead expose an error in the operator factorization, while (14)--(20) prove it symbolically.

Least-prime-factor partitions, rough numbers, and Buchstab-type decompositions are classical sieve structure. In particular, weighted rough/smooth sums for arithmetic functions are treated in Debika Banerjee and Makoto Minamide, *On an analogue of Buchstab's identity*, Notes on Number Theory and Discrete Mathematics **22**(1) (2016), 8--17. No novelty is claimed for inclusion--exclusion, least-prime decomposition, or rough-number filtering themselves, and no theorem from that literature is used in the derivation above.

This finding is also distinct from `FD-029`. There the source is a squarefree sign relaxation and a growing exact prime-prefix ancestry law eventually recovers the Möbius signs pointwise. Here the source is already the fixed physical coefficient (1), prime powers remain present, and the question is what **linear ordered observables** the source permits. Equations (6)--(11) show that those observables remain inside the commuting cumulative incidence algebra of `FD-109`.

The conclusion has a strict boundary. It does **not** show that least-prime-factor organization is useless. The growing family `{L_p}` can still be combined nonlinearly before summation, compared across different horizons, inserted into the quadratic Jordan energy, or coupled to a refinement vector whose exterior defect is not a Boolean divisibility statistic. Nor does (11) control a nonlinear functional of an unbounded prime prefix merely because every finite truncation lies in the incidence algebra. Those are exactly the ways in which order could still matter.

What is closed is the simpler escape left by `FD-109`: **linear least-prime-factor ordering by itself does not manufacture noncommutative prime geometry or a new same-scale source-rich constraint.** Under the physical coefficient law it is an exact telescoping rough-sieve filtration with positive dilation coefficients and the same product-depth budget. The live terminal alternatives therefore narrow to nonlinear products before summation, cross-horizon/global source descent, or refinement geometry not reducible to prime-divisibility Boolean labels.

No external theorem is load-bearing in the derivation, so `SOURCES.md` requires no change.