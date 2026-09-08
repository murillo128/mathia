# MC-157 — Single-prime commutator spectral filters have an exact top-mode dichotomy

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state representation and the pulled-back prime commutator from `MC-156`:

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn},
\qquad
D_\mu\varepsilon_n=\mu(n)\varepsilon_n,
\]

\[
B_p:=S_p^*[D_\mu,S_p],
\qquad
B_p\varepsilon_n=b_p(n)\varepsilon_n,
\qquad
b_p(n)=\mu(pn)-\mu(n).
\tag{1}
\]

`MC-156` proves

\[
b_p(n)\in\{-2,-1,0,1,2\}
\tag{2}
\]

and that the complete signed coefficient field is already target-complete. The natural next attempt is therefore to retain only a scalar spectral quotient `g(B_p)` of this five-point alphabet before cumulative aggregation.

For every **odd** function

\[
g:\{-2,-1,0,1,2\}\to\mathbb C,
\qquad g(-t)=-g(t),
\tag{3}
\]

put

\[
a:=g(2),
\qquad
c:=g(1),
\qquad
R_{p,g}(x):=\sum_{n\le x}g(b_p(n)).
\tag{4}
\]

Then the cumulative readout has the exact form

\[
\boxed{
R_{p,g}(x)
=-aM(x)-(a-c)\sum_{j\ge1}M(x/p^j),
}
\tag{5}
\]

where `M(y)=0` for `0\le y<1`, so the sum is finite for every `x`.

Consequently the coefficient of the **unsifted top-scale Mertens mode at the same observation scale** is exactly

\[
\boxed{-g(2).}
\tag{6}
\]

However, removing that coefficient does **not** make the complete scale family information-poor. In fact:

\[
\boxed{
\text{every nonzero odd scalar spectral filter }g
\text{ reconstructs }M
\text{ exactly from }R_{p,g}
\text{ across }p\text{-dilated scales.}
}
\tag{7}
\]

Thus scalar functional calculus does not provide the sought genuinely lossy-but-cancellation-preserving quotient. It only moves the target between the current scale and neighboring `p`-dilates.

The two canonical spectral bands expose both possibilities. Define

\[
g_{\rm in}(t)=\frac{4t-t^3}{3},
\qquad
g_{\rm out}(t)=\frac{t^3-t}{3}.
\tag{8}
\]

On the five-point spectrum,

\[
g_{\rm in}(\pm1)=\pm1,
\quad g_{\rm in}(0)=g_{\rm in}(\pm2)=0,
\tag{9}
\]

while

\[
g_{\rm out}(\pm2)=\pm2,
\quad g_{\rm out}(0)=g_{\rm out}(\pm1)=0.
\tag{10}
\]

Thus

\[
I_p:=g_{\rm in}(B_p),
\qquad
O_p:=g_{\rm out}(B_p),
\qquad
B_p=I_p+O_p,
\tag{11}
\]

with diagonal coefficients

\[
I_p(n)=-\mu(n)\mathbf 1_{p\mid n},
\qquad
O_p(n)=-2\mu(n)\mathbf 1_{p\nmid n}.
\tag{12}
\]

Writing

\[
J_p(x):=\sum_{n\le x}I_p(n),
\qquad
K_p(x):=\sum_{n\le x}O_p(n),
\tag{13}
\]

one obtains

\[
\boxed{
J_p(x)=\sum_{j\ge1}M(x/p^j),
}
\tag{14}
\]

and

\[
\boxed{
K_p(x)=-2\sum_{j\ge0}M(x/p^j).
}
\tag{15}
\]

The outer band recovers `M` by a downward two-scale difference,

\[
\boxed{
M(x)=-\frac12\bigl(K_p(x)-K_p(x/p)\bigr),
}
\tag{16}
\]

while the inner band, despite having no same-scale `M(x)` term, recovers it by an upward two-scale difference,

\[
\boxed{
M(x)=J_p(px)-J_p(x).
}
\tag{17}
\]

Therefore for every fixed prime `p` and fixed `\theta>0`,

\[
\boxed{
J_p(x)=O(x^\theta)
\Longleftrightarrow
M(x)=O(x^\theta)
\Longleftrightarrow
K_p(x)=O(x^\theta).
}
\tag{18}
\]

At a **single scale**, the inner band can still look much cheaper. Under a prior estimate

\[
M(y)=O(y^\beta),
\qquad \beta>0,
\tag{19}
\]

it satisfies

\[
|J_p(x)|
\ll_\beta
\frac{x^\beta}{p^\beta-1}.
\tag{20}
\]

If the prime is allowed to move with the observation scale,

