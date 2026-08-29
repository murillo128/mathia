# PC-050 — cotangent refinement averaging is radical-invariant

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for extracting nontrivial repeated-prime or prime-power information from the canonical primitive cotangent fiber pushforward of PC-049. If a refinement prime is already present in the coarse level, the unnormalized pushforward is exactly a scalar `p^2`; after natural fiber averaging it is exactly the identity. More generally, for an arbitrary refinement multiplier `m`, the normalized pushed operator depends only on the set of prime divisors of `m` that are genuinely new relative to the coarse level `d`, and is completely independent of all refinement exponents.

This closes the repeated-prime branch left explicitly open by PC-049. It does **not** rule out operators that retain the fine fiber degrees of freedom, cross-level Gram/dilation constructions, nonlinear uses of the unaveraged tower, or the global uniformization/monodromy direction.

## 1. Setup

For `N>1`, write

\[
U(N)=(\mathbb Z/N\mathbb Z)^\times
\]

and use the primitive compression of the oriented cotangent kernel from PC-045,

\[
H_N(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}N\right),&a\ne b,\\[2mm]
0,&a=b,
\end{cases}
\qquad a,b\in U(N).
\]

Whenever `d|N`, let `R_{N,d}` be the incidence matrix of reduction

\[
U(N)\longrightarrow U(d),
\qquad x\longmapsto x\pmod d,
\]

so that

\[
(R_{N,d}f)(a)=\sum_{x\equiv a\,(d)} f(x).
\]

PC-049 treated one prime step `N=dp` with `p not| d`. The unresolved case is the intrinsically different lift geometry when `p|d`.

## 2. Repeated-prime refinement is an exact scalar

Let `p|d`. Every `a in U(d)` has exactly `p` unit lifts to `U(dp)`, namely

\[
a+kd,\qquad 0\le k<p.
\]

There is no excluded residue modulo `p`: because `p|d`, all these lifts are congruent to the already nonzero unit `a mod p`.

For distinct `a,b in U(d)`, put `delta=a-b`. Then

\[
\begin{aligned}
(R_{dp,d}H_{dp}R_{dp,d}^*)_{a,b}
&=\sum_{k,l=0}^{p-1}
 i\cot\!\left(
 \frac{\pi(\delta+d(k-l))}{dp}
 \right).
\end{aligned}
\]

For every residue `t=k-l mod p` there are exactly `p` ordered pairs `(k,l)`. Hence

\[
\begin{aligned}
(R_{dp,d}H_{dp}R_{dp,d}^*)_{a,b}
&=p\sum_{t=0}^{p-1}
 i\cot\!\left(
 \frac{\pi\delta}{dp}+\frac{\pi t}{p}
 \right)\\
&=p^2 i\cot\!\left(\frac{\pi\delta}{d}\right),
\end{aligned}
\]

where the last equality is the classical cotangent multiplication formula

\[
\sum_{t=0}^{p-1}\cot\!\left(x+\frac{\pi t}{p}\right)
=p\cot(px).
\]

On the diagonal, the `k=l` contributions are zero by the definition of `H_{dp}`. For every nonzero difference `t`, there are again `p` ordered pairs, so

\[
(R_{dp,d}H_{dp}R_{dp,d}^*)_{a,a}
=p i\sum_{t=1}^{p-1}\cot\frac{\pi t}{p}=0.
\]

Therefore the matrix identity is exact:

\[
\boxed{
R_{dp,d}H_{dp}R_{dp,d}^*=p^2H_d,
\qquad p\mid d.
}
\]

Since each reduction fiber has size `p`, the naturally averaged operator is literally unchanged:

\[
\boxed{
\frac1{p^2}R_{dp,d}H_{dp}R_{dp,d}^*=H_d.
}
\]

Thus once a prime is already present in the level, increasing its exponent produces no nontrivial coarse cotangent datum at all.

## 3. Prime-power towers forget the exponent exactly

Iterating the previous identity gives, for every `r>=1` and `p|d`,

\[
\boxed{
R_{dp^r,d}H_{dp^r}R_{dp^r,d}^*
=p^{2r}H_d.
}
\]

The reduction fiber has cardinality `p^r`, hence

\[
\boxed{
\frac1{p^{2r}}
R_{dp^r,d}H_{dp^r}R_{dp^r,d}^*
=H_d.
}
\]

