# PC-049 — cotangent primitive refinement is a commuting invertible local pushforward

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for the canonical **cross-level fiber-sum/average route** in which a primitive cotangent operator at level `dp` is pushed to the primitive shell at level `d` along the intrinsic reduction map `U(dp) -> U(d)`. PC-045/PC-048 show that the relevant single-level cotangent channels are fixed `L(0)` / generalized-Bernoulli data. The present result shows that the most direct divisor-refinement pushforward does not create a new scale spectrum: every new prime acts by an explicit invertible superoperator, the prime-step actions commute exactly, and after natural fiber averaging their character multipliers form a nonzero absolutely convergent local product.

This is not a no-go for Lewis–Zagier-type cross-scale Gram/dilation constructions, for operators retaining fine/coarse correlations instead of summing fibers, or for nonlinear/global uniformization data.

## 1. The intrinsic primitive reduction map

Let `d>1`, let `p` be prime with `p not| d`, and write

\[
U(N)=(\mathbb Z/N\mathbb Z)^\times.
\]

Use the primitive compression of the oriented cotangent kernel from PC-045,

\[
H_N(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}N\right),&a\ne b,\\[2mm]
0,&a=b,
\end{cases}
\qquad a,b\in U(N).
\]

The root map `z -> z^p` from primitive `dp`-th roots to primitive `d`-th roots is exactly reduction of exponents,

\[
\rho_{p,d}:U(dp)\longrightarrow U(d),
\qquad x\longmapsto x\pmod d.
\]

Each fiber has `p-1` elements. Let `R_{p,d}` be the unnormalized incidence/fiber-sum matrix

\[
R_{p,d}(a,x)=
\begin{cases}
1,&x\equiv a\pmod d,\\
0,&\text{otherwise},
\end{cases}
\qquad a\in U(d),\ x\in U(dp).
\]

The most direct linear coarse operator obtained from the fine primitive shell is therefore

\[
\boxed{
\mathcal P_{p,d}(H_{dp})
:=R_{p,d}H_{dp}R_{p,d}^*.
}
\]

This construction is intrinsic to the cyclotomic refinement map: no ordering of lifts, auxiliary metric, or spectral parameter is introduced.

## 2. Exact prime-step pushforward identity

Let `p^{-1}` denote the inverse of `p` modulo `d`, and let `V_p` be the permutation of `C^{U(d)}` induced by multiplication by `p`, normalized here as

\[
(V_pf)(a)=f(p^{-1}a).
\]

Then the fiber pushforward is exactly

\[
\boxed{
R_{p,d}H_{dp}R_{p,d}^*
=
 p(p-2)H_d+V_pH_dV_p^{-1}.
}
\]

The proof is finite. Fix distinct `a,b in U(d)` and put `delta=a-b mod d`. Label the two fibers by their nonzero CRT residues `u,v in F_p^*`. For a fixed difference

\[
t=u-v\in\mathbb F_p,
\]

there are

\[
N_0=p-1,
\qquad
N_t=p-2\quad(t\ne0)
\]

ordered pairs `(u,v)` giving that difference. Let `z_t mod dp` be the unique CRT lift satisfying

\[
z_t\equiv\delta\pmod d,
\qquad
z_t\equiv t\pmod p.
\]

Hence the matrix entry is

\[
(p-2)\sum_{t\in\mathbb F_p}
i\cot\!\left(\frac{\pi z_t}{dp}\right)
+
i\cot\!\left(\frac{\pi z_0}{dp}\right).
\]

The `z_t` run through all `p` lifts of `delta mod d`. The classical cotangent multiplication formula

\[
\sum_{r=0}^{p-1}
\cot\!\left(x+\frac{\pi r}{p}\right)
=p\cot(px)
\]

therefore gives

\[
\sum_t i\cot\!\left(\frac{\pi z_t}{dp}\right)
=p\,i\cot\!\left(\frac{\pi\delta}{d}\right).
\]

The special lift `z_0` is divisible by `p`: writing `z_0=pc`, one has

\[
c\equiv p^{-1}\delta\pmod d,
\]

so its contribution is the `(a,b)` entry of `V_pH_dV_p^{-1}`. For `a=b`, the diagonal pairs contribute zero and the remaining differences give

\[
(p-2)i\sum_{r=1}^{p-1}\cot\frac{\pi r}{p}=0,
\]

which agrees with the zero diagonal on the right. Thus the identity is exact entry by entry.

The doubling case is especially rigid:

\[
\boxed{
R_{2,d}H_{2d}R_{2,d}^*=V_2H_dV_2^{-1}.
}
\]

