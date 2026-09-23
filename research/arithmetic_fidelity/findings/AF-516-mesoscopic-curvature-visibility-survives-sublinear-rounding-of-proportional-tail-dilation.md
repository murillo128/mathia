# AF-516 — Mesoscopic curvature visibility survives sublinear rounding of proportional tail dilation

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-SEPARATION` · `DIRICHLET-SOURCE` · `PROPORTIONAL-TAIL-DILATION` · `ROUNDING-STABILITY` · `MESOSCOPIC-BOUNDARY-SCALE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1.
\]

Fix real constants

\[
c>1,
\qquad 0\le \alpha<1,
\qquad C>0.
\]

Suppose that for all sufficiently large primes `p` there are pairwise distinct positive atoms `q_p` satisfying

\[
|q_p-cp|\le C p^\alpha.
\tag{1}
\]

For a cutoff `A`, retain every prime at or below `A` and replace every prime above `A` by `q_p`:

\[
\widetilde R_A
=
\{p\in\mathbb P:p\le A\}
\cup
\{q_p:p\in\mathbb P,\ p>A\}.
\tag{2}
\]

For all sufficiently large `A`, the two parts in `(2)` are disjoint because `q_p/p\to c>1`. Write

\[
\widetilde\kappa_A(s)
=
\frac{d^2}{ds^2}
\log\!\left(\sum_{q\in\widetilde R_A}q^{-s}\right).
\]

For every fixed `k>1`, set

\[
s_A=1+t_A,
\qquad
t_A=(\log A)^{-k}.
\tag{3}
\]

Then

\[
\boxed{
\frac{\widetilde\kappa_A(s_A)-\kappa_P(s_A)}
{\kappa_P(s_A)}
\longrightarrow
-\frac{c-1}{k+c-1}.
}
\tag{4}
\]

Equivalently,