\[
p=x^{\delta+o(1)},
\qquad 0<\delta<1,
\tag{21}
\]

then

\[
J_p(x)=O\!\left(x^{\beta(1-\delta)+o(1)}\right).
\tag{22}
\]

Equation `(17)` shows exactly what this apparent gain has omitted: the neighboring upscale value `J_p(px)`. The cheap single-scale statistic is not a globally cheaper cancellation observable once its natural scale family is retained.

The result closes scalar spectral functional calculus of one raw prime commutator as an intermediate information carrier. A surviving semigroup route must use a genuinely relational quotient whose compression cannot be inverted by the prime-dilation structure itself.

## 1. The five-point commutator alphabet separates divisibility and sign

From `MC-156`, there are exactly three cases:

\[
b_p(n)=
\begin{cases}
0,&\mu(n)=0,\\
-2\mu(n),&\mu(n)\ne0\text{ and }p\nmid n,\\
-\mu(n),&\mu(n)\ne0\text{ and }p\mid n.
\end{cases}
\tag{23}
\]

Hence an odd spectral function needs only its two positive values `a=g(2)` and `c=g(1)`. Equation `(23)` gives

\[
g(b_p(n))=
\begin{cases}
0,&\mu(n)=0,\\
-a\mu(n),&p\nmid n,\\
-c\mu(n),&p\mid n.
\end{cases}
\tag{24}
\]

Let

\[
A_p(x):=\sum_{\substack{n\le x\\p\mid n}}\mu(n).
\tag{25}
\]

Then

\[
R_{p,g}(x)
=-a\bigl(M(x)-A_p(x)\bigr)-cA_p(x)
=-aM(x)+(a-c)A_p(x).
\tag{26}
\]

It remains only to identify the `p`-divisible signed mass.

## 2. The p-divisible signed mass is an exact lower-dilation tail

Define

\[
F_p(x):=\sum_{n\le x}\mu(pn).
\tag{27}
\]

Since `\mu(pn)=-\mu(n)` when `p\nmid n` and `\mu(pn)=0` when `p\mid n`,

\[
F_p(x)
=-\sum_{\substack{n\le x\\p\nmid n}}\mu(n)
=-M(x)+A_p(x).
\tag{28}
\]

But writing a nonzero term of `A_p(x)` as `n=pm` gives

\[
A_p(x)=F_p(x/p).
\tag{29}
\]

Hence

\[
F_p(x)=-M(x)+F_p(x/p).
\tag{30}
\]

Iterating terminates after finitely many steps:

\[
F_p(x)=-\sum_{j\ge0}M(x/p^j).
\tag{31}
\]

Therefore

\[
\boxed{
A_p(x)=-\sum_{j\ge1}M(x/p^j).
}
\tag{32}
\]

Substituting `(32)` into `(26)` proves `(5)`.

This identity is entirely discrete. It uses neither `1/\zeta(s)`, Perron inversion, contour shifting, analytic continuation, nor a zero-free region.

## 3. Every nonzero odd spectral filter is scale-family target-complete

The exact formula `(5)` can be written using the dilation operator

\[
(T_pf)(x):=f(x/p)
\tag{33}
\]

and the finite pointwise geometric sum

\[
H_p(x):=\sum_{j\ge0}M(x/p^j).
\tag{34}
\]

Since

\[
M=(I-T_p)H_p,
\tag{35}
\]

formula `(5)` becomes

\[
\boxed{
R_{p,g}=-(aI-cT_p)H_p.
}
\tag{36}
\]

There are only two nontrivial cases.

### Case A: `a\ne0`

Equation `(36)` gives the finite downward recurrence

\[
\boxed{
H_p(x)=\frac ca H_p(x/p)-\frac1aR_{p,g}(x).
}
\tag{37}
\]

Because repeated division by `p` eventually reaches `<1`, and `H_p(y)=0` there, `(37)` reconstructs `H_p(x)` from finitely many values

\[
R_{p,g}(x),
R_{p,g}(x/p),
R_{p,g}(x/p^2),\ldots.
\]

Then `(35)` reconstructs `M(x)` exactly. No convergence assumption is required for this information-theoretic inversion.

The quantitative cost can nevertheless be nontrivial. If

\[
R_{p,g}(x)=O(x^\theta),
\tag{38}
\]

then the recurrence preserves exponent `\theta` whenever

\[
\left|\frac ca\right|p^{-\theta}<1.
\tag{39}
\]

At equality one can incur a logarithmic factor; above it the raw recurrence can amplify to the exponent `\log_p|c/a|`. Thus pointwise reconstructibility and same-exponent quantitative transfer are distinct claims.