So odd-level doubling carries no new coarse cotangent spectrum at all; it is only a permutation conjugacy.

## 3. Squarefree refinement is exactly path independent

For a prime `p not| d`, define the superoperator on matrices over `U(d)`

\[
\boxed{
\mathcal T_p(X)
:=p(p-2)X+V_pXV_p^{-1}.
}
\]

Now let `m` be squarefree and coprime to `d`, and let `R_{m,d}` be the incidence map for

\[
U(dm)\to U(d).
\]

Incidence maps compose under successive reductions. Moreover multiplication by a second new prime permutes each fiber compatibly with reduction, so conjugation by `V_q` commutes with pushing a `p`-fiber. Induction over the prime divisors of `m` therefore gives

\[
\boxed{
R_{m,d}H_{dm}R_{m,d}^*
=
\left[
\prod_{p\mid m}\mathcal T_p
\right](H_d).
}
\]

All `V_p` are commuting multiplicative permutations of `U(d)`. Consequently

\[
\boxed{
\mathcal T_p\mathcal T_q
=
\mathcal T_q\mathcal T_p
}
\]

for distinct new primes `p,q`. Thus two refinement chains with the same squarefree endpoint set give exactly the same pushed operator. There is no ordered-prime commutator, curvature, or refinement holonomy in this canonical cotangent coarse-graining.

This is a cotangent analogue of the path-independence obstruction in PC-039, but the mechanism is different: PC-039 uses Schur/Kron associativity for the positive inverse-square energy, whereas here path independence comes from the exact trigonometric distribution relation and commuting multiplicative permutations.

## 4. Character channels acquire only explicit local factors

For a character `chi` of `U(d)`, let

\[
e_\chi(a)=\frac{\chi(a)}{\sqrt{\varphi(d)}}.
\]

Since

\[
V_pe_\chi=\chi(p)^{-1}e_\chi,
\]

one obtains for any two characters `chi,psi`

\[
\boxed{
\left\langle e_\chi,
\mathcal T_p(H_d)e_\psi\right\rangle
=
\left(p(p-2)+\overline{\chi(p)}\psi(p)\right)
\langle e_\chi,H_de_\psi\rangle.
}
\]

Writing

\[
\eta=\chi\overline\psi,
\]

this is

\[
\boxed{
\left\langle e_\chi,
R_{m,d}H_{dm}R_{m,d}^*e_\psi\right\rangle
=
\prod_{p\mid m}
\left(p(p-2)+\overline{\eta(p)}\right)
\langle e_\chi,H_de_\psi\rangle.
}
\]

When `d` is odd and squarefree, PC-045 already classifies the base coefficient `\langle e_chi,H_de_psi\rangle`: same-parity channels vanish, while every surviving off-diagonal channel is an explicit Gauss/Ramanujan factor times the fixed generalized-Bernoulli value `L(0,eta)`.

Therefore this cross-level pushforward does not free that special value into an analytic family. It only multiplies the same fixed `L(0)` channel by elementary local factors attached to the newly adjoined primes.

## 5. Every prime step is invertible on the coarse matrix algebra

The superoperator `Ad_{V_p}:X -> V_pXV_p^{-1}` has finite order and all of its eigenvalues lie on the unit circle. Hence

\[
\mathcal T_p=p(p-2)I+\operatorname{Ad}_{V_p}
\]

is invertible for every new prime:

- for `p=2`, it is exactly the invertible conjugation `Ad_{V_2}`;
- for `p>=3`, every eigenvalue has the form `p(p-2)+omega` with `|omega|=1`, and `p(p-2)>1`.

Thus, once the extension prime is known, the retained coarse matrix is an explicit invertible transform of `H_d`. The dimensional reduction `U(dp) -> U(d)` certainly discards fine-level degrees of freedom, but **the pushed operator itself contains no operator information beyond the base primitive cotangent matrix and the known prime label**.

The same fact is visible channelwise under natural fiber averaging. Since each fiber has `p-1` elements,

\[
\frac{p(p-2)+\overline{\eta(p)}}{(p-1)^2}
=
1+
\frac{\overline{\eta(p)}-1}{(p-1)^2}.
\]

Consequently, for squarefree added scale `m`,

\[
\boxed{
\prod_{p\mid m}
\left(p(p-2)+\overline{\eta(p)}\right)
=
\varphi(m)^2
\prod_{p\mid m}
\left(
1+
\frac{\overline{\eta(p)}-1}{(p-1)^2}
\right).
}
\]

