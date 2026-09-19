# MC-402 — Truncated lcm masks are exact Mertens-weighted divisor energies

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the lcm-fiber setup of `MC-398`--`MC-401`. Let

\[
C_g(\ell)
:=
\sum_{\substack{d,e\le B\\[d,e]=\ell}} g(d)g(e),
\qquad
A_\chi(X)
:=
\sum_{\ell\le X} C_g(\ell)\chi(\ell),
\tag{1}
\]

where `g(d)=0` for `d>B`, `X` is a positive integer, and `\chi` is one of the quadratic source characters used in the current source-signature frame. Write

\[
M(y)=\sum_{m\le y}\mu(m).
\]

The incomplete lcm mask has the exact inversion

\[
\boxed{
\mathbf 1_{r\le X}
=
\sum_{\substack{n\le X\\r\mid n}}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right)
}
\tag{2}
\]

for every positive integer `r`. Consequently,

\[
\boxed{
A_\chi(X)
=
\sum_{n\le X}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right)
E_{\chi,g}(n;B),
}
\tag{3}
\]

with the finite divisor-incidence energy

\[
E_{\chi,g}(n;B)
:=
\sum_{\substack{d,e\le B\\d\mid n,\ e\mid n}}
g(d)g(e)\chi([d,e]).
\tag{4}
\]

For a quadratic character define

\[
b(d):=g(d)\chi(d),
\qquad
\eta_\chi:=\mu *_D \chi.
\tag{5}
\]

Then the same meet-matrix factorization used at the complete endpoint in `MC-401` applies **inside each incidence fiber**:

\[
\boxed{
E_{\chi,g}(n;B)
=
\sum_{\substack{k\mid n\\k\le B}}
\eta_\chi(k)
\left(
\sum_{\substack{d\le B\\d\mid n\\k\mid d}}
b(d)
\right)^2.
}
\tag{6}
\]

Equations (3) and (6) classify what happens when one tries to extend the complete-endpoint divisor-energy factorization of `MC-401` to a genuinely truncated cutoff `X<B^2`: the cutoff does not disappear, but its exact incidence resolution carries the **Mertens staircase** `M(floor(X/n))` as the outer weight.

Therefore the generic truncation mask by itself is not a free positive or cheaply signed replacement for the complete endpoint. A proof that proceeds by resolving only the indicator `[d,e]\le X` into divisor incidence has transferred the missing arithmetic into Mertens weights rather than created an independent cancellation mechanism.

This is deliberately narrower than saying that `A_\chi(X)` is Mertens-equivalent. The special coefficient `g`, source-signature family, or a joint estimate across the energies `E_{\chi,g}(n;B)` may still supply genuinely new information. What is ruled out is crediting the **cutoff mask alone**, after generic incidence factorization, as the missing source of a cheaper theorem.

No estimate for `M(x)` follows.

## 1. Exact cutoff inversion

For `r>X`, both sides of (2) vanish. Suppose `r\le X` and put

\[
Y=\left\lfloor\frac Xr\right\rfloor.
\]

Writing `n=rq` gives

\[
\sum_{\substack{n\le X\\r\mid n}}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right)
=
\sum_{q\le Y} M\!\left(\left\lfloor\frac Yq\right\rfloor\right).
\tag{7}
\]

Expand the Mertens function and interchange the finite sums:

\[
\begin{aligned}
\sum_{q\le Y} M\!\left(\left\lfloor\frac Yq\right\rfloor\right)
&=
\sum_{q\le Y}
\sum_{m\le Y/q}\mu(m)\\
&=
\sum_{t\le Y}\sum_{m\mid t}\mu(m)\\
&=1.
\end{aligned}
\tag{8}
\]

The last equality is the classical divisor identity `\sum_{m\mid t}\mu(m)=1` for `t=1` and `0` otherwise. This proves (2).

The mechanism is standard Möbius inversion, not a new number-theoretic identity. NIST DLMF §27.5 records both the divisor identity and the general Möbius inversion formulas; equation (2) is their finite floor-sum specialization.

## 2. The truncated lcm sum becomes a Mertens-weighted incidence sum

Expanding `C_g` in (1),

\[
A_\chi(X)
=
\sum_{d,e\le B}
g(d)g(e)\chi([d,e])
\mathbf 1_{[d,e]\le X}.
\tag{9}
\]

Apply (2) with `r=[d,e]`. Since `[d,e]\mid n` is equivalent to `d\mid n` and `e\mid n`,

\[
\mathbf 1_{[d,e]\le X}
=
\sum_{\substack{n\le X\\d\mid n,\ e\mid n}}
M\!\left(\left\lfloor\frac Xn\right\rfloor\right).
\tag{10}
\]

All sums are finite, so exchanging their order yields exactly (3)--(4).

This step is the missing representation audit between `MC-400` and `MC-401`. `MC-400` shows that the moving hyperbola family is an invertible Dirichlet-convolution coordinate, while `MC-401` classifies the complete endpoint `X=B^2` by a signed GCD energy. Equation (3) shows what the simplest exact incidence extension of that endpoint factorization costs before the lcm cutoff has disappeared: a Mertens-valued floor-quotient weight.

## 3. Each incidence fiber still has the signed GCD factorization