### Case B: `a=0`, `c\ne0`

Now `(5)` is

\[
R_{p,g}(x)=c\sum_{j\ge1}M(x/p^j).
\tag{40}
\]

The missing same-scale term reappears after one upscale:

\[
R_{p,g}(px)-R_{p,g}(x)=cM(x),
\tag{41}
\]

so

\[
\boxed{
M(x)=\frac{R_{p,g}(px)-R_{p,g}(x)}c.
}
\tag{42}
\]

For fixed `p`, `(42)` preserves every power exponent in both directions.

If `a=c=0`, then the odd spectral filter is identically zero on `(2)` and contains no signed information. These cases exhaust all odd scalar functions on the spectrum.

Thus the actual information classification is sharper than the same-scale coefficient test `(6)`: **a nonzero odd scalar filter can move the target off the current scale, but it cannot remove it from the full canonical `p`-dilation family.**

## 4. Canonical inner and outer spectral filters realize the two recovery directions

The polynomials in `(8)` are the Lagrange spectral selectors for the two nonzero magnitude bands of `B_p`. Direct evaluation gives `(9)` and `(10)` and also

\[
g_{\rm in}(t)+g_{\rm out}(t)=t.
\tag{43}
\]

Therefore `(11)` is an exact operator decomposition.

For the inner filter, `a=0`, `c=1`, so `(5)` gives `(14)`, and `(42)` is precisely `(17)`. It retains Möbius sign only on the `p`-divisible shell at each fixed scale, but the prime dilation moves every square-free state between the two local divisibility cases. The full scale family therefore restores the supposedly omitted top mode.

For the outer filter, `a=2`, `c=0`, so `(5)` gives `(15)`. Equations `(36)`–`(37)` collapse to

\[
H_p(x)=-\frac12K_p(x),
\]

and `(35)` gives `(16)` directly.

Under `M(x)=O(x^\theta)`, the geometric tails give

\[
|J_p(x)|
\le \frac{C}{p^\theta-1}x^\theta,
\tag{44}
\]

\[
|K_p(x)|
\le \frac{2C}{1-p^{-\theta}}x^\theta.
\tag{45}
\]

Conversely `(16)` and `(17)` give

\[
|M(x)|
\le \frac12\left(|K_p(x)|+|K_p(x/p)|\right)
\tag{46}
\]

and

\[
|M(x)|
\le |J_p(px)|+|J_p(x)|.
\tag{47}
\]

These prove `(18)`. In particular, an RH-scale bound for either complete band family is simply another RH-equivalent Mertens criterion.

## 5. Single-scale cheapness is not scale-family compression

The inner identity `(14)` has a tempting feature absent from the outer one: it begins at `x/p`. If `p=x^{\delta+o(1)}` and a prior exponent `\beta` is available, `(22)` gives a polynomially smaller one-scale bound. But the same choice makes the recovery point `px`, and `(17)` says that the missing target lives exactly in the difference between those adjacent scale observations.

This distinguishes two notions that should not be conflated:

- **one-scale omission:** `J_p(x)` has no `M(x)` term and can be controlled from smaller arguments;
- **information compression:** the retained object across its canonical scale family fails to reconstruct `M`.

The first holds; the second does not. A proposed semigroup statistic cannot claim a cancellation mechanism merely because it looks cheaper at one selected scale if the source dynamics recovers the target by an exact neighboring-scale identity.

This is the same kind of audit demanded elsewhere in the line for moving windows, smoothing, and omitted blocks: the reconstruction channel must be included in the information budget.

## 6. General scalar functional calculus: even part is support, odd part is target-complete across scales

Any scalar function `h` on the spectrum `(2)` splits uniquely into even and odd parts.

The even part depends only on

\[
|b_p(n)|\in\{0,1,2\},
\tag{48}
\]

so it sees square-free support and whether `p` divides the square-free state, but not the Möbius orientation. It cannot by itself encode first-order signed Mertens cancellation.

The odd part is exhausted by the two parameters `a=g(2)` and `c=g(1)`. If it is zero, there is no signed information. If it is nonzero, Section 3 gives an exact scale-family reconstruction of `M`.

Therefore scalar functional calculus of `B_p` has no nontrivial intermediate signed information layer:

\[
\boxed{
\text{even} \Rightarrow \text{support/orientation-blind},
\qquad
\text{nonzero odd} \Rightarrow \text{Mertens-reconstructible across }p\text{-scales}.
}
\tag{49}
\]

A mixed scalar filter contains both pieces, but its cancellation-bearing component is still subject to the odd classification above. This does not say every mixed scalar aggregate is quantitatively equivalent to `M` without subtracting or controlling its even support contribution; it says the scalar spectral operation itself has not produced a new signed intermediate carrier.

## Prior art and novelty assessment

The Bost–Connes semigroup representation, its canonical isometries, and the relevant operator-algebraic setting are established prior art already audited in `MC-138`–`MC-156`. The weighted-shift commutator calculation `(1)` and the exact five-point coefficient classification `(23)` are persisted in `MC-149` and `MC-156`. Polynomial functional calculus on a finite spectrum and the local multiplicative rules for `\mu` are elementary classical tools.

A targeted literature search for Bost–Connes/prime-semigroup commutators combined with Möbius spectral projections or cumulative spectral-band identities recovered the standard Bost–Connes/operator-algebra setting but did not locate `(5)`, `(17)`, `(36)`, or `(42)` as named theorems. That absence is **not** used as evidence of novelty. The present result is an exact line-level synthesis of already-audited source structure with elementary finite spectral calculus and dilation recurrences, so no novelty claim is made.

The substantive delta relative to `MC-156` is the information classification after scalar spectral filtering. `MC-156` showed that the complete signed coefficient table overshoots by reconstructing `D_\mu` pointwise. The present result proves that the most immediate lossy-looking alternative also fails: discarding one magnitude band merely transfers the target to a neighboring prime-dilated scale.

There is a close structural analogy with `MC-090`, where a gcd-sieve split of the Huxley–Watt carrier makes one component lower-scale while the retained component keeps the unsifted top mode. The objects and derivations are different: `MC-090` is a divisor-sieve decomposition of a bilinear sawtooth form, while `(5)`–`(49)` classify scalar spectral functions of one prime commutator. The recurrence of the same reconstruction-versus-cheapness tension is therefore evidence for a line-level obstruction pattern, not a claim that the two constructions are identical.

## Boundaries and falsification tests

- **Scalar functional calculus only.** The theorem classifies `g(B_p)` for a single commutator followed by the canonical prefix family. Joint noncommutative words in several primes, matrix-valued filters, non-scalar conditional expectations, or relational statistics coupling different states are outside `(49)`.
- **Full scale family is load-bearing.** The one-scale inner statistic can be genuinely smaller under a moving prime. Target completeness uses `p`-dilated observations, especially the upscale value in `(42)`.
- **Pointwise recovery is not automatically same-exponent recovery for arbitrary `a,c`.** When `a\ne0`, the stability condition `(39)` controls whether a power bound transfers without exponent loss. The canonical inner and outer filters avoid this ambiguity and satisfy the exact exponent equivalences `(18)`.
- **A fixed prime is different from a moving-prime family.** For fixed `p`, `(20)` is only a constant-factor reduction at the same exponent. The polynomial saving `(22)` requires `p=p(x)` and therefore a scale-dependent readout.
- **No RH progress is claimed.** The theorem classifies information flow. It supplies no new bound for `M`.
- **Even filters are support controls, not signed cancellation carriers.** A mixed filter may require subtracting or independently controlling its even part before the odd reconstruction is exposed.
- **Relational compression remains live.** A quotient that couples different primes, bands, scales, or states before scalarization can evade this theorem if it does not permit recovery through the same dilation identities. It must still survive the line's support-matched biased controls and prove an anchored Mertens transfer.

The decisive falsification tests are finite and exact. For `(5)`, evaluate any proposed odd scalar filter on the five values `{-2,-1,0,1,2}`. For `(7)`, if `a\ne0`, run the finite recurrence `(37)`; if `a=0` and `c\ne0`, apply the two-scale identity `(42)`. A nonzero odd filter that evades both recovery mechanisms would refute the classification.

## Consequence for the research line

The immediate post-`MC-156` question was whether a natural scalar spectral quotient of one signed commutator could sit between cancellation-blind norms and the target-complete coefficient table. The answer is now **no**, in a stronger sense than same-scale top-mode retention alone suggested.

At one scale, `g(2)` decides whether the unsifted Mertens mode is visible. Across the canonical prime-dilation family, however, every nonzero odd filter reconstructs `M`: either by the finite downward recurrence `(37)` or by the upscale difference `(42)`. The inner and outer spectral bands are both power-bound equivalent to `M` for fixed `p`, despite looking very different at a single scale.

A surviving semigroup route must therefore leave one-variable scalar spectral functional calculus. The next admissible carrier must use a genuinely relational signed coupling — across bands, primes, scales, or states — whose compression survives the prime-dilation reconstruction audit and whose quantitative transfer to `M(x)` is not merely target recovery in another coordinate.