The normalized local corrections differ from `1` by `O(p^{-2})`, so the product over any expanding set of new primes is absolutely convergent. It is also nonzero: for `p>=3`, `|(p-1)^2|> |\overline{\eta(p)}-1|`, while the `p=2` factor is simply `\overline{\eta(2)}`. Thus the naturally fiber-averaged tower has no hidden critical Euler-product zero set; after the elementary `varphi(m)^2` scale it approaches a finite nonzero character-dependent correction.

## 6. Prior-art and novelty audit

The ingredients surrounding this calculation are classical.

- The cotangent multiplication formula is the logarithmic derivative of the standard sine multiplication/product identity; no novelty is claimed for it.
- Matthias Beck, **Dedekind cotangent sums**, *Acta Arithmetica* 109:2 (2003), 109–130, DOI `10.4064/aa109-2-1`, develops generalized cotangent sums and proves Petersson–Knopp identities. This is a direct prior-art boundary for interpreting scale-distribution identities of cotangent data as a new phenomenon.
- L. Alayne Parson, **Dedekind sums and Hecke operators**, *Mathematical Proceedings of the Cambridge Philosophical Society* 88:1 (1980), 11–14, DOI `10.1017/S0305004100057315`, explains the classical Hecke-operator origin of Petersson–Knopp-type scale identities. The commuting prime actions above therefore should not be advertised as a new Hecke mechanism.
- Lewis and Zagier, **Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis**, *Research in the Mathematical Sciences* 6 (2019), Article 4, DOI `10.1007/s40687-018-0159-8`, prove a genuine GRH criterion for a different cross-scale cotangent construction. Their mechanism uses a family of dilates and Gram determinants together with Mellin/Beurling-type functional analysis; it is not the finite primitive-fiber pushforward classified here.

Directed searches did not locate this exact matrix identity for the reduction `U(dp) -> U(d)`. That absence is not evidence of historical priority. No theorem novelty is claimed for cotangent distribution, Petersson–Knopp/Hecke scaling, or character diagonalization.

The durable prime-circle contribution is the exact obstruction specific to its primitive-root refinement: **the most direct linear fiber pushforward is a commuting, invertible, locally factored action on the already-classical single-level cotangent data.**

## 7. Consequence for the RH search

The natural chain

\[
\boxed{
\text{primitive root tower}
\to
\text{oriented cotangent operator}
\to
\text{fiber pushforward along }U(dp)\to U(d)
\to
\text{ordered prime-scale dynamics}
\to
\text{RH}
}
\]

is ruled out under its stated hypotheses. Exact cross-level aggregation does not produce a new noncommutative scale curvature, an `s`-dependent spectrum, a gamma completion, or a mechanism selecting `Re(s)=1/2`; it preserves the fixed `L(0)` coefficient algebra up to explicit commuting local factors.

The boundary is important. This finding does **not** rule out:

- a cross-level operator that retains both fine and coarse degrees of freedom instead of summing each reduction fiber;
- rectangular Gram operators coupling several levels simultaneously;
- Lewis–Zagier-type dilation spaces or determinant asymptotics;
- nonlinear compositions for which the prime-step maps no longer commute;
- repeated-prime local structure not covered by the squarefree iteration formula;
- or the global uniformization/monodromy direction of PC-017.

Any surviving cotangent/refinement mechanism must therefore exploit structure discarded by the canonical conditional fiber aggregation, rather than merely composing that aggregation over prime refinements.

## 8. Exact audit and falsification tests

The claim is finite-dimensional and can be checked without asymptotics.

1. For any `p not| d`, construct the primitive cotangent matrices directly and verify
   \[
   R_{p,d}H_{dp}R_{p,d}^*=p(p-2)H_d+V_pH_dV_p^{-1}.
   \]
2. Check the CRT difference multiplicities `p-1` for `t=0` and `p-2` for every `t != 0`, then apply the cotangent multiplication identity.
3. Verify the exact doubling specialization `R_{2,d}H_{2d}R_{2,d}^*=V_2H_dV_2^{-1}`.
4. For coprime new primes `p,q`, compare direct reduction from `dpq` with both staged orders and verify `T_p T_q=T_q T_p`.
5. In multiplicative-character coordinates, check the factor `p(p-2)+conj(chi(p)) psi(p)` against direct matrix coefficients.
6. Divide by `(p-1)^2` per fiber pair and verify the normalized factor `1+(conj(eta(p))-1)/(p-1)^2` and its nonvanishing.

Failure of any one of the finite prime-step identities would invalidate the obstruction. The claims about `L(0)` content at odd squarefree base level inherit the exact hypotheses and audit boundary of PC-045 rather than extending them silently.