The exponent `r` is therefore completely invisible after the canonical pairwise fiber average.

If instead `p not| d`, only the **first** appearance of `p` is nontrivial. PC-049 gives

\[
R_{dp,d}H_{dp}R_{dp,d}^*
=\mathcal T_p(H_d),
\]

with

\[
\mathcal T_p(X)=p(p-2)X+V_pXV_p^{-1}.
\]

Every later `p`-adic lift is a repeated-prime step. Therefore for every `r>=1`,

\[
\boxed{
R_{dp^r,d}H_{dp^r}R_{dp^r,d}^*
=p^{2(r-1)}\mathcal T_p(H_d),
\qquad p\nmid d.
}
\]

The fiber size is `p^{r-1}(p-1)`, so after averaging

\[
\boxed{
\frac{1}{p^{2(r-1)}(p-1)^2}
R_{dp^r,d}H_{dp^r}R_{dp^r,d}^*
=
\frac{\mathcal T_p(H_d)}{(p-1)^2},
}
\]

independently of `r`. The tower distinguishes whether `p` is new, but not how many additional powers of `p` are subsequently inserted.

## 4. Arbitrary refinement depends only on new prime support

Let

\[
m=\prod_p p^{e_p}
\]

be arbitrary and define the set of genuinely new refinement primes

\[
S(m;d)=\{p:p\mid m,\ p\nmid d\}.
\]

The total fiber cardinality of `U(dm) -> U(d)` is

\[
q_{m,d}
:=\frac{\varphi(dm)}{\varphi(d)}
=
\prod_{\substack{p\mid m\\p\mid d}}p^{e_p}
\prod_{\substack{p\mid m\\p\nmid d}}p^{e_p-1}(p-1).
\]

Reduction incidence matrices compose. Remove repeated prime powers first; every such step contributes only the scalar `p^2` above. What remains is a squarefree extension by the primes in `S(m;d)`, to which the commuting PC-049 prime-step formula applies. Hence

\[
\boxed{
R_{dm,d}H_{dm}R_{dm,d}^*
=
A_{m,d}
\left[
\prod_{p\in S(m;d)}\mathcal T_p
\right](H_d),
}
\]

where

\[
A_{m,d}
=
\prod_{\substack{p\mid m\\p\mid d}}p^{2e_p}
\prod_{\substack{p\mid m\\p\nmid d}}p^{2(e_p-1)}.
\]

Because

\[
q_{m,d}^2
=A_{m,d}
\prod_{p\in S(m;d)}(p-1)^2,
\]

the normalized formula becomes

\[
\boxed{
\frac1{q_{m,d}^2}
R_{dm,d}H_{dm}R_{dm,d}^*
=
\left[
\prod_{p\in S(m;d)}
\widehat{\mathcal T}_p
\right](H_d),
}
\]

with

\[
\boxed{
\widehat{\mathcal T}_p
:=\frac{\mathcal T_p}{(p-1)^2}
=I+\frac{\operatorname{Ad}_{V_p}-I}{(p-1)^2}.
}
\]

This is the radical-invariance statement: the normalized coarse operator depends on `m` only through the set of primes in `rad(m)` that are absent from `rad(d)`. All exponents `e_p` disappear exactly.

In particular, if every prime divisor of `m` already divides `d`, then

\[
\boxed{
\operatorname{rad}(m)\mid\operatorname{rad}(d)
\quad\Longrightarrow\quad
\frac1{q_{m,d}^2}
R_{dm,d}H_{dm}R_{dm,d}^*=H_d.
}
\]

## 5. Character channels confirm that no hidden prime-power factor survives

For multiplicative characters `chi,psi` of `U(d)`, PC-049 gives

\[
\left\langle e_\chi,
\widehat{\mathcal T}_p(H_d)e_\psi
\right\rangle
=
\left(
1+\frac{\overline{\eta(p)}-1}{(p-1)^2}
\right)
\langle e_\chi,H_de_\psi\rangle,
\]

where

\[
\eta=\chi\overline\psi.
\]

Therefore the arbitrary-refinement channel is

\[
\boxed{
\left\langle e_\chi,
\frac1{q_{m,d}^2}R_{dm,d}H_{dm}R_{dm,d}^*e_\psi
\right\rangle
=
\prod_{p\in S(m;d)}
\left(
1+\frac{\overline{\eta(p)}-1}{(p-1)^2}
\right)
\langle e_\chi,H_de_\psi\rangle.
}
\]

