# MC-454 — Internal factorization does not increase source-frame occupancy

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-453` left one factorability-specific escape alive: instead of merely splitting a linear-sieve coefficient into boundedly many well-factorable components and squaring those components separately, expose the internal convolution variables of one component before positivity. That is genuinely how well-factorability is used in classical dispersion arguments. However, internal factor labels do **not by themselves** create additional translated-character source samples in the shifted kernel already isolated in `MC-413`.

Let the shifted divisor-expanded kernel be written abstractly as

\[
K_h(d,e)
:=
\sum_{\substack{n\le N-h\\ d\mid n+h\\ e\mid n}}
\chi(n+h)\overline{\chi(n)},
\tag{1}
\]

with the same compatibility and coprimality conventions as in `MC-413`. For a single factorable coefficient

\[
\lambda=\alpha*\beta,
\qquad
\lambda_d=\sum_{uv=d}\alpha_u\beta_v,
\tag{2}
\]

the corresponding quadratic shifted form becomes

\[
\begin{aligned}
C_h(\lambda)
&=\sum_{d,e}\lambda_d\overline{\lambda_e}K_h(d,e)\\
&=\sum_{u,v,u',v'}
\alpha_u\beta_v\overline{\alpha_{u'}}\overline{\beta_{v'}}
K_h(uv,u'v').
\end{aligned}
\tag{3}
\]

Define the multiplication map

\[
\pi(u,v)=uv.
\tag{4}
\]

Then the lifted source kernel is exactly

\[
K_h^{\mathrm{lift}}\bigl((u,v),(u',v')\bigr)
=
K_h\bigl(\pi(u,v),\pi(u',v')\bigr).
\tag{5}
\]

Hence `K_h^lift` is constant on every fiber of `pi x pi`. The factor variables enlarge the **coefficient representation**, but as long as the analytic kernel remains `(1)` they do not enlarge the image of the source-frame map: two internal factorizations with the same products `uv=d` and `u'v'=e` produce the same congruence pair, the same CRT source start, and the same translated-character sample.

The same statement holds for any finite factor depth. If

\[
\pi_k(u_1,\ldots,u_k)=u_1\cdots u_k,
\tag{6}
\]

then pulling the product-indexed kernel back to factor coordinates gives

\[
K_h^{(k)}(\mathbf u,\mathbf u')
=K_h\bigl(\pi_k(\mathbf u),\pi_k(\mathbf u')\bigr),
\tag{7}
\]

so the source kernel still factors through the multiplication quotient.

Therefore a factorable parametrization cannot defeat the `MC-448` source-occupancy barrier merely by increasing the nominal number of internal tuples. At fixed product-level conductor data, extra decompositions inside the same products are repeated labels of the **same source samples**, not new samples over which a large-sieve or orthogonality estimate can average.

This does **not** show that well-factorability is useless. It identifies the precise condition under which it is invisible. A viable escape must use the factor variables **before they collapse through multiplication** -- for example by a dispersion, completion, reciprocity, or bilinear transformation whose kernel depends separately on `u` and `v` rather than only on `uv` -- or must retain cross-component interference excluded by the positive splitting considered in `MC-453`.

No improved Möbius estimate, character-sum estimate, prime-distribution exponent, zero-free region, or RH consequence follows.

## 1. Exact quotient structure

The point is algebraic and does not depend on a bound for the character sum. Start from

\[
C_h(\lambda)
=
\sum_{d,e}\lambda_d\overline{\lambda_e}K_h(d,e).
\tag{8}
\]

Substituting `(2)` gives `(3)` by finite rearrangement. Thus introducing factor coordinates has replaced the coefficient matrix by a pullback under

\[
\Pi:(u,v,u',v')\mapsto(uv,u'v'),
\tag{9}
\]

but has not changed the source kernel itself:

\[
K_h^{\mathrm{lift}}=K_h\circ\Pi.
\tag{10}
\]

Consequently every fiber

\[
\Pi^{-1}(d,e)
\tag{11}
\]

is analytically indistinguishable to the source kernel before some additional operation is introduced. Summing many factor tuples in one fiber may change the resulting **coefficient attached to** `K_h(d,e)`, including through cancellation among the coefficients. It cannot create new translated-character locations or new source-frame occupancy.

This separates two notions that can otherwise be conflated:

- **representation multiplicity:** how many tuples `(u,v)` realize a product `d`;
- **source occupancy:** how many distinct analytic samples `K_h(d,e)` or CRT source starts are actually presented to the character-sum estimate.

Only the second can directly pay an occupancy tariff of the type isolated in `MC-446`--`MC-448`. Equation `(10)` shows that the first does not automatically increase the second.

## 2. Fixed-lcm consequence

The distinction is especially sharp in the fixed-lcm source frame studied in `MC-447`--`MC-451`. Fix an lcm shell `L`. Product-level pairs contributing to that shell satisfy

\[
[d,e]=L,
\tag{12}
\]

so necessarily `d|L` and `e|L`. Hence even before the additional compatibility restrictions from the shift are imposed, the number of product-level pairs is bounded by

\[
\#\{(d,e):[d,e]=L\}
\le \tau(L)^2
=L^{o(1)}.
\tag{13}
\]

For the squarefree partition regime used in `MC-447`, the CRT source set is smaller still because the prime divisors of `L` are allocated among the congruence constraints and compatibility eliminates overlaps with the shift.

Now replace `d` and `e` by arbitrarily many internal factor labels satisfying

\[
u_1\cdots u_k=d,
\qquad
u'_1\cdots u'_k=e.
\tag{14}
\]

The number of tuples in `(14)` can be much larger than the number of product pairs. But by `(7)` all tuples over a fixed `(d,e)` land on the same source kernel value. Therefore the polynomial-versus-subpolynomial occupancy comparison in `MC-448` cannot be improved merely by counting factor tuples as additional observations.

In particular, if a proposed large-sieve step claims a larger sample family solely because a well-factorable coefficient has been expanded into many `(u,v)` pairs, the sample count must first be quotiented by `(u,v)~(\tilde u,\tilde v)` whenever `uv=\tilde u\tilde v`. Without an analytic transformation that separates those representatives, the extra count is multiplicity, not occupancy.

## 3. Why this does not contradict classical well-factorable gains

Classical well-factorable estimates exploit exactly the structure left outside the quotient no-go.

Shao--Teräväinen define a well-factorable sequence of level `D` through factorizations

\[
\lambda=\beta*\gamma
\tag{15}
\]

adapted to arbitrary splittings `D=RS`, with the two factors supported in their respective ranges. Maynard's large-modulus work likewise emphasizes that the useful analytic leverage comes from taking a suitable factorization of the sieve weight and then feeding the separated variables into Type I/II or dispersion estimates.

Those arguments do **not** merely relabel a pre-existing product-indexed kernel by writing `d=uv`. They transform or estimate the expression while `u` and `v` still occupy different analytic roles. Once a completion, Cauchy step, modulus split, Poisson/Kloosterman transformation, or another bilinear operation produces a kernel

\[
\widetilde K_h(u,v,u',v')
\tag{16}
\]

that is not a function only of `(uv,u'v')`, equation `(10)` no longer applies. That is precisely where well-factorability can add genuine information.

So the obstruction is not “factorization cannot help.” It is:

> **factorization cannot increase source-frame occupancy while the source-dependent kernel still factors through the product map.**

The next successful argument must identify the first mathematically justified operation that breaks this product quotient and then quantify what new cancellation becomes available.

## 4. Relation to the existing frontier

`MC-409` identified well-factorability as a potentially meaningful escape because a component `lambda=alpha*beta` can expose bilinear variables before positive closure. The present finding keeps that possibility alive but makes its success criterion exact: merely substituting the convolution into the already product-indexed `MC-413` kernel changes notation and coefficients, not the source family.

`MC-424` gave a more generic fixed-depth state-counting obstruction: finite factor lifts do not automatically increase the polynomial exponent of the available shell state space. The present result is different and stronger on this specific branch. It identifies an exact quotient map for the translated-character kernel, so even a very large internal representation multiplicity is invisible to source occupancy unless a later analytic operation separates representatives of the same product.

`MC-447` and `MC-448` then supply the quantitative consequence. Their fixed-lcm source frame has only a subpolynomial family of product-level source starts against a polynomial large-sieve tariff. Equation `(10)` prevents internal convolution tuples from being counted as new source observations while that frame is unchanged.

Finally, `MC-453` removed bounded component splitting as a polynomial diagonal-dilution mechanism after separate positive closure. Combining the two findings leaves two genuinely different escape routes:

1. **factor-level analytic separation:** use internal convolution variables in a transformation whose kernel no longer factors through their products before positivity;
2. **retained interference:** preserve cross-component or cross-factor oscillation that is destroyed by the separately positive estimates treated in `MC-453`.

The first route is now the sharper target for the accepted local clue about retaining source-frame variables through an averaged/differenced object.

## Prior-art and novelty boundary

The convolution identity `(2)`, the substitution leading to `(3)`, and the fact that a pullback kernel is constant on fibers of its defining map are elementary. No novelty is claimed for them. Classical sieve theory already knows that well-factorable sequences are useful because their convolution variables can be exploited in dispersion and Type I/II arguments; the Shao--Teräväinen and Maynard references cited in `MC-453` are explicit modern examples.

A targeted audit found no basis for claiming a new general theorem about well-factorable sequences. The durable contribution here is a **frontier-specific no-go classification**: for the exact shifted translated-character kernel isolated in `MC-413`, internal factor coordinates remain analytically quotient-equivalent until an operation makes the kernel depend on those coordinates separately. Therefore representation multiplicity cannot be used as source-frame occupancy against the `MC-448` tariff.

This is deliberately narrower than saying that factorization cannot improve the estimate, and it is compatible with the classical literature in which factorization helps precisely because it is used before such product collapse.

## Boundaries and falsification tests

- **Kernel dependence is load-bearing.** The conclusion holds only while the analytic kernel has the form `K_h(uv,u'v')`. If a justified transformation creates separate dependence on the factor variables, the finding no longer blocks a gain.
- **Coefficient cancellation is not ruled out.** Different tuples in one multiplication fiber may cancel when their coefficients are summed. That changes the effective product-level coefficient; it is not additional source occupancy and must be analyzed as coefficient cancellation.
- **No claim about optimal divisor counts is needed.** The fixed-lcm conclusion uses only the standard subpolynomial divisor bound in `(13)`. The exact number of compatible CRT starts may be smaller.
- **Variable factor depth does not defeat the quotient algebraically.** Equation `(7)` holds for every finite `k`. A growing `k` can alter coefficient complexity, but cannot by itself separate source samples if the kernel still sees only the product.
- **Classical dispersion gains are outside the no-go when they break the quotient.** Any candidate based on Maynard/Fouvry--Iwaniec-style factor-level manipulation must be judged after writing its transformed kernel explicitly, not rejected by analogy with `(10)`.
- **No circular analytic continuation is used.** Everything here is a finite rearrangement of the shifted coefficient kernel and a counting consequence at fixed lcm.

## Consequence for the research line

The internal-factorization branch should no longer measure progress by the number of factor tuples exposed after writing `lambda=alpha*beta`. The decisive test is whether the **source-dependent incomplete character object itself** acquires a new factor-level degree of freedom before the first positive closure.

Concretely, the next calculation should start from one genuine well-factorable component and carry its balanced variables through the shifted incomplete sum before recombination. After the first nontrivial analytic transformation, write the resulting kernel explicitly and ask whether it still factors through `(uv,u'v')`. If it does, the apparent enlargement is only a pullback of the old source frame. If it does not, the new variable dependence is a genuine candidate mechanism and its occupancy/cancellation gain can then be tested quantitatively against the `MC-415` and `MC-448` budgets.