For source quadratic characters, the same algebra as in `MC-401` applies to (4). If `d` and `e` are units for the character modulus, then

\[
\chi([d,e])
=
\chi(d)\chi(e)\chi((d,e)),
\tag{11}
\]

because `[d,e](d,e)=de` and `\chi((d,e))^2=1`. If either `d` or `e` is a non-unit, both sides of the corresponding contribution vanish.

Since

\[
\eta_\chi=\mu *_D\chi,
\qquad
\chi=1 *_D\eta_\chi,
\]

we have

\[
\chi((d,e))
=
\sum_{k\mid(d,e)}\eta_\chi(k).
\tag{12}
\]

Insert (11)--(12) into (4) and regroup by `k`; this gives (6).

Thus truncation has not created a new positive kernel. The inner energy retains the same signed local GCD structure diagnosed in `MC-401`, while the outer cutoff resolution introduces another sign-changing object, `M(floor(X/n))`. Taking absolute values at either stage discards precisely the cancellation one would need to exploit.

## 4. What this does and does not close

The finding closes one specific interpretation of the accepted retained-variable clue: **“the incomplete lcm mask itself prevents factorization, therefore generic truncation supplies a new cheap arithmetic dimension.”** It does prevent the one-line complete-endpoint square decomposition, but exact Möbius inversion restores a divisor-incidence decomposition whose coefficients are Mertens values.

That is an obstruction to a representation-only gain, not to a theorem about truncated lcm sums. Several live possibilities remain:

- the actual Selberg coefficient `g` may force sparsity, cancellation, or a rigid source-signature law inside `E_{\chi,g}(n;B)`;
- a collective estimate may control the Mertens-weighted energy without separately estimating `M`;
- the source family may provide cancellation unavailable for a single generic character;
- a pre-quadratic representation may retain a genuinely non-lcm variable before the mask reaches the form in (9).

A candidate is therefore not killed merely because it studies `A_\chi(X)`. It is killed only if its claimed new resource is **nothing beyond** the generic cutoff-to-incidence conversion (2)--(6), or if its estimate closes by inserting an RH-scale or otherwise unavailable Mertens bound into (3).

There is also no converse assertion here. From (3) alone, a bound for `A_\chi(X)` need not imply a comparable bound for `M(X)`, because the structured energies at `n>1` may cancel the `n=1` contribution. The transform is useful as an audit of where the arithmetic has moved, not as a new RH-equivalent criterion.

## 5. Prior art and novelty boundary

The algebra behind (2) is classical Möbius inversion. NIST DLMF §27.5, equations 27.5.2--27.5.6, records the divisor identity, divisor Möbius inversion, and the corresponding floor-sum inversion framework, with references to Apostol. Recent work of Lagarias and Richman on the floor-quotient partial order (*Advances in Applied Mathematics* 153 (2024), 102615, DOI `10.1016/j.aam.2023.102615`) studies the combinatorics and Möbius theory of the same floor-quotient geometry at a much broader level.

A targeted literature check on 19 September 2026 found these classical/floor-quotient mechanisms and the meet/lcm-matrix literature already audited in `MC-401`, but no reason to claim a new general theorem for (2)--(6). None is claimed. The durable contribution is the **line-specific frontier classification**: applying ordinary Möbius inversion to the exact truncated lcm mask identifies the price of extending the `MC-401` incidence factorization—Mertens staircase weights—so generic truncation cannot be counted as an unexplained independent carrier.

## Boundaries and falsification tests

- **No Mertens estimate is proved.** Equations (2)--(6) are finite exact identities.
- **No RH equivalence is claimed.** A useful bound for `A_\chi(X)` could still arise from structure not visible in the generic incidence expansion.
- **Actual-weight structure remains open.** Any theorem using the specific Selberg coefficient must be tested directly; replacing it by a generic `g` can erase the very source information sought.
- **The source family remains open.** Cancellation across signatures/characters is not classified by this single-mode identity.
- **Pre-quadratic variables remain open.** The result begins only after the squared Selberg pair has collapsed to the lcm coefficient.
- **Absolute-value arguments are especially suspect.** They turn (3) into a sum of `|M|` times unsigned energy and therefore cannot advertise the Mertens staircase as a gain.
- **At `X=B^2`, use `MC-401`.** The complete endpoint has the simpler direct signed-GCD factorization; (3) merely gives a consistent but more redundant resolution of the same scalar.
- **The mechanism is representation-level.** Any proposed saving that survives a different proof route and genuinely exploits `g`, source signatures, or a joint bilinear theorem is not excluded.

## Consequence for the research line

`MC-398` compressed the Selberg divisor pair to lcm fibers, `MC-399` removed the lcm scalar from the first source phase, `MC-400` showed that the moving hyperbola coordinate is invertible, and `MC-401` classified the complete endpoint as a signed GCD/divisor energy.

The remaining “truncated lcm” branch is now narrower again. **The incomplete mask itself is no longer an unexplained resource:** its natural divisor-incidence resolution is exactly Mertens-weighted. The next useful theorem must exploit the actual Selberg/source structure inside that weighted energy, prove a genuinely collective estimate unavailable from generic Möbius inversion, or leave the lcm-factorable quadratic frame entirely.