No `e_p` occurs. At odd squarefree base level, PC-045 already reduces the surviving base coefficients to fixed `L(0,eta)` / generalized-Bernoulli data. Repeated prime refinement neither changes that special value nor adds a new local Euler factor: after averaging it adds exactly `1`.

The unnormalized powers `p^{2e}` or `p^{2(e-1)}` do remember the obvious fiber multiplicity, but this is a deterministic dimension/counting scale. It is removed by the canonical average and carries no hidden geometry beyond the known refinement degree.

## 6. Prior-art and novelty audit

The analytic ingredient is classical. The cotangent multiplication identity is the logarithmic derivative of the sine multiplication formula. Distribution and scale identities for Dedekind/cotangent sums are also classical: Beck's **Dedekind cotangent sums** develops Petersson–Knopp identities for generalized cotangent sums, while Parson's **Dedekind sums and Hecke operators** identifies the Hecke-operator origin of the classical scale relations. These sources are already anchored in `research/prime_circle/SOURCES.md` for PC-049.

A directed literature check on cotangent distribution, Petersson–Knopp identities, Hecke scaling, and generalized Dedekind cotangent sums did not locate this exact primitive-unit matrix statement for the reduction `U(dp)->U(d)` with the repeated-prime/new-prime dichotomy. That absence is not evidence of theorem novelty. The matrix identity is an elementary specialization of classical cotangent distribution once the prime-circle primitive fibers are written correctly.

The durable contribution here is therefore not a novelty claim about cotangent identities. It is the **prime-circle obstruction**: the canonical primitive cotangent conditional average factors through new prime support and is exactly blind to prime-power depth.

This also prevents a misleading bridge to the common-vertex von Mangoldt identity. PC-001/PC-002 show that other prime-circle quantities detect prime-power structure. The present operator does not: one cannot infer that its coarse refinement dynamics inherit von Mangoldt's prime-power support merely because both arise from the same roots-of-unity tower.

## 7. Consequence for the RH search

PC-049 left repeated-prime local structure outside its squarefree iteration formula. The exact calculation above closes that escape route for the same canonical fiber pushforward:

\[
\boxed{
\text{primitive cotangent tower}
\to
\text{fiber-average refinement}
\to
\text{prime-power depth / repeated-prime dynamics}
\to
\text{new RH mechanism}
}
\]

fails under the stated construction. After normalization, repeated prime powers are not merely simple or approximately universal; they are **exactly invisible**.

Together with PC-049, the full multiplicative refinement law is now classified at this level: first appearances of new primes give commuting invertible local conjugation corrections, while every repeated appearance gives the identity after averaging. There is no ordered-prime curvature, no p-adic depth variable, no new analytic parameter `s`, and no intrinsic route to the critical line in this coarse operator.

The remaining cotangent/refinement frontier must retain information that `R H R^*` destroys. Natural examples still outside this result are:

- the orthogonal complement of fiber-constant functions and its coupling to the coarse subspace;
- rectangular fine/coarse Gram operators before both fiber indices are summed;
- simultaneous multi-level dilation spaces of Lewis–Zagier type;
- nonlinear compositions using fine-level states rather than only their conditional average;
- or global nonlocal data from the PC-017 uniformization direction.

## 8. Exact audit tests

The claim is finite-dimensional and has direct falsifiers.

1. For any `p|d`, construct `H_d`, `H_{dp}`, and the reduction incidence matrix and verify
   \[
   R_{dp,d}H_{dp}R_{dp,d}^*=p^2H_d.
   \]
2. Check separately that each difference class `t mod p` occurs exactly `p` times between two full lift fibers when `p|d`.
3. Verify the diagonal cancellation
   \[
   \sum_{t=1}^{p-1}\cot(\pi t/p)=0.
   \]
4. For `p not|d` and `r>=2`, verify
   \[
   R_{dp^r,d}H_{dp^r}R_{dp^r,d}^*
   =p^{2(r-1)}\mathcal T_p(H_d).
   \]
5. For mixed `m`, compare the direct reduction with the factored arbitrary-refinement formula and verify that dividing by `q_{m,d}^2` removes every exponent.
6. Hold `rad(m)` fixed while changing one or more exponents `e_p`; the normalized matrices must remain identical.

Failure of any of these exact finite identities would invalidate the radical-invariance obstruction.