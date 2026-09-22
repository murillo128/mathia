# MC-460 — One-sided residual conditioning promotes the reduced divisor to a reciprocal source shift

**Status:** `EXACT-DERIVED` · `CANDIDATE-NEW-STRUCTURE` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The staged kernel of `MC-458` has an exact one-sided refinement in which a complementary residual divisor moves from the amplitude into the **source-character coordinate itself** before the second residual block is expanded.

Write

\[
r=g r_1,
\qquad
r'=g r_2,
\qquad
(r_1,r_2)=1,
\qquad
h=g h_0\ne0,
\tag{1}
\]

and let the two quotient progressions from `MC-458` be

\[
y_1(k)=A_1+r_2k,
\qquad
y_2(k)=A_2+r_1k,
\qquad
r_1y_1-r_2y_2=h_0.
\tag{2}
\]

The source phase is

\[
F(k)=\chi(k+u+\delta)\overline{\chi(k+u)},
\qquad
\delta\equiv h_0(r_1r_2)^{-1}\pmod q,
\tag{3}
\]

for a primitive character modulo `q`; only terms with the relevant outer and residual divisors coprime to `q` can contribute.

Now expand only the first residual block

\[
B_\beta(y_1)=\sum_{s\mid y_1}\beta_s
\tag{4}
\]

and fix one contributing divisor `s|y_1`. Put

\[
d=(s,r_2),
\qquad
s=d s_0,
\qquad
r_2=d t,
\qquad
(s_0,t)=1.
\tag{5}
\]

By `MC-459`, compatibility forces `d|h_0`; write `h_0=d h_1`. Parametrize

\[
n+h=rsm=g r_1 s m.
\tag{6}
\]

The second outer divisibility condition `r'|n` is then exactly

\[
t\mid r_1s_0m-h_1.
\tag{7}
\]

Since `(r_1s_0,t)=1`, there is a unique class `m_s (mod t)` satisfying `(7)`. Writing

\[
m=m_s+t j,
\tag{8}
\]

the still-unexpanded second quotient becomes

\[
\boxed{
y_2=C_s+r_1s_0j,
\qquad
C_s=\frac{r_1s_0m_s-h_1}{t}.
}
\tag{9}
\]

At the same time the character phase becomes

\[
\boxed{
\chi(j+U_s)\overline{\chi(j+U_s-D_s)},
}
\tag{10}
\]

where

\[
U_s\equiv m_s t^{-1}\pmod q,
\qquad
D_s\equiv \delta s_0^{-1}\pmod q.
\tag{11}
\]

Thus the reduced residual divisor `s_0=s/(s,r_2)` enters the source oscillation through the reciprocal map

\[
\boxed{s_0\longmapsto D_s=\delta/s_0\pmod q.}
\tag{12}
\]

This is stronger than merely retaining `s` inside a coefficient amplitude: after one-sided conditioning, the factor-specific variable survives in the translated-character shift itself.

There is a second exact alignment. Equations `(9)`--`(11)` imply

\[
\boxed{
C_s\equiv r_1s_0(U_s-D_s)\pmod q,
}
\tag{13}
\]

and hence

\[
y_2(j)
\equiv
r_1s_0\,(j+U_s-D_s)
\pmod q.
\tag{14}
\]

So the affine argument of the unexpanded second residual weight is congruent, up to the invertible scalar `r_1s_0`, to the **conjugate-character leg** in `(10)`. The remaining staged sum for this divisor therefore has the exact shape

\[
\boxed{
\sum_{j\in J_s}
\chi(j+U_s)\overline{\chi(j+U_s-D_s)}
\,\overline{B_\beta(C_s+r_1s_0j)},
\qquad
D_s=\delta s_0^{-1}.
}
\tag{15}
\]

up to the outer coefficient `\beta_s` and the previously fixed `(r,r')` block.