\[
\boxed{
\frac{\widetilde\kappa_A(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{k}{k+c-1}.
}
\tag{5}
\]

Thus the positive mesoscopic separation found in AF-515 for an exact proportional tail dilation is stable under any uniformly sublinear additive perturbation of that dilation.

In particular, for every real `c>1`, define for all sufficiently large odd primes

\[
q_p=2\left\lfloor\frac{cp}{2}\right\rfloor.
\tag{6}
\]

Then `q_p` is an even composite integer, the sequence `p\mapsto q_p` is strictly increasing, and

\[
|q_p-cp|<2.
\tag{7}
\]

Hence `(4)`--`(5)` hold for an **ordinary-integer control whose entire moved tail is composite**, even when `c` is not an integer. The AF-515 visibility mechanism is therefore not an artifact of exact multiplicative placement on the real line or of choosing an integer dilation factor.

## Derivation

### 1. Exact proportional dilation has the AF-515 asymptotic for every real `c>1`

Put

\[
S_A(s)=\sum_{p\le A}p^{-s},
\qquad
T_A(s)=P(s)-S_A(s).
\]

The exact proportional comparison source is

\[
Q_{A,c}(s)
=S_A(s)+c^{-s}T_A(s).
\tag{8}
\]

AF-515 proves the mesoscopic asymptotic for integer `c\ge2`. Its derivation uses the factor

\[
a(s)=c^{-s}
\]

only as a positive smooth scalar with bounded first two derivatives near `s=1`; no arithmetic property of integer `c` enters the analytic calculation. Therefore the same proof applies verbatim to every fixed real `c>1` and gives

\[
\frac{\kappa_{Q_{A,c}}(s_A)-\kappa_P(s_A)}{\kappa_P(s_A)}
\longrightarrow
-\frac{c-1}{k+c-1}.
\tag{9}
\]

The same calculation also gives the scale estimates, with

\[
L=\log A,
\qquad
\ell=\log L,
\qquad
t_A=L^{-k},
\]

\[
P(s_A)=k\ell+O(1),
\qquad
\kappa_P(s_A)\sim\frac{L^{2k}}{k\ell},
\tag{10}
\]

and

\[
Q_{A,c}(s_A)\asymp \ell,
\qquad
\left|\frac{Q_{A,c}'(s_A)}{Q_{A,c}(s_A)}\right|
=O\!\left(\frac{L^k}{\ell}\right),
\qquad
\left|\frac{Q_{A,c}''(s_A)}{Q_{A,c}(s_A)}\right|
=O\!\left(\frac{L^{2k}}{\ell}\right).
\tag{11}
\]

Only stability of `(9)` under the perturbation `(1)` remains to be proved.

### 2. A sublinear perturbation of the proportional tail is tiny through two source derivatives

Define

\[
\widetilde Q_A(s)
=S_A(s)+\sum_{p>A}q_p^{-s}
\]

and

\[
E_A(s)=\widetilde Q_A(s)-Q_{A,c}(s)
=\sum_{p>A}\bigl(q_p^{-s}-(cp)^{-s}\bigr).
\tag{12}
\]

Because `(1)` has exponent `\alpha<1`, for sufficiently large `p` one has

\[
q_p\asymp p
\]

uniformly. For `j=0,1,2`, differentiate `x^{-s}` with respect to `s` exactly `j` times and then apply the mean-value theorem in the support variable `x`. Uniformly for `s\ge1` sufficiently close to `1`,

\[
\left|
\partial_s^j q_p^{-s}
-
\partial_s^j (cp)^{-s}
\right|
\le
C_j p^{\alpha-s-1}(1+\log^j p).
\tag{13}
\]

Therefore, at `s=s_A>1`, comparison with the full integer tail gives

\[
|E_A^{(j)}(s_A)|
\le
C_j\sum_{n>A}n^{\alpha-2}(1+\log^2 n)
=O\!\left(A^{\alpha-1}(1+L^2)\right)
\tag{14}
\]

for all `j=0,1,2`. Set

\[
\eta_A=A^{\alpha-1}(1+L^2).
\tag{15}
\]

Since `\alpha<1`, `\eta_A` tends to zero faster than any negative power of `L` after multiplication by any fixed power of `L`.

### 3. The induced curvature change is negligible relative to prime curvature

At `s_A`, write

\[
\delta_A=\frac{E_A}{Q_{A,c}},
\qquad
u_A=\frac{Q_{A,c}'}{Q_{A,c}},
\qquad
\kappa_{A,c}=(\log Q_{A,c})''.
\tag{16}
\]

Equations `(11)` and `(14)` imply

\[
\delta_A
=O\!\left(\frac{\eta_A}{\ell}\right)
=o(1).
\tag{17}
\]

Differentiating the quotient gives

\[
\delta_A'
=\frac{E_A'}{Q_{A,c}}-\delta_A\nu_A,
\tag{18}
\]

and

\[
\delta_A''
=\frac{E_A''}{Q_{A,c}}
-2\frac{E_A'}{Q_{A,c}}\nu_A
+\delta_A\bigl(\nu_A^2-\kappa_{A,c}\bigr).
\tag{19}
\]

Using `(10)`--`(14)` and AF-515's finite relative-curvature limit,

\[
\frac{|\delta_A''|}{\kappa_P(s_A)}
=O\!\left(\frac{\eta_A}{\ell}\right)
+O\!\left(\frac{\eta_A L^{-k}}{\ell}\right)
+O\!\left(\frac{\eta_A}{\ell}\right)
\longrightarrow0,
\tag{20}
\]

while

\[
\frac{|\delta_A'|^2}{\kappa_P(s_A)}
\longrightarrow0.
\tag{21}
\]

The exact displayed rates in `(20)` are deliberately stronger than needed; the decisive fact is that every polynomial factor in `L` is dominated by `A^{\alpha-1}`.

Since

\[
\widetilde Q_A
=Q_{A,c}(1+\delta_A),
\]

one has

\[
\widetilde\kappa_A-\kappa_{Q_{A,c}}
=(\log(1+\delta_A))''
=
\frac{\delta_A''}{1+\delta_A}
-
\frac{(\delta_A')^2}{(1+\delta_A)^2}.
\tag{22}
\]

Equations `(17)`, `(20)`, and `(21)` yield

\[
\boxed{
\frac{\widetilde\kappa_A(s_A)-\kappa_{Q_{A,c}}(s_A)}
{\kappa_P(s_A)}
\longrightarrow0.
}
\tag{23}
\]

Combining `(23)` with `(9)` proves `(4)`, and `(5)` follows immediately.

### 4. Bounded even rounding gives an ordinary all-composite moved tail

For the explicit control `(6)`,

\[
0\le cp-q_p<2,
\]

so `(1)` holds with `\alpha=0`. Every sufficiently large `q_p` is even and greater than `2`, hence composite.

If `p_2>p_1` are odd primes, then `p_2-p_1\ge2`, so

\[
\frac{c p_2}{2}-\frac{c p_1}{2}
\ge c>1.
\]

Consequently

\[
\left\lfloor\frac{c p_2}{2}\right\rfloor
>
\left\lfloor\frac{c p_1}{2}\right\rfloor,
\]

and the moved atoms are pairwise distinct. Moreover, because `q_p/p\to c>1`, one has `q_p>p>A` for every moved prime once `A` is large enough, so the composite tail cannot collide with the retained prime prefix.

This proves the integer-control corollary.

## Fidelity and matched-control audit

AF-514 and AF-515 isolate two qualitatively different transport regimes for the same curvature representation:

- a direct tail displacement `p\mapsto p+h_p` with sufficiently small weighted sublinear budget can become uniformly invisible;
- a coherent proportional displacement `p\mapsto cp` leaves a fixed mesoscopic defect because it creates an interface between two dilation gauges.

AF-516 shows that the second regime is **structurally stable under sublinear jitter around the proportional ray**. The exact equality `q_p=cp` is not carrying the witness. What matters is the surviving first-order ratio

\[
\frac{q_p}{p}\longrightarrow c\ne1.
\tag{24}
\]

under the quantitative control `(1)`.

The explicit rounded family is a particularly strong matched control. It preserves the entire prime prefix below `A`, replaces every sufficiently large prime by a distinct ordinary composite integer, and differs from the exact proportional model by less than two units per atom. Nevertheless it retains the same nonzero curvature defect `(4)`.

This rules out two possible artifacts of AF-515:

1. visibility does not rely on allowing noninteger support points when the dilation factor is not integral;
2. visibility does not rely on exact common multiplication of every tail atom.

The discriminator is therefore robust to a substantial class of microscopic support errors while remaining blind, by AF-514, to a substantial class of direct sublinear transports away from the prime source.

## Representation audit

The representation remains the full relative-curvature carrier

\[
\|Q-\mathbb P\|_{\mathrm{rel}\,\kappa}
=
\sup_{s>1}
\frac{|\kappa_Q(s)-\kappa_P(s)|}{\kappa_P(s)}.
\tag{25}
\]

AF-516 does not alter the representation or add a mark. It identifies a local stability property of one of its positive separation mechanisms.

The result sharpens the current transport picture without completing it. AF-514 supplies a sufficient invisibility criterion expressed by a weighted transport budget; AF-515 supplies one exact linear-scale visibility witness; AF-516 proves that this witness persists on a full sublinear neighborhood of each proportional ray `q_p\sim cp`, `c>1`.

That leaves the genuinely harder boundary problem: characterize variable relative displacements

\[
q_p=p(1+\theta_p)
\]

when `\theta_p` does not converge to a nonzero constant. In particular, this finding does not decide oscillatory linear-scale transports, sparse proportional moves, or controls with `\theta_p\to0` too slowly for AF-514's weighted budget to vanish.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is the classical source for the prime-zeta Möbius relation and logarithmic singularity at `s=1` already used in AF-512--AF-515.
- AF-515 supplies the exact proportional-tail mesoscopic asymptotic and the cutoff-interface mechanism.
- AF-514 supplies the complementary perturbative estimates for tail support transport and the sublinear invisibility regime.
- The new comparison `(13)`--`(23)` is an elementary mean-value / quotient-differentiation stability argument. A focused search did not locate a standard theorem stated specifically as stability of prime-zeta log-curvature under sublinear rounding of a cofinite proportional tail.

The literature search also confirms that the prime-zeta boundary behavior itself is classical and should not be treated as an Arithmetic Fidelity discovery. The value here is narrower: it removes exact-placement and integrality artifacts from the AF-515 threshold witness.

## Boundaries and failure modes

1. **Sublinear rounding is sufficient, not claimed necessary.** The theorem assumes the uniform bound `(1)`. It does not classify the largest perturbation class that preserves `(4)`.
2. **A nonzero limiting dilation ratio is essential to this argument.** The theorem does not address `c=1`, where the AF-515 limiting gap vanishes and finer scales determine visibility.
3. **The result is mesoscopic.** It establishes the defect at the cutoff-adapted points `(3)` and hence a lower bound for the full relative-curvature distance; it does not assert pointwise separation at every fixed `s>1`.
4. **The moved tail being composite is a corollary of one rounding choice, not part of the abstract stability theorem.** Other admissible `q_p` satisfying `(1)` need not be integers or composites.
5. **This is not a complete linear-transport threshold.** Oscillatory, sparse, blockwise, or vanishing-relative-shift families remain open and may behave differently.
6. **No RH consequence is asserted.** The result concerns fidelity of a prime-derived compression and does not connect the recovered provenance to the zeta-zero problem.

## Dependencies

- `AF-509`: exact curvature equality classifies simple Dirichlet sources up to common dilation.
- `AF-510`: the quotient by common dilation has an explicit canonical inverse.
- `AF-514`: weighted tail transport can destroy any uniform curvature provenance margin throughout a broad sublinear regime.
- `AF-515`: exact proportional tail dilation produces the mesoscopic defect that AF-516 proves stable.

## Next theorem-level question

Determine the visibility criterion for variable relative transports

\[
q_p=p(1+\theta_p),
\]

starting with two falsifiable intermediate regimes: sparse proportional blocks with `\theta_p` bounded away from zero on a thinning subset, and slowly vanishing `\theta_p\to0` outside AF-514's weighted-budget hypothesis. The target is a necessary-or-nearly-necessary condition for a nonzero mesoscopic curvature defect, not another isolated transport example.