This realizes, algebraically, the factor-specific oscillatory dependence that `MC-456` identified as missing from the failed product-level and independent-residue orderings. It does **not** yet supply the required estimate. In particular, the starting parameter `U_s` varies with `s` through the residue class `m_s (mod t)`, so `(15)` is not automatically a one-parameter family indexed only by the reciprocal shifts `D_s`. No one-dimensional large-sieve or complete-shift mean-square gain may be imported without controlling that coupled `U_s` dependence.

No conductor-power saving, no improvement to the `MC-415`/`MC-448` source budget, no bound for `M(x)`, and no RH consequence follows.

## 1. One-sided divisor conditioning

From `s|y_1=(n+h)/r`, write

\[
n+h=rsm=g r_1 d s_0m.
\tag{16}
\]

Since `h=gdh_1`,

\[
n=g d(r_1s_0m-h_1).
\tag{17}
\]

The condition `r'=gdt|n` is therefore equivalent to `(7)`. Coprimality follows from

\[
(r_1,t)=1
\quad\text{because}\quad
(r_1,r_2)=1,
\tag{18}
\]

and `(s_0,t)=1` by construction, so `(7)` fixes exactly one class `m_s (mod t)`. Substitution of `(8)` into

\[
y_2=\frac n{r'}
=\frac{r_1s_0m-h_1}{t}
\tag{19}
\]

gives `(9)`.

This is precisely the asymmetric ordering that is unavailable after both residual blocks are expanded. The first residual divisor has been conditioned into the parametrization, while the second divisor sum remains inside `B_\beta(y_2)`.

## 2. The residual divisor enters the source shift reciprocally

For a nonzero character contribution, `(g r_1 s,q)=1`. From `(16)`--`(17)`, multiplicativity gives

\[
\begin{aligned}
\chi(n+h)\overline{\chi(n)}
&=\chi(g r_1 s m)
  \overline{\chi(g(r_1sm-h_0))}\\
&=\chi(m)\overline{\chi(m-\eta_s)},
\end{aligned}
\tag{20}
\]

where

\[
\eta_s\equiv h_0(r_1s)^{-1}\pmod q.
\tag{21}
\]

Because `t|r_2` and contributing outer factors are coprime to `q`, `(t,q)=1`. Substitution `m=m_s+t j` into `(20)` and cancellation of the constant character factors `\chi(t)\overline{\chi(t)}` gives `(10)` with

\[
U_s\equiv m_st^{-1},
\qquad
D_s\equiv\eta_s t^{-1}
\pmod q.
\tag{22}
\]

Using `s=ds_0` and `r_2=dt`,

\[
D_s
\equiv
h_0(r_1d s_0t)^{-1}
\equiv
h_0(r_1r_2s_0)^{-1}
\equiv
\delta s_0^{-1}
\pmod q,
\tag{23}
\]

which proves `(11)`--`(12)`.

There is an equivalent source-variable view that is useful for checking the algebra. Since `n=r'y_2=g r_2y_2`,

\[
\chi(n+h)\overline{\chi(n)}
=
\chi(y_2+h_0r_2^{-1})\overline{\chi(y_2)}.
\tag{24}
\]

The shift in the raw `y_2` coordinate is fixed. The reciprocal `s_0^{-1}` in `(23)` appears exactly because conditioning on `s` thins `y_2` to the progression `(9)` and then rescales that progression to unit step in `j`. It is therefore genuine factor-specific source geometry, but it is not newly created arithmetic information.

## 3. The surviving amplitude is aligned with one character leg

From the definition of `C_s`,

\[
tC_s=r_1s_0m_s-h_1.
\tag{25}
\]

Modulo `q`, multiplication by `t^{-1}` gives

\[
C_s
\equiv
r_1s_0U_s-h_1t^{-1}.
\tag{26}
\]

On the other hand, `(22)`--`(23)` imply

\[
r_1s_0D_s
\equiv
h_0r_2^{-1}
\equiv
h_1t^{-1}
\pmod q.
\tag{27}
\]

Subtracting `(27)` from `(26)` proves `(13)`, and adding the progression term `r_1s_0j` proves `(14)`.

This alignment is structurally sharper than simply observing that both the character phase and the residual amplitude depend on the same integer `j`. Modulo the source conductor, the amplitude argument itself sits on the conjugate-character coordinate after one invertible dilation. Any future completion or bilinear estimate for `(15)` should preserve this identity long enough to test whether it yields cancellation; replacing the residual amplitude by an unrelated norm discards it.

## 4. What this changes in the live branch

`MC-457` showed that retaining a factor only as an independent coprime residue mask tensorizes away under full completion. `MC-458` then exhibited a staged divisor-sum carrier not covered by that no-go. `MC-459` proved that the positive residual-weight diagonal is affordable and that progression divisibility is controlled by the normalized shift rather than the quotient slopes.

The present calculation answers the next structural question: **yes, one-sided residual conditioning can make the retained factor enter the nonzero-frequency source object itself before product collapse.** The dependency is explicit and reciprocal, `D_s=\delta s_0^{-1}`, and the unexpanded second residual amplitude remains tied to the conjugate source leg by `(14)`.

This does not establish that the resulting family is analytically cheaper. The exact next target is narrower: derive a Cauchy/dispersion/completion estimate for `(15)` or for its outer average that exploits the coupled map

\[
s\longmapsto (U_s,D_s,C_s,r_1s_0)
\tag{28}
\]

without first expanding the remaining `B_\beta`, and determine whether the variable `U_s` restores the two-dimensional source-frame occupancy barrier of `MC-446` or whether the congruence relation `(13)` reduces the true effective family.

## 5. Prior-art and novelty boundary

The algebraic steps above are elementary consequences of the exact `MC-458`/`MC-459` parametrization and character multiplicativity. No novelty is claimed for congruence thinning, affine rescaling, or the appearance of reciprocal variables in character sums.

The closest already-audited positive template remains `MC-456`: modern well-factorable dispersion arguments obtain gains only when factor variables survive into genuinely oscillatory reciprocal/Kloosterman-type phases before positive closure. Classical and modern bilinear character-sum literature also contains many reciprocal-variable estimates. Those neighboring results justify treating `(12)` as an analytically meaningful shape, but they do not by themselves estimate the coupled family `(15)`, whose start `U_s`, reciprocal shift `D_s`, and surviving divisor-sum amplitude arise from the same residual divisor.

The Mathia-specific delta is therefore only the exact reduction `(5)`--`(15)` for the already-defined staged Möbius source kernel. Whether an existing bilinear/trace-function estimate applies after the full parameter dependencies are exposed remains a prior-art and hypothesis-matching question for the next quantitative step.

## Boundaries and falsification tests

- **`U_s` is not fixed.** Reciprocal variation of `D_s` alone does not turn the family into a one-parameter source-frame average. Any claimed `q/H` rather than `q^2/H` occupancy threshold must first control the coupled start variable.
- **The raw `y_2` shift is fixed.** Equation `(24)` shows that the reciprocal shift is created by arithmetic thinning and rescaling, not by a new character conductor. A proof that ignores this may double-count the apparent new degree of freedom.
- **Expanding the second residual block still restores product variables.** The useful window is between one-sided conditioning and full residual expansion.
- **Absolute majorization destroys the new alignment.** Replacing `B_\beta(C_s+r_1s_0j)` by a divisor-function bound retains diagonal affordability from `MC-459` but forgets `(13)`--`(14)`.
- **Nonzero-character support is load-bearing.** The inverses in `(11)`, `(21)`, and `(23)` are used only on contributing terms; residual divisors sharing primes with the primitive conductor force the relevant character value to vanish and must be removed before inversion.
- **No automatic large-sieve theorem has been identified.** Existing reciprocal/bilinear character-sum results require their own range, independence, smoothness, and coefficient hypotheses. They cannot be imported merely from the visual form of `(12)`.
- **A useful estimate must survive recombination.** Any local saving for `(15)` must still beat outer `(r,r')`, residual-`s`, shift, exceptional-range, and source-depth costs when propagated through the existing `MC-415`/`MC-448` budget.

This is a structural frontier advance, not progress toward RH by